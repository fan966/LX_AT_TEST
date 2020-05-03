# -*-coding:utf-8-*-
from selenium.webdriver.common.by import By
class TradiGameLocator:
    # 信用游戏各玩法元素通用list
    tradi_play_list = (By.XPATH,'//ul[@data-bind="foreach:navList"]/li')

    # 快捷按钮
    fast_btn = (By.XPATH,'//a[@title="快捷"][text()="快捷"]')
    # 确定按钮
    commit_btn = (By.XPATH,'//input[@class="btn btn-green"][@title="确认"]')
    # 页面所有投注选项通用list
    play_bet_list = (By.XPATH,'//div[contains(@data-bind,"foreach:{data:item.list")]/div[contains(@class,"bd clear")]')
    # 快捷按钮点击后页面金额输入框
    amount = (By.XPATH,'//div[@class="btn-wrap"]/input[@class="amount"]')



    # 三次次确认投注文本
    three_text = (By.XPATH,'//div[@class="tip"][text()="是否确认下注?"]')

    # 二次确认投注按钮
    second_btn = (By.XPATH,'//button[@i-id="ok"][text()="确认下注"]')

    # 投注成功文本
    text = (By.XPATH,'//div[@i="content"]//span[@class]')
    # 投注成功确定按钮
    bet_sceeuse_btn = (By.XPATH,'//button[@i-id="ok"][text()="确定"]')

    # 期数完结操作提示确认按钮
    btn = (By.XPATH,'//button[@i-id="ok"]')






    # 验证关闭的玩法是否可见--关闭的玩法元素在页面dom树可以定位到，但是不可见
    ll = (By.XPATH, '//ul[@class="clear"]/li[1]/div[3]/div[4]//input[@class="amount"]')



    # 信用游戏excel配置玩法元素
    # 信用游戏玩法1通用定位替换text
    tradi_play_text = (By.XPATH, '//ul[@data-bind="foreach:navList"]//a[text()="两面盘"]')
    # 信用游戏玩法2为 前三，中三，后三通用定位
    play2_in3 = (By.XPATH,'//div/div[text()="前三"]/../div[2]//span[text()="顺子"]')
    # 信用玩法2不为前三 后三 中三定位
    play2_not3 = (By.XPATH,'//div[@class="zm16_nav"][text()="第一球"]/../div[3]//span[text()="大"]/../span[3]/input[@class="amount"]')
    # 信用玩法2为空通用定位
    play2_ = (By.XPATH,'//div[@class="s1_nav clear_fix"]/ul[@class="clear"]/li//span[text()="总单"]/../span[3]/input')
    #     # 龙虎斗玩法项2通用定位
    longhu_bet = (By.XPATH,'//li[@class="wid1"]/div[1]/label[text()="第四球VS第五球"]/../following-sibling::div[1]//span[text()="龙"]/../following-sibling::div[1]/input')

    @staticmethod
    def get_tradigame_play_loc(loc_name):
        '''
        获取信用游戏玩法1locator
        :param loc_name:
        :return:
        '''
        locator = (By.XPATH,'//ul[@data-bind="foreach:navList"]//a[text()="{}"]'.format(loc_name))
        return locator
    @staticmethod
    def get_play2_1(loc_name,item):
        '''
        信用的首个玩法项2整合一类
        :return:
        '''
        locator = (By.XPATH,'//div[@class="zm16_nav"][text()="{}"]/../div[3]//span[text()="{}"]/../span[3]/input[@class="amount"]'.format(loc_name,item))
        return locator
    @staticmethod
    def get_play2_2(loc_name,item):
        '''
        龙虎斗玩法项2
        :return:
        '''
        locator = (By.XPATH,'//li[@class="wid1"]/div[1]/label[text()="{}"]/../following-sibling::div[1]//span[text()="{}"]/../following-sibling::div[1]/input'.format(loc_name, item))
        return locator
    @staticmethod
    def get_play2_3(item):
        '''
        玩法项2为空通用
        :param item:
        :return:
        '''
        print(item)
        locator = (By.XPATH,'//div[@class="s1_nav clear_fix"]/ul[@class="clear"]/li//span[text()="{}"]/../span[3]/input'.format(item))
        return locator


