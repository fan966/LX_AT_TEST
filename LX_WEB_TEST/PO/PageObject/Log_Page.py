#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class Loginlocator:
    # 前台登录信息
    # 用户名
    usernae = (By.XPATH,'//label[text()="请输入账号"]/following-sibling::input[1]')
    # 密码
    password = (By.XPATH,'//label[text()="请输入密码"]/following-sibling::input[1]')
    # 登录按钮
    log_btu = (By.XPATH,'//input[@title="立即登陆"]')