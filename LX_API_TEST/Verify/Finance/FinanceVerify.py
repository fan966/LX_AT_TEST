# !/usr/bin/env python
# -*- coding: utf-8 -*-
from Verify.User.UserVerify import *
from Libs.Time_Util import get_time_stamp
from Libs.CheckRresult_Util import *
from Libs.Random_util import *
def get_finance_paymentindex(LoginSessionID=None,return_data=True,paytype=0):
    '''
    获取充值导航通道
    :param paytype: 获取通道类型 0 为线下转账  1为线上支付
    :param LoginSessionID: cookie
    :param return_data: 返回参数/为False时返回全部信息，Ture返回一条信息
    :return:
    '''
    LoginSessionID = login_api(Config().get_ini_value('Global_ini', 'WebUserName'),
                               Config().get_ini_value('Global_ini', 'WebPwd')) if not LoginSessionID else LoginSessionID
    logging.info('=======================调用【充值导航-可用通道】接口====================================')
    actual_result = http_api_requests('充值提现.充值导航', Headers={"LoginSessionID":LoginSessionID},NewVerifParmsData={})
    paymeng_data = get_payment_data_from_api_data(actual_result)
    paymeng_data = get_paytype_data(paymeng_data,paytype)

    return paymeng_data if not return_data else random.choice(paymeng_data) if paymeng_data else None


def get_payment_data_from_api_data(paymentIndex):
    '''
    分解充值导航通道数据/返回
    :param data: API接收数据
    :return:
    '''
    paymentIndex = get_json_value(paymentIndex, '/Data/PaymentList')
    payment_info = []
    for payment in paymentIndex:
        payment_dict = {}
        payment_dict.update({'ID': payment['ID']})
        payment_dict.update({'PayType': payment['PayType']})
        payment_info.append(payment_dict)
    return payment_info

def get_paytype_data(data,type):
    '''
    根据type返回不同支付数据
    :param data:
    :param type:
    :return:
    '''

    pay_data = []
    for pay_data_ in data:
        payment_ = {}
        if type == 0:
            if '转账' in pay_data_['PayType']:
                payment_.update({"ID":pay_data_['ID']})
                payment_.update({"PayType": pay_data_['PayType']})
                payment_.update({"Type": type})
                pay_data.append(payment_)

        elif type == 1:
            if '转账' not in pay_data_['PayType'] and 'VIP代理充值' not in pay_data_['PayType'] and '官方充值' not in pay_data_['PayType'] and '银商充值' not in  pay_data_['PayType']\
                    and '快速充值' not in pay_data_['PayType']:
                payment_.update({"ID":pay_data_['ID']})
                payment_.update({"PayType": pay_data_['PayType']})
                payment_.update({"Type": type})
                pay_data.append(payment_)
        else:
            raise ('支付类型传参有误，请检查paytype参数值！')
    return pay_data

def payment_PreferenceNewConfig(LoginSessionID=None,id=None,isonline=None,return_data = True):
    '''
    获取支付通道下可用支付商
    :param LoginSessionID:
    :param id: 导航通道ID
    :param isonline: 获取可用支付商类型 0线下 1线上
    :return:
    '''
    LoginSessionID = login_api(Config().get_ini_value('Global_ini', 'WebUserName'),
                               Config().get_ini_value('Global_ini', 'WebPwd')) if not LoginSessionID else LoginSessionID
    id = id
    isonline = isonline
    actual_result = http_api_requests('充值提现.获取可用支付通道', Headers={"LoginSessionID":LoginSessionID},NewVerifParmsData={"id":id,"isonline":isonline})
    pay_data = get_json_value(actual_result, '/Data')
    temp = '/OnlinePayment' if pay_data['OnlinePayment'] else '/OfflinePayment' # 判断支付商类型来获取线上线下可用支付商
    pay_data_ = get_json_value(pay_data, '{}'.format(temp))
    payment_info = []
    for payment_ in pay_data_:
        payment_.update({'OrderNumber': pay_data['OrderNumber']})
        payment_.update({'Number': pay_data['Number']})
        payment_info.append(payment_)
    return payment_info if not return_data else random.choice(payment_info) if payment_info else None

def get_payment_PreferenceNewConfig(LoginSessionID=None,Type=None,CashConfigId=None,):
    '''
    获取支付商优惠参数配置
    :param LoginSessionID:
    :param Type: 1为线下/2为线上
    :param CashConfigId: 支付商ID
    :return:
    '''
    actual_result = http_api_requests('充值提现.获取支付商优惠设置', Headers={"LoginSessionID": LoginSessionID},
                                      NewVerifParmsData={"Type":Type,"CashConfigId":CashConfigId,"_":get_time_stamp()})
    preferenceNewConfig = get_json_value(actual_result, '/Data')

    return preferenceNewConfig

def FShortcutSet_amount(data):
    '''
    快捷金额随机选择
    :param data:
    :return:
    '''

# 提款前置数据构成方法
def get_GetEncashment_data(LoginSessionID=None):
    '''
    提款基础数据获取
    返回手续费/银行卡ID/出款设置基础数据
    :param LoginSessionID:
    :return:
    '''
    r = RandomUtil()
    LoginSessionID = login_api(Config().get_ini_value('Global_ini', 'WebUserName'),
                               Config().get_ini_value('Global_ini', 'WebPwd')) if not LoginSessionID else LoginSessionID
    logging.info('=======================调用【获取提现基础数据】接口====================================')
    actual_result = http_api_requests('充值提现.获取提现基础数据', Headers={"LoginSessionID": LoginSessionID},
                                           NewVerifParmsData={})
    expected_result = {"Status":True,"Info":"","Code":0}
    check_result(expected_result, actual_result)
    WithdrawI_data = get_json_value(actual_result, '/Data') # 获取基础出款数据
    Charge_data = get_json_value(actual_result, '/Data/ChargeModel') # 获取手续费数据
    BankList = get_json_value(actual_result, '/Data/BankList') # 获取银行卡ID
    bank_card_id = []
    for bank_data in BankList:
        bank_card_id.append(bank_data['FID'])
    logging.info('=======================调用【获取提现基础数据】接口====================================')
    actual_result = http_api_requests('用户相关.获取用户基础数据', Headers={"LoginSessionID": LoginSessionID},
                                      NewVerifParmsData={})
    expected_result = {"Status": True, "Info": "", "Code": 0}
    check_result(expected_result, actual_result)
    Balance = get_json_value(actual_result, '/Data/CreditBalance') # 获取当前用户余额
    # 行政费和优惠扣除金额和手续费
    passRebate_amount = WithdrawI_data['TotalDeductionRebate'] # 优惠扣除金额
    passCom_amount = WithdrawI_data['TotalDeductionAdmincharge'] # 行政费

    # 构建提款余额
    while True:
        amount = r.get_random_int(WithdrawI_data['EncashmentMin'],WithdrawI_data['EncashmentMax'])
        if amount > passRebate_amount + passCom_amount:
            if amount < int(float(Balance)):
                break

    # 计算手续费
    if passCom_amount: # 是否行政费
        charge = 0
    else:
        if Charge_data['FreeChargeCount'] == 0: # 收取手续费次数
            if Charge_data['DeductionCharge']: # 是否收取手续费
                if Charge_data['IsPercent']:
                    charge = amount * Charge_data['EncashmentCharge']
                else:
                    charge = Charge_data['EncashmentCharge']
                if charge >= Charge_data['MaxAmount']:
                    charge = Charge_data['MaxAmount']
            else:
                charge = 0
        else:
            charge = 0
    return amount,charge,random.choice(bank_card_id)







if __name__ == '__main__':
    set_log()
    # data = get_finance_paymentindex(return_data=False,paytype=0)
    # print(data)
    # data = payment_PreferenceNewConfig(id=0,isonline=0,return_data=False)
    # print(data)
    # print(len(data))
    # temp = {"FShortcutSet":"50,100,200,500,1000,2000,5000,10000,20000"}
    # print()
    # post
    # {"orderNumber":"45208102350131220003","amount":1000,"userBankId":1,"companyCardId":133191,"date":"2020/08/10 19:50:25","way":"网银转账","realName":"11","place":"","bankId":133191,"choicePre":true}
    # get
    # {"orderNumber":"45308102348429170002","amount":200,"userBankId":44,"CompanyCardId":133860,"date":"2020/08/10 19:49:21","way":"","realName":"Qq","place":"","bankId":133860,"choicePre":true,"CardNo":"15154512784","_":1597074569436}
    # [{'ID': 0, 'PayType': '银行卡转账'},
    # {'ID': 7, 'PayType': '快速充值'},
    # {'ID': 99, 'PayType': '快速充值'},
    # {'ID': 3, 'PayType': '支付宝转账'},
    # {'ID': 2, 'PayType': '微信'},
    # {'ID': 1, 'PayType': '在线支付'},
    # {'ID': 5, 'PayType': 'QQ钱包'},
    # {'ID': 5, 'PayType': 'QQ钱包转账'},
    # {'ID': 66, 'PayType': 'VIP代理充值'},
    # {'ID': 9, 'PayType': '百度'},
    # {'ID': 14, 'PayType': '云闪付'},
    # {'ID': 11, 'PayType': '微信条形码'},
    # {'ID': 8, 'PayType': '京东'},
    # {'ID': 15, 'PayType': '企业支付宝'},
    # {'ID': 12, 'PayType': '支付宝条形码'},
    # {'ID': 199, 'PayType': '官方充值'}]
    amount,charge,id = get_GetEncashment_data()
    print(amount,charge,id)

