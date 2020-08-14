# !/usr/bin/env python
# -*- coding: utf-8 -*-
from Libs.Time_Util import *
from Libs.Random_util import RandomUtil
import requests
import json
r = RandomUtil()
def login_activity_fromdata():
    '''
    登录活动fromdata数据组织
    :return:
    '''
    file = {
        "act_type":(None,1),
        "bonus_type":(None,2),
        "act_status":(None,""),
        "ko_unique_1":(None,0),
        "FName":(None,"{}".format("Auto"+ r.get_random_info_str(4) + "活动")),
        "FAuditBeginTime":(None,"02:00:00"),
        "FAuditEndTime":(None,"02:00:00"),
        "FIntervalTime":(None,0),
        "FActivityImage":("haha.jpg", open("E:/tupian/haha.jpg", "rb"), "image/jpeg"),
        "FActivityImageEnroll":("haha.jpg", open("E:/tupian/haha.jpg", "rb"), "image/jpeg"),
        "FActivityPhoneImage":("haha.jpg", open("E:/tupian/haha.jpg", "rb"), "image/jpeg"),
        "FActivityPhoneImageEnroll":("haha.jpg", open("E:/tupian/haha.jpg", "rb"), "image/jpeg"),
        "FActivityPhoneImageHorizontal":(None,""),
        "FPopUpActivityImage":(None,""),
        "audit_cont":(None,4),
        "ip":(None,""),
        "saveItem":(None,False),
        "FActivityTypeId":(None,1),
        "FActivitySubTypeId":(None,2),
        "FRechargeMode":(None,1),
        "FGetMode":(None,2),
        "FIsShowCustomerService":(None,False),
        "FAutoJoin":(None,0),
        "FAPPActivityType":(None,0),
        "FAPPActivityWay":(None,0),
        "FActivityMode":(None,1),
        "FStatus":(None,1),
        "FBeginTime":(None,"{}".format(get_nowday_and_yestday()[1])),
        "FEndTime":(None,"{}".format(get_nowday_and_yestday()[0])),
        "FActivityContext":(None,0),
        "FAuditOption":(None,4),
        "FIsLimitPercent":(None,False),
        "FLimitPercent":(None,""),
        "FIsRebateLimit":(None,False),
        "FIsLimitIP":(None,False),
        "FIpArray":(None,""),
        "FVersion":(None,0),
        "FCodeType":(None,1),
        "FIsSetSingleAmount":(None,True),
        "stage":(None,""),
        "FSingleBonusAmount":(None,10),
        "FSingleBonusLimit":(None,10),
        "FIsSetTotalAmount":(None,False),
        "FBonusTotalAmount":(None,0),
        "FActivityListSort":(None,5),
        "FGameIds":(None,441),
        "FDomainName":(None,""),
        "ffirstagentids":(None,""),
        "FAccountReAmount":(None,""),
        "FAccountReCount":(None,""),
        "FAccountCurtReAmount":(None,""),
        "FAccountCurtReCount":(None,""),
        "FAccountRegisterStartDate":(None,""),
        "FAccountRegisterEndDate":(None,""),
        "homeView":(None,"haocai"),
        "FPhoneTemplates":(None,""),
        "FCycle":(None,0),
        "FIsReAmount":(None,False),
        "FIsBet":(None,False),
        "FReAmount":(None,0),
        "FTotalBet":(None,0),
        "FStyle":(None,1),
        "activitySignDetail":(None,'{"FirstForceDailog":0,"FDayRechargeNeed":"0","FDayRechargeType":"0","FDayRechargeMoney":"1","FDayBetNeed":"0","FDayBetMoney":"1","FRetroactiveEnable":0,"FRetroactiveType":"0","FRetroactiveMoney":"1","FSignSetJson":"[{\"SignDays\":\"1\",\"SignAward\":\"5\",\"SignLimit\":\"5\"}]"}'),
        "FReceiveNumber":(None,0),
        "FDescription":(None,""),
        "FHtmlDescription":(None,"Q"),
        "FMHtmlDescription":(None,"Q"),
    }
    return file


if __name__ == '__main__':
    file = login_activity_fromdata()
    print(file['FName'][1])
    # url = 'https://graph.baidu.com/upload?uptime=1589827612036'
    # res = requests.post(url, files=file, verify=False)
    # print(res.json())