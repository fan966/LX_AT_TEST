# -*-coding:utf-8-*-
from Libs.Base_Action import BaseAction
from PO.pageobject.usercenter_page import UserCenterPage
import logging
import sys
import time
class Us_Center_action(BaseAction):

    def close_board(self):
        '''
        关闭平台公告
        :return:
        '''
        if self.check_element_displayed(UserCenterPage.user_ptgg):
            self.click_element(UserCenterPage.usercenter_board)

    def close_activ(self):
        '''
        关闭签到活动弹窗
        :return:
        '''
        if self.check_element_displayed(UserCenterPage.user_actvi):
            self.click_element(UserCenterPage.usercenter_actviboard)

    def to_top_page(self):
        '''
        判断前台当前所在页面，进入充值页面
        :return:
        '''
        # 判断是否在首页
        if self.check_element_displayed(UserCenterPage.home_log):
            self.click_element(UserCenterPage.home_deposit)
            self.switch_window("充值")
        # 判断是否在用户中心
        elif self.check_element_displayed(UserCenterPage.usercenter_log):
            self.click_element(UserCenterPage.user_deposit)
            self.switch_window("充值")
        # 判断是否在游戏页面
        elif self.check_element_displayed(UserCenterPage.game_reault):
            self.click_element(UserCenterPage.user_deposit)
            self.switch_window("充值")
        else:
            logging.info('【INFO】页面不存在充值入口：请检查【{}】'.format(sys._getframe().f_code.co_name))

    def to_withdraw_page(self):
        '''
        判断页面，进入提款页面
        :return:
        '''
        # 判断是否在首页
        if self.check_element_displayed(UserCenterPage.home_log):
            self.click_element(UserCenterPage.home_withdraw)
            self.switch_window("充值")
        # 判断是否在用户中心
        elif self.check_element_displayed(UserCenterPage.usercenter_log):
            self.click_element(UserCenterPage.user_withdraw)
            self.switch_window("充值")
        # 判断是否在游戏页面
        elif self.check_element_displayed(UserCenterPage.game_reault):
            self.click_element(UserCenterPage.user_withdraw)
            self.switch_window("充值")
        else:
            logging.info('【INFO】页面不存在提款入口：请检查【{}】'.format(sys._getframe().f_code.co_name))

    def to_officialgame_page(self,data):
        '''
        根据ID进入游戏页面
        :return:
        '''
        if data.find(',') != -1:
            datas = data.split(',')
            self.get_url(UserCenterPage.get_officialgame_url(int(datas[1])))
            time.sleep(3)
            if self.title_in(datas[0]):
                logging.info('【INFO】【{}】进入页面成功'.format(datas[0]))
            else:
                logging.info('【INFO】【{}】进入页面失败，请检查文件数据'.format(datas[0]))
        time.sleep(2)


    def to_traditiongame_page(self,data):
        '''
        根据ID进入游戏页面
        :return:
        '''
        if data.find(',') != -1:
            datas = data.split(',')
            self.get_url(UserCenterPage.get_traditiongame_url(int(datas[1])))
            time.sleep(3)
            if self.title_in(datas[0]):
                logging.info('【INFO】【{}】进入页面成功'.format(datas[0]))
            else:
                logging.info('【INFO】【{}】进入页面失败，请检查文件数据'.format(datas[0]))

    def check_msg_txt(self, locator, str_):
        """
        判断消息弹框是否存在，验证消息弹框内容并关闭
        :param locator:
        :param str_:
        :return:
        """
        flag = False
        time.sleep(1.5)
        try:
            if self.check_element_displayed(locator):
                el = self.find_element(locator)
                if str_ in el.text:
                    logging.info(el.text)
                    flag = True
                    self.click_element(UserCenterPage.msg_prompt_sbmit)
                else:
                    logging.error(el.text)
                self.click_element(UserCenterPage.msg_prompt_sbmit)
        except Exception as err:
            logging.error(err)
        return flag








