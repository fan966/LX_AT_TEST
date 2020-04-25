# -*-coding:utf-8-*-
from PO.pageaction.us_center_action import *
import logging
from selenium.webdriver.common.by import By
class BankCardLocator:
    # 新增按钮
    new_btn = (By.XPATH,'//div[@class="form-box"]/span/a')
    # 开户银行
    bank = (By.XPATH,'//input[@id="bank"]')
    # 热门银行
    hot_bank = (By.XPATH,'//div[@class="char-box"]/ul[@class="clear bank-hot"]/li/a[@class="clo-item"]')
    # 开户人姓名
    name = (By.XPATH,'//input[@type="text"][contains(@data-verify,"开户人姓名")]')
    # 银行卡号
    card_number = (By.XPATH,'//input[@type="text"][@id="IPcardNO"]')
    # 确认卡号
    card_number2 = (By.XPATH,'//input[@type="text"][contains(@data-confirm,"两次输入的卡号不")]')
    # 提交按钮
    sabmit_btn = (By.XPATH,'//div[@id="firstStep"]/div[contains(@class,"acenter")]/a[@class="btn"][text()="提交"]')
    # 返回按钮
    back_btn = (By.XPATH,'//div[@id="firstStep"]/div[contains(@class,"acenter")]/a[@class="btn"][text()="返回"]')

    # 可配置显示参数
    # 开户银行省份
    account_province= (By.XPATH,'//div[@class="controls inputMD"]/input[contains(@data-verify,"开户银行省份不可为空")]')
    # 开户银行城市
    account_city = (By.XPATH,'//input[@name="city"]')
    # 支行名称
    bank_name = (By.XPATH,'//input[@name="branch"]')