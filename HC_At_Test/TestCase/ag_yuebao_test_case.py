# -*- coding:utf-8 -*-
import logging
import unittest
from Libs.log_util import set_log
from PO.common.cs_excel_util import *
from Libs.cnfg_util import config_ini
from Libs.webdriver import WebDriver
from PO.pageaction.log_action import Login
from PO.pageaction.ag_yuebao_activ import *
from PO.pageaction.web_yuebao_action import *
from PO.common.cs_data_excel_util import login_info
@unittest.skipIf(excel_test_classmod('AgYueBaoTestCase'),'AgYueBaoTestCase is skip')
class AgYueBaoTestCase(unittest.TestCase):
    browesr_name = config_ini('config.ini', 'default', 'browesr_name')
    env_type = config_ini('config.ini', 'default', 'env_type')
    skin = config_ini('config.ini', 'default', 'skin')
    datas_path = get_project_path() + '\\Data\\activ\\activ_data.xls'
    first = config_ini('agmod.ini', 'menu', 'first_activ')
    second = config_ini('agmod.ini', 'menu', 'second_zdyhd')
    datas = ExcelUtil(datas_path,1).read_excel_value_type_getdata()
    loninfo = login_info(env_type,skin,'前端')
    @classmethod
    def setUpClass(self):
        WebDriver.start_browser(self.browesr_name)
        self.driver = WebDriver().get_driver()
        # 后台添加余额宝数据
        ah = AgHome(self.driver)
        Login(self.driver).login_page(self.env_type,self.skin,'后台')
        ah.close_ag_pop()
        ah.swith_mod(self.first,self.second)
        ah.swith_table(self.second)
        self.ac_name = AgYueBao(self.driver).add_yuebao_activ(self.datas[0])


        # 前台
        Login(self.driver).login_page(self.env_type, self.skin, '前端')

    @classmethod
    def tearDownClass(cls):
        WebDriver().driver_quit()
    @unittest.skipIf(excel_test_case(3,'test1_min_amount'),'test1_min_amount is skip')
    def test1_min_amount(self):
        '''
        小于最低限额test
        :return:
        data = [['产品名称', '单笔限额', '计算周期(小时)', '利率', '利息上限', '续存次数', '剩余数量', '利息稽核倍数', '操作'], ['2', '2-23', '2小时', '2%', '2', '2', '1', '2倍', '立即购买'], ['3', '23-456', '4小时', '4%', '4', '4', '4', '4倍', '立即购买']]
        '''
        logging.info('开始执行case：{}'.format(self._testMethodName))
        logging.info('【功能检查】【余额宝购买金额小于最低限额】')
        self.data = WebYueBao(self.driver).get_web_yuebao_testdata(self.ac_name,self.loninfo)
        flag = WebYueBao(self.driver).min_amount_test(self.data)
        self.assertTrue(flag,'小于最低金额执行失败，请检查！')

    @unittest.skipIf(excel_test_case(3, 'test2_max_amount'), 'test2_max_amount is skip')
    def test2_max_amount(self):
        '''
        超过最大限额test
        :return:
        '''
        logging.info('开始执行case：{}'.format(self._testMethodName))
        logging.info('【功能检查】【余额宝购买金额超过最大限额】')
        self.data = WebYueBao(self.driver).get_web_yuebao_testdata(self.ac_name,self.loninfo)
        flag = WebYueBao(self.driver).max_amount_test(self.data)
        self.assertTrue(flag,'超过最大限额执行失败，请检查！')

    @unittest.skipIf(excel_test_case(3, 'test3_yuebao_success'), 'ttest3_yuebao_success is skip')
    def test3_yuebao_success(self):
        '''
        正确金额购买test
        :return:
        '''
        logging.info('开始执行case：{}'.format(self._testMethodName))
        logging.info('【功能检查】【正确金额购买】')
        self.data = WebYueBao(self.driver).get_web_yuebao_testdata(self.ac_name, self.loninfo)
        flag = WebYueBao(self.driver).amount_success(self.data)
        self.assertTrue(flag, '正确金额购买执行失败，请检查！')


if __name__ == "__main__":
    unittest.main()







