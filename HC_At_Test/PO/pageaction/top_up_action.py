# -*-coding:utf-8-*-
from PO.pageaction.us_center_action import Us_Center_action
from PO.pageobject.tup_up_page import TopUpLocator
import logging
import sys
from PO.pageobject.usercenter_page import UserCenterPage
from Libs.cnfg_util import config_ini
from PO.pageaction.securitycenter_action import Security_Center
from PO.pageobject.security_center_page import SecurityCenterLocator
from PO.common.common_util import *
from Libs.random_util import RandomUtil
import time
class TopUp(Us_Center_action):
    r = RandomUtil()
    name = r.random_name()
    # 初始化资金密码
    pwd = config_ini('config.ini','default','amount_pwd2')
    num = get_random_int(1000,2000)
    code = config_ini('config.ini','default','code')
    pmt = config_ini('financial.ini','web','pmtp')
    on_top = config_ini('financial.ini','web','on_top')

    # 判断是否有充值通道
    def check_pay(self,data):
        '''
        支付通道检查
        :return:
        '''
        flag = False
        if self.check_element_displayed(TopUpLocator.no_pay):
            text = self.find_element(TopUpLocator.no_pay).text
            logging.error(text)
            logging.info('【INFO】没有充值通道：请检查【{}】'.format(sys._getframe().f_code.co_name))
        else:
            flag = self.data_split(data)
        return flag
   # 切割支付方式和金额数据
    def data_split(self,datas):
        flag = False
        if datas.find(",") != -1:
            data = datas.split(',')
            flag = self.swith_pay_type(data[0],data[1])
        else:
            logging.info("【INFO】支付通道或充值金额填写错误，请检查！")
        return flag
    # 切换支付平台
    def swith_pay_type(self,pay_type,num):
        '''
        获取支付渠道/切换支付方式
        :param pay_type:配置文件获取的支付渠道
        :param num: 金额
        :return:
        '''
        flag = False
        onlne_top = ['支付宝', '在线支付', 'QQ钱包', '财付通', '京东','百度','企业支付宝','微信']
        offline_top =['QQ钱包转账','云闪付转账','微信转账','支付宝转账']
        if self.check_element_displayed(TopUpLocator.pmt_platform(pay_type)):
            locator = TopUpLocator.pmt_platform(pay_type)
            self.click_element(locator)
            if pay_type == "银行卡转账":
                flag = self.bank_top1(num)
            elif pay_type in onlne_top:
                flag = self.on_top2(pay_type,num)
            elif pay_type in offline_top:
                flag = self.offline_top3(pay_type,num)
        else:
            logging.error("【INFO】支付通道不存在当前页面，请检查文件数据！")
        return flag


    def bank_top1(self,num):
        '''
        银行卡转账
        :return:
        '''
        flag = False
        # 判断是否有资金密码
        if self.check_element_displayed(SecurityCenterLocator.withdrawalpwd):
            Security_Center(self.driver).new_amount_pwd(self.pwd)
        # 判断银行卡更换卡弹窗并关闭
        self.check_msg_txt(UserCenterPage.prompt_texts,"入款卡已更换")
        # 判断充值指引弹窗并关闭
        self.close_tup_gui()
        # 随机选择银行并点击
        self.random_click_el(TopUpLocator.bank_list)
        # 输入
        self.bank_util_input(num)
        # 判断存款优惠方案
        self.preference()
        # 判断是否存在选择支付方式有则随机点击
        if self.check_element_displayed(TopUpLocator.pay_type):
            self.random_pay_type(TopUpLocator.pay_type)
            # 点击提交按钮
            self.click_element(TopUpLocator.submit_button)
            # 判断提示框文字是否为“提交成功”并关闭
            time.sleep(1)
            flag = self.check_msg_txt(UserCenterPage.bank_tc_text,"成功")
        else:
            # 点击提交按钮
            self.click_element(TopUpLocator.submit_button)
            # 判断提示框文字是否为“提交成功”并关闭
            time.sleep(1)
            flag = self.check_msg_txt(UserCenterPage.prompt_text, "成功")
        return flag



    def on_top2(self,pay_type,num):
        '''
        线上支付
        :param num:
        :return:
        '''
        # 判断是否有资金密码
        if self.check_element_displayed(SecurityCenterLocator.withdrawalpwd):
            Security_Center(self.driver).new_amount_pwd(self.pwd)
            self.click_element(TopUpLocator.pmt_platform(pay_type))
            self.close_tup_gui()
        else:
            self.close_tup_gui()
        # 随机选择支付渠道
        self.random_click_el(TopUpLocator.online_pay)
        # 通用支付输入方法
        self.onpay_util_input(num)
        #  提交
        self.click_element(TopUpLocator.rbank_btn)
        self.click_element(TopUpLocator.rbank_btn)
        # 判断优惠方案
        self.preference()
        # 关闭支付多出页面
        self.close_other_page()
        # 判断文本
        flag = self.check_msg_txt(UserCenterPage.prompt_text,"提交成功")
        return flag
    def offline_top3(self,pay_type,num):
        '''
        线下转账（微信转账，支付宝转账。。。）
        :param num:
        :return:
        '''

        # 判断是否有资金密码
        if self.check_element_displayed(SecurityCenterLocator.withdrawalpwd):
            Security_Center(self.driver).new_amount_pwd(self.pwd)
            self.click_element(TopUpLocator.pmt_platform(pay_type))
        # 随机选择支付渠道
        self.random_click_el(TopUpLocator.online_pay)
        # 输入
        self.send_value(TopUpLocator.amount3,num)
        self.send_value(TopUpLocator.dep_person3,self.name)
        # 提交
        self.click_element(TopUpLocator.rbank_btn)
        # 优惠方案
        time.sleep(1)
        self.preference()
        time.sleep(2)


        # 判断文本
        flag = self.check_msg_txt(UserCenterPage.prompt_text,'成功')
        return flag
    def random_offline_top(self):
        '''
        随机一种线下转账:金额随机
        :return:
        '''
        flag = False
        if self.pmt.find(',') != -1:
            data = self.pmt.split(',')
            for i in range(len(data)-1):
                flag = self.swith_pay_type(data[i],self.num)
                break
        else:
            logging.error("【INFO】配置文件数据写入有误，请检查")

        return flag

    def random_online_top(self):
        '''
        随机一种线上支付:金额随机
        :return:
        '''
        flag = False
        if self.on_top.find(',') != -1:
            data = self.on_top.split(',')
            for i in range(len(data)-1):
                flag = self.swith_pay_type(data[i],self.num)
                break
        else:
            logging.error("【INFO】配置文件数据写入有误，请检查")
        return flag

    def random_click_el(self,locator):
        '''
        获取一组元素随机点击一个
        :param locator:
        :return:
        '''
        el = self.find_elements(locator)
        for i in range(len(el)):
            i = get_random_int(i,len(el)-1)
            logging.info('【INFO】【{}】'.format(el[i].text))
            el[i].click()
            break

    def random_pay_type(self,locator):
        '''
        转账类型随机选择并判断
        :param locator:
        :return:
        '''
        el = self.find_elements(locator)
        for i in range(len(el)):
            i = get_random_int(i,len(el)-1)
            el[i].click()
            text = el[i].text
            print(text)
            if "银行柜台" in text:
                self.send_value(TopUpLocator.bank_counter,self.name)
            elif "微信" in text:
                self.check_msg_txt(UserCenterPage.prompt_text,"微信")
            break


    def top_gui_close(self):
        '''
        检查充值指引提示框并关闭
        :return:
        '''
        if self.check_element_displayed(TopUpLocator.top_gui):
            self.click_element(TopUpLocator.top_gui)

    def preference(self):
        '''
        存款优惠方案弹窗处理
        :return:
        '''
        if self.check_element_displayed(UserCenterPage.msg_prompt):
            self.random_click_el(TopUpLocator.get_Preference)
            self.click_element(UserCenterPage.msg_prompt_sbmit)

    def close_tup_gui(self):
        '''
        判断是否存在充值指引弹窗并关闭
        :return:
        '''
        if self.check_element_displayed(TopUpLocator.top_gui):
            self.click_element(TopUpLocator.top_gui)
        else:
            logging.info("【INFO】该支付渠道没有充值指引！跳过此操作步骤")


    def onpay_util_input(self,num):
        '''
        线上支付通用操作
        :param num:
        :return:
        '''
        if self.check_element_displayed(TopUpLocator.pay_for_code):
            self.send_value(TopUpLocator.pay_for_code,self.code)
        if self.check_element_displayed(TopUpLocator.online_amount):
            self.send_value(TopUpLocator.online_amount,num)
        if self.check_element_displayed(TopUpLocator.get_amount_val):
            self.random_click_el(TopUpLocator.get_amount_val)

    def bank_util_input(self,num):
        '''
        银行卡转账通用输入操作
        :return:
        '''
        self.send_value(TopUpLocator.amount1,num)
        self.send_value(TopUpLocator.dep_person1,self.name)


    def close_other_page(self):
        all_page = self.driver.window_handles
        for page in all_page:
            self.driver.switch_to.window(page)
            if "用户中心" not in self.driver.title:
                self.driver.close()
        self.switch_window("用户中心")




