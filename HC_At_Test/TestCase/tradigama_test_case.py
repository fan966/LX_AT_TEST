# -*-coding:utf-8-*-
import unittest
from PO.pageaction.log_action import Login
from Libs.webdriver import WebDriver
from ddt import ddt,file_data,data
from Libs.cnfg_util import config_ini
from PO.common.common_util import *
from PO.pageaction.us_center_action import *
from PO.pageaction.tradi_game_action import TradiGame
from PO.pageaction.game_time_action import BetGameTime
from threading import Thread
from PO.common.cs_excel_util import *
@ddt
@unittest.skipIf(excel_test_classmod('TradiGameTestCase'),'TradiGameTestCase mod is skip')
class TradiGameTestCase(unittest.TestCase):
    tradition_path = get_project_path() + '\\Data\\game\\traditiongame.yaml'
    browesr_name = config_ini('config.ini', 'default', 'browesr_name')
    env_type = config_ini('config.ini', 'default', 'env_type')
    skin = config_ini('config.ini', 'default', 'skin')
    data_path = get_project_path() + '\\Data\\game\\hc_game.xls'
    datas = ExcelUtil(data_path,1).read_excel_addlist()

    @classmethod
    def setUpClass(cls):
        WebDriver.start_browser(cls.browesr_name)
        cls.driver = WebDriver().get_driver()
        Login(cls.driver).login_page(cls.env_type,cls.skin,'前端')

    @classmethod
    def tearDownClass(cls):
        WebDriver().driver_quit()

    @file_data(tradition_path)
    @unittest.skipIf(excel_test_case(1,'test1_traditiongame'), 'test1_traditiongame case is skip')
    def test1_traditiongame(self, data):
        '''
        传统随机/配置游戏文件
        :param data:
        :return:
        '''
        logging.info('开始执行用例： {}'.format(self._testMethodName))
        logging.info("【功能检查】传统游戏下注")
        t = Thread(target=BetGameTime(self.driver).get_hc_game_time)
        t.start()
        Us_Center_action(self.driver).to_traditiongame_page(data)
        TradiGame(self.driver).random_play()

    @data(*datas)
    @unittest.skipIf(excel_test_case(1, 'test2_excel_traditiongame'), 'test2_excel_traditiongame case is skip')
    def test2_excel_traditiongame(self,datas):
        '''
        信用玩法excel文件配置下注
        :return:
        '''
        logging.info('开始执行用例： {}'.format(self._testMethodName))
        logging.info("【功能检查】传统游戏下注")
        t = Thread(target=BetGameTime(self.driver).get_hc_game_time)
        t.start()
        TradiGame(self.driver).excel_tradi_gameing(datas)



if __name__ == "__main__":

    unittest.main()


