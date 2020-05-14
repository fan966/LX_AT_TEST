# -*-coding:utf-8-*-
import time
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as ec
from PO.pageobject.log_page import Loglocator
from Libs.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pykeyboard import PyKeyboard
from selenium import webdriver
from PO.pageobject.usercenter_page import UserCenterPage
#from pykeyboard import PyKeyboard  待查看使用方法
class BaseAction(WebDriver):
    def __init__(self,driver):
        self.driver = driver
        #self.driver = webdriver.Chrome()

    def get_url(self,url):
        '''
        输入传参url
        :param url:
        '''
        self.driver.get(url)

    def find_element(self,locator):
        '''
        查找页面元素
        :param locator: 传入BY.XXX元素参数
        :return:
        '''
        element = None
        try:
            # 添加智能等待时间
            temp = WebDriverWait(self.driver, 3)
            temp.until(lambda X: X.find_element(*locator))
            element = self.driver.find_element(*locator)
        except Exception as err:
            #logging.info('元素查找失败：{}:{}'.format(locator,err))
            pass
        return element

    def find_elements(self,locator):
        '''
        获取元素列表
        :param locator:
        '''
        element = None
        try:
            # 添加智能等待时间
            temp = WebDriverWait(self.driver, 5)
            temp.until(lambda X: self.driver.find_elements(*locator))
            element = self.driver.find_elements(*locator)
        except Exception as err:
            logging.info('元素查找失败：{}:{}'.format(locator, err))
        return element



    def click_element(self,locator):
        '''
        点击元素
        :param locator:
        :return:
        '''
        temp = False
        el = self.red_style(locator)
        if el:
            try:
                el.click()
                temp = True
            except Exception as e:
                logging.error(e)
                logging.info('元素点击失败{}'.format(locator))
        else:
            logging.info("值点击失败：{}".format(locator))
        return temp

    def send_value(self,locator,value):
        '''
        输入值
        :param locator:
        '''
        temp = False
        el = self.find_element(locator)
        if el != None:
            #el.clear()
            time.sleep(0.5)
            el.send_keys(value)
            temp = True
        else:
            print("{}:值输入失败：{}".format(value,locator))
            logging.info("{}:值输入失败：{}".format(value,locator))
        return temp

    def get_el_text(self,locator):
        '''
        获取元素文本
        :param locator:
        :return:
        '''
        el = self.find_element(locator)
        if el != None:
            text = el.text
            return text
        else:
            logging.info('空类型无text属性')

    def red_style(self, locator):
        '''
        元素添加一个红色像素
        :param locator:
        :return:
        '''
        element = self.find_element(locator)
        time.sleep(1)
        self.driver.execute_script("arguments[0].style.border='6px solid red'", element)
        return element

    def check_element_displayed(self,locator):
        '''
        检查元素是否可见
        :param locator:
        :return:
        '''
        temp = False
        el = self.find_element(locator)
        if el is not None:
            if el.is_displayed():
                temp = True
        return temp

    def move_to_element(self,locator):
        '''
        模拟鼠标移动至元素
        :param locator:
        :return:
        '''
        el = self.find_element(locator)
        ActionChains(self.driver).move_to_element(el).perform()

    def get_drop_down_list(self,locator,text):
        '''
        通过元素获取下拉列表元素
        :param locator: 需要点击的下拉框主元素
        :param text:  获取的下拉框选项text
        '''
        el = self.find_element(locator)
        if el != None:
            Select(el).select_by_visible_text(text)
        else:
            print('下拉框选择失败{}'.format(locator))
            logging.info('下拉框选择失败{}'.format(locator))

    def title_in(self,title_name):
        '''
        字符串是否在当前title
        :param title_name:
        :return:
        '''
        temp = False
        if title_name in self.driver.title:
            temp = True
        return temp


    def upload_file(self, file_path):
        '''
        上传文件方法封装
        传入文件路径
        :return:
        '''
        pykey = PyKeyboard()
        pykey.tap_key(pykey.shift_key)  # 切换英文输入法
        pykey.type_string(file_path)  # 输入文件路径
        time.sleep(2)
        pykey.tap_key(pykey.enter_key)  # 点击Enter键上传文件

    def download_file(self):
        '''
        下载文件
        :return:
        '''
        pykey = PyKeyboard()
        pykey.tap_key(pykey.enter_key)  # 点击Enter键确定下载文件

    def switch_window(self,title_name):
        '''切换浏览器窗口'''
        try:
            all_page = self.driver.window_handles # 获取所有窗口
            for page in all_page:
                time.sleep(2)
                self.driver.switch_to.window(page)
                if title_name in self.driver.title:
                    break
        except Exception:
            print('切换窗口失败')

    def scroll_element(self,locator):
        '''
        项目通用滑动页面查找元素方法封装
        '''
        js = "document.documentElement.scrollTop=200" # 滑动页面1000像素待执行js语句
        while True:
            try:
                el = self.find_element(locator)
                time.sleep(3)
                el.click()
                break
            except:
                self.driver.execute_script(js) # 执行js语句往下滑动页面1000像素

    def seitch_alert(self, temp, value=None):
        '''
        系统级弹窗alert
        :param temp: 确认 or 取消
        :param value: 是否有输入值
        '''
        flag = False
        windows_alert = self.driver.switch_to.alert
        if temp == '确认':
            if value != None:
                windows_alert.send_keys(value)
            windows_alert.accept()
            flag = True
        else:
            windows_alert.dismiss()
        return flag

    def handle_alter(self,temp, value=None):
        '''
        判断alter弹窗
        :param temp:确认/取消
        :param value: 输入值
        :return:
        '''
        flag = False
        alter = ec.alert_is_present()(self.driver)
        if alter:
            if value == None:
                flag = self.seitch_alert(temp)
            else:
                flag = self.seitch_alert(temp, value)
        else:
            print('没有alter弹窗')
        return flag

    def switch_iframe(self,locator):
        '''
        切换iframe
        :return:
        '''
        element = self.find_element(locator)
        self.driver.switch_to.frame(element)
        time.sleep(2)

    def freed_iframe(self):
        '''
        释放iframe--driver回到原本窗口
        :return:
        '''
        self.driver.switch_to.default_content()

    def is_check_box(self,locator,check = None):
        '''
        1.封装判断复选框是否勾选
         2.根据情况来确定是否点击 勾选/取消 复选框
         :return:
        '''
        element = self.find_element(locator)
        if element.is_selected() == True: # 判断复选框元素是否被选中（返回True或者False）
            if check != 'on':
                self.click_element(locator)

        else:
            if check == 'on':
                self.click_element(locator)

    def page_contains(self, text):
        """
        检查指定文本是否在页面上出现
        :param text: 待检查的文本
        :return: True or False
        """
        try:
            xpath = "//*[contains(.,'%s')]" % text
            self.driver.find_element_by_xpath(xpath)
        except Exception as e:
            logging.error(e)
            return False
        return True

    def common_status_switch_selector(self, el_locator, expecte_switch):
        """
        通用开关状态选择器
        :param el_locator: 元素定位
        :param expecte_switch: 预期开关
        """
        status = self.find_element(el_locator).get_attribute('checked')
        if (expecte_switch == 'ON' and not status) or (expecte_switch == 'OFF' and status):
            self.click_element(el_locator)

    def remove_all_input_readonly(self):
        """
        移除页面所有只读输入框的只读属性
        """
        js = '''
                   var element = document.querySelectorAll("input[readonly='readonly']");
                   for(var i = 0;i < element.length; i++)
                   {
                   element[i].readOnly = false;
                   }
               '''
        self.driver.execute_script(js)

    def get_js_readonly(self, by, value, number=None):
        '''
        获取元素by，value判断哪种使用哪种方法remove_readonly
        :return:
        '''
        js = None
        if by == 'id':
            by_key = 'getElementById'
            js = "document.%s('%s').removeAttribute('readonly')" % (by_key, value)
        elif by == 'class':
            by_key = 'getElementsByClassName'
            js = "document.%s('%s')[%d].removeAttribute('readonly')" % (by_key, value, number)
        else:
            print('%s，%s：传递值有误，去除readonly属性失败')
        return js

    def remove_readonly(self, by, value, number=None):
        '''
        去掉input标签read_only属性
        '''

        js = self.get_js_readonly(by, value, number)
        self.driver.execute_script(js)

    def get_table_content(self,locator,x,y):
        '''
        根据table的id属性和table中的某一个元素定位其在table中的位置
        table包括表头，位置坐标都是从1开始算，打印数据坐标列和行都是从1开始(但是我们从列表取值列和行都是从0记坐标)
        PS：我们从列表取值列和行都是从0记坐标 例如：table_list[x][y] 取第x行第y列值，这时候就从0开始计算行列
        tableId：table的id属性
        queryContent：需要确定位置的内容
        :param tableId:
        :param queryContent:
        :return:
        '''
        # 按行查询表格的数据，取出的数据是一整行，按空格分隔每一列的数据
        table_tr_list = self.driver.find_element(*locator).find_elements(By.TAG_NAME, "tr")
        table_list = []  # 存放table数据
        for tr in table_tr_list:  # 遍历每一个tr
            # 将每一个tr的数据根据td查询出来，返回结果为list对象
            table_td_list = tr.find_elements(By.TAG_NAME, "td")
            row_list = []
            #print(table_td_list)
            for td in table_td_list:  # 遍历每一个td
                row_list.append(td.text)  # 取出表格的数据，并放入行列表里
            table_list.append(row_list)
        return table_list[x][y]

        # 循环遍历table数据，确定查询数据的位置
        # for i in range(len(table_list)):
        #     for j in range(len(table_list[i])):
        #         if queryContent == table_list[i][j]:
        #             print("%r坐标为(%r,%r)" % (queryContent, i + 1, j + 1))

    def web_crawler_table_data(self,table_loc):
        '''
        网络爬虫table数据
        :return:
        '''
        table_tr_list = self.driver.find_element(*table_loc).find_elements(By.TAG_NAME,'tr')

        data_list = []
        for tr in range(len(table_tr_list)):

            if tr == 0:
                row_list = []
                data = table_tr_list[tr].find_elements(By.TAG_NAME, "th")
                for j in data:
                    row_list.append(j.text)
                data_list.append(row_list)
            else:
                row_list1 = []
                temp = table_tr_list[tr].find_elements(By.TAG_NAME, "td")
                for k in temp:
                    row_list1.append(k.text)
                data_list.append(row_list1)

        return data_list
            #data_list [['产品名称', '单笔限额', '计算周期(小时)', '利率', '利息上限', '续存次数', '剩余数量', '利息稽核倍数', '操作'], ['2', '2-23', '2小时', '2%', '2', '2', '1', '2倍', '立即购买'], ['3', '23-456', '4小时', '4%', '4', '4', '4', '4倍', '立即购买']]











if __name__ == "__main__":
    try:
        b = BaseAction()
        b.driver.maximize_window()
        b.get_url("http://csdqthcweb.lx901.com/Login")
        b.send_value(Loglocator.username,"ttt1")
        b.send_value(Loglocator.userpwd,"aaaa2222")
        b.click_element(Loglocator.log_btn)
        time.sleep(3)
        b.get_url("http://csdqthcweb.lx901.com/BalanceActivity/Index")
        l = (By.XPATH,'//div[@class="mainNav-list"]/a')
        el = b.find_elements(*l)

        # b.click_element(UserCenterPage.home_withdraw)
        # value = b.get_table_content('//table//tbody',0,1)
        # print(value)
        time.sleep(2)
    except Exception as err:
        print(err)

    finally:
        b.driver.quit()
