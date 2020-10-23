# -*-coding:utf-8-*-
from selenium import webdriver
import logging
class WebDriver:
    '''
    driver打开浏览器获取driver通用模块
    '''
    @classmethod
    def start_browser(cls,browser_name):
        if browser_name == "chrome":
            cls.driver = webdriver.Chrome()
        elif browser_name == "firefox":
            cls.driver = webdriver.Firefox()
        else:
            cls.driver = webdriver.Chrome()
        logging.info("启动:{}".format(browser_name))
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)

    def open_url(self,url):
        self.driver.get(url)


    def get_driver(self):
        '''
        获取driver
        :return:
        '''
        return self.driver

    def driver_quit(self):
        '''
        退出浏览器
        :return:
        '''
        self.driver.quit()

    def driver_close(self):
        '''
        关闭所在页面
        :return:
        '''
        self.driver.close()
