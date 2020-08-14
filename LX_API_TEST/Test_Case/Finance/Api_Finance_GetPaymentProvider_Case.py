# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 获取导航通道下可用支付通道
# OrderNumber 订单号
# Number 附言码
# 可用支付商字段信息 ID 通道ID/MaxAmount 最大存款金额/MinAmount  	最小存款金额/IsCharge 是否需要手续费/Charge 手续费比例/IsDepositAddRandom 是否充值时增加随机金额（0.00-0.08） /
# WayType 通道类型。0、全部通道；1、扫码支付；2、客户端支付/FIsShowShortcut 是否显示金额快捷方式/FShortcutSet 金额快捷设置/OrderNumber 当前交易的订单号/Number 附言码
import unittest
from Libs.data_util import write_result_data_to_excel
from Libs.data_util import get_case_from_excel
from ddt import ddt,data
from Verify.Finance.FinanceVerify import *
from Libs.CheckRresult_Util import *
@ddt
class Api_Finance_GetPaymentProvider(unittest.TestCase):
    run_rules_dic = Config().get_run_rules_config()
    run_rules_dic.update({'ScriptName': os.path.basename(__file__)})
    datas = get_case_from_excel(Config().case_data_file_path, ['Finance'], run_rules_dic, 'Finance')

    def setUp(self) -> None:
        logging.info('启动脚本文件 :  {}'.format(os.path.basename(__file__)))
        self.account = Config().get_ini_value('Global_ini', 'WebUserName')
        self.password = Config().get_ini_value('Global_ini', 'WebPwd')

    @data(*datas)
    def test_paymentindex(self,datas):
        self._testMethodDoc = datas['CaseName']
        logging.info('开始执行用例： {} ( {} )'.format(self._testMethodDoc, self._testMethodName))
        logging.info('=======================调用【用户登录】接口====================================')
        self.LoginSessionID = login_api(self.account, self.password)
        if not self.LoginSessionID:
            logging.error('登录失败，请检查登录接口是否异常！')
        payment_id = get_finance_paymentindex(LoginSessionID=self.LoginSessionID,paytype=1)
        logging.info('获取通道ID:{},获取通道名称：{}'.format(payment_id['ID'],payment_id['PayType']))
        logging.info('=======================调用【获取可用支付通道】接口====================================')
        datas['NewVerifParmsData'].update({"id":payment_id['ID']})
        datas['NewVerifParmsData'].update({"isonline": payment_id['Type']})
        self.actual_result = http_api_requests('充值提现.获取可用支付通道', Headers={"LoginSessionID": self.LoginSessionID},NewVerifParmsData=datas['NewVerifParmsData'])
        self.expected_result = datas['ExpectResult']
        result = None
        try:
            check_result(self.expected_result, self.actual_result)
            result = 'pass'
        except InterfaceVerifyError:
            result = 'false'
        finally:
            write_result_data_to_excel(Config().case_data_file_path, 'Finance', 'ID', datas['ID'], result)
        pay_data = get_json_value(self.actual_result,'/Data')
        temp = '/OnlinePayment' if payment_id['Type'] else '/OfflinePayment'
        pay_data_ = get_json_value(pay_data,'{}'.format(temp))
        payment_info = []
        for payment_ in pay_data_:
            payment_.update({'OrderNumber':pay_data['OrderNumber']})
            payment_.update({'Number': pay_data['Number']})
            payment_info.append(payment_)
        print(payment_info)


    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    set_log()
    unittest.main()