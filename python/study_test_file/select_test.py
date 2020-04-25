# coding = 'utf-8'
from selenium import webdriver
import time
from selenium.webdriver.support import ui as ui
from selenium.webdriver.support.select import Select
try:
    driver = webdriver.Chrome()
    driver.get('https://www.imooc.com')
    driver.maximize_window()
    ui.WebDriverWait(driver,30).until(lambda x:driver.find_element_by_id('js-signin-btn'))
    driver.find_element_by_id('js-signin-btn').click()
    time.sleep(2)
    ui.WebDriverWait(driver,30).until(lambda x:driver.find_element_by_name('email'))
    driver.find_element_by_name('email').send_keys('13874857561')
    time.sleep(2)
    ui.WebDriverWait(driver,30).until(lambda x:driver.find_element_by_name('password'))
    driver.find_element_by_name('password').send_keys('502011')
    time.sleep(2)
    ui.WebDriverWait(driver,30).until(lambda x:driver.find_element_by_class_name('moco-btn'))
    driver.find_element_by_class_name('moco-btn').click()
    time.sleep(5)
    driver.get('https://www.imooc.com/user/setprofile')
    # time.sleep(2)
    # ui.WebDriverWait(driver,30).until(lambda x:driver.find_element_by_xpath("//ul/li/a[text('文本信息')]"))
    # time.sleep(2)
    # print('---1---')
    # driver.find_elements_by_xpath("//ul[@class='menu']/li/a")[1].click()
    ui.WebDriverWait(driver, 30).until(lambda x: driver.find_element_by_class_name('pull-right'))
    driver.find_element_by_class_name('pull-right').click()
    time.sleep(2)
    ui.WebDriverWait(driver, 30).until(lambda x: driver.find_elements_by_xpath("//select[@id='job']")[1])
    #driver.find_elements_by_xpath("//select[@id='job']")[1].find_elements_by_tag_name('option')[5].click() # 下拉框元素选择方式
    time.sleep(2)
    print('---1---')
    select_element = driver.find_elements_by_xpath("//select[@id='job']")[1]
    Select(select_element).select_by_index(6)
    time.sleep(1)
    Select(select_element).select_by_value('18')
    time.sleep(1)
    Select(select_element).select_by_visible_text('Web前端工程师')
except Exception as er:
    print(er)
finally:
    time.sleep(3)
    driver.quit()