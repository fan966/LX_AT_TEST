#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Libs.log_util import set_log
from Libs.Base_Action import BaseAction
from Config.Config import *
import logging
import time
from PO.PageObject.Log_Page import Loginlocator
class Login(BaseAction):
    '''
    登录公共类
    '''
    web_url = Config().test_web_url + '/Login'
    ag_url = Config().test_ag_url
    def web_login(self,username,password):
        '''
        前台登录
        :param username:
        :param password:
        :return:
        '''
        self.get_url(self.web_url)
        self.driver.maximize_window()
        self.send_value(Loginlocator.usernae,username)
        self.send_value(Loginlocator.password,password)
        self.click_element(Loginlocator.log_btu)
        time.sleep(5)








if __name__ == '__main__':
    set_log()
