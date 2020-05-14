# -*- coding:utf-8 -*-
from PO.pageaction.us_center_action import *
import time
from PO.pageobject.web_yuebao_page import WebYueBaoLocator
import logging
from PO.common.common_util import *
class WebYueBao(Us_Center_action):
    def get_web_yuebao_testdata(self,ac_name,info):
        '''
        :return: 爬虫data
        '''
        url = info['url'] + '/BalanceActivity/Index'
        self.get_url(url)
        time.sleep(2)
        self.click_element(WebYueBaoLocator.program_link)
        time.sleep(2)
        self.find_element(WebYueBaoLocator.get_yuebao_program_loc(ac_name)).click()
        time.sleep(1)
        data = self.web_crawler_table_data(WebYueBaoLocator.table_loc)
        return data

    def min_amount_test(self,data):
        '''
        小于最低金额test
        :return:
        '''
        datas = data
        flag = False
        for i in range(1,len(datas)):

            if datas[i][8] == '立即购买':
                num = int(datas[i][1].split('-')[0]) - 1
                self.find_element(WebYueBaoLocator.get_rows_buy_btn(i)).click()
                time.sleep(1)
                self.send_value(WebYueBaoLocator.input_amount,num)
                self.click_element(UserCenterPage.msg_prompt_sbmit)
                time.sleep(1)
                # 判断文本
                flag = self.check_msg_txt(UserCenterPage.prompt_text,'金额不在限额内')
                break
            else:
                logging.info('{}该方案已售完,选择下个方案购买'.format(datas[i][0]))
        return flag

    def max_amount_test(self,data):
        '''
        超过最大选限额
        :param data:
        :return:
        '''
        datas = data
        flag = False
        for i in range(1,len(datas)):
            if datas[i][8] == '立即购买':
                num = int(datas[i][1].split('-')[1])+1
                self.find_element(WebYueBaoLocator.get_rows_buy_btn(i)).click()
                time.sleep(1)
                self.send_value(WebYueBaoLocator.input_amount,num)
                self.click_element(UserCenterPage.msg_prompt_sbmit)
                time.sleep(1)
                # 判断文本
                flag = self.check_msg_txt(UserCenterPage.prompt_text,'金额不在限额内')
                break
            else:
                logging.info('{}该方案已售完,选择下个方案购买'.format(datas[i][0]))
        return flag

    def amount_success(self,data):
        '''
        正确金额购买
        :param dats:
        :return:
        '''
        datas = data
        flag = False
        for i in range(1, len(datas)):
            if datas[i][8] == '立即购买':
                num = get_random_int(int(datas[i][1].split('-')[0]),int(datas[i][1].split('-')[1]))
                self.find_element(WebYueBaoLocator.get_rows_buy_btn(i)).click()
                time.sleep(1)
                self.send_value(WebYueBaoLocator.input_amount, num)
                self.click_element(UserCenterPage.msg_prompt_sbmit)
                time.sleep(1)
                # 判断文本
                flag = self.check_msg_txt(UserCenterPage.prompt_text, '成功')
                break
            else:
                logging.info('{}该方案已售完,选择下个方案购买'.format(datas[i][0]))
        return flag
