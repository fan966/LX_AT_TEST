# -*-coding:utf-8-*-
import logging
from Libs.Base_Action import BaseAction
import time
from PO.pageobject.betgame_page import BetPageLocator
from PO.common.common_util import *
class BetGameTime(BaseAction):
    # 期数提示
    period_tip = {}
    # 游戏倒计时
    game_time = {}

    def get_hc_game_time(self):
        '''
        豪彩游戏时间
        :return:
        '''
        while True:
            time_list = []
            try:
                url = self.driver.current_url  # 获取当前窗口url
                #print(url)
                dict_key = re_findall('Index/[0-9].*', url)
                #print(dict_key)
                if len(dict_key) > 0:
                    dict_key = re_sub('#[0-9].*', '', self.driver.current_url)
                    #print(dict_key)

                    try:
                        self.period_tip[dict_key] = self.find_element(BetPageLocator.period_tip).text
                        #  period_tip = {'http://csdqthcweb.lx901.com/OtherGame/Index/319'：’未开盘‘}

                        if self.period_tip[dict_key] in ['未开盘']:
                            break

                        game_time_list = self.find_elements(BetPageLocator.hc_game_time)
                        for game_time_el in game_time_list:
                            game_time_ = game_time_el.get_attribute('outerHTML')

                            len_game_time = len(game_time_)
                            time_list.append(int(game_time_[len_game_time - 27:len_game_time - 26]))
                        # hours
                        game_time_ = time_list[0] * 60 * 60 * 10
                        game_time_ += time_list[1] * 60 * 60
                        # minutes
                        game_time_ += time_list[2] * 60 * 10
                        game_time_ += time_list[3] * 60
                        # seconds
                        game_time_ += time_list[4] * 10
                        game_time_ += time_list[5]
                        self.game_time[dict_key] = game_time_
                        # print(game_time_)
                        # print(self.period_tip)
                        # print(self.game_time)
                    except Exception as e:
                        logging.debug(e)
                else:
                    time.sleep(0.1)
            except Exception as e:
                logging.debug(e)
                break
    # print(period_tip)
    # print(game_time)

    def test_el_html(self):
        el_list = self.find_elements(BetPageLocator.hc_game_time)
        for game_time_el in el_list:
            game_time_ =game_time_el.get_attribute('outerHTML')
            print(game_time_)
            len_game_time = len(game_time_)
            print('长度：',len_game_time)
            # print(int(game_time_[len_game_time-27]))
            # print(int(game_time_[len_game_time - 26]))
            print(int(game_time_[len_game_time - 27:len_game_time - 26]))
            time.sleep(5)


