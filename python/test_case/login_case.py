# conding = utf-8
#from business.login_handie_business import HandleBusiness
from python.business.login_handie_business import HandleBusiness
from selenium import webdriver
import unittest
class Login_case_test(unittest.TestCase):
    # case执行前置条件
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://csdqtttyweb.lx901.com/Register?Intr=')
        self.driver.maximize_window()
        self.business = HandleBusiness(self.driver)
    # case执行后置条件
    def tearDown(self):
        self.driver.quit() # 关闭浏览器

    # 输入错误用户名
    def test_login_username_error(self):
        user_name = self.business.Login_username_error('1','aaaa1111','aaaa1111','13585214562')
        if user_name ==None: # 返回空则获取错误文本失败，注册成功了，case失败
            print('用户名检验失败（注册成功），此条case执行失败')
        else:
            print('用户名错误校验成功（注册失败），此条case执行成功')
    # 输入错误密码
    def test_login_password_error(self):
        password = self.business.Login_password_error('ttt210','1','aaaa1111','13585214562')
        if password == None:# 返回空则获取错误文本失败，注册成功了，case失败
            print('密码检验失败（注册成功），此条case执行失败')
        else:
            print('密码校验错误成功（注册失败），此条case执行成功')

    # 输入二次密码错误
    def tets_secend_password_error(self):
        secend_password = self.business.Login_secend_password_error('test52','aaaa1111','1','13585214562')
        if secend_password == None:# 返回空则获取错误文本失败，注册成功了，case失败
            print('二次密码检验失败（注册成功），此条case执行失败')
        else:
            print('二次密码错误校验成功（注册失败），此条case执行成功')

    # 输入手机号错误
    def test_phone_number_error(self):
        phone_number = self.business.Login_phone_number_error('ttt210', 'aaaa1111', 'aaaa1111', '1')
        if phone_number == None:  # 返回空则获取错误文本失败，注册成功了，case失败
            print('手机号检验失败（注册成功），此条case执行失败')
        else:
            print('手机号错误校验成功（注册失败），此条case执行成功')


    # 登录成功
    def test_login_succes(self):
        succes = self.business.Login_succes('ttt3451', 'aaaa1111', 'aaaa1111', '13585214562')
        if succes == True:
            print('注册成功，此条case执行成功')
        else:
            print('注册失败，此条case执行失败')



if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Login_case_test('test_phone_number_error'))
    suite.addTest(Login_case_test('tets_secend_password_error'))
    suite.addTest(Login_case_test('test_login_password_error'))
    suite.addTest(Login_case_test('test_login_username_error'))
    suite.addTest(Login_case_test('test_login_succes'))
    unittest.TextTestRunner().run(suite)
    # login_case_text = Login_case_test() # 实例化case对象
    # login_case_text.test_login_username_error()
    # login_case_text.test_login_password_error()
    # login_case_text.tets_secend_password_error()
    # login_case_text.test_phone_number_error()
    # login_case_text.test_login_succes()

