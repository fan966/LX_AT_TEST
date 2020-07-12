# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 获取游戏玩法项
# 返回玩法项ID

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
class Api_Game_GetCPYXGameList(unittest.TestCase):
    run_rules_dic = Config().get_run_rules_config()
    run_rules_dic.update({'ScriptName': os.path.basename(__file__)})
    datas = get_case_from_excel(Config().case_data_file_path, ['Game'], run_rules_dic, 'Game')
    def setUp(self) :
        logging.info('启动脚本文件 :  {}'.format(os.path.basename(__file__)))
        self.account = Config().get_ini_value('Global_ini','WebUserName')

        self.password = Config().get_ini_value('Global_ini','WebPwd')

    @data(*datas)
    def test_unit_001(self,datas):
        self.testcasename = datas['CaseName']
        logging.info('开始执行用例： {} ( {} )'.format(datas['CaseName'], self._testMethodName))
        logging.info('=======================调用【用户登录】接口====================================')
        LoginSessionID = login_api(self.account,self.password)
        if not LoginSessionID:
            logging.error('登录失败，请检查登录接口是否异常！')
        logging.info('=======================调用【获取游戏玩法数据】接口====================================')
        self.actual_result = http_api_requests('游戏相关.获取游戏玩法数据',Headers={"LoginSessionID":LoginSessionID},NewVerifParmsData=datas['NewVerifParmsData'])
        self.expected_result = datas['ExpectResult']
        self.play_data = get_json_value(self.actual_result,'/Data')
        print(self.play_data)
        play_list = []
        guolv = [4269, 4268, 4267, 4266, 4265, 4264, 4263, 4262, 4261, 4260, 4259, 4258, 4257]
        for data in self.play_data:
            #print(data)
            play_name = data['Name']
            play_id = data['Id']
            for data_dict in data['Child']:
                #print(data_dict)
                for data_play_dict in data_dict['C']:
                    if data_play_dict['Id'] not in guolv: # 过滤禁用玩法
                        #print(data_play_dict)
                        for dats2 in data_play_dict['Child']:
                            dic = {}
                            #print(dats2)
                            #print(dats2['Name'], dats2['FId'])
                            dic.update({"{} {}".format(play_name,play_id):{dats2['Name']: dats2['FId']}})
                            play_list.append(dic)
                            print(dats2)
        #print(play_list)
# [4269, 4268, 4267, 4266, 4265, 4264, 4263, 4262, 4261, 4260, 4259, 4258, 4257]
        try:
            check_result(self.expected_result, self.actual_result)
            result = 'pass'
        except InterfaceVerifyError:
            result = 'false'
        finally:
            write_result_data_to_excel(Config().case_data_file_path, 'Game', 'ID', datas['ID'], result)


    def tearDown(self) :
        pass

if __name__ == '__main__':
    unittest.main()
    # [{"i":21044,"c":"01|02|03","n":1,"t":1,"k":0,"m":1,"a":2,"ts":1593927523}]