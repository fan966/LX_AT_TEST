# -*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time
# def test_alert_is_present():
#     try:
#         alter = driver.switch_to.alert
#         text = alter.text
#         print(text)
#         return alter
#     except Exception as er:
#         return False

def seitch_alert(temp, value=None):
    '''
    系统级弹窗alert
    :param temp: 确认 or 取消
    :param value: 是否有输入值
    '''
    windows_alert = driver.switch_to.alert
    if temp == '确认':
        if value != None:
            windows_alert.send_keys(value)
        windows_alert.accept()
    else:
        windows_alert.dismiss()

def handle_alter(temp,value=None):

    alter = ec.alert_is_present()(driver)
    if alter:
        if value == None:
            seitch_alert(temp)
        else:
            seitch_alert(temp,value)
    else:
        print('没有alter弹窗')



try:
    driver = webdriver.Chrome()
    driver.get('http://sahitest.com/demo/confirmTest.htm')
    time.sleep(1)
    driver.maximize_window()
    time.sleep(1)
    driver.find_element_by_name("b1").click()
    time.sleep(1)
    handle_alter('取消')
    time.sleep(1)



    # if alter:
    #     time.sleep(1)
    #     alter.accept()
    #     print('关闭alter成功')
    #     time.sleep(2)
    # else:
    #     print('没有弹窗')

except Exception as err:
    print(err)
finally:
    driver.close()
