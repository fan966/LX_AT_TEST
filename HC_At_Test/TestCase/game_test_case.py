# -*-coding:utf-8-*-
import unittest
from PO.pageaction.log_action import Login
from Libs.webdriver import WebDriver
from PO.common.cs_data_excel_util import login_info
from PO.pageaction.us_center_action import *
from ddt import ddt,file_data,data
from PO.common.common_util import *
from PO.pageaction.game_action import *
from Libs.cnfg_util import config_ini
from PO.common.cs_excel_util import *
@ddt
@unittest.skipIf(excel_test_classmod('GameTestCase'),'GameTestCase mod is skip')
class GameTestCase(unittest.TestCase):
    # 配置项循环数/num
    num = config_ini('game.ini', 'game', 'number')
    offical_path = get_project_path() + '\\Data\\game\\officialgame.yaml'
    browesr_name = config_ini('config.ini', 'default', 'browesr_name')
    env_type = config_ini('config.ini', 'default', 'env_type')
    skin = config_ini('config.ini', 'default', 'skin')
    loginfo = login_info(env_type,skin,'前端')
    game_path = get_project_path() + '\\'
    data_path = get_project_path() + '\\Data\\game\\hc_game.xls'
    datas = ExcelUtil(data_path).read_excel_addlist()

    @classmethod
    def setUpClass(cls):
        logging.info('启动测试脚本文件： {}.py'.format(cls.__module__))
        WebDriver.start_browser(cls.browesr_name)
        cls.driver = WebDriver().get_driver()
        Login(cls.driver).login_page(cls.env_type,cls.skin,'前端')


    @classmethod
    def tearDownClass(cls):
        WebDriver().driver_quit()

    @file_data(offical_path)
    @unittest.skipIf(excel_test_case(1, 'test1_officialgame'), 'test1_officialgame case is skip')
    def test1_officialgame(self,data):
        '''
        官方随机/配置游戏文件
        :param data:
        :return:
        '''

        logging.info('开始执行用例： {}'.format(self._testMethodName))
        logging.info("【功能检查】官方游戏下注")
        Us_Center_action(self.driver).to_officialgame_page(data)

        Gameing(self.driver).official_gameing()


    # @file_data(tradition_path)
    # @unittest.skipIf(excel_test_case(1, 'test2_traditiongame'), 'test2_traditiongame case is skip')
    # def test2_traditiongame(self,data):
    #     '''
    #     传统随机/配置游戏文件
    #     :param data:
    #     :return:
    #     '''
    #     logging.info('开始执行用例： {}'.format(self._testMethodName))
    #     logging.info("【功能检查】传统游戏下注")
    #     Us_Center_action(self.driver).to_traditiongame_page(data)


    @data(*datas)
    @unittest.skipIf(excel_test_case(1, 'test3_game_playtype'), 'test3_game_playtype case is skip')
    def test3_game_playtype(self,datas):
        '''
        配置项玩法投注
        :return:
        '''

        logging.info('开始执行用例： {}'.format(self._testMethodName))
        logging.info("【功能检查】玩法配置项投注")
        Gameing(self.driver).official_excel_gamging(datas)







if __name__ == "__main__":
    unittest.main()


