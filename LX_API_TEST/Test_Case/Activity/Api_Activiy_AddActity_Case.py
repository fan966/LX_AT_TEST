# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 参加活动接口
# writeer ： Fan
# time ： 2020-7-24
import unittest
from Libs.data_util import write_result_data_to_excel
from Libs.data_util import get_case_from_excel
from ddt import ddt,data
from Verify.Activity.ActiviyVerifty import *
@ddt
class Api_Activiy_AddActity(unittest.TestCase):
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
        logging.info('=======================调用【后台添加活动接口】接口====================================')
        activity_name = Ag_AddActity_from_api()
        if not activity_name:
            logging.error('活动名称获取失败！')
            raise
        activity_data = get_activity_data_from_api(LoginSessionID=self.LoginSessionID, ActivityType=1,FActivitySubTypeId=None, return_data=False)
        activity_id = []
        for activity in activity_data:
            if activity['活动名称'] == activity_name:
                activity_id.append(activity['活动ID'])
        logging.info('=======================调用【参加活动】接口====================================')
        datas['NewVerifParmsData'].update({"ActityID":activity_id[0]})
        self.actual_result = http_api_requests('活动相关.参加活动', Headers={"LoginSessionID":self.LoginSessionID},NewVerifParmsData=datas['NewVerifParmsData'])
        self.expected_result = datas['ExpectResult']
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