# coding = 'utf-8'
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
driver.save_screenshot('test.png')
driver.close()