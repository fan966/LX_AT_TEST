# coding = utf-8
from handle_element.login_handie_element import Loginhandle
class HandleBusiness(object):
    # 执行操作
    def __init__(self,driver):
        self.login_handle = Loginhandle(driver)

    def util_handle(self,user_name,password,password1,phone_number):
        '''
        公共操作封装
        '''
        self.login_handle.close_tanchuang() # 关闭页面弹窗
        self.login_handle.send_user_name(user_name)  # 输入用户名
        self.login_handle.send_password(password)  # 输入密码
        self.login_handle.send_secend_password(password1)  # 输入二次面膜
        self.login_handle.send_phone_number(phone_number)  # 输入手机号
        self.login_handle.click_zcbtn()  # 点击注册按钮

    # 检查用户名错误
    def Login_username_error(self,user_name,password,password1,phone_number):# 检查用户名错误
        self.util_handle(user_name,password,password1,phone_number)
        if self.login_handle.get_error_text('user_name_error','登录账号位数在6-8位') == None: # 获取用户名错误文本信息
            #print('用户名检验失败（注册成功），此条case执行失败')
            return None
        else:
            return True

    # 检查密码错误
    def Login_password_error(self,user_name,password,password1,phone_number):
        self.util_handle(user_name,password,password1,phone_number)
        if self.login_handle.get_error_text('password_error','1') == None : # 获取密码错误文本信息
            return None
        else:
            return  True

    # 检查二次密码错误
    def Login_secend_password_error(self,user_name,password,password1,phone_number) :
        self.util_handle(user_name,password,password1,phone_number)
        if self.login_handle.get_error_text('secend_password_error','2') == None:# 获取二次密码错误文本信息为空则获取失败，注册成功
           return None
        else:
            return True

    # 检查手机号错误
    def Login_phone_number_error(self,user_name,password,password1,phone_number):
        self.util_handle(user_name,password,password1,phone_number)
        if self.login_handle.get_error_text('phone_number_error','3') == None:# 获取手机号错误文本信息，为空则获取失败，注册成功
            return None
        else:
            return True

    # 检查注册成功
    def Login_succes(self,user_name,password,password1,phone_number):
        self.util_handle(user_name,password,password1,phone_number)
        if self.login_handle.get_login_btn_text() == '注册成功': # 注册成功后通过获取注册按钮文本信息判断是否成功，为空则注册失败
            return True
        else:
            return None




