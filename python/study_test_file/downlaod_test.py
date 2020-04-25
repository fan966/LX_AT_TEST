# coding = uyf-8
from selenium import webdriver
import time
try:
    options_test = webdriver.ChromeOptions()
    perfs = {'download.default_directory':'F:\Download\\','profile.default_content_settings.popups':0}
    options_test.add_experimental_option('perfs',perfs)
    driver = webdriver.Chrome(options=options_test)
    driver.get('https://www.imooc.com/')
    driver.maximize_window()
    time.sleep(10)
    driver.find_element_by_id('js-signin-btn')
    time.sleep(5)
    driver.find_element_by_name('email').send_keys('13874857561')
    time.sleep(2)
    driver.find_element_by_name('password').send_keys('502011')
    time.sleep(3)
    driver.find_element_by_class_name('moco-btn').click()
    time.sleep(2)
    driver.get('https://www.imooc.com/mobile/app')

    time.sleep(15)
    driver.find_element_by_class_name('btn-download ios').click()
    time.sleep(10)
    driver.quit()
except Exception as er:
    print(er)
finally:
    pass




