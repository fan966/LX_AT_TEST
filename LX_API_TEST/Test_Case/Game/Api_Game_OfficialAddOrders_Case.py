# !/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from Libs.data_util import write_result_data_to_excel
from Config.Config import *
import logging
from Libs.log_util import set_log
from Libs.data_util import get_case_from_excel
from ddt import ddt,data
from Libs.http_requests import *
from Libs.CheckRresult_Util import *
from Verify.User.UserVerify import login_api
from Verify.User.UserVerify import *
from Verify.Game.GameVerify import *

@ddt
class Api_Game_OfficialAddOrders(unittest.TestCase):
    run_rules_dic = Config().get_run_rules_config()
    run_rules_dic.update({'ScriptName': os.path.basename(__file__)})
    datas = get_case_from_excel(Config().case_data_file_path, ['Game'], run_rules_dic, 'Game')
    #print(datas)
    def setUp(self):
        logging.info('启动脚本文件 :  {}'.format(os.path.basename(__file__)))
        self.account = Config().get_ini_value('Global_ini', 'WebUserName')

        self.password = Config().get_ini_value('Global_ini', 'WebPwd')
        # 数据库获取用户ID
        #self.user_id = from_db_get_user_ID(self.account)[0]['id']
        # 数据库获取用户余额
        #self.user_blance = from_db_TCredits_get_user_FBalance(self.user_id)[0]['Balance']

    @data(*datas)
    def test_Game_OfficialAddOrders(self,datas):
        self._testMethodDoc = datas['CaseName']
        logging.info('开始执行用例： {} ( {} )'.format(self._testMethodDoc,self._testMethodName))
        logging.info('=======================调用【用户登录】接口====================================')
        self.LoginSessionID = login_api(self.account, self.password)
        if not self.LoginSessionID:
            logging.error('登录失败，请检查登录接口是否异常！')

        logging.info('=======================调用【官方游戏下注】接口====================================')
        while True:
            # 获取游戏ID
            #self.game_id = get_official_game_id()[1]
            #self.game_name = get_official_game_id()[0]
            self.game_id = 612
            datas['NewVerifParmsData'].update({'GameId': self.game_id})
            #logging.info('成功获取游戏:{}：游戏ID：{}'.format(self.game_name,self.game_id))
            #print(datas)
            # 获取期数ID
            self.period_info = get_game_period_info(self.LoginSessionID,{"GameID":self.game_id})
            if not self.period_info:
                logging.error('获取期数ID失败')
                #raise ('获取期数ID失败,请检查！')
            datas['NewVerifParmsData'].update({"PeriodId":self.period_info})
        # 获取官方游戏赔率/玩法项数据
            game_data = get_officia_gam_bet_data(self.LoginSessionID,self.game_id)
            if game_data :
                break
        OrderList = '[{\"a\":%s,\"c\":\"%s\",\"i\":%s,\"k\":\"%s\",\"m\":%s,\"n\":%s,\"t\":%s,\"ts\":%s}]'%(game_data[0]['a'],game_data[0]['c'],game_data[0]['i'],game_data[0]['k'],game_data[0]['m'],game_data[0]['n'],game_data[0]['t'],get_time_stamp())
        datas['NewVerifParmsData'].update({"OrderList":OrderList})

        #print(datas['NewVerifParmsData'])
        self.actual_result = http_api_requests('游戏相关.官方游戏下注', Headers={"LoginSessionID": self.LoginSessionID},NewVerifParmsData=datas['NewVerifParmsData'])
        self.expected_result = datas['ExpectResult']
        result = None
        try:
            check_result(self.expected_result, self.actual_result)
            result = 'pass'
        except InterfaceVerifyError:
            result = 'false'
        finally:
            write_result_data_to_excel(Config().case_data_file_path, 'Game', 'ID', datas['ID'], result)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()