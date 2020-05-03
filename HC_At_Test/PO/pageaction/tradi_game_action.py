# -*-coding:utf-8-*-
from PO.pageaction.us_center_action import *
from PO.pageobject.tradi_game_page import TradiGameLocator
import logging
from PO.pageaction.game_time_action import BetGameTime
from PO.common.common_util import *
from Libs.cnfg_util import config_ini
class TradiGame(Us_Center_action):
    bet_longhu = config_ini('game.ini','game','bet_longhu')

    def random_play(self):
        '''
        信用游戏随机下注
        :return:
        '''
        # 快捷按钮点击
        self.click_element(TradiGameLocator.fast_btn)
        # 获取玩法项list
        el = self.find_elements(TradiGameLocator.tradi_play_list)
        for i in range(len(el)):
            self.get_game_time()
            el[i].click()
            # 获取投注项list
            try:
                element = self.find_elements(TradiGameLocator.play_bet_list)
                for i in range(len(element)):
                    self.get_game_time()
                    if i%4 == 0:
                        element[i].click()
                # 输入金额
                self.get_game_time()
                self.send_value(TradiGameLocator.amount,10)
                # 点击确定按钮
                self.get_game_time()
                self.scroll_element(TradiGameLocator.commit_btn)
                # 投注二次确认
                time.sleep(1)
                if self.check_element_displayed(TradiGameLocator.second_btn):
                    self.click_element(TradiGameLocator.second_btn)
                #
                time.sleep(1)
                self.bet_text_exit()
            except Exception as eer:
                logging.debug(eer)

    def excel_tradi_gameing(self,data):
        '''
        excel配置玩法项下注
        :return:
        '''

        try:
            # 根据ID判断游戏页面
            self.to_swith_game_page(data['lottery'], data['lottery_id'])
            # 获取玩法locator点击
            self.get_game_time()
            self.click_element(TradiGameLocator.get_tradigame_play_loc(data['play1']))
            print(data['play1'])
            print(data['play2'])
            # 玩法判断并输入金额
            if data['play1'] == '龙虎斗':
                self.play1_bet_longhu(data['play2'],data['item'],data['amount'])
            else:
                self.play2_bet(data['play2'],data['item'],data['amount'])
            # 点击确定按钮
            self.get_game_time()
            self.scroll_element(TradiGameLocator.commit_btn)
            # 投注二次确认
            time.sleep(0.5)
            if self.check_element_displayed(TradiGameLocator.second_btn):
                self.get_game_time()
                self.find_element(TradiGameLocator.second_btn).click()
            else:
                self.click_element(TradiGameLocator.bet_sceeuse_btn)
            # 投注三次确认
            if self.check_element_displayed(TradiGameLocator.three_text):
                self.find_element(TradiGameLocator.bet_sceeuse_btn).click()
            # 下注文本检测
            time.sleep(0.5)
            self.bet_text_exit()
        except Exception as error:
            logging.error(error)
        finally:
            try:
                self.click_element(TradiGameLocator.bet_sceeuse_btn)
            except Exception as t:
                pass


    def to_swith_game_page(self, data1,data2):
        '''
        根据游戏名判断页面
        :return:
        '''
        if data1 not in self.driver.title:
            self.get_url(UserCenterPage.get_traditiongame_url(data2))
            time.sleep(3)
            if data1 in self.driver.title:
                logging.info('【INFO】【{}】进入页面成功'.format(data1))
            else:
                logging.info('【INFO】【{}】进入页面失败，请检查文件数据'.format(data1))
        else:
            logging.info('【INFO】【{}】处于当前游戏页面'.format(data1))
            time.sleep(2)




    def get_game_time(self):
        '''
        获取期数和时间状态
        :return:
        '''
        # 判断和获取到的期数和时间的键值是否一致
        #  获取当前url正则
        dict_key = re_sub('#[0-9].*', '', self.driver.current_url)
        if BetGameTime.period_tip.values() in ['未开盘']:
            logging.info('【游戏未开盘，请检查】')
        for i in range(4):
            # 确定在同一游戏页面
            if dict_key in BetGameTime.period_tip.keys() and dict_key in BetGameTime.game_time.keys():

                # 判断当前期数状态
                if BetGameTime.period_tip[dict_key] == '剩余投注时间' and BetGameTime.game_time[dict_key] > 1:
                    break
            else:
                try:
                    time.sleep(1)
                    print('3')
                    self.click_element(TradiGameLocator.btn)
                except Exception as e:
                    logging.debug(e)


    def bet_text_exit(self):
        if self.check_element_displayed(TradiGameLocator.text):
            text = self.find_element(TradiGameLocator.text).text
            if '成功' in text:
                logging.info('【功能检查】信用游戏下注成功')
                self.get_game_time()
                self.find_element(TradiGameLocator.bet_sceeuse_btn).click()
            else:
                self.click_element(TradiGameLocator.bet_sceeuse_btn)
        else:
            self.find_element(TradiGameLocator.bet_sceeuse_btn).click()

    def play2_bet(self,play2,item,amount):

        '''
        玩法2判断
        :return:
        '''
        if play2 == '':
            items = item.split(',')
            for i in range(len(items)):
                el = self.find_element(TradiGameLocator.get_play2_3(items[i]))
                self.get_game_time()
                el.send_keys(amount)
        else:
            items = item.split(',')
            for i in range(len(items)):
                el = self.find_element(TradiGameLocator.get_play2_1(play2, items[i]))
                self.get_game_time()
                el.send_keys(amount)

    def play1_bet_longhu(self,play2,item,amount):
        '''
        龙虎斗玩法特殊处理
        :return:
        '''
        if play2 in self.bet_longhu:
            items = item.split(',')
            for i in range(len(items)):
                el = self.find_element(TradiGameLocator.get_play2_2(play2, items[i]))
                self.get_game_time()
                el.send_keys(amount)




















