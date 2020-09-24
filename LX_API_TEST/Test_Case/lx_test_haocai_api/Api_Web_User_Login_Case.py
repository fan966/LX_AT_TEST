#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from Libs.data_util import write_result_data_to_excel
from Config.Config import *
import logging
from Libs.log_util import set_log
from Libs.data_util import get_case_from_excel
from ddt import ddt,data
from Libs.http_requests import http_api_requests,get_json_value
from Libs.CheckRresult_Util import *
from Libs.common import *

@ddt
class Api_Web_User_Login(unittest.TestCase):
    run_rules_dic = Config().get_run_rules_config()
    run_rules_dic.update({'ScriptName': os.path.basename(__file__)})
    datas = get_case_from_excel(Config().case_data_file_path, ['Test_Web'], run_rules_dic, 'Test_Web')

    def setUp(self):
        logging.info('启动脚本文件 :  {}'.format(os.path.basename(__file__)))
        self.account = Config().get_ini_value('Global_ini', 'WebUserName')

        self.password = Config().get_ini_value('Global_ini', 'WebPwd')
    @data(*datas)
    def test_web_user_login_01(self,datas):
        self._testMethodDoc = datas['CaseName']
        logging.info('开始执行用例： {} ( {} )'.format(self._testMethodDoc, self._testMethodName))
        logging.info('======================调用：用户登录接口=======================')
        self.actual_result = http_api_requests('前台相关.用户登录', NewVerifParmsData={"username": self.account, "password": md5_encryption(md5_encryption(self.password))})
        self.expected_result = datas['ExpectResult']
        result = None
        try:
            check_result(self.expected_result, self.actual_result)
            result = 'pass'
        except InterfaceVerifyError:
            result = 'false'
        finally:
            write_result_data_to_excel(Config().case_data_file_path, 'Test_Web', 'ID', datas['ID'], result)

    def tearDown(self):
        pass

if __name__ == '__main__':
    set_log()
    unittest.main()