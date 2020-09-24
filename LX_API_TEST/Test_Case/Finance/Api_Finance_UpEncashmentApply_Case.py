# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 获取提现基础数据

import unittest
from Libs.data_util import get_case_from_excel
from ddt import ddt,data
from Verify.Finance.FinanceVerify import *
from Libs.CheckRresult_Util import *
from Libs.data_util import write_result_data_to_excel
@ddt
class Api_Finance_UpEncashmentApply(unittest.TestCase):
    run_rules_dic = Config().get_run_rules_config()
    run_rules_dic.update({'ScriptName': os.path.basename(__file__)})
    datas = get_case_from_excel(Config().case_data_file_path, ['Finance'], run_rules_dic, 'Finance')

    def setUp(self) -> None:
        logging.info('启动脚本文件 :  {}'.format(os.path.basename(__file__)))
        self.account = Config().get_ini_value('Global_ini', 'WebUserName')
        self.password = Config().get_ini_value('Global_ini', 'WebPwd')
    @data(*datas)
    def test_UpEncashmentApply(self,datas):
        self.testcasename = datas['CaseName']
        logging.info('开始执行用例： {} ( {} )'.format(datas['CaseName'], self._testMethodName))
        logging.info('=======================调用【用户登录】接口====================================')
        LoginSessionID = login_api(self.account, self.password)
        if not LoginSessionID:
            logging.error('登录失败，请检查登录接口是否异常！')
        withdrawI_data,charg_data,bank_id = get_GetEncashment_data(LoginSessionID)
        datas['NewVerifParmsData'].update({"Amount":withdrawI_data,"CardID":bank_id,"Password":md5_encryption(Config().get_ini_value('Global_ini', 'amount_pwd'))})
        logging.info('=======================调用【前台出款申请】接口====================================')
        self.actual_result = http_api_requests('充值提现.前台出款申请', Headers={"LoginSessionID": LoginSessionID},
                                               NewVerifParmsData=datas['NewVerifParmsData'])
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