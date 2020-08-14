# !/usr/bin/env python
# -*- coding: utf-8 -*-
# FId 活动ID
# FBeginTime 开始时间  FEndTime 结束时间
# ActivityType 为 2的时候 表示页面活动，隐藏参加活动按钮
# FActivitySubTypeId  1=注册活动,2=登录活动,3=充值流水活动,4=投注活动,5=红包活动,6=红包雨活动,7=大转盘活动，9=余额宝活动，11=签到活动
# FDescription 活动描述
import unittest
from Libs.data_util import write_result_data_to_excel
from Config.Config import *
import logging
from Libs.log_util import set_log
from Libs.data_util import get_case_from_excel
from ddt import ddt,data
from Libs.http_requests import *
from Libs.CheckRresult_Util import *
from Verify.User.UserVerify import login_api
from Verify.User.UserVerify import *
from Verify.Game.GameVerify import *
@ddt
class Api_Activity_GetActivityList(unittest.TestCase):
    run_rules_dic = Config().get_run_rules_config()
    run_rules_dic.update({'ScriptName': os.path.basename(__file__)})
    datas = get_case_from_excel(Config().case_data_file_path, ['Activity'], run_rules_dic, 'Activity')

    def setUp(self) -> None:
        logging.info('启动脚本文件 :  {}'.format(os.path.basename(__file__)))
        self.account = Config().get_ini_value('Global_ini', 'WebUserName')
        self.password = Config().get_ini_value('Global_ini', 'WebPwd')
    @data(*datas)
    def test_get_activitylist(self,datas):
        self._testMethodDoc = datas['CaseName']
        logging.info('开始执行用例： {} ( {} )'.format(self._testMethodDoc, self._testMethodName))
        logging.info('=======================调用【用户登录】接口====================================')
        self.LoginSessionID = login_api(self.account, self.password)
        if not self.LoginSessionID:
            logging.error('登录失败，请检查登录接口是否异常！')
        logging.info('=======================调用【获取活动列表】接口====================================')
        self.actual_result = http_api_requests('活动相关.获取活动列表', Headers={"LoginSessionID": self.LoginSessionID},NewVerifParmsData={})
        self.expected_result = datas['ExpectResult']
        activiy_data = get_json_value(self.actual_result,'/Data')
        activiy_info = []
        for game_data in activiy_data:
            activiy_list = {}
            if game_data['BalanceActivityDetails']:
               for game_dict_data in game_data['BalanceActivityDetails']: # 余额宝活动数据
                   activiy_dict = {}
                   activiy_dict.update({"活动ID": game_data['FId']})
                   activiy_dict.update({"活动名称": game_data['FName']})
                   activiy_dict.update({"余额宝方案ID": game_dict_data['FId']})
                   activiy_dict.update({"余额宝方案名称": game_dict_data['FName']})
                   activiy_dict.update({"活动大类": game_data['ActivityType']})
                   activiy_dict.update({"活动类型": game_data['FActivitySubTypeId']})
                   activiy_info.append(activiy_dict)

            else:
                activiy_list.update({"活动ID":game_data['FId']})
                activiy_list.update({"活动名称":game_data['FName']})
                activiy_list.update({"活动大类": game_data['ActivityType']})
                activiy_list.update({"活动类型": game_data['FActivitySubTypeId']})
                activiy_info.append(activiy_list)

        print(activiy_info)

        result = None
        try:
            check_result(self.expected_result, self.actual_result)
            result = 'pass'
        except InterfaceVerifyError:
            result = 'false'
        finally:
            write_result_data_to_excel(Config().case_data_file_path, 'Activity', 'ID', datas['ID'], result)
    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    set_log()
    unittest.main()