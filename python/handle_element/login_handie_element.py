# conding = utf-8
from login_page_handle.login_page import LoginPage
class Loginhandle(object):
    def __init__(self,driver):
        self.login_pg_handle = LoginPage(driver)

    # 关闭页面弹窗按钮
    def close_tanchuang(self):
        self.login_pg_handle.page_tanchuang()

    # 输入用户名
    def send_user_name(self,user_name):
        self.login_pg_handle.get_user_name_element().send_keys(user_name)
    # 输入密码
    def send_password(self,password):
        self.login_pg_handle.get_password_element().send_keys(password)
    # 输入二次密码
    def send_secend_password(self,password1):
        self.login_pg_handle.get_secend_password_element().send_keys(password1)
    # 输入与手机号
    def send_phone_number(self,phone_number):
        self.login_pg_handle.get_phone_number_element().send_keys(phone_number)

    # 点击注册按钮
    def click_zcbtn(self):
        self.login_pg_handle.get_zcbtn_element().click()

    # 获取错误文本信息
    def get_error_text(self,info,user_info):
        if info == 'user_name_error':
            text = self.login_pg_handle.get_user_name_error_element().text
        elif info == 'password_error':
            text = self.login_pg_handle.get_password_error_element().text
        elif info == 'secend_password_error':
            text = self.login_pg_handle.get_secend_password_error_element().text
        else:
            text = self.login_pg_handle.get_phone_number_error_element().text
        return text

    # 获取注册成功文本信息
    def get_login_btn_text(self):
        text = self.login_pg_handle.get_phone_number_error_element().text
        print(text)
        return text


