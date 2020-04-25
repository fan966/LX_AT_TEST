# -*-coding:utf-8-*-
from PO.pageobject.game_page import GamePageLocator
from PO.common.common_util import *
from PO.pageaction.us_center_action import *
import logging
from Libs.cnfg_util import config_ini
class Gameing(Us_Center_action):
    yamlbs_num = config_ini('game.ini', 'game', 'yamlbs_num')
    yamlsj_num = config_ini('game.ini', 'game', 'yamlsj_num')
    def official_gameing(self):
        '''
        官方游戏随机下注
        :return:
        '''

        self.random_play_list(GamePageLocator.play_type)

    def random_play_list(self,locator):
        el = self.find_elements(locator)
        for i in range(len(el)):
            el[i].click()
            if self.check_element_displayed(GamePageLocator.random_btn):
                # 倍数
                element = self.find_element(GamePageLocator.pow_num)
                element.clear()
                element.send_keys(self.yamlbs_num)
                #self.send_value(GamePageLocator.random_num,5) 随机注数
                temp = self.find_element(GamePageLocator.random_num)
                temp.clear()
                temp.send_keys(self.yamlsj_num)
                # 随机
                self.click_element(GamePageLocator.random_btn)
                time.sleep(0.5)
                self.click_element(GamePageLocator.confirm_btn)
                if self.check_msg_txt(UserCenterPage.prompt_text,'投注成功'):
                    logging.info('【功能检查】游戏下注成功')
                else:
                    logging.info('【功能检查】游戏下注失败，请检查')

    def official_excel_gamging(self,data):
        # 根据游戏类型判断调用方法
        if data['types'] in '11选5,PK拾,分分彩,时时彩':
            self.official_lottery_min(data)
        else:
            logging.error('【INFO】【游戏类型有误，请检查】【{}】'.format(data['types']))


    def official_lottery_min(self,data):
        '''
        官方分分彩
        :param data:
        :return:
        '''
        # 根据游戏ID进入游戏
        self.swith_game_page(data['lottery'],data['lottery_id'])
        # 获取玩法点击
        self.get_playtypr_loc_click(data['play1'])
        if self.check_element_displayed(GamePageLocator.play_num_list):
            # 循环投注项投注玩法
            item = data['item'].split('|')
            for i in range(len(item)):
                j = 1
                j += i
                temp = item[i].split(',')
                for t in range(len(temp)):
                    self.click_element(GamePageLocator.get_game_loc(j,temp[t]))
            # 获取游戏倍数
            ele = self.find_element(GamePageLocator.pow_num)
            ele.clear()
            ele.send_keys(data['multip'])
            # 立即下注按钮
            self.click_element(GamePageLocator.fast_btn)
            if self.check_msg_txt(UserCenterPage.prompt_text, '投注成功'):
                logging.info('【功能检查】游戏下注成功')
            else:
                logging.info('【功能检查】游戏下注失败，请检查')
        else:
            logging.info('【INFO】游戏玩法没有点击投注选项，请确认')











    def swith_game_page(self,data1,data2):
        '''
        根据ID进入游戏页面
        :return:
        '''
        if data1 not in self.driver.title:
            '''
            根据游戏名判断页面
            '''
            self.get_url(UserCenterPage.get_officialgame_url(data2))
            time.sleep(3)
            if self.title_in(data1):
                logging.info('【INFO】【{}】进入页面成功'.format(data1))
            else:
                logging.error('【INFO】【{}】进入页面失败，请检查文件数据'.format(data1))
        else:
            logging.info('【INFO】【{}】处于当前游戏页面'.format(data1))
        time.sleep(2)

    def get_playtypr_loc_click(self,data):
        '''
        获取玩法locator并点击操作
        :param data:
        :return:
        '''

        self.click_element(GamePageLocator.get_playtype_loc(data))























