# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 获取游戏赔率数据
# 单注下注金额基数
# 投注模式
# 该游戏被禁用玩法项
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

@ddt
class Api_Game_GetGameOddsData_01(unittest.TestCase):

    run_rules_dic = Config().get_run_rules_config()
    run_rules_dic.update({'ScriptName': os.path.basename(__file__)})
    print(run_rules_dic)
    datas = get_case_from_excel(Config().case_data_file_path, ['Game'], run_rules_dic, 'Game')

    def setUp(self):
        logging.info('启动脚本文件 :  {}'.format(os.path.basename(__file__)))
        self.account = Config().get_ini_value('Global_ini', 'WebUserName')

        self.password = Config().get_ini_value('Global_ini', 'WebPwd')

    @data(*datas)
    def test_get_game_odddata(self, datas):
        self.testcasename = datas['CaseName']
        logging.info('开始执行用例： {} ( {} )'.format(datas['CaseName'], self._testMethodName))
        logging.info('=======================调用【用户登录】接口====================================')
        LoginSessionID = login_api(self.account, self.password)
        if not LoginSessionID:
            logging.error('登录失败，请检查登录接口是否异常！')
        logging.info('=======================调用【获取游戏最新开盘期数】接口====================================')
        self.actual_result = http_api_requests('游戏相关.获取游戏赔率数据', Headers={"LoginSessionID": LoginSessionID},NewVerifParmsData=datas['NewVerifParmsData'])
        self.expected_result = datas['ExpectResult']
        try:

            check_result(self.expected_result, self.actual_result)
            result = 'pass'
            DisablePlay = get_json_value(self.actual_result,'/Data/DisablePlay')
            print(DisablePlay)
            DisablePlay_item = get_json_value(self.actual_result,'/Data/DisablePlayItem')
            print('111')
            print(DisablePlay_item)
            list = []
            for i in DisablePlay:
                if isinstance(i,str):
                    list.append(int(i))
            logging.info('该游戏被禁用玩法项：{}'.format(list))
            odd_list = get_json_value(self.actual_result,'/Data/OddsList')
            print(odd_list)
            self.odd_data = get_json_value(self.actual_result, '/Data')
            # 单注下注金额基数
            Radix = self.odd_data['Radix']
            # 投注模式
            moneyModel = self.odd_data['moneyModel']
            logging.info('单注下注金额基数：{}，投注模式：{}'.format(Radix,moneyModel))

        except InterfaceVerifyError:
            result = 'false'
        finally:
            write_result_data_to_excel(Config().case_data_file_path, 'Game', 'ID', datas['ID'], result)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()


