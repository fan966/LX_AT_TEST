# coding = utf-8
import ddt
import unittest
import time
import sys
sys.path.append('F:\\python')
from selenium import webdriver
from business.login_handie_business import HandleBusiness
import os
import HTMLTestRunnerCN
from  util.read_exce_data import Excel_data
ex = Excel_data()
temp = ex.get_data()
# 用户名，密码，二次密码，手机号，错误文本元素，错误提示
@ddt.ddt
class FirstDataCase(unittest.TestCase):
    # case执行前置条件
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://csdqtttyweb.lx901.com/Register?Intr=')
        self.driver.maximize_window()
        self.business = HandleBusiness(self.driver)

    # case执行后置条件
    def tearDown(self):
        for method_name, error in self._outcome.errors:
            if error:
                method_name = self._testMethodName  # 获取测试用例方法名用来命名截图的图片名
                print(method_name)
                # 得到图片保存路径和保存文件名的拼接
                img_path_name = os.path.join(os.getcwd(), "\\python\\report\\" + method_name + ".png")
                print(img_path_name)
                self.driver.save_screenshot(img_path_name)  # 图片保存地
        self.driver.quit()  # 关闭浏览器
    # @ddt.data(
    #     ['1','aaaa1111','aaaa1111','1353524758','user_name_error'],
    #     ['ttt1','1','aaaa1111','1353524758','user_name_error'],
    #     ['ttt1','aaaa1111','1','1353524758','user_name_error'],
    #     ['ttt1', 'aaaa1111', 'aaaa1111', '1', 'user_name_error']
    # )
    # # 注册用例
    # @ddt.unpack
    @ddt.data(*temp)
    def test_login_case(self,temp):
        username, password, secendpassword, phonenumber, assertcode = temp
        user_name = self.business.regster_funtion(username,password, secendpassword, phonenumber,assertcode)
        self.assertTrue(user_name, 'case执行失败')







if __name__ == '__main__':
    path = os.path.join(os.getcwd(), "\\python\\report\\first_test_reportddt.html")
    f = open(path, 'wb')
    suite =unittest.TestLoader().loadTestsFromTestCase(FirstDataCase)
    HTMLTestRunnerCN.HTMLTestRunner(stream=f,title='数据驱动测试报告',verbosity=2,tester='Fan').run(suite)
