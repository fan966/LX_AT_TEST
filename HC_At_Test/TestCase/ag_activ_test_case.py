# -*- coding:utf-8 -*-
from PO.pageaction.ag_activ_action import *
from PO.pageaction.log_action import Login
import unittest
from Libs.webdriver import WebDriver
from PO.common.cs_excel_util import *
from Libs.cnfg_util import config_ini
from Libs.excel_util import ExcelUtil
from ddt import ddt,file_data,data
import logging
@ddt
@unittest.skipIf(excel_test_classmod('AgActivTestCase'),'AgActivTestCase is skip')
class AgActivTestCase(unittest.TestCase):
    # 环境/用户信息
    browesr_name = config_ini('config.ini', 'default', 'browesr_name')
    env_type = config_ini('config.ini', 'default', 'env_type')
    skin = config_ini('config.ini', 'default', 'skin')
    # 获取一二级菜单
    first = config_ini('agmod.ini', 'menu', 'first_activ')
    second = config_ini('agmod.ini', 'menu', 'second_activset')
    # 获取测试数据
    data_path = get_project_path() + '\\Data\\activ\\activ_data.xls'
    datas = ExcelUtil(data_path).read_excel_value_type_getdata()

    @classmethod
    def setUpClass(cls):
        WebDriver.start_browser(cls.browesr_name)
        cls.driver = WebDriver().get_driver()
        Login(cls.driver).login_page(cls.env_type,cls.skin,'后台')
        AgHome(cls.driver).close_ag_pop()

    @classmethod
    def tearDownClass(cls):
        WebDriver().driver_quit()

    @data(*datas)
    @unittest.skipIf(excel_test_case(3,'test1_add_activ'),'test1_add_activ is skip')
    def test1_add_activ(self,datas):
        '''
        配置文件添加活动
        :return:
        '''
        logging.info('【INFO】【开始执行用例】{}'.format(self._testMethodName))
        # 调用切换菜单进入活动设置页面
        AgHome(self.driver).swith_mod(self.first,self.second)
        logging.info('【INFO】【切换模块】【{}】【{}】'.format(self.first,self.second))
        # 调用切换table栏目菜单进入活动设置页面里
        AgHome(self.driver).swith_table(self.second)
        flag = AgActiv(self.driver).test_activ(datas)
        self.assertTrue(flag,'活动添加失败，请检查')

if __name__ == "__main__":
    unittest.main()


