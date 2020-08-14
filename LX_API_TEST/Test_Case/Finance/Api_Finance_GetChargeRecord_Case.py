# !/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from Libs.data_util import write_result_data_to_excel
from Libs.data_util import get_case_from_excel
from ddt import ddt,data
from Verify.Finance.FinanceVerify import *
from Libs.CheckRresult_Util import *
from Libs.Time_Util import *
@ddt
class Api_Finance_GetChargeRecord(unittest.TestCase):
    run_rules_dic = Config().get_run_rules_config()
    run_rules_dic.update({'ScriptName': os.path.basename(__file__)})
    datas = get_case_from_excel(Config().case_data_file_path, ['Finance'], run_rules_dic, 'Finance')
    def setUp(self) -> None:
        logging.info('启动脚本文件 :  {}'.format(os.path.basename(__file__)))
        self.account = Config().get_ini_value('Global_ini', 'WebUserName')
        self.password = Config().get_ini_value('Global_ini', 'WebPwd')

    @data(*datas)
    def test_Finance_GetChargeRecord(self, datas):
        self._testMethodDoc = datas['CaseName']
        logging.info('开始执行用例： {} ( {} )'.format(self._testMethodDoc, self._testMethodName))
        logging.info('=======================调用【用户登录】接口====================================')
        self.LoginSessionID = login_api(self.account, self.password)
        if not self.LoginSessionID:
            logging.error('登录失败，请检查登录接口是否异常！')
        logging.info('=======================调用【充值记录】接口====================================')
        end_time,start_time = get_nowday_and_yestday()
        datas['NewVerifParmsData'].update({"EndTime":end_time,"StartTime":start_time,"OrderNum":43608080142211480007})
        self.actual_result = http_api_requests('充值提现.充值记录', Headers={"LoginSessionID": self.LoginSessionID},NewVerifParmsData=datas['NewVerifParmsData'])
        self.expected_result = datas['ExpectResult']
        result = None
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