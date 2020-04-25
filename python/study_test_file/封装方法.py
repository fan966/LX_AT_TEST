# coding = 'utf-8'
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support import ui as ui
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import random
class Selenium_Driver(object):
    def __init__(self):
        '''封装打开浏览器方法'''
        self.driver = webdriver.Chrome()
    def get_url(self,url):
        '''封装输入网址方法'''
        self.driver.get(url)
    def cz_browser(self,temp):
        '''封装操作

        浏览器常用方法封装'''
        if temp == "最大":
            self.driver.maximize_window() # 浏览器最大化方法
        elif temp == "最小":
            self.driver.minimize_window() # 浏览器最小化方法
        elif temp == "返回":
            self.driver.back() # 浏览器返回方法
        elif temp == "前进":
            self.driver.forward() # 浏览器前进方法
        elif temp == "刷新":
            self.driver.refresh() # 刷新浏览器方法
        else:
            print('浏览器无此操作方法')
    def switch_window(self,title_name):
        '''切换浏览器窗口'''
        try:
            hand_list = self.driver.window_handles # 获取所有窗口
            cuurent_window = self.driver.current_window_handle # 获取当前窗口
            for i in hand_list:
                time.sleep(2)
                if i != cuurent_window:
                    time.sleep(3)
                    self.driver.switch_to.window(i)
                    t_name = ec.title_contains(title_name)
                    if t_name(self.driver) == True: # 切换窗口成功
                        break
        except Exception:
            print('切换窗口失败')
    def get_element(self,element_type,element_value):
        '''元素定位方法'''
        element = None
        try:
            if element_type == 'id':
                temp = ui.WebDriverWait(self.driver,20)
                temp.until(lambda X: self.driver.find_element_by_id(element_value))
                element = self.driver.find_element_by_id(element_value)
            elif element_type == 'class':
                ui.WebDriverWait(self.driver, 10).until(lambda X: self.driver.find_element_by_class_name(element_value))
                element =self.driver.find_element_by_class_name(element_value)
            elif element_type == 'name':
                ui.WebDriverWait(self.driver, 10).until(lambda X: self.driver.find_element_by_name(element_value))
                element =self.driver.find_element_by_name(element_value)
            elif element_type =='text':
                ui.WebDriverWait(self.driver, 10).until(lambda X: self.driver.find_element_by_link_text(element_value))
                element =self.driver.find_element_by_link_text(element_value)
            elif element_type =='css':
                ui.WebDriverWait(self.driver, 20).until(lambda X: self.driver.find_elements_by_css_selector(element_value))
                element =self.driver.find_element_by_css_selector(element_value)
            elif element_type =='xpath':
                ui.WebDriverWait(self.driver, 10).until(lambda X: self.driver.find_element_by_xpath(element_value))
                element =self.driver.find_element_by_xpath(element_value)
            else:
                print('传入元素值属性有误')
        except Exception:
            print('属性:',element_type,'属性值:',element_value,' ','元素查找失败')
        return self.is_dis_played(element)

    def get_level_element(self,by,value,node_by,node_value):
        '''封装子层级父节点定位元素方法'''
        element = self.get_element(by,value)
        if node_by == 'id':
            element = element.find_element_by_id(node_by,node_value)
        return element
    def get_list_elements(self,by,value,number):
        '''封装层级定位元素方法'''
        element = None
        try:
            if by == 'css':
                ui.WebDriverWait(self.driver,20).until(lambda X:self.driver.find_elements_by_css_selector(value)[number])
                element = self.driver.find_elements_by_css_selector(value)[number]
            elif by == 'xpath':
                ui.WebDriverWait(self.driver, 20).until(lambda X: self.driver.find_elements_by_xpath(value)[number])
                element = self.driver.find_elements_by_xpath(value)[number]
            else:
                print('get_list_elements方法传入参数有误')
        except Exception:
            print('属性:',by,'属性值:',value,'下标',number,'元素查找失败')
        return self.is_dis_played(element)
    def send_value(self,value,*args):
        '''
        ---封装输入操作---
        1.调用定位元素方法获取element
        2.element输入值
        '''
        element_lisi = args
        if len(element_lisi) == 2:
            element = self.get_element(args[0],args[1])
            if element != False:
                if element != None:
                    element.send_keys(value)
                else:
                    print(element,':','输入失败，元素查找失败')
            else:
                print('元素不可见，无法输入')
        elif len(element_lisi) == 3:
            element = self.get_list_elements(args[0],args[1],args[2])
            if element != False:
                if element != None:
                    element.send_keys(value)
                else:
                    print('输入失败，元素查找失败')
            else:
                print('元素不可见，无法输入')
    def click_element(self,*args):
        '''
        ---封装点击操作---
         1.调用定位元素方法获取element
         2.element进行点击
        '''
        element_list = args
        if len(element_list) == 2:
            element = self.get_element(args[0],args[1])
            if element != False:
                if element != None:
                    element.click()
                else:
                    print('点击失败，元素查找失败')
            else:
                print('元素不可见，无法点击')
        elif len(element_list) == 3:
            element = self.get_list_elements(args[0],args[1],args[2])
            if element != False:
                if element != None:
                    element.click()
                else:
                    print('点击失败，元素查找失败')
            else:
                print('点击失败，元素查找失败')
    def mouse(self):
        '''
        模拟鼠标悬浮
        1.调用定位元素方法获取element
        2.通过 ActionChains模块方法模拟鼠标悬浮
        '''

        #ActionChains(self.driver).move_to_element(element).perform()

    def is_check_box(self,by,value,check = None):
        '''
        1.封装判断复选框是否勾选
         2.根据情况来确定是否点击 勾选/取消 复选框
        '''
        element = self.get_element(by,value)
        if element.is_selected() == True:
            if check != 'check':
                self.click_element(by,value)
        else:
            if check == 'check':
                self.click_element(by,value)

    def is_dis_played(self,element):
        '''
        封装判断元素是否启用
        '''
        # element = self.get_element(element)
        flge = element.is_displayed()
        if flge == True:
            print(element,' : ','查找成功')
            return element
        else:
            return False
    def get_select(self,temp,value,*args):
        '''
        定位下拉框的select——element
        调用selenium中Select中方法选择下拉框选项
        '''
        element_list = args
        if len(element_list) == 2:
            element = self.get_element(args[0], args[1])
            if element != False:
                if element != None:
                    if temp == 'index':
                        Select(element).select_by_index(value) # 实例化对象调用index方法选择下拉框元素
                    elif temp == 'text':
                        Select(element).select_by_visible_text(value)
                    elif temp == 'value':
                        Select(element).select_by_value(value)
                    else:
                        print('下拉框选择方式（value/text/index）传递有误！')
        elif len(element_list) == 3:
            element = self.get_list_elements(args[0], args[1], args[2])
            if element != False:
                if element != None:
                    if temp == 'index':
                        Select(element).select_by_index(value)  # 实例化对象调用index方法选择下拉框元素
                    elif temp == 'text':
                        Select(element).select_by_visible_text(value)
                    elif temp == 'value':
                        Select(element).select_by_value(value)
                    else:
                        print('下拉框选择方式（value/text/index）传递有误！')

    def  user_name(self):
        '''
        获取随机用户名信息
        :return:
        '''
        user_info = random.sample('0123456789zxcvbnmasdfghjklqwertyuiop',6)
        return user_info

    def get_code_img(self):
        pass

    def close(self):
        '''封装关闭浏览器方法'''
        self.driver.quit()

if __name__ == '__main__':
    '''入口程序'''
    try:
        # selenium_driver = Selenium_Driver()
        # selenium_driver.get_url('http://csdqthcweb.lx901.com/')
        # selenium_driver.cz_browser("最大")
        # selenium_driver.click_element('class','ui-dialog-close')
        # selenium_driver.send_value('ttt1','css','span.login-mane>input')
        # selenium_driver.send_value('aaaa2222','css','span.login-password>input')
        # selenium_driver.send_value('9999','css','.login-code')
        # selenium_driver.click_element("text",'登录')
        # selenium_driver.click_element('class', 'ui-dialog-close')
        # time.sleep(3)
        selenium_driver = Selenium_Driver()
        selenium_driver.get_url('https://www.imooc.com')
        selenium_driver.cz_browser("最大")



    except Exception as err:
        print(err)
    finally:
        time.sleep(15)
        selenium_driver.close()

