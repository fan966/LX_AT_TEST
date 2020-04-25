# -*-coding:utf-8-*-
from PO.pageaction.us_center_action import Us_Center_action
from PO.pageobject.security_center_page import SecurityCenterLocator
import logging
class Security_Center(Us_Center_action):
    def new_amount_pwd(self,pwd):
        '''
        资金密码
        :param pwd:
        :return:
        '''
        try:
            self.send_value(SecurityCenterLocator.withdrawalpwd,pwd)
            self.send_value(SecurityCenterLocator.secend_withdrawalpwd,pwd)
            self.click_element(SecurityCenterLocator.button)
            self.click_element(SecurityCenterLocator.ok_button)
        except Exception as err:
            logging.info(err)
