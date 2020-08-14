#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Config.Config import *
from Libs.CheckRresult_Util import *
from Libs.common import *
from Libs.data_util import *
from Libs.http_requests import *
import unittest
import logging
from ddt import ddt,data
from Verify.User.UserVerify import *

from Libs.Random_util import RandomUtil

@ddt
class Api_User_Mod_UpdatewithdrawPwd(unittest.TestCase):
    # 获取测试数据
    run_rules_dic = Config().get_run_rules_config()
    run_rules_dic.update({'ScriptName':os.path.basename(__file__)})
    datas = get_case_from_excel(Config().case_data_file_path,['User'],run_rules_dic,'User')

    def setUp(self):
        logging.info('启动脚本文件 :  {}'.format(os.path.basename(__file__)))
        self.account = Config().Global.get('Global_ini','testaccount')
        self.password = Config().Global.get('Global_ini','testpwd')
    @data(*datas)
    def test_mod_updatawithdrawpwd_01(self,datas):
        self.TestCaseName = datas['CaseName']
        logging.info('开始执行用例： {} ( {} )'.format(self.TestCaseName,self._testMethodName))
        logging.info('=======================调用【用户登录】接口====================================')
        LoginSessionID = login_api(self.account,self.password)
        if not LoginSessionID:
            logging.error('登录接口异常，请检查')
        logging.info('=======================调用【重置/修改资金密码】接口====================================')
        self.actual_result = http_api_requests('密码相关.重置/修改资金密码',Headers={"LoginSessionID":LoginSessionID},NewVerifParmsData=datas['NewVerifParmsData'])
        self.expected_result = datas['ExpectResult']
        self.old_pwd = datas['NewVerifParmsData']['OldPwd']
        result = None
        try:
            check_result(self.expected_result, self.actual_result)
            if self.old_pwd == 'aaaa22':
                self.actual_result = http_api_requests('密码相关.重置/修改资金密码',Headers={"LoginSessionID":LoginSessionID},NewVerifParmsData={"IsReset":"true"})
                self.expected_result = datas['ExpectResult']
                check_result(self.expected_result, self.actual_result)
            result = 'pass'
        except InterfaceVerifyError:
            result = 'false'
        finally:
            write_result_data_to_excel(Config().case_data_file_path, 'User', 'ID', datas['ID'], result)

    def tearDown(self):
        pass


if __name__ == '__main__':
    set_log()
    unittest.main()