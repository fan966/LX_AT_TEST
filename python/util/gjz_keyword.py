# coding = utf-8
from base.封装练习 import Selenium_Driver
from selenium import webdriver
import time
class Gjzmethod(object):
    # def __init__(self,driver):
    #     self.driver = driver
    #     self.selenium_driver = Selenium_Driver(self.driver)

    #打开浏览器

    def  open_browser(self,browser):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Firefox()
        self.selenium_driver = Selenium_Driver(self.driver)



    #  输入url
    def send_url(self,url):
        #self.selenium_driver = Selenium_Driver(self.driver)
        self.selenium_driver.get_url(url)


    # 关键字输入操作
    def send_excel_value(self,value,key):
        #self.selenium_driver = Selenium_Driver(self.driver)
        self.selenium_driver.get_ini_element_send_value(value,key)

    # 关键字点击操作
    def click_cz(self,key):
        #self.selenium_driver = Selenium_Driver(self.driver)
        self.selenium_driver.get_ini_element_click_element(key)
    # 等待时间
    def time_sleep(self):
        time.sleep(3)
    # 获取title
    def get_title(self):
       return self.driver.title
    # 获取元素
    def get_elements_attributes(self,data):
        value = None
        element = self.selenium_driver.get_excel_element(data)
        try:
            value = element.tag_name
        except Exception:
            pass
        finally:
            return value







    # 关闭浏览器
    def closebrowser(self):
        #self.selenium_driver = Selenium_Driver(self.driver)
        self.selenium_driver.close()




