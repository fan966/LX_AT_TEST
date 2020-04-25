# -*-coding:utf-8-*-
from Libs.cnfg_util import config_ini
import unittest
import logging
from PO.pageaction.log_action import Login
from Libs.webdriver import WebDriver
from PO.common.cs_data_excel_util import login_info
from PO.pageaction.top_up_action import *
from PO.pageaction.ag_offline_action import *
from Libs.log_util import set_log
from PO.common.cs_excel_util import *
@unittest.skipIf(excel_test_classmod('AgOfflineTestCase'),'AgOfflineTestCase mod is skip')
class AgOfflineTestCase(unittest.TestCase):
    browesr_name = config_ini('config.ini', 'default', 'browesr_name')
    env_type = config_ini('config.ini', 'default', 'env_type')
    skin = config_ini('config.ini', 'default', 'skin')
    loginfo = login_info(env_type,skin,'前端')
    first_financial = config_ini('agmod.ini', 'menu', 'first_financial')
    second_offline = config_ini('agmod.ini', 'menu', 'second_offline')


    def setUp(self):
        logging.info('启动测试脚本文件： {}.py'.format(self.__module__))
        WebDriver.start_browser(self.browesr_name)
        self.driver = WebDriver().get_driver()
        # 前台造数据
        logging.info("【INFO】登录前台环境准备公司入款数据......")
        Login(self.driver).login_page(self.env_type, self.skin, '前端')
        Us_Center_action(self.driver).to_top_page()
        TopUp(self.driver).random_offline_top()

        # 后台登录
        Login(self.driver).login_page(self.env_type, self.skin, '后台')
        AgHome(self.driver).close_ag_pop()
        # 点击财务管理-公司入款栏目
        AgHome(self.driver).swith_mod(self.first_financial,self.second_offline)
        # 点击进入公司入款栏目
        AgHome(self.driver).swith_table(self.second_offline)
        # 下面一行用于测试
        #AgOffline(cls.driver).check_is_page()
        # 调用公司入款对象-输入用户名-拿到订单号-唯一标识
        self.order_number = AgOffline(self.driver).get_order_number(self.loginfo['user'])




    def tearDown(self):
        WebDriver().driver_quit()

    @unittest.skipIf(excel_test_case(2, 'test1_offline_confirm'), 'test1_offline_confirm case is skip')
    def test1_offline_confirm(self):
        '''
        公司入款审核确认
        :return:
        '''

        logging.info('【INFO】执行case【公司入款审核】【{}】'.format(self._testMethodName))
        flag = AgOffline(self.driver).offline_confirm(self.order_number)
        self.assertTrue(flag,'case执行失败,公司入款审核异常，请检查')

    @unittest.skipIf(excel_test_case(2, 'test2_offline_lock'), 'test2_offline_lock case is skip')
    def test2_offline_lock(self):
        '''
        公司入款锁定
        :return:
        '''

        logging.info('【INFO】执行case【公司入款锁定】【{}】'.format(self._testMethodName))
        flag = AgOffline(self.driver).offline_lock(self.order_number)
        self.assertTrue(flag, 'case执行失败,公司入款锁定异常')

    @unittest.skipIf(excel_test_case(2, 'test3_offline_cel'), 'test3_offline_cel case is skip')
    def test3_offline_cel(self):
        '''
        公司入款取消
        :return:
        '''
        logging.info('【INFO】执行case【公司入款取消】【{}】'.format(self._testMethodName))
        flag = AgOffline(self.driver).offline_cel(self.order_number)
        self.assertTrue(flag, 'case执行失败,公司入款取消异常')



if __name__ == "__main__":
    # suite = unittest.TestSuite()
    # suite.addTest(AgOfflineTestCase("test_top1"))
    # unittest.TextTestRunner.run(suite)
    unittest.main()