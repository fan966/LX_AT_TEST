# -*-coding:utf-8-*-
from PO.pageaction.us_center_action import *
import logging
from PO.pageaction.securitycenter_action import *
from Libs.random_util import RandomUtil
from PO.pageobject.bank_card_page import BankCardLocator
from PO.pageaction.top_up_action import TopUp
import time
class Bank_Card(TopUp):
    r = RandomUtil()
    bnakcard = r.full_bankno()
    name = r.random_name()
    province = "北京市"
    city = "市辖区"
    bank_name = name + "支行"
    def new_bank_card(self):
        self.click_element(BankCardLocator.new_btn)
        self.click_element(BankCardLocator.bank)
        self.random_click_el(BankCardLocator.hot_bank)
        self.util_input()
        self.send_value(BankCardLocator.name,self.name)
        self.send_value(BankCardLocator.card_number,self.bnakcard)
        self.send_value(BankCardLocator.card_number2,self.bnakcard)
        self.click_element(BankCardLocator.sabmit_btn)
        self.check_msg_txt(UserCenterPage.prompt_texts,'成功')


    def util_input(self):
        if self.check_element_displayed(BankCardLocator.account_province):
            self.send_value(BankCardLocator.account_province,self.province)
            self.send_value(BankCardLocator.account_city,self.city)
            self.send_value(BankCardLocator.bank_name,self.bank_name)






if __name__ == "__main__":
    b = Bank_Card(driver=1)
    print(b.bnakcard)
    print(b.bnakcard)
    print(b.name)