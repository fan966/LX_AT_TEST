from pykeyboard import PyKeyboard
import time
from selenium import webdriver
from pymouse import PyMouse
from selenium.webdriver.support.select import Select
pykey = PyKeyboard()
m = PyMouse()
driver = webdriver.Chrome()
driver.get('chrome://settings/importData')
driver.maximize_window()
time.sleep(10)
pykey.tap_key(pykey.shift_key) # 模拟键盘按Shift键
time.sleep(1)
pykey.type_string('E:\\test.html') # 模拟键盘输入路径
time.sleep(1)
pykey.tap_key(pykey.enter_key) # 模拟键盘按Enter键

js = "document.getElementById('start').remvoAttribute('readonly');" # 清除只读属性赋值给js
driver.execute_script(js) # 通过js去除掉element的readonly只读属性
element1 = selenium_driver.get_element('id', 'start')  # 这个只读input标签属性已经没有只读属性了
element1.clear() # 清楚input标签输入框默认值
element1.send_keys('2018-11-22 02:25:00') # 输入新值


time.sleep(15)
driver.quit()