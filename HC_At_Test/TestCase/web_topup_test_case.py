# -*-coding:utf-8-*-
from Libs.cnfg_util import config_ini
import unittest
import logging
from PO.pageaction.log_action import Login
from Libs.webdriver import WebDriver
from PO.pageaction.us_center_action import Us_Center_action
from PO.pageaction.top_up_action import TopUp
from ddt import ddt, file_data
from PO.common.common_util import *
import HTMLTestRunnerCN
from PO.pageaction.withdraw_action import Withdram
from PO.common.cs_excel_util import *
@ddt
@unittest.skipIf(excel_test_classmod('WebTopUpTestCase'),'WebTopUpTestCase mod is skip')
class WebTopUpTestCase(unittest.TestCase):
    # 类属性（环境信息：浏览器，环境，皮肤）
    file_path = get_project_path() + "\\Data\\financial\\touup_online.yaml"
    browesr_name = config_ini('config.ini','default','browesr_name')
    env_type = config_ini('config.ini','default','env_type')
    skin = config_ini('config.ini','default','skin')
    online_top = config_ini('financial.ini','web','pmtp') # 配置文件支付方式
    withdram_file_path = get_project_path() + "\\Data\\financial\\withdram.yaml"
    # 根据环境信息获取登录信息（url，user，password）
    @classmethod
    def setUpClass(cls):
        logging.info('启动测试脚本文件： {}.py'.format(cls.__module__))
        WebDriver.start_browser(cls.browesr_name)
        cls.driver = WebDriver().get_driver()
        Login(cls.driver).login_page(cls.env_type,cls.skin,'前端')

    @classmethod
    def tearDownClass(cls):
        WebDriver().driver_quit()


    @file_data(file_path)
    @unittest.skipIf(excel_test_case(2,'test1_file_top'),'test1_file_top case is skip')
    def test1_file_top(self,data):
        '''
        配置文件yaml支付方式
        :param data:
        :return:
        '''
        flag = False
        logging.info('【INFO】[开始执行用例]{}'.format(self._testMethodName))
        datas = data.split(',')
        logging.info('【INFO】支付平台:'+datas[0]+'---'+"充值金额:"+datas[1])
        try:
            Us_Center_action(self.driver).to_top_page()
            print('进入充值页面成功')
            flag = TopUp(self.driver).check_pay(data)
        except Exception as err:
            logging.error(err)
        self.assertTrue(flag,"案例执行失败")

    @unittest.skipIf(excel_test_case(2, 'test2_ini_top'), 'test2_ini_top case is skip')
    def test2_ini_top(self):
        '''
        配置文件ini线上支付方式
        :return:
        '''
        logging.info('【INFO】[开始执行用例]{}'.format(self._testMethodName))

        Us_Center_action(self.driver).to_top_page()
        flag = TopUp(self.driver).random_online_top()
        self.assertTrue(flag,'案例执行失败')

    @unittest.skipIf(excel_test_case(2, 'test3_ini_offline'), 'test3_ini_offline case is skip')
    def test3_ini_offline(self):
        '''
        配置文件线下转账
        :return:
        '''
        logging.info('【INFO】[开始执行用例]{}'.format(self._testMethodName))
        Us_Center_action(self.driver).to_top_page()
        flga = TopUp(self.driver).random_offline_top()
        if flga == True:
            print('anlichenggong')
        else:
            print('2')
        self.assertTrue(flga,'案例执行失败')
    @file_data(withdram_file_path)
    @unittest.skipIf(excel_test_case(2, 'test4_file_withdraw'), 'test4_file_withdraw case is skip')
    def test4_file_withdraw(self,data):
        '''
        配置文件yaml格式提款
        :return:
        '''
        logging.info('【INFO】[开始执行用例]{}'.format(self._testMethodName))
        Us_Center_action(self.driver).to_withdraw_page()
        Withdram(self.driver).withdram1()
        Us_Center_action(self.driver).to_withdraw_page()
        flag = Withdram(self.driver).withdram(data)
        self.assertTrue(flag,'案例执行失败')










if __name__ == "__main__":
    suite = unittest.TestSuite()
    #suite.addTest(WebTopUpTestCase("test1_file_top"))
    suite.addTest(WebTopUpTestCase("test2_ini_top"))
    suite.addTest(WebTopUpTestCase("test3_ini_offline"))
    report_path = get_project_path() + '\\Report\\test_report\\Auto_test_reporting.html'
    f = open(report_path,'wb')
    runner = HTMLTestRunnerCN.HTMLTestRunner(stream=f, title='Lx自动化测试报告', tester='Fan', description='首次测试报告',verbosity=2)
    runner.run(suite)





