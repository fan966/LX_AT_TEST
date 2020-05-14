# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
class WebYueBaoLocator:
    # 方案选择
    program_link = (By.XPATH,'//span[text()="方案选择"]')
    # table
    table_loc = (By.XPATH,'//div/div[@i="header"]/../following-sibling::table//th[text()="产品名称"]/../../..')
    # table下tr行数
    table_tr_num = (By.XPATH,'//div/div[@i="header"]/../following-sibling::table//th[text()="产品名称"]/../../..//tr')
    # 余额宝金额输入框
    input_amount = (By.XPATH,'//input[@type="text"]')

    # 通用usercenterpage确定按钮/提示文本


    # 钱包管理对应余额宝详情方案按钮
    @staticmethod
    def get_yuebao_program_loc(activ_name):
        '''
        根据余额宝名称获取对应方案详情按钮
        :return:
        '//td[text()="wqeq"]/../td/a[text()="详情"]'
        '''
        locator = (By.XPATH,'//td[text()="{}"]/../td/a[text()="详情"]'.format(activ_name))
        return locator

    @staticmethod
    def get_tr_and_td_loc(tr,td):
        '''
        根据tr和td获取table具体列的字段定位
        :param tr:
        :param td:
        :return:
        '''
        locator = (By.XPATH,'//div/div[@i="header"]/../following-sibling::table//th[text()="产品名称"]/../../..//tr[{}]/td[{}]'.format(tr,td))
        return locator
    @staticmethod
    def get_rows_buy_btn(item):
        '''
        获取每行的购买按钮
        :param item:
        :return:
        '//div/div[@i="header"]/../following-sibling::table//th[text()="产品名称"]/../../..//tr[2]/td/a[@class="details"][not(contains(@style,"display: none;"))]'
        '''
        locator = (By.XPATH,'//div/div[@i="header"]/../following-sibling::table//th[text()="产品名称"]/../../..//tr[{}]/td/a[@class="details"][not(contains(@style,"display: none;"))]'.format(item))
        return locator