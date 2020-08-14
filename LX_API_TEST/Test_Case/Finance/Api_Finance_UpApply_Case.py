# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 公司充值
import unittest
from Libs.data_util import write_result_data_to_excel
from Libs.data_util import get_case_from_excel
from ddt import ddt,data
from Verify.Finance.FinanceVerify import *
from Libs.CheckRresult_Util import *
from Libs.Random_util import RandomUtil
from Libs.Time_Util import *
@ddt
class Api_Finance_UpApply(unittest.TestCase):
    r = RandomUtil()
    run_rules_dic = Config().get_run_rules_config()
    run_rules_dic.update({'ScriptName': os.path.basename(__file__)})
    datas = get_case_from_excel(Config().case_data_file_path, ['Finance'], run_rules_dic, 'Finance')
    def setUp(self) -> None:
        logging.info('启动脚本文件 :  {}'.format(os.path.basename(__file__)))
        self.account = Config().get_ini_value('Global_ini', 'WebUserName')
        self.password = Config().get_ini_value('Global_ini', 'WebPwd')

    @data(*datas)
    def test_Finance_UpApply(self, datas):
        self._testMethodDoc = datas['CaseName']
        logging.info('开始执行用例： {} ( {} )'.format(self._testMethodDoc, self._testMethodName))
        logging.info('=======================调用【用户登录】接口====================================')
        self.LoginSessionID = login_api(self.account, self.password)
        if not self.LoginSessionID:
            logging.error('登录失败，请检查登录接口是否异常！')
        # 获取导航通道-公司
        payment_info = get_finance_paymentindex(LoginSessionID=self.LoginSessionID, paytype=0)
        logging.info('获取通道ID:{},获取通道名称：{}'.format(payment_info['ID'], payment_info['PayType']))
        # 获取导航通道下可用商户字典信息
        payment_data = payment_PreferenceNewConfig(LoginSessionID=self.LoginSessionID, id=payment_info['ID'],isonline=payment_info['Type'], return_data=True)
        print('获取商户字典信息' + '\n', json.dumps(payment_data, indent=4))
        # 金额判断
        if datas['NewVerifParmsData']['amount'] == 1:
            self.Amount = self.r.get_random_int(payment_data['MinAmount'], payment_data['MaxAmount']) if not payment_data['FIsShowShortcut']\
                else int(random.choice(payment_data['FShortcutSet'].split(',')))
        elif datas['NewVerifParmsData']['amount'] == 2:
            self.Amount = payment_data['MinAmount'] - 1
        elif datas['NewVerifParmsData']['amount'] == 3:
            self.Amount = payment_data['MaxAmount'] + 1
        else:
            raise ('金额类型写入有误，请检查测试数据！')
        logging.info('=======================调用【公司充值】接口====================================')
        datas['NewVerifParmsData'].update({"orderNumber": payment_data['OrderNumber'], "amount": self.Amount,"userBankId": payment_data['BankId'],
                                           "CompanyCardId":payment_data['ID'],"date":get_now_time(),"way":"","bankId":payment_data['ID'],
                                           "CardNo":payment_data['CardNo'],"_":get_time_stamp()})
        self.actual_result = http_api_requests('充值提现.公司充值', Headers={"LoginSessionID": self.LoginSessionID},NewVerifParmsData=datas['NewVerifParmsData'])
        self.expected_result = datas['ExpectResult']
        # 写入结果
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