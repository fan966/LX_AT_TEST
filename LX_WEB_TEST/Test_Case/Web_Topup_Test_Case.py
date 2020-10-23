#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Libs.webdriver import WebDriver
from PO.PageAction.Log_Action import Login
from Config.Config import *
import unittest
import logging
from Libs.log_util import set_log
class login(unittest.TestCase):
    browser_type = Config().browser_type
    username = Config().get_ini_value('Global_ini','WebUserName')
    password = Config().get_ini_value('Global_ini','WebPwd')
    def setUp(self) -> None:
        logging.info('启动测试脚本文件： {}.py'.format(self.__module__))
        WebDriver.start_browser(self.browser_type)
        self.driver = WebDriver().get_driver()
        Login(self.driver).web_login(self.username,self.password)

    def test_1(self):
        pass


    def tearDown(self) -> None:
        WebDriver().driver_quit()

if __name__ == '__main__':
    set_log()
    login()
