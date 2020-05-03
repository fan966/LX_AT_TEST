# -*-coding:utf-8-*-
from selenium.webdriver.common.by import By
class GamePageLocator:
    # 官方玩法项list
    play_type = (By.XPATH,'//div[@class="mainNav-list"]/a')
    # 官方随机按钮
    random_btn = (By.XPATH,'//a[@class="btn Random-btn"]')
    # 随机注数输入框
    random_num = (By.XPATH,'//a[@class="btn Random-btn"]/../input[@type="text"]')
    # 投注倍数
    pow_num = (By.XPATH,'//div[@class="amount"]/input[@type="text"]')
    # 立即下注按钮（不随机选择投注号码点击按钮下注）
    fast_btn = (By.XPATH,'//a[@class="btn confirm-btn activate1"][@title="立即下注"]')
    # 确认下注按钮（随机后点击此按钮可下注成功）
    confirm_btn = (By.XPATH,'//a[@class="btn deter-btn"][@title="确认下注"]')

    # 官方投注列表左球号通用 list
    play_num_list = (By.XPATH,'//div[@class="sumBtn_list clear"]')
    # 官方游戏玩法项通用 list
    game_type = (By.XPATH,'//div[@class="mainNav-list"]/a[text()="猜前二"]')

    # 信用游戏玩法项通用 list
    traditiongame_type = (By.XPATH,'//ul[@data-bind="foreach:navList"]//a[text()="特码"]')

    #影藏的输入框
    # $x('//ul[@class="clear"]/li[1]/div[3]/div[5]//input[@class="amount"]') 江苏11选5影藏的输入框
    temp = (By.XPATH,'//ul[@class="clear"]/li[1]/div[3]/div[5]//input[@class="amount"]')
    @staticmethod
    def get_playtype_loc(play_name):
        '''
        根据玩法项获取locator
        :param play_name:
        :return:
        '''
        locator = (By.XPATH,'//div[@class="mainNav-list"]/a[text()="{}"]'.format(play_name))
        return locator

    @staticmethod
    def get_game_loc(temp,temp1):
        '''
        根据循环投注做列表和循环投注项获取locator
        :param temp:
        :param temp1:
        :return:
        '''
        locator = (By.XPATH,'//div[@class="sumBtn_list clear"][{}]//*[text()="{}"]/..'.format(temp,temp1))
        return locator



