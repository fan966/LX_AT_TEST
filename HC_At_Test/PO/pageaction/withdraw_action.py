# -*-coding:utf-8-*-
from PO.pageobject.withdraw_page import WithdrawLocator
from Libs.cnfg_util import config_ini
from PO.pageaction.securitycenter_action import *
from PO.pageobject.bank_card_page import BankCardLocator
from PO.pageaction.bank_card_action import *
import logging
import sys
class Withdram(Us_Center_action):
    # 用户资金密码
    pwd = config_ini('config.ini','default','amount_pwd1')
    # 初始化资金密码
    pwd2 = config_ini('config.ini', 'default', 'amount_pwd2')
    def withdram1(self):
        if self.check_element_displayed(SecurityCenterLocator.withdrawalpwd):
            Security_Center(self.driver).new_amount_pwd(self.pwd2)
        if self.check_element_displayed(BankCardLocator.new_btn):
            Bank_Card(self.driver).new_bank_card()

    def withdram(self,data):
        logging.info('【INFO】进入提款页面，开始执行提款操作：{}'.format(sys._getframe().f_code.co_name))
        logging.info('【INFO】开始提款：提款金额：{}...资金密码：{}'.format(data,self.pwd))
        self.send_value(WithdrawLocator.w_amount,data)
        self.send_value(WithdrawLocator.password,self.pwd)
        text = self.find_element(WithdrawLocator.balance).text
        logging.info('【INFO】可提款金额：{}...本次提款金额：{}'.format(text,data))
        self.click_element(WithdrawLocator.btn)
        if self.check_element_displayed(WithdrawLocator.tk_button):
            self.click_element(WithdrawLocator.tk_button)
        flag = self.check_msg_txt(UserCenterPage.prompt_texts,"已提交")
        return flag

