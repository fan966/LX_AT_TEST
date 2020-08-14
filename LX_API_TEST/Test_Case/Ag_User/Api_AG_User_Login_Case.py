# !/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from Libs.data_util import write_result_data_to_excel
import logging
from Libs.log_util import set_log
from Libs.data_util import get_case_from_excel
from ddt import ddt,data
from Libs.CheckRresult_Util import *
from Verify.User.UserVerify import *
from Libs.Time_Util import *
@ddt
class Api_AG_User_Login(unittest.TestCase):
    run_rules_dic = Config().get_run_rules_config()
    run_rules_dic.update({'ScriptName': os.path.basename(__file__)})
    datas = get_case_from_excel(Config().case_data_file_path, ['User'], run_rules_dic, 'User')

    def setUp(self) -> None:
        logging.info('启动脚本文件 :  {}'.format(os.path.basename(__file__)))
        self.account = Config().get_ini_value('Global_ini', 'AgUserName')
        self.password = Config().get_ini_value('Global_ini', 'AgPwd')
    @data(*datas)
    def test_AG_uesr_login(self,datas):
        self._testMethodDoc = datas['CaseName']
        datas['NewVerifParmsData'].update({"username":self.account})
        datas['NewVerifParmsData'].update({"password":md5_encryption(md5_encryption(self.password))})
        logging.info('开始执行用例： {} ( {} )'.format(self._testMethodDoc, self._testMethodName))
        logging.info('=======================调用【后台用户登录】接口====================================')
        self.actual_result = http_api_requests('后台相关.用户登录',return_result=True,server_host=Config().ag_host,NewVerifParmsData=datas['NewVerifParmsData'])
        time.sleep(1)
        self.expected_result = datas['ExpectResult']
        if self.expected_result in self.actual_result:
            result = 'pass'
        else:
            result = 'false'
        write_result_data_to_excel(Config().case_data_file_path, 'User', 'ID', datas['ID'], result)

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    set_log()
    unittest.main()











# url = 'http://csdqtjcag.lx901.com/Login'
# url2 = 'http://csdqtjcag.lx901.com/Admin/Index'
# url3 = 'http://csdqthcweb.lx901.com/SpecialActivity/GetRedPocketConfig'
# datas = {
#     "password":"8196658ecaeceb870d0ad3053dd579d2",
#     "googlecode":"",
#     "username":"qazwsx2",
#     "validateCode":"",
#     "accountfid":""
# }
#
# res = requests.post(url=url,data=datas,verify=False)
# #print(res.text)
# str1 = res.request.headers
# print(str1)
# str1 = str1['Cookie']
# #new_url = res.headers['Location']
# # str1 = res.headers['Set-Cookie']
# #
# p =re.compile('LoginSessionID=.*; ',re.I)
# id = p.findall(str1)
# LoginSessionID = id[0].split(';')
# LoginSessionID = LoginSessionID[0].split('=')[1]
# print(LoginSessionID)
# print(res.status_code)
#
# headers = {"LoginSessionID":LoginSessionID}
#
# res = requests.get(url=url3,headers=headers,verify=False)
# print(res.text)