# !/usr/bin/env python
# -*- coding: utf-8 -*-
# RechargePrivilege  	存款优惠。1、首次存款送优惠，2、每次存款送优惠,3、首次优惠但可放弃优惠，4、每次优惠但可放弃优惠
# PreferenceMax  优惠上限
# PreferenceLine 达多少量
# PreferencePercent 优惠百分比
# IsFirst 首次存款
import unittest
from Libs.data_util import write_result_data_to_excel
from Libs.data_util import get_case_from_excel
from ddt import ddt,data
from Verify.Finance.FinanceVerify import *
from Libs.CheckRresult_Util import *
from Libs.Time_Util import get_time_stamp
@ddt
class Api_Finance_GetPreferenceNewConfig(unittest.TestCase):
    run_rules_dic = Config().get_run_rules_config()
    run_rules_dic.update({'ScriptName': os.path.basename(__file__)})
    datas = get_case_from_excel(Config().case_data_file_path, ['Finance'], run_rules_dic, 'Finance')
    def setUp(self) -> None:
        logging.info('启动脚本文件 :  {}'.format(os.path.basename(__file__)))
        self.account = Config().get_ini_value('Global_ini', 'WebUserName')
        self.password = Config().get_ini_value('Global_ini', 'WebPwd')

    @data(*datas)
    def test_Finance_GetPreferenceNewConfig(self,datas):
        self._testMethodDoc = datas['CaseName']
        logging.info('开始执行用例： {} ( {} )'.format(self._testMethodDoc, self._testMethodName))
        logging.info('=======================调用【用户登录】接口====================================')
        self.LoginSessionID = login_api(self.account, self.password)
        if not self.LoginSessionID:
            logging.error('登录失败，请检查登录接口是否异常！')
        self.type = 0 if datas['NewVerifParmsData']['Type'] == 1 else 1 # 根据测试数据type类型来决定获取通道的类型 测试数据type-1为线下/2为线上 -paytype获取通道时0为线下/1为线上
        payment_info = get_finance_paymentindex(LoginSessionID=self.LoginSessionID, paytype=self.type)
        logging.info('获取通道ID:{},获取通道名称：{}'.format(payment_info['ID'], payment_info['PayType']))
        # 返回单个可用商户字典信息
        payment_data = payment_PreferenceNewConfig(LoginSessionID=self.LoginSessionID,id=payment_info['ID'],isonline=payment_info['Type'],return_data=True)
        # 可用支付商字段信息 ID 通道ID/MaxAmount 最大存款金额/MinAmount  	最小存款金额/IsCharge 是否需要手续费/Charge 手续费比例/IsDepositAddRandom 是否充值时增加随机金额（0.00-0.08） /
        # WayType 通道类型。0、全部通道；1、扫码支付；2、客户端支付/FIsShowShortcut 是否显示金额快捷方式/FShortcutSet 金额快捷设置/OrderNumber 当前交易的订单号/Number 附言码
        logging.info('=======================调用【获取支付商优惠设置】接口====================================')
        datas['NewVerifParmsData'].update({"CashConfigId":payment_data['ID'],"_":get_time_stamp()})
        self.actual_result = http_api_requests('充值提现.获取支付商优惠设置', Headers={"LoginSessionID": self.LoginSessionID},
                                               NewVerifParmsData=datas['NewVerifParmsData'])
        self.expected_result = datas['ExpectResult']
        result = None
        try:
            check_result(self.expected_result, self.actual_result)
            result = 'pass'
        except InterfaceVerifyError:
            result = 'false'
        finally:
            write_result_data_to_excel(Config().case_data_file_path, 'Finance', 'ID', datas['ID'], result)
        print(get_json_value(self.actual_result,'/Data'))
    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    set_log()
    unittest.main()


