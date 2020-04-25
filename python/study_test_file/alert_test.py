import time
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from pykeyboard import PyKeyboard
from selenium.webdriver.common.action_chains import ActionChains
try:

    driver = webdriver.Chrome()
    driver.get('http://sahitest.com/demo/promptTest.htm')
    driver.maximize_window()
    # driver.find_element_by_name('b1').click()
    # time.sleep(2)
    # driver.switch_to.alert.accept()
    # time.sleep(2)
    # driver.find_element_by_name('b1').click()
    # time.sleep(2)
    driver.switch_to.alert.dismiss()
    time.sleep(2)
    driver.find_element_by_name('b1').click()
    time.sleep(2)
    a1 = driver.switch_to.alert
    time.sleep(2)
    print(a1.text)
    a1.send_keys('test')
    a1.accept()
    time.sleep(2)


    # #temp.send_keys('test')
    # time.sleep(2)
    # pykey = PyKeyboard()
    # pykey.type_string('键盘输入test')
except Exception as ER:
    print(ER)
finally:
    driver.quit()