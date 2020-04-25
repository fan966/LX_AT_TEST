# -*-coding:utf-8-*-
from selenium.webdriver.common.by import By
class WithdrawLocator:
    # 可提款金额
    balance = (By.XPATH,'//strong[@id="balanceLb"]')
    # 提款金额
    w_amount = (By.XPATH,'//input[@id="aumount"]')
    # 资金密码
    password = (By.XPATH,'//input[@id="pwd"][@type="password"]')
    # 提交按钮
    btn = (By.XPATH,'//dl[@class="clear"]//a[@class="ban-btn"][text()="提交申请"]')
    # 查看提款进度
    l = (By.XPATH,'//dl[@class="clear"]//a[@class="ban-btn"][text()="查看提款进度"]')
    # 查看流水
    liushui = (By.XPATH,'//dl[@class="clear"]//a[@class="ban-btn"][text()="查看流水"]')
    # 坚持出款按钮
    tk_button = (By.XPATH,'//button[@type="button"][@i-id="ok"]')
    # 提示框查看流水文本


