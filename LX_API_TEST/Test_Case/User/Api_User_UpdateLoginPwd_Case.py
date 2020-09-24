#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from ddt import ddt,data
from Config.Config import *
from Libs.data_util import *
from Libs.CheckRresult_Util import *
from Verify.User.UserVerify import login_api
from Libs.http_requests import http_api_requests
import logging
from Libs.Random_util import RandomUtil
from Libs.log_util import set_log
@ddt
class Api_User_UpdateLoginPwd_01(unittest.TestCase):

    r = RandomUtil()
    # 获取全局运行过滤规则字典
    run_rules_dic = Config().get_run_rules_config()
    run_rules_dic.update({'ScriptName':os.path.basename(__file__)})
    # 获取测试数据
    datas = get_case_from_excel(Config().case_data_file_path,['User'],run_rules_dic,'User')

    def setUp(self):
        logging.info('已经启动脚本文件： {}.py'.format(os.path.basename(__file__)))
        self.account = Config().get_ini_value('modify_loginpwd','mod_account')
        self.password = Config().get_ini_value('modify_loginpwd','mod_pwd')
        print(self.password)
        self.new_password = 'aa' + self.r.get_random_info_str(6)
        print(self.new_password)
    @data(*datas)
    def test_updateloginpwd_01(self,datas):
        self.TestCaseName = datas['CaseName']
        logging.info('开始执行用例：{}  |  运行case：{}'.format(self.TestCaseName, self._testMethodName))
        logging.info('=======================调用【用户登录】接口====================================')
        LoginSessionID = login_api(self.account,self.password)
        if not LoginSessionID:
            logging.error('登录失败，请检查登录接口是否异常！')
        datas['NewVerifParmsData'].update({"OldPwd":self.password})
        datas['NewVerifParmsData'].update({"OkPwd":self.new_password,"NewPwd":self.new_password})
        print(datas)
        logging.info('=======================调用【修改登录密码】接口====================================')
        self.actual_result = http_api_requests('密码相关.修改登录密码',Headers={"LoginSessionID":LoginSessionID},NewVerifParmsData=datas['NewVerifParmsData'])
        self.expected_result = datas['ExpectResult']
        try:
            check_result(self.expected_result,self.actual_result)
            result = 'pass'
            Config().set_options_value('mod_pwd',self.new_password,setions='modify_loginpwd')
        except InterfaceVerifyError:
            result = 'false'
        finally:
            write_result_data_to_excel(Config().case_data_file_path,'User','ID',datas['ID'],result)
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
