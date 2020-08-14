# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 主要查询一下三个活动
# type 活动类型: 5 红包活动 、6 红包雨活动 、7 大转盘活动
# HasActivity 是否有活动
# ActivityId 活动ID
import unittest
from Libs.data_util import write_result_data_to_excel
from Libs.data_util import get_case_from_excel
from ddt import ddt,data
from Libs.CheckRresult_Util import *
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
        self.actual_result = http_api_requests('活动相关.查询是否有活动', Headers={"LoginSessionID": self.LoginSessionID},NewVerifParmsData={})
        self.expected_result = datas['ExpectResult']
        activiy_info = []
        for activiy_data in get_json_value(self.actual_result,'/Data'):
            activiy_dict = {}
            if activiy_data['HasActivity']:
                if activiy_data['Type'] == 5:
                    activiy_dict.update({'红包活动ID':activiy_data['ActivityId']})
                elif activiy_data['Type'] == 6:
                    activiy_dict.update({'红包雨活动ID': activiy_data['ActivityId']})
                else:
                    activiy_dict.update({'大转盘活动ID': activiy_data['ActivityId']})
            activiy_info.append(activiy_dict)
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