# -*-coding:utf-8-*-
from Libs.Base_Action import BaseAction
from PO.pageobject.ag_home_page import AgHomeLocator
import time
import logging
import sys
class AgHome(BaseAction):
    '''
    首页通用操作
    '''
    def close_ag_pop(self):
        '''
        关闭公告弹窗
        :return:
        '''
        self.top_iframe()
        if self.check_element_displayed(AgHomeLocator.sys_pop):
            self.click_element(AgHomeLocator.sys_pop_btn)
        time.sleep(1)


    def swith_mod(self,first,second):
        '''
        切换一级菜单---二级菜单
        :return:
        '''
        try:
            self.top_iframe()
            self.click_element(AgHomeLocator.get_menu_loc(first))
            self.click_element(AgHomeLocator.get_menu_loc(second))
        except Exception as err:
            logging.error(err)
            logging.info('【INFO】切换菜单失败，请检查{}：一级菜单【{}】：二级菜单【{}】'.format(sys._getframe().f_code.co_name,first,second))

    def swith_table(self,table_name):
        '''
        根据table名点击table栏目
        :param table_name: table名
        :return:
        '''
        try:
            self.top_iframe()
            self.click_element(AgHomeLocator.get_table_loc(table_name))
            # 切换进入table_iframe
            self.switch_iframe(AgHomeLocator.tab_iframe)
        except Exception as err:
            logging.error(err)
            logging.info('【INFO】切换table失败，请检查{}：table栏目：{}'.format(sys._getframe().f_code.co_name, table_name))

    def close_table_act(self,table_name):
        '''
        关闭table栏目
        :return:
        '''
        self.top_iframe()
        self.click_element(AgHomeLocator.get_table_close_btn_loc(table_name))

    def refresh_table_act(self,table_name):
        '''
        刷新你table栏目
        :param table_name:
        :return:
        '''
        self.top_iframe()
        self.click_element(AgHomeLocator.get_table_refresh_loc(table_name))

    def top_iframe(self):
        '''
        切换至首页，主页左边栏目iframe
        :return:
        '''
        # 释放iframe
        self.freed_iframe()
        # 切换进入首页iframe
        self.switch_iframe(AgHomeLocator.top_iframe)

    def financial_pop_confirm(self):
        '''
        财务操作弹窗确认
        :return:
        '''
        if self.check_element_displayed(AgHomeLocator.financia_pop):
            self.click_element(AgHomeLocator.financia_pop_btn)
        if self.check_element_displayed(AgHomeLocator.mag_panel):
            self.click_element(AgHomeLocator.mag_panel_btn)
            self.click_element(AgHomeLocator.financia_pop_btn)





