# -*-coding:utf-8-*-
"""
登录页面元素定位信息
"""
from selenium.webdriver.common.by import By

class Loglocator:


    # 登录用户名
    username = (By.XPATH,'//input[contains(@data-bind,"textinput:fields.username")]') # 包含函数时，元素值用‘，’隔开
    # 登录密码
    userpwd = (By.XPATH,'//input[contains(@data-bind,"textinput:fields.password")]')
    # 验证码
    code = (By.XPATH,'//input[@class="codeipt"]') # 属性值用=连接
    # 登录按钮
    log_btn = (By.XPATH,'//input[@type="submit" and @class="regsiter-btn"]') # 运用多属性时用and连接
    # 登陆页面-线路检测
    log_testing = (By.XPATH,'//a[@class="detection-login"]')
    # 登陆页面-客服QQ
    log_service_qq = (By.XPATH,'//span[text() = "客服QQ"]')
    # 登陆页面-联系客服
    log_contact_srvice = (By.XPATH,'//a[text() = "联系客服"]')
    # 登陆页面-免费开户
    log_register_accont = (By.LINK_TEXT,"免费开户")


    # 后台登录信息
    # 首页iframe(包含登录页面)
    top_iframe = (By.XPATH, '//frame[@name="topFrame"]')
    # 登录用户名
    ag_log_name = (By.XPATH, '//input[@data-bind="textInput:uname"][@text-trim="trim"]')
    # 登录验证码
    ag_log_code = (By.XPATH, '//input[@data-bind="textInput:verify"][@text-trim="trim"]')
    # 下一步按钮
    ag_next_btn = (By.XPATH, '//div[@class="lg_btn"]/input[@type="submit"]')
    # 登录密码
    ag_log_password = (By.ID,'password')
    # 登录按钮
    ag_log_btn = (By.XPATH,'//input[@type="submit"][@value="确定"][@id="dgSubmit"]')

