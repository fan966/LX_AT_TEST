# coding = utf-8
from base.封装练习 import Selenium_Driver
class LoginPage(object):
    def __init__(self,driver):
        # self.selenium_driver = Selenium_Driver()
        # self.selenium_driver.get_url('http://csdqtttyweb.lx901.com/Register?Intr=')
        # self.selenium_driver.cz_browser('最大')
        # self.selenium_driver.click_element('class','ui-dialog-close')
        self.selenium_driver = Selenium_Driver(driver)
    # 获取用户名元素
    def get_user_name_element(self):
        return self.selenium_driver.get_list_elements('class','inp',0)
    # 获取密码元素
    def get_password_element(self):
        return self.selenium_driver.get_list_elements('class','inp',1)
    # 获取二次密码元素
    def get_secend_password_element(self):
        return self.selenium_driver.get_list_elements('class','inp',2)
    # 获取手机号元素
    def get_phone_number_element(self):
        return self.selenium_driver.get_list_elements('class','inp',3)
    # 获取注册按钮元素
    def get_zcbtn_element(self):
        return self.selenium_driver.get_element('text','免费注册')
    # 获取用户名错误提示元素
    def get_user_name_error_element(self):
        return self.selenium_driver.get_element('class','ui-dialog-content')
    # 获取密码错误提示信息
    def get_password_error_element(self):
        return self.selenium_driver.get_element('class','ui-dialog-content')
    # 获取二次密码错误提示信息
    def get_secend_password_error_element(self):
        return self.selenium_driver.get_element('class','ui-dialog-content')
    # 获取手机号错误提示信息
    def get_phone_number_error_element(self):
        return self.selenium_driver.get_element('class','ui-dialog-content')
    # def close_liulanqi(self):
    #     #     self.selenium_driver.close()

    # 获取页面弹窗关闭按钮
    def page_tanchuang(self):
        self.selenium_driver.click_element('class','ui-dialog-close')