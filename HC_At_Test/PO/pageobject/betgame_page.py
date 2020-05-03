# -*-coding:utf-8-*-

from selenium.webdriver.common.by import By


class BetPageLocator(object):
    """
    下注页面公共部分元素定位信息
    """

    # 投注倒计时
    hc_game_time = (By.XPATH, r'//ul[contains(@class ,"flip")]')
    tty_game_time = (By.XPATH, r'//div[@class="alert-box"]')
    # 停售
    div_stop_selling = (By.ID, 'stopSellingPop')

    # 奖金拉杆条拖动按钮0~135px（style="left: 0px;"）
    bonus_percen = (By.XPATH, r'//span[@class="ui-handle"]')
    # 拉杆条
    pull_rod = (By.XPATH, r'//div[@class="ranger"]')
    # 游戏分类
    game_tyep_div = (By.XPATH, r'//div[contains(@class, "sidem_item")]//ul')
    game_type_claer = (By.XPATH, r'//div[contains(@class, "sidem_item")]//a[@class="sidem_b clear"]')
    # 开奖结果
    run_lottery = (By.XPATH, r'//a[text()="开奖结果"]')
    # 期数状态
    period_tip = (By.XPATH, r'//div[@id="PeriodInfo"]//*[@data-bind="text:periodTip"]')
