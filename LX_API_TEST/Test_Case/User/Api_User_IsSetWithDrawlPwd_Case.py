#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from ddt import ddt,data
from Libs.http_requests import *
from Libs.data_util import *
from Libs.common import *
from Verify.User.UserVerify import login_api
from Libs.CheckRresult_Util import *

@ddt
class Api_User_IsSetWithDrawlPwd_Case(unittest.TestCase):

    # 获取全局过滤规则字典
    run_rules_dic = Config().get_run_rules_config()
    run_rules_dic.update({'ScriptName':os.path.basename(__file__)})

    # 获取测试数据
    datas = get_case_from_excel(Config().case_data_file_path,['User'],run_rules_dic,'User')

    def setUp(self):
        logging.info('已经启动脚本文件： {}.py'.format(self.__module__))
        # 获取全局用户数据
        self.account = Config().get_ini_value('Global_ini','WebUserName')
        self.password = Config().get_ini_value('Global_ini','WebPwd')
    @data(*datas)
    def test_is_set_withdrawpwd(self,datas):
        self.TestCaseName = datas['CaseName']
        logging.info('开始执行用例： {} ( {} )'.format(datas['CaseName'], self._testMethodName))
        logging.info('=======================调用【用户登录】接口====================================')
        LoginSessionID = login_api(self.account,self.password)
        logging.info('=======================调用【是否设置资金密码】接口====================================')
        self.actual_result = http_api_requests('密码相关.是否设置资金密码',Headers={"LoginSessionID":LoginSessionID},NewVerifParmsData=datas['NewVerifParmsData'])
        self.expected_result = datas['ExpectResult']
        try:
            check_result(self.expected_result,self.actual_result)
            result = 'pass'
        except InterfaceVerifyError:
            result = 'false'
        finally:
            write_result_data_to_excel(Config().case_data_file_path,'User','ID',datas['ID'],result)

    def tearDown(self):
        pass





if __name__ == '__main__':
    unittest.main()