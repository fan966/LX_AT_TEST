#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Config.Config import *
from Libs.CheckRresult_Util import *
from Libs.common import *
from Libs.data_util import *
from Libs.http_requests import *
import unittest
from ddt import ddt,data
import logging
from Verify.User.UserVerify import *
from Libs.Random_util import RandomUtil

@ddt
class Api_User_UpdateWithdrawalPwd(unittest.TestCase):
    # 获取测试数据
    # 获取全局规则过滤字典
    run_rules_dic = Config().get_run_rules_config()
    run_rules_dic.update({"ScriptName":os.path.basename(__file__)})
    datas = get_case_from_excel(Config().case_data_file_path,['User'],run_rules_dic,'User')

    def setUp(self):
        r = RandomUtil()
        logging.info('启动脚本文件 :  {} '.format(os.path.basename(__file__)))
        self.account = Config().get_ini_value('Global_ini','WebUserName')
        self.password = Config().get_ini_value('Global_ini', 'WebPwd')
        self.amount_pwd = Config().get_ini_value('Global_ini', 'amount_pwd')
        self.new_amount_pwd = r.get_random_info_str(6)

    @data(*datas)
    def test_updatewithdrawapwd_01(self,datas):
        self.TestCaseName = datas['CaseName']
        logging.info('开始执行用例 ： {} ({})'.format(self.TestCaseName,self._testMethodName))
        logging.info('=======================调用【用户登录】接口====================================')
        LoginSessionID = login_api(self.account,self.password)
        if not LoginSessionID:
            logging.error('登录失败，请检查登录接口')
        logging.info('=======================调用【设置资金密码】接口====================================')
        if self.TestCaseName == '密码相关,设置资金密码，原密码正确':
            datas['NewVerifParmsData']['OldPwd'] = self.amount_pwd
            datas['NewVerifParmsData']['NewPwd'] = self.new_amount_pwd
            datas['NewVerifParmsData']['OkPwd'] = self.new_amount_pwd

        self.actual_result = http_api_requests('密码相关.设置资金密码',Headers={"LoginSessionID":LoginSessionID},NewVerifParmsData=datas['NewVerifParmsData'])
        self.expected_result = datas['ExpectResult']
        try:
            check_result(self.expected_result,self.actual_result)
            if self.amount_pwd != self.new_amount_pwd  and self.TestCaseName == '密码相关,设置资金密码，原密码正确':
                Config().set_options_value('amount_pwd',self.new_amount_pwd)
            result = 'pass'
        except InterfaceVerifyError:
            result = 'false'
        finally:
            write_result_data_to_excel(Config().case_data_file_path,'User','ID',datas['ID'],result)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
