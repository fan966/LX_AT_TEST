# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 获取出款稽核数据

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
class Api_Finance_GetAuditData(unittest.TestCase):
    run_rules_dic = Config().get_run_rules_config()
    run_rules_dic.update({'ScriptName': os.path.basename(__file__)})
    datas = get_case_from_excel(Config().case_data_file_path, ['Finance'], run_rules_dic, 'Finance')

    def setUp(self) -> None:
        logging.info('启动脚本文件 :  {}'.format(os.path.basename(__file__)))
        self.account = Config().get_ini_value('Global_ini', 'WebUserName')
        self.password = Config().get_ini_value('Global_ini', 'WebPwd')
    @data(*datas)
    def test_GetAuditData(self,datas):
        self.testcasename = datas['CaseName']
        logging.info('开始执行用例： {} ( {} )'.format(datas['CaseName'], self._testMethodName))
        logging.info('=======================调用【用户登录】接口====================================')
        LoginSessionID = login_api(self.account, self.password)
        if not LoginSessionID:
            logging.error('登录失败，请检查登录接口是否异常！')
        logging.info('=======================调用【获取出款稽核数据】接口====================================')
        self.actual_result = http_api_requests('充值提现.获取出款稽核数据', Headers={"LoginSessionID": LoginSessionID},
                                               NewVerifParmsData={})
        self.expected_result = datas['ExpectResult']
        try:
            check_result(self.expected_result, self.actual_result)
            result = 'pass'
        except InterfaceVerifyError:
            result = 'false'
        finally:
            write_result_data_to_excel(Config().case_data_file_path, 'Finance', 'ID', datas['ID'], result)

    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    set_log()
    unittest.main()