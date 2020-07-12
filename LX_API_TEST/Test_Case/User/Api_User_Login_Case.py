#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from ddt import ddt,data
from Libs.http_requests import *
from Libs.common import *
import logging
from Libs.data_util import *
from Libs.CheckRresult_Util import *

@ddt
class Api_User_Login(unittest.TestCase):

    run_rules_dic = Config().get_run_rules_config()
    run_rules_dic.update({'ScriptName':os.path.basename(__file__)})
    datas = get_case_from_excel(Config().case_data_file_path,['User'],run_rules_dic,'User')


    def setUp(self):
        logging.info('启动脚本文件 :  {}'.format(os.path.basename(__file__)))

    @data(*datas)
    def test_login_01(self,datas):
        self.TestCaseName = datas['CaseName']
        logging.info('开始执行用例： {} ( {} )'.format(datas['CaseName'], self._testMethodName))
        res_msg = http_api_requests('登录注册.获取全局Token值',NewVerifParmsData={})
        if not res_msg:
            logging.error('获取全局Token失败')
        else:
            ValidateToken = get_json_value(res_msg,'/Data/Value')
        res_msg = http_api_requests('登录注册.获取图片验证码',Headers={'ValidateToken':ValidateToken},NewVerifParmsData={})
        if not res_msg:
            logging.error('获取图片验证码失败')
        logging.info('======================调用：用户登录接口=======================')
        datas['NewVerifParmsData'].update({"Password":pwd_md5_encryption('aaaa2222','9999')})
        self.actual_result = http_api_requests('登录注册.用户登录',Headers={'ValidateToken':ValidateToken},NewVerifParmsData=datas['NewVerifParmsData'])
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