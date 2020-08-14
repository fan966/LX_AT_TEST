# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 线上充值
import unittest
from Libs.data_util import write_result_data_to_excel
from Libs.data_util import get_case_from_excel
from ddt import ddt,data
from Verify.Finance.FinanceVerify import *
from Libs.CheckRresult_Util import *
from Libs.Random_util import RandomUtil
from Libs.Time_Util import *
@ddt
class Api_Finance_GoPay(unittest.TestCase):
    r = RandomUtil()
    run_rules_dic = Config().get_run_rules_config()
    run_rules_dic.update({'ScriptName': os.path.basename(__file__)})
    datas = get_case_from_excel(Config().case_data_file_path, ['Finance'], run_rules_dic, 'Finance')

    def setUp(self) -> None:
        logging.info('启动脚本文件 :  {}'.format(os.path.basename(__file__)))
        self.account = Config().get_ini_value('Global_ini', 'WebUserName')
        self.password = Config().get_ini_value('Global_ini', 'WebPwd')

    @data(*datas)
    def test_Finance_GoPay(self, datas):
        self._testMethodDoc = datas['CaseName']
        logging.info('开始执行用例： {} ( {} )'.format(self._testMethodDoc, self._testMethodName))
        logging.info('=======================调用【用户登录】接口====================================')
        self.LoginSessionID = login_api(self.account, self.password)
        if not self.LoginSessionID:
            logging.error('登录失败，请检查登录接口是否异常！')
        # 获取导航通道-线上
        payment_info = get_finance_paymentindex(LoginSessionID=self.LoginSessionID,paytype=1)
        logging.info('获取通道ID:{},获取通道名称：{}'.format(payment_info['ID'], payment_info['PayType']))
        # 获取导航通道下可用商户字典信息
        payment_data = payment_PreferenceNewConfig(LoginSessionID=self.LoginSessionID,id=payment_info['ID'],isonline=payment_info['Type'],return_data=True)
        print('获取商户字典信息'+'\n',json.dumps(payment_data,indent=4))
        # 获取通道优惠设置
        preferenceNewConfig = get_payment_PreferenceNewConfig(LoginSessionID=self.LoginSessionID,Type=2,CashConfigId=payment_data['ID'])
        print('获取商户优惠配置信息' + '\n', json.dumps(preferenceNewConfig, indent=4))
        # 线上充值
        # 金额判断
        Amount = self.r.get_random_int(payment_data['MinAmount'],payment_data['MaxAmount']) if not payment_data['FIsShowShortcut'] else int(random.choice(payment_data['FShortcutSet'].split(',')))
        logging.info('=======================调用【线上充值】接口====================================')
        datas['NewVerifParmsData'].update({"LoginSessionID":self.LoginSessionID,"paymentId":payment_data['ID'],"amount":Amount,"wayType":payment_data['WayType']})
        self.actual_result = http_api_requests('充值提现.线上充值', Headers={"LoginSessionID": self.LoginSessionID},NewVerifParmsData=datas['NewVerifParmsData'])
        # 手续费判断
        IsCharge = payment_data['IsCharge']
        if IsCharge:
            Charge = Amount*payment_data['Charge']
        else:
            Charge = 0
        # 优惠判断
        preference_amount = 0
        if preferenceNewConfig['RechargePrivilege'] == 1:
            if preferenceNewConfig['IsFirst']:
                if Amount < preferenceNewConfig['PreferenceLine']:
                    preference_amount = 0
                else:
                    preference_amount = Amount * preferenceNewConfig['PreferencePercent'] / 100
                    if preference_amount >= preferenceNewConfig['PreferenceMax'] and preferenceNewConfig['PreferenceMax']!=0.0:
                        preference_amount = preferenceNewConfig['PreferenceMax']
            else:
                preference_amount = 0
        elif preferenceNewConfig['RechargePrivilege'] == 2:
            if Amount >= preferenceNewConfig['PreferenceLine']:
                preference_amount = Amount * preferenceNewConfig['PreferencePercent'] / 100
                if preference_amount >= preferenceNewConfig['PreferenceMax'] and preferenceNewConfig['PreferenceMax']!=0.0:
                    preference_amount = preferenceNewConfig['PreferenceMax']
        elif preferenceNewConfig['RechargePrivilege'] == 3:
            if preferenceNewConfig['IsFirst']:
                if Amount >= preferenceNewConfig['PreferenceLine']:
                    preference_amount = Amount * preferenceNewConfig['PreferencePercent'] / 100
                    if preference_amount >= preferenceNewConfig['PreferenceMax'] and preferenceNewConfig['PreferenceMax']!=0.0:
                        preference_amount = preferenceNewConfig['PreferenceMax']
        elif preferenceNewConfig['RechargePrivilege'] == 4:
            if Amount >= preferenceNewConfig['PreferenceLine']:
                preference_amount = Amount * preferenceNewConfig['PreferencePercent'] / 100
                if preference_amount >= preferenceNewConfig['PreferenceMax'] and preferenceNewConfig['PreferenceMax']!=0.0:
                    preference_amount = preferenceNewConfig['PreferenceMax']
        else:
            raise ('优惠数据返回有误，请检查接口数据')

        # 充值记录检查
        end_time, start_time = get_nowday_and_yestday()
        self.actual_result = http_api_requests('充值提现.充值记录', Headers={"LoginSessionID": self.LoginSessionID},NewVerifParmsData={"EndTime":end_time,"StartTime":start_time,"OrderNum":payment_data['OrderNumber']})
        self.actual_result = get_json_value(self.actual_result, '/Data/ChargeRecordList')
        datas['ExpectResult'].update({"SerialNumber":str(payment_data['OrderNumber']),"ActualAmount":float(Amount + preference_amount - Charge)})
        self.expected_result = datas['ExpectResult']
        logging.error('充值成功：充值原始金额：{}，存款优惠：{}，入款手续费：{}，实际充值金额：{}，充值订单号：{}'.format(Amount, preference_amount, Charge,Amount + preference_amount - Charge,payment_data['OrderNumber']))

        # 写入结果
        result = None
        try:
            check_result(self.expected_result, self.actual_result[0])
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