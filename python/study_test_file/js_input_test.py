# conding = utf-8
import time
from pykeyboard import PyKeyboard
from base.封装练习 import Selenium_Driver


class js_test(Selenium_Driver):
    def pykey_input(self,value):
        pykey = PyKeyboard()
        pykey.tap_key(pykey.shift_key)
        pykey.type_string(value)
if __name__ == '__main__':
    try:
        selenium_driver = js_test()
        selenium_driver.get_url('http://csdqtttyweb.lx901.com')
        selenium_driver.cz_browser('最大')
        selenium_driver.click_element('class','ui-dialog-close')
        time.sleep(3)
        print('1')
        selenium_driver.click_element('xpath','//label',3)
        print('2')
        selenium_driver.pykey_input('ttt22')
        print('3')
        time.sleep(4)
        selenium_driver.click_element('xpath','//label',4)
        print('4')
        selenium_driver.pykey_input('aaaa2222')
        print('5')
        selenium_driver.click_element('css','.regsiter-btn')
        time.sleep(3)
        selenium_driver.get_url('http://csdqtttyweb.lx901.com/Report/AccountChange')
        time.sleep(5)
        selenium_driver.remove_readonly('id','start')
        element = selenium_driver.get_element('id','start')
        element.clear()
        time.sleep(2)
        selenium_driver.send_value('2055-10-15 20:20:20','id','start')
        selenium_driver.remove_readonly('id', 'end')
        element1 = selenium_driver.get_element('id', 'end')
        element1.clear()
        time.sleep(2)
        selenium_driver.send_value('2055-10-15 20:20:20','id','end')
        time.sleep(3)

        # driver = webdriver.Chrome()
        # driver.get('http://csdqtttyweb.lx901.com')
        # driver.maximize_window()
        # time.sleep(2)
        # driver.find_element_by_class_name('ui-dialog-close').click()
        # time.sleep(3)
        # temp = driver.find_elements_by_tag_name('label')[3].click()
        # pykey = PyKeyboard()
        # pykey.tap_key(pykey.shift_key)
        # time.sleep(1)
        # pykey.type_string('ttt22')
        time.sleep(3)
        # time.sleep(3)
        # ac = ActionChains(driver).move_to_element(temp)
        # time.sleep(3)
        # driver.execute_script('document.getElementsByTagName("label")[3].value="ttt22"')

    except Exception as er:
        print(er)
    finally:

        selenium_driver.close()