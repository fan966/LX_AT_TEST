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
@ddt
class Api_User_AddAccount_Case_01(unittest.TestCase):
    r = RandomUtil()
    # 获取全局运行过滤规则字典
    run_rules_dic = Config().get_run_rules_config()
    run_rules_dic.update({"ScriptName":os.path.basename(__file__)})
    # 获取case数据
    datas = get_case_from_excel(Config().case_data_file_path,['User'],run_rules_dic,'User')


    def setUp(self):
        logging.info('已经启动脚本文件： {}.py'.format(self.__module__))
        self.account = Config().get_ini_value('Global_ini','WebUserName')
        self.password = Config().get_ini_value('Global_ini','WebPwd')

    @data(*datas)
    def test_addaccount(self,datas):
        self.TestCaseName = datas['CaseName']
        logging.info('开始执行用例：{}  |  运行case：{}'.format(self.TestCaseName,self._testMethodName))
        account_name = 'atuotest' + self.r.get_random_info_int(4)
        if '成功' in self.TestCaseName:
            datas['NewVerifParmsData'].update({'AccountName':account_name})
        logging.info('=======================调用【用户登录】接口====================================')
        LoginSessionID = login_api(self.account, self.password)
        if not LoginSessionID:
            logging.error('登录失败，请检查接口是否异常！')
        logging.info('=======================调用【添加账户】接口====================================')
        self.actual_result = http_api_requests('用户相关.添加账户',Headers={"LoginSessionID":LoginSessionID},NewVerifParmsData=datas['NewVerifParmsData'])
        self.expected_result = datas['ExpectResult']
        try:
            check_result(self.expected_result,self.actual_result)
            result = 'pass'
            logging.info('新增用户（{}）成功'.format(account_name))
        except InterfaceVerifyError:
            result = 'false'
        finally:
            write_result_data_to_excel(Config().case_data_file_path,'User','ID',datas['ID'],result)
    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()