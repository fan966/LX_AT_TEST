# coding = 'utf-8'
import sys
from selenium import webdriver
import time
from pykeyboard import PyKeyboard
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support import ui as ui
from study_test_file.read_ini import readini
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from study_test_file.handle_json import Handle_json
import random
from PIL import Image
import pytesseract
class Selenium_Driver(object):
    def __init__(self,driver):
        '''封装打开浏览器方法'''
        self.driver = driver
    def get_url(self,url):
        #url1 = readini.get_ini_value()
        '''封装输入网址方法'''
        self.driver.get(url)
    def cz_browser(self,temp):
        '''
        浏览器常规操作封装
        :param temp: 最大 or 最小...
        '''
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
                ui.WebDriverWait(self.driver, 20).until(lambda X: self.driver.find_element_by_class_name(element_value))
                element =self.driver.find_element_by_class_name(element_value)
            elif element_type == 'name':
                ui.WebDriverWait(self.driver, 20).until(lambda X: self.driver.find_element_by_name(element_value))
                element =self.driver.find_element_by_name(element_value)
            elif element_type =='text':
                ui.WebDriverWait(self.driver, 20).until(lambda X: self.driver.find_element_by_link_text(element_value))
                element =self.driver.find_element_by_link_text(element_value)
            elif element_type =='css':
                ui.WebDriverWait(self.driver, 20).until(lambda X: self.driver.find_elements_by_css_selector(element_value))
                element =self.driver.find_element_by_css_selector(element_value)
            elif element_type =='xpath':
                ui.WebDriverWait(self.driver, 20).until(lambda X: self.driver.find_element_by_xpath(element_value))
                element =self.driver.find_element_by_xpath(element_value)
            elif element_type == 'tagname':
                ui.WebDriverWait(self.driver, 20).until(lambda X: self.driver.find_element_by_tag_name(element_value))
                element = self.driver.find_element_by_tag_name(element_value)
            else:
                print('传入元素值属性有误')
        except Exception:
            print('属性:',element_type,'属性值:',element_value,' ','元素查找失败')
        return self.is_dis_played(element)
    def get_element_nodisplayed(self,element_type,element_value):
        '''元素定位方法'''
        element = None
        try:
            if element_type == 'id':
                temp = ui.WebDriverWait(self.driver,20)
                temp.until(lambda X: self.driver.find_element_by_id(element_value))
                element = self.driver.find_element_by_id(element_value)
            elif element_type == 'class':
                ui.WebDriverWait(self.driver, 20).until(lambda X: self.driver.find_element_by_class_name(element_value))
                element =self.driver.find_element_by_class_name(element_value)
            elif element_type == 'name':
                ui.WebDriverWait(self.driver, 20).until(lambda X: self.driver.find_element_by_name(element_value))
                element =self.driver.find_element_by_name(element_value)
            elif element_type =='text':
                ui.WebDriverWait(self.driver, 20).until(lambda X: self.driver.find_element_by_link_text(element_value))
                element =self.driver.find_element_by_link_text(element_value)
            elif element_type =='css':
                ui.WebDriverWait(self.driver, 20).until(lambda X: self.driver.find_elements_by_css_selector(element_value))
                element =self.driver.find_element_by_css_selector(element_value)
            elif element_type =='xpath':
                ui.WebDriverWait(self.driver, 20).until(lambda X: self.driver.find_element_by_xpath(element_value))
                element =self.driver.find_element_by_xpath(element_value)
            else:
                print('传入元素值属性有误')
        except Exception:
            print('属性:',element_type,'属性值:',element_value,' ','元素查找失败')
        return element

    def get_elements(self,by,value):
        '''封装list定位元素方法'''
        try:
            elements = None
            if by == 'class':
                elements = self.driver.find_elements_by_class_name(value)
            elif by == 'name':
                elements = self.driver.find_elements_by_name(value)
            elif by == 'css':
                elements = self.driver.find_elements_by_css_selector(value)
            else:
                print('传递%s参数有误--get_elements方法查找元素失败'%by)
        except Exception:
            print('%s,%s,元素查找失败！'%(by,value))
        return elements
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
            elif by == 'tagname':
                ui.WebDriverWait(self.driver,20).until(lambda X:self.driver.find_elements_by_tag_name(value)[number])
                element = self.driver.find_elements_by_tag_name(value)[number]
            elif by == 'class':
                ui.WebDriverWait(self.driver, 20).until(lambda X: self.driver.find_elements_by_class_name(value)[number])
                element = self.driver.find_elements_by_class_name(value)[number]
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
        #print(element_lisi) test
        if len(element_lisi) == 2:
            #print('test') test
            element = self.get_element(args[0],args[1])
            if element != False:
                if element != None:
                    element.send_keys(value)
                else:
                    print(element,':','%s,%s输入失败，元素查找失败'%(args[0],args[1]))
            else:
                print('%s,%s元素不可见，无法输入'%(args[0],args[1]))
        elif len(element_lisi) == 3:
            element = self.get_list_elements(args[0],args[1],args[2])
            if element != False:
                if element != None:
                    element.send_keys(value)
                else:
                    print('%s,%s,%s输入失败，元素查找失败'%(args[0],args[1],args[2]))
            else:
                print('%s,%s,%s元素不可见，无法输入'%(args[0],args[1],args[2]))
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
                    print('%s,%s点击失败，元素查找失败'%(args[0],args[1]))
            else:
                print('%s,%s元素不可见，无法点击'%(args[0],args[1]))
        elif len(element_list) == 3:
            element = self.get_list_elements(args[0],args[1],args[2])
            if element != False:
                if element != None:
                    element.click()
                else:
                    print('%s,%s,%s点击失败，元素查找失败'%(args[0],args[1],int(args[2])))
            else:
                print('%s,%s,%s点击失败，元素查找失败!!!'%(args[0],args[1],int(args[2])))
    def switch_mouse(self,*args):
        '''
        封装模拟鼠标悬浮
        1.调用定位元素方法获取element
        2.通过 ActionChains模块方法模拟鼠悬浮
        '''
        element_list = args
        if len(element_list) == 2:
            element = self.get_element(element_list[0],element_list[1])
        elif len(element_list) == 3:
            element = self.get_list_elements(element_list[0],element_list[1],element_list[2])
        ActionChains(self.driver).move_to_element(element).perform()
    def mouse_click(self,*args):
        '''
        模拟鼠标点击
        '''
        element_list = args
        if len(element_list) == 2:
            element = self.get_element(element_list[0], element_list[1])
        elif len(element_list) == 3:
            element = self.get_list_elements(element_list[0], element_list[1], element_list[2])
        ActionChains(self.driver).click(element).perform()

    def ctrl_f5_refresh(self):
        '''
        强制刷新浏览器
        :return:
        '''
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys(Keys.F5).key_up(Keys.CONTROL).perform()

    def switch_iframe(self,by,value):
        '''
        切换iframe
        :return:
        '''
        element = self.get_element(by,value)
        self.driver.switch_to.frame(element)
        time.sleep(3)
    def freed_iframe(self):
        '''
        释放iframe--driver回到原本窗口
        :return:
        '''
        self.driver.switch_to.default_content()

    def is_check_box(self,by,value,check = None):
        '''
        1.封装判断复选框是否勾选
         2.根据情况来确定是否点击 勾选/取消 复选框
         :return:
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
        :return:
        '''
        # element = self.get_element(element)
        flge = element.is_displayed()
        if flge == True:
            #print(element,' : ','查找成功') # test
            return element
        else:
            return False

    def get_ini_element_send_value(self,sections,key):
        '''
        获取配置文件的-定位方法/定位元素
        输入从配置文件获取需要输入的-value
         完成元素定位--完成输入值操作
         :return:
        '''
        data = readini.get_ini_value(sections,key)
        data_list = data.split(':')
        # print(data_list) test
        if len(data_list) == 3:
            self.send_value(data_list[0],data_list[1],data_list[2])
        else:

            self.send_value(data_list[0],data_list[1],data_list[2],int(data_list[3]))

    def get_ini_element_click_element(self,sections,key):
        '''
        获取配置文件的-定位方法/定位元素
         完成元素定位--完成点击操作
         :return:
        '''
        data = readini.get_ini_value(sections,key)
        data_list = data.split(':')
        if len(data_list) == 2:
            self.click_element(data_list[0],data_list[1])
        else:
            self.click_element(data_list[0],data_list[1],int(data_list[2]))

    def get_select(self,sections,key,text):
        '''
        定位下拉框的select——element
        调用selenium中Select中方法选择下拉框选项
        :return:
        '''
        data = readini.get_ini_value(sections,key)
        data_list = data.split(':')
        if len(data_list) == 2:
            element = self.get_element(data_list[0],data_list[1])
            Select(element).select_by_visible_text(text)
        elif len(data_list) == 3:
            element = self.get_list_elements(data_list[0],data_list[1],int(data_list[2]))
            Select(element).select_by_visible_text(text)
        else:
            print('localelment配置文件值录入有误！')

    def upload_file(self,file_path):
        '''
        上传文件方法封装
        传入文件路径
        :return:
        '''
        pykey = PyKeyboard()
        pykey.tap_key(pykey.shift_key) # 切换英文输入法
        pykey.type_string(file_path) # 输入文件路径
        time.sleep(3)
        pykey.tap_key(pykey.enter_key) # 点击Enter键上传文件
    def download_file(self):
        '''
        下载文件
        :return:
        '''
        pykey = PyKeyboard()
        pykey.tap_key(pykey.enter_key)  # 点击Enter键确定下载文件
    def get_js_readonly(self,by,value,number=None):
        '''
        获取元素by，value判断哪种使用哪种方法remove_readonly
        :return:
        '''

        if by == 'id':
            by_key = 'getElementById'
            js = "document.%s('%s').removeAttribute('readonly')"%(by_key,value)
        elif by == 'class':
            by_key = 'getElementsByClassName'
            js = "document.%s('%s')[%d].removeAttribute('readonly')"%(by_key,value,number)
        else:
            print('%s，%s：传递值有误，去除readonly属性失败')
        return js
    def remove_readonly(self,by,value,number=None):
        '''
        去掉input标签read_only属性
        '''

        js = self.get_js_readonly(by,value,number)
        self.driver.execute_script(js)

    def seitch_alert(self,temp,value=None):
        '''
        系统级弹窗alert
        :param temp: 确认 or 取消
        :param value: 是否有输入值
        '''
        windows_alert = self.driver.switch_to.alert
        if temp == '确认':
            if value != None:
                windows_alert.send_keys(value)
            windows_alert.accept()
        else:
            windows_alert.dismiss()
    def scroll_get_element(self,by,value,str_title):# 不通用
        '''
        滑动页面查找元素
        :param by:
        :param value:
        '''
        js = "document.documentElement.scrollTop=1000"
        element_list = self.get_elements(by,value)
        while True:
            for element in element_list:
                tatle_name = element.text
                if tatle_name in str_title:
                    element.click()
                    break
            self.driver.execute_script(js)
            time.sleep(3)
    def scroll_element(self,by,value):
        '''
        项目通用滑动页面查找元素方法封装
        '''
        js = "document.documentElement.scrollTop=1000" # 滑动页面1000像素待执行js语句
        while True:
            try:
                element = self.get_element(by,value)
                tiale_name = element.text
                print(tiale_name)
                time.sleep(5)
                element.click()
                break
            except:
                self.driver.execute_script(js) # 执行js语句往下滑动页面1000像素
    def get_cookie(self,temp):
        '''
        接口也依赖
        获取cookie
        :return:
        '''
        time.sleep(2)
        cookie = self.driver.get_cookie(temp)
        time.sleep(2)
        handle_json.write_cookie(cookie)

    def set_cookie(self):
        '''
        植入cookie
        :param cookie:
        :return:
        '''
        cookie = handle_json.get_data()
        self.driver.delete_all_cookies()
        time.sleep(2)
        self.driver.add_cookie(cookie)

    def save_png(self):
        '''
        处理截图
        :return:
        '''
        now_time = time.strftime('%y%m%d-%H-%M-%S') # 获取当前系统时间格式 年月日-时-分-秒
        self.driver.save_screenshot('%s.png'%now_time) # 以当前时间命名图片


    def  user_name(self):
        '''
        获取随机用户名信息
        :return:
        '''
        user_info = random.sample('0123456789zxcvbnmasdfghjklqwertyuiop',7)
        name = ''.join(user_info)
        return name

    def get_code_img(self,img_path,by,value):
        '''
        获取验证码截取图片
        :param img_path: 图片路径
        :param by: 验证码图片元素获取方式
        :param value: 验证码图片元素值
        :return:
        '''
        self.driver.save_screenshot(img_path) # 截取图片保存至img_path路径
        element = self.get_element(by,value)# 获取验证码元素
        a = element.location['x']# 获取x坐标，对应长方形左上角点坐标
        b = element.location['y']# 获取y坐标，对应长方形右下角坐标
        c = element.size['weith']+a# 获取宽度和X坐标组成的长方形右上角点坐标
        d = element.size['height']+b# 获取宽度和X坐标组成的长方形左下角点坐标
        img = Image.open(img_path)# 打开需要识别的图片
        img1 = img.crop((a,b,c,d))# 按照传入尺寸裁剪图片
        img1.save(img_path)# 截取验证码图片保存至路径

    def get_yzm_code(self,img_path):
        '''
        获取验证码图片的验证码文本信息
        :param img_path:验证码图片路径
        :return:
        '''
        img = Image.open(img_path) # 需要先用imge模块打开验证码图片
        text = pytesseract.image_to_string(img) # 利用pytesseract库获取验证码图片的验证码文本信息
        return text # 返回验证码

    def close(self):
        '''
        封装关闭浏览器方法
        :return:
        '''
        self.driver.quit()

    def main(self):
        selenium_driver = Selenium_Driver()



if __name__ == '__main__':
    '''入口程序'''
    try:
        pass
        driver = webdriver.Chrome()
        selenium_driver = Selenium_Driver(driver)
        # user_na = selenium_driver.user_name()
        # print(user_na)
        selenium_driver.get_url('http://csdqtttyweb.lx901.com/Register?Intr=')
        selenium_driver.cz_browser("最大")
        selenium_driver.click_element('class','ui-dialog-close')
        selenium_driver.send_value('ttt210','class','inp',0)
        selenium_driver.send_value('1','class', 'inp', 1)
        selenium_driver.send_value('aaaa1111','class', 'inp', 2)
        selenium_driver.send_value('13585214562', 'class', 'inp', 3)
        selenium_driver.click_element('text','免费注册')
        element = selenium_driver.get_element('class','ui-dialog-content')
        time.sleep(3)
        print(element.text)
        time.sleep(3)
        # selenium_driver.save_png()

        # http://www.5itest.cn/register?goto=http%3A//5itest.cn/  学习网页
        # selenium_driver.get_url('http://csdqthcweb.lx901.com/')
        # selenium_driver.cz_browser("最大")
        # selenium_driver.click_element('class','ui-dialog-close')
        # selenium_driver.send_value('ttt1','css','span.login-mane>input')
        # selenium_driver.send_value('aaaa2222','css','span.login-password>input')
        # selenium_driver.send_value('9999','css','.login-code')
        # selenium_driver.click_element("text",'登录')
        # selenium_driver.click_element('class', 'ui-dialog-close')
        # time.sleep(3)
        # selenium_driver.get_url('http://csdqthcweb.lx901.com/UserCenter/UserInfo')
        # element1 = selenium_driver.get_element('id','start') # 只读input标签属性
        # element1.clear()
        #element1.send_keys(Keys.CONTROL,'a')
        #element1.send_keys('2018-11-22 02:25:00')
        # 豪彩数据

        # selenium_driver.get_url('https://www.imooc.com')
        # selenium_driver.cz_browser("最大")
        # time.sleep(2)
        # #selenium_driver.cz_browser('刷新')
        #
        # print('0')
        # time.sleep(10)
        # selenium_driver.get_ini_element_click_element('element','login')
        # print('1')
        # time.sleep(10)
        # selenium_driver.get_ini_element_send_value('element','username')
        # print('2')
        # time.sleep(2)
        # selenium_driver.get_ini_element_send_value('element', 'password')
        # print('3')
        # time.sleep(2)
        # selenium_driver.get_ini_element_click_element('element', 'clicklogin')
        # print('4')
        #
        # selenium_driver.get_cookie('apsid')



        # time.sleep(5)
        # selenium_driver.get_url('https://www.imooc.com/wenda/save')
        # selenium_driver.switch_iframe('id','ueditor_0')
        # element = selenium_driver.get_element('tagname','p')
        # selenium_driver.mouse_click('tagname','p')


        # print('5')
        # selenium_driver.switch_mouse('css','.avator-img') # 鼠标悬浮至元素对象上面
        # time.sleep(2)
        # selenium_driver.click_element('css','.js-avator-link') # 操作悬浮出现元素
        # time.sleep(2)
        # selenium_driver.click_element('css','.avator-btn-fake') # 点击上传文件按钮
        # time.sleep(2)
        # selenium_driver.upload_file('E:\\cmj.jpg') # E:\cmj.jpg
        # time.sleep(100)
        # temp = selenium_driver.get_element_nodisplayed('id','upload') # input标签的上传文件，直接send_keys（传入照片或文件路径）
        # time.sleep(2)
        # temp.send_keys('E:/陈明菊.jpg')
        # 慕课数据

        # selenium_driver = Selenium_Driver()
        # selenium_driver.get_url('http://csdqtttyweb.lx901.com')
        # selenium_driver.cz_browser("最大")
        # selenium_driver.click_element('class', 'ui-dialog-close')
        # time.sleep(3)
        # selenium_driver.send_value('ttt22','xpath','//label',0)
        # selenium_driver.send_value('aaaa2222','xpath','//label',1)
        # selenium_driver.click_element('class','regsiter-btn')
        # selenium_driver.click_element('class', 'ui-dialog-close')
        # selenium_driver.get_url('http://csdqtttyweb.lx901.com/Report/AccountChange')
        # selenium_driver.remove_readonly('id','start')
        # time.sleep(3)
        # selenium_driver.send_value('2017-10-28 11:11:11','id','start')
        # time.sleep(5)
        # print('6')
        # selenium_driver.get_ini_element_click_element('element', 'edit')
        # print('6')
        # selenium_driver.get_select('element','selec','Web前端工程师')

        # selenium_driver.get_url('https://www.imooc.com/article/be')
        # selenium_driver.cz_browser('最大')
        # selenium_driver.scroll_element('text','2019年Java生态状况')
        # selenium_driver.switch_window('2019年Java生态状况')
        # time.sleep(2)
        # selenium_driver.send_value('test','class','search-input')
        # time.sleep(2)

    except Exception as err:
        print(err)
    finally:
        time.sleep(2)
        selenium_driver.close()

