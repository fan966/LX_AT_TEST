# -*-coding:utf-8-*-
from PO.pageaction.ag_home_action import *
from PO.pageobject.ag_offlinepay_page import AgOfflinePaylocator
import logging
class AgOffline(AgHome):

    def get_order_number(self,account):
        self.send_value(AgOfflinePaylocator.account,account)
        self.click_element(AgOfflinePaylocator.quire_btn)
        time.sleep(2)
        text = self.get_el_text(AgOfflinePaylocator.table_order_num)
        return text

    def offline_confirm(self,num):
        '''
        公司入款审核确认
        :return:
        '''
        flag = False
        # self.refresh_table_act("公司入款")
        # # 重新切换iframe
        # self.top_iframe()
        # self.switch_iframe(AgHomeLocator.tab_iframe)
        # 输入订单号
        self.send_value(AgOfflinePaylocator.order_num,num)
        self.click_element(AgOfflinePaylocator.quire_btn)
        time.sleep(3)
        self.click_element(AgOfflinePaylocator.table_submit_btn)
        self.financial_pop_confirm()
        time.sleep(2)
        text = self.find_element(AgOfflinePaylocator.table_stauas).text
        if text == "同意":
            flag = True
            logging.info('【INFO】【公司入款审核】:【执行成功】')
        return flag
    def offline_lock(self,num):
        '''
        公司入款锁定
        :param num:
        :return:
        '''
        # self.refresh_table_act("公司入款")
        # # 重新切换iframe
        # self.top_iframe()
        # self.switch_iframe(AgHomeLocator.tab_iframe)
        # 输入订单号
        self.send_value(AgOfflinePaylocator.order_num, num)
        self.click_element(AgOfflinePaylocator.quire_btn)
        time.sleep(2)
        self.click_element(AgOfflinePaylocator.table_lock)
        time.sleep(1)
        flag = self.handle_alter('确认')
        time.sleep(1)
        if flag:
            logging.info('【INFO】【公司入款锁定】:【执行成功】')
        return flag

    def offline_cel(self, num):
        '''
        公司入款取消
        :param num:
        :return:
        '''
        flag = False
        # self.refresh_table_act("公司入款")
        # # 重新切换iframe
        # self.top_iframe()
        # self.switch_iframe(AgHomeLocator.tab_iframe)
        # 输入订单号
        self.send_value(AgOfflinePaylocator.order_num, num)
        self.click_element(AgOfflinePaylocator.quire_btn)
        time.sleep(2)
        self.click_element(AgOfflinePaylocator.table_cell_btn)
        self.financial_pop_confirm()
        time.sleep(1)
        text = self.find_element(AgOfflinePaylocator.table_stauas).text
        if text == "拒绝":
            flag = True
            logging.info('【INFO】【公司入款取消】:【执行成功】')
        return flag


















    def check_is_page(self):
        '''
        测试
        :return:
        '''
        self.send_value(AgOfflinePaylocator.account,"wg520")
        self.click_element(AgOfflinePaylocator.quire_btn)
        time.sleep(2)
        if self.check_element_displayed(AgOfflinePaylocator.table_lock):
            text = self.find_element(AgOfflinePaylocator.table_lock).text
            print(text)
            print('yuidhasuhdioashdiuoasd')
            print(type(text))
            time.sleep(5)

