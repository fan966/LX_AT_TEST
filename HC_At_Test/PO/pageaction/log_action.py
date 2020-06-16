# -*-coding:utf-8-*-
from Libs.Base_Action import BaseAction
from PO.pageobject.log_page import Loglocator
from PO.pageobject.usercenter_page import UserCenterPage
import logging
import time
from PO.common.cs_data_excel_util import login_info
class Login(BaseAction):
    '''
    登录公共模块
    '''
    def login_page(self,env_type,skin,type):
        '''
        判断前后台，调用相应的登录方法
        :param env_type:环境名称
        :param skin:环境名称
        :param type:环境类型
        :return:
        '''
        l_info = login_info(env_type,skin,type)
        if type == '前端':
            self.web_login(l_info['url'],l_info['user'],l_info['pwd'])
        if type == '后台':
            self.ag_login(l_info['url'],l_info['user'],l_info['pwd'])



    def web_login(self,url,user,pwd):
        # 输入url
        self.get_url(url+'/Login')
        self.driver.refresh()
        time.sleep(2)
        self.send_value(Loglocator.username,user)
        self.send_value(Loglocator.userpwd,pwd)
        # 判断验证码元素是否存在
        if self.check_element_displayed(Loglocator.code):
            self.send_value(Loglocator.code,"9999")
        self.click_element(Loglocator.log_btn)
        # 判断签到活动弹窗/公告
        self.close_dialog()
        time.sleep(1)



    def ag_login(self,url,user,pwd):
        # 输入url
        self.get_url(url + '/Login')
        # 切换iframe
        self.switch_iframe(Loglocator.top_iframe)
        self.send_value(Loglocator.ag_log_name,user)
        self.send_value(Loglocator.ag_log_code,'8888')
        self.click_element(Loglocator.ag_next_btn)
        self.send_value(Loglocator.ag_log_password,pwd)
        self.click_element(Loglocator.ag_log_btn)

    def close_dialog(self):
        # 签到活动弹窗
        if self.check_element_displayed(UserCenterPage.user_actvi):
            self.click_element(UserCenterPage.usercenter_actviboard)
        else:
            pass
        # 公告弹窗
        if self.check_element_displayed(UserCenterPage.user_ptgg):
            self.click_element(UserCenterPage.usercenter_board)
        else:
            pass
        # 签到活动弹窗
        if self.check_element_displayed(UserCenterPage.user_actvi):
            self.click_element(UserCenterPage.usercenter_actviboard)
        else:
            pass




if __name__ == "__main__":
    l = Login(driver)
    temp = l.login_page("演示环境","豪彩","前端")
