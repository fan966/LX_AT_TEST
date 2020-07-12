# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 获取游戏最新开盘期数
# 返回最新期数/开盘时间/封盘时间
# 期数ID/期数状态

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

@ddt
class Api_Game_GetNewPeriod_Case_01(unittest.TestCase):
    run_rules_dic = Config().get_run_rules_config()
    run_rules_dic.update({'ScriptName': os.path.basename(__file__)})
    datas = get_case_from_excel(Config().case_data_file_path, ['Game'], run_rules_dic, 'Game')
    def setUp(self) :
        logging.info('启动脚本文件 :  {}'.format(os.path.basename(__file__)))
        self.account = Config().get_ini_value('Global_ini','WebUserName')

        self.password = Config().get_ini_value('Global_ini','WebPwd')
    @data(*datas)
    def test_get_gameperiod(self,datas):
        self.testcasename = datas['CaseName']
        logging.info('开始执行用例： {} ( {} )'.format(datas['CaseName'], self._testMethodName))
        logging.info('=======================调用【用户登录】接口====================================')
        LoginSessionID = login_api(self.account, self.password)
        if not LoginSessionID:
            logging.error('登录失败，请检查登录接口是否异常！')
        logging.info('=======================调用【获取游戏最新开盘期数】接口====================================')
        self.actual_result = http_api_requests('游戏相关.获取游戏最新开盘期数', Headers={"LoginSessionID": LoginSessionID},NewVerifParmsData=datas['NewVerifParmsData'])
        self.expected_result = datas['ExpectResult']
        try:
            #print(type(self.actual_result))
            check_result(self.expected_result, self.actual_result)
            result = 'pass'
            json_data = get_json_value(self.actual_result,'/Data')
            json_period_data = json.loads(json_data, encoding='utf-8')

            print(json_period_data)
            # 本期期数
            current_period = json_period_data['fnumberofperiod']
            print(current_period)
            # 本期开盘时间
            start_time = json_period_data['fstarttime']
            print(start_time)
            # 本期封盘时间
            #end_time = json_period_data['fclosetime']
            # 期数状态 （0未开盘，1开盘中，2已封盘，3已开奖，4、已结算，5、返还金额）
            period_status = json_period_data['fstatus']
            print(period_status)
            # 游戏是否停售 ：false代表开售中，true代表停售中
            is_off_stop = json_period_data['fisstopseles']
            print(is_off_stop)
            # 期数ID
            fid = json_period_data['fid']
            print(fid)
            # print('本期期数:', current_period)
            # print('本期开盘时间:', start_time)
            # print('本期封盘时间:', end_time)
            # print('期数状态:', period_status)
            # print('游戏是否停售:', is_off_stop)
            # print('期数ID：', fid)
            # 六合彩特殊字段
            # 六合封盘时间
            liuhe_end_time = json_period_data['fspecialcodeclosetime']
            print(liuhe_end_time)


        except InterfaceVerifyError:
            result = 'false'
        finally:
            write_result_data_to_excel(Config().case_data_file_path, 'Game', 'ID', datas['ID'], result)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

w = {"PeriodId":"0","OrderList":"[{\"a\":2.0,\"c\":\"小\",\"i\":25333,\"k\":\"0\",\"m\":1,\"n\":1,\"t\":1,\"ts\":1593607662}]","GameId":"396"}