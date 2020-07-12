# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 获取首页分类游戏列表
# FID 游戏分类ID
# FCategoryName 分类名称 秒秒彩  ，分分彩等

# 返回 FGroupID 0为信用游戏，，3为官方游戏


import unittest
from Libs.data_util import write_result_data_to_excel
from Config.Config import *
import logging
from Libs.log_util import set_log
from Libs.data_util import get_case_from_excel
from ddt import ddt,data
from Libs.http_requests import http_api_requests,get_json_value
from Libs.CheckRresult_Util import *



@ddt
class Api_Game_GetCPYXGameList(unittest.TestCase):
    run_rules_dic = Config().get_run_rules_config()
    run_rules_dic.update({'ScriptName': os.path.basename(__file__)})
    datas = get_case_from_excel(Config().case_data_file_path, ['Game'], run_rules_dic, 'Game')
    def setUp(self) :
        logging.info('启动脚本文件 :  {}'.format(os.path.basename(__file__)))
    @data(*datas)
    def test_unit_001(self,datas):
        self.testcasename = datas['CaseName']
        logging.info('开始执行用例： {} ( {} )'.format(datas['CaseName'], self._testMethodName))
        logging.info('=======================调用【获取首页游戏列表接口】接口====================================')
        self.actual_result = http_api_requests('游戏相关.获取首页游戏列表',NewVerifParmsData=datas['NewVerifParmsData'])
        print(self.actual_result)
        self.expected_result = datas['ExpectResult']
        try:
            check_result(self.expected_result, self.actual_result)
            result = 'pass'
            data = get_json_value(self.actual_result,'/Data/GameData')
            game_id_list = []
            for game_data in data:
                # print(game_data)
                for game_list in game_data['GameCateList']:
                    if game_list['FCategoryName'] not in ['真人视讯','VR彩','体育竞技','电子游戏','棋牌']:
                        # 过滤掉信用游戏
                        if game_list['FGroupID'] ==0:
                            FCategoryName = game_list['FCategoryName']
                            for game_info in game_list['GameInfoList']:
                                game_dic = {}
                                #print(FCategoryName,game_info)
                                game_dic.update({FCategoryName:{game_info['FGameName']:game_info['FGameID']}})
                                game_id_list.append(game_dic)
            print(game_id_list)
            for game in game_id_list:
                if list(list(game.values())[0].values())[0] == 57:
                    print(game)
            # [{'秒秒彩': {511: '深圳秒秒彩'}}, {'秒秒彩': {363: '豪彩重庆刮刮乐'}}, {'秒秒彩': {396: '快三刮刮乐'}}, {'时时彩': {26: '重庆时时彩'}}, {'时时彩': {40: '新疆时时彩'}}, {'时时彩': {57: '北京时时彩'}}, {'时时彩': {222: '三方重庆时时彩'}}, {'时时彩': {507: '重疆时时彩'}}, {'时时彩': {567: '三方时时彩'}}, {'时时彩': {612: '幸运时时彩'}}, {'分分彩': {51: '韩式1.5分彩'}}, {'分分彩': {81: '腾讯分分彩'}}, {'分分彩': {86: '东京1.5分彩'}}, {'分分彩': {125: '极速分分彩'}}, {'分分彩': {180: '豪彩韩式1.5分彩'}}, {'分分彩': {182: '东京1.5分彩'}}, {'分分彩': {442: '豪彩1.5分11选5彩'}}, {'快三': {39: '江苏快三'}}, {'快三': {95: '安徽快3'}}, {'快三': {97: '河北快3'}}, {'快三': {103: '甘肃快3'}}, {'快三': {109: '湖北快3'}}, {'快三': {115: '广西快3'}}, {'快三': {198: '5分快三'}}, {'快三': {509: '奖期快三'}}, {'快三': {512: '测试复制江苏快三'}}, {'快三': {584: 'pland五分快三'}}, {'快三': {310: '豪彩 LX3分快三'}}, {'低频彩': {44: '排列三、五'}}, {'低频彩': {30: '福彩3D'}}, {'低频彩': {85: '上海时时乐'}}, {'低频彩': {566: '三方福彩3D'}}, {'11选5': {32: '山东11选5'}}, {'11选5': {45: '广东11选5'}}, {'11选5': {46: '江西11选5'}}, {'11选5': {50: '黑龙江11选5'}}, {'11选5': {74: '江苏11选5'}}, {'11选5': {320: 'LX1分11选5'}}, {'PC蛋蛋': {116: '幸运28'}}, {'PC蛋蛋': {119: '东京28'}}, {'PC蛋蛋': {121: '韩式28'}}, {'PC蛋蛋': {285: 'PC蛋蛋(自)'}}, {'PC蛋蛋': {371: '新斯洛伐克28期数模板'}}, {'PC蛋蛋': {4: '广东11选5'}}, {'极速彩': {166: '测试1.5分彩'}}, {'极速彩': {222: '三方重庆时时彩'}}, {'极速彩': {237: '自研重庆'}}, {'极速彩': {284: '自研福彩3D'}}, {'PK拾': {231: '豪彩11选5'}}, {'PK拾': {29: '北京PK拾'}}, {'PK拾': {93: '幸运飞艇'}}, {'PK拾': {195: '5分pk拾'}}, {'PK拾': {202: '极速幸运飞艇1分彩'}}, {'PK拾': {204: '极速幸运飞艇2分彩'}}, {'PK拾': {206: '极速幸运飞艇3.5分彩'}}, {'PK拾': {476: '极速赛车'}}, {'PK拾': {190: '豪彩1分PK拾'}}, {'PK拾': {333: 'LX1分PK拾再名1'}}, {'PK拾': {334: '豪彩LX1.5分PK拾'}}, {'快乐彩': {63: '韩国快乐8'}}, {'快乐彩': {279: '自研快乐8'}}, {'快乐彩': {28: '北京快乐8'}}, {'快乐彩': {565: '三方官方快乐8'}}]

        except InterfaceVerifyError:
            result = 'false'
        finally:
            write_result_data_to_excel(Config().case_data_file_path, 'Game', 'ID', datas['ID'], result)


    def tearDown(self) :
        pass

if __name__ == '__main__':
    unittest.main()