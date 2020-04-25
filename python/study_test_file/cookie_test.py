import time
from selenium import webdriver
from selenium.webdriver.support import ui as ui

#driver.get('https://www.imooc.com/')

try:
    driver = webdriver.Chrome()
    driver.get('https://www.imooc.com/u/index/allcourses')
    driver.maximize_window()
    time.sleep(2)
    driver.delete_all_cookies()# 删除页面所有的cookie
    # ui.WebDriverWait(driver, 30).until(lambda x: driver.find_element_by_id('js-signin-btn'))
    # driver.find_element_by_id('js-signin-btn').click()
    # time.sleep(2)
    # ui.WebDriverWait(driver, 30).until(lambda x: driver.find_element_by_name('email'))
    # driver.find_element_by_name('email').send_keys('13874857561')
    # time.sleep(2)
    # ui.WebDriverWait(driver, 30).until(lambda x: driver.find_element_by_name('password'))
    # driver.find_element_by_name('password').send_keys('502011')
    # time.sleep(2)
    # ui.WebDriverWait(driver, 30).until(lambda x: driver.find_element_by_css_selector('.moco-btn'))
    # driver.find_element_by_css_selector('.moco-btn').click()
    # time.sleep(5)
    # cookie = driver.get_cookie('apsid')
    # print(cookie)
    cookie_1 ={'domain': '.imooc.com',
               'expiry': 1576084073.120995,
               'httpOnly': False,
               'name': 'apsid',
               'path': '/',
               'secure': False,
               'value': 'EzNzNjMDM1N2QwMjIzZmUwMjMzYTk0YWU0NDYzODQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANzMzNzI4MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAxMzg3NDg1NzU2MUAxNjMuY29tAAAAAAAAAAAAAAAAADBmZDFmMTQ2NTdlNGU0NzZjZmYzZWI0NTkwNDc0MjIw5ufnXebn510%3DMD'}
    driver.add_cookie(cookie_1)# 植入登录的cookir
    time.sleep(3)
    driver.get('https://www.imooc.com/u/index/allcourses')
    time.sleep(8)
except Exception as er:
    print(er)
finally:
    driver.quit()