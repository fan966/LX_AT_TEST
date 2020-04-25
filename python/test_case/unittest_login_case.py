# conding = utf-8
import sys
sys.path.append('E:\\python_test\\python')
from business.login_handie_business import HandleBusiness
from selenium import webdriver
import unittest
import os
from study_test_file.read_ini import Read_ini
import HTMLTestRunnerCN
class Login_case_test(unittest.TestCase):
    # case执行前置条件
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://csdqtttyweb.lx901.com/Register?Intr=')
        self.driver.maximize_window()
        self.business = HandleBusiness(self.driver)
    # case执行后置条件
    def tearDown(self):
        for method_name,error in self._outcome.errors:
            if error:
                method_name = self._testMethodName  # 获取测试用例方法名用来命名截图的图片名
                print(method_name)
                # 得到图片保存路径和保存文件名的拼接
                img_path_name = os.path.join(os.getcwd(),"\\python\\report\\" + method_name + ".png")
                print(img_path_name)
                self.driver.save_screenshot(img_path_name)# 图片保存地
        self.driver.quit() # 关闭浏览器

    # 输入错误用户名
    #@unittest.skip('1')
    def test_login_username_error(self):
        user_name = self.business.Login_username_error('1','aaaa1111','aaaa1111','13585214562')
        self.assertFalse(user_name,'case执行成功')

    # 输入错误密码
    @unittest.skip('不执行此条case')
    def test_login_password_error(self):
        password = self.business.Login_password_error('ttt210','1','aaaa1111','13585214562')
        self.assertTrue(password,'case执行失败')

    # 输入二次密码错误
    #@unittest.skip('不执行此条case')
    def tets_secend_password_error(self):
        secend_password = self.business.Login_secend_password_error('test52','aaaa1111','1','13585214562')
        self.assertEqual(secend_password,"两次密码不一致")

    # 输入手机号错误
    @unittest.skip('不执行此条case')
    def test_phone_number_error(self):
        phone_number = self.business.Login_phone_number_error('ttt210', 'aaaa1111', 'aaaa1111', '1')

        self.assertEqual(phone_number, 'case执行失败')


    # 登录成功
    @unittest.skip('不执行此条case')
    def test_login_succes(self):
        succes = self.business.Login_succes('ttt3453', 'aaaa1111', 'aaaa1111', '13585214562')
        self.assertTrue(succes,'case执行失败')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Login_case_test("test_login_succes"))
    suite.addTest(Login_case_test("test_phone_number_error"))
    suite.addTest(Login_case_test("tets_secend_password_error"))
    #unittest.TextTestRunner().run(suite)
    path = "..//report//first_test_report.html"
    print(path)
    f = open(path,'wb')
    runner = HTMLTestRunnerCN.HTMLTestRunner(stream=f,title='超级自动化测试报告',tester='Fan',description='首次测试报告',verbosity=2)
    runner.run(suite)
