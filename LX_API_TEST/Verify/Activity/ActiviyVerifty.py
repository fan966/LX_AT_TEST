# !/usr/bin/env python
# -*- coding: utf-8 -*-
from Verify.User.UserVerify import login_api
from Config.Config import *
from Verify.Activity.fromdata_util import *
from Libs.log_util import set_log
from Libs.http_requests import *
from Libs.Errors import *
from Libs.CheckRresult_Util import check_result
from Verify.User.UserVerify import *
def get_activity_data_from_api(LoginSessionID=None,ActivityType=None,FActivitySubTypeId=None,return_data=True):
    '''
    return_data: 为False时返回全部信息，Ture返回一条信息
    接口获取活动数据
    # ActivityType 为1的时候-表示红利活动，为2时表示-页面活动（页面活动不可参加），为3时-表示签到活动
    # FActivitySubTypeId  1=注册活动,2=登录活动,3=充值流水活动,4=投注活动,5=红包活动,6=红包雨活动,7=大转盘活动，9=余额宝活动，11=签到活动
    :return:
    '''
    LoginSessionID = login_api(Config().get_ini_value('Global_ini', 'WebUserName'),Config().get_ini_value('Global_ini', 'WebPwd')) if not LoginSessionID else LoginSessionID
    FActivitySubTypeId = 2 if not FActivitySubTypeId else FActivitySubTypeId
    ActivityType = 2 if not ActivityType else ActivityType
    logging.info('=======================调用【获取活动列表】接口====================================')
    activity_result =  http_api_requests('活动相关.获取活动列表', Headers={"LoginSessionID":LoginSessionID},NewVerifParmsData={})
    expected_result = {"Status":True,"Info":"","Code":0}
    check_result(expected_result,activity_result)
    activiy_data = get_json_value(activity_result, '/Data')
    activiy_info = []
    for game_data in activiy_data:
        activiy_list = {}
        if game_data['BalanceActivityDetails']:
            for game_dict_data in game_data['BalanceActivityDetails']:  # 余额宝活动数据
                activiy_dict = {}
                activiy_dict.update({"活动ID": game_data['FId']})
                activiy_dict.update({"活动名称": game_data['FName']})
                activiy_dict.update({"余额宝方案ID": game_dict_data['FId']})
                activiy_dict.update({"余额宝方案名称": game_dict_data['FName']})
                activiy_dict.update({"活动大类": game_data['ActivityType']})
                activiy_dict.update({"活动类型": game_data['FActivitySubTypeId']})
                activiy_info.append(activiy_dict)
        else:
            activiy_list.update({"活动ID": game_data['FId']})
            activiy_list.update({"活动名称": game_data['FName']})
            activiy_list.update({"活动大类": game_data['ActivityType']})
            activiy_list.update({"活动类型": game_data['FActivitySubTypeId']})
            activiy_info.append(activiy_list)
    return_activity_data = []
    for activity in range(len(activiy_info)):
        if activiy_info[activity]['活动大类'] == ActivityType:
            if activiy_info[activity]['活动类型'] == FActivitySubTypeId:
                return_activity_data.append(activiy_info[activity])

    return return_activity_data if not return_data else random.choice(return_activity_data) if return_activity_data else None

def Ag_AddActity_from_api(LoginSessionID=None):
    '''
    后台添加登录活动
    返回活动名称
    :return:
    '''
    LoginSessionID = ag_login_api(Config().get_ini_value('Global_ini', 'AgUserName'),Config().get_ini_value('Global_ini', 'AgPwd')) if not LoginSessionID else LoginSessionID
    logging.info('=======================调用【后台添加活动】接口====================================')
    url = 'http://csdqtjcag.lx901.com/ActivesManage/AddActity'
    file = login_activity_fromdata()
    headers = {"LoginSessionID":LoginSessionID}
    activity_result = requests.post(url,files=file,cookies=headers,verify=False,allow_redirects=False)
    expected_result = {"infor":"活动添加成功","status":True}
    try:
        check_result(expected_result,activity_result.json())
        result = file['FName'][1]
        logging.info('新增活动成功，活动名称：{}'.format(file))
    except InterfaceVerifyError:
        result = None
        logging.info('新增活动失败')
    return result








if __name__ == '__main__':
    set_log()
    # print(get_activity_data_from_api(ActivityType=1,FActivitySubTypeId=2,return_data=True))
    #Ag_AddActity_from_api()
    # data = get_activity_data_from_api(ActivityType=1,FActivitySubTypeId=None,return_data=False)
    # print(data)
    name = Ag_AddActity_from_api()
    print(name)