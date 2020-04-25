# -*-coding:utf-8-*-
from selenium.webdriver.common.by import By
class SecurityCenterLocator:
    # 初始资金密码
    withdrawalpwd = (By.XPATH,('//input[@type="password"][@data-bind="value:newWithdrawalPwd"]'))
    # 确认资金密码
    secend_withdrawalpwd = (By.XPATH,'//input[@type="password"][@data-bind="value:okNewWithdrawalPwd"]')
    # 资金密码设置按钮
    button = (By.XPATH,'//a[@data-bind="click:modifyWithdrawalPwd"]')
    # 资金密码充值按钮
    reset_button = (By.XPATH,)
    # 设置成功按钮
    ok_button = (By.XPATH,'//button[@i-id="ok"][text()="确定"]')
