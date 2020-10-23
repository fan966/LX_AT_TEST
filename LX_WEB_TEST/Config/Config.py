#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import configparser
import logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
class MyConfig(configparser.ConfigParser):
    def __init__(self):
        configparser.ConfigParser.__init__(self, defaults=None)

    def optionxform(self, optionstr):
        return optionstr




class Config(object):
    def __init__(self):
        '''
        初始化配置
        '''
        self.current_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.cofig_path = os.path.join(self.current_path,'Config')
        self.data_path = os.path.join(self.current_path, 'Data')
        self.report_path = os.path.join(self.current_path, 'Report')
        self.log_path = os.path.join(self.report_path,'Log')
        self.html_report_path = os.path.join(os.path.join(self.report_path,'Html_Report'),'html_report.html')
        self.ini_config_path = os.path.join(self.cofig_path,'config.ini')
        self.ini_global_path = os.path.join(self.cofig_path,'global.ini')
        # config配置文件实例化
        self.C = MyConfig()
        self.C.read(self.ini_config_path,encoding='utf-8')
        # global配置文件实例化
        self.G = MyConfig()
        self.G.read(self.ini_global_path,encoding='utf-8')
        self.config_sections_list = self.C.sections()
        self.test_type = self.G.getint('Global_ini','TEST_Type')
        self.test_web_url = self.C.get(self.config_sections_list[self.test_type],'web_host')
        self.test_ag_url = self.C.get(self.config_sections_list[self.test_type],'ag_host')
        self.browser_type = self.G.get('Global_ini','browesr_type')




        #print(self.test_web_url)

    def get_ini_value(self,section,option):
        '''
        获取global.ini配置数据
        :param section:
        :param option:
        :return:
        '''
        value = self.G.get(section,option)
        return value





if __name__ == '__main__':
    c = Config()
    print(c.get_ini_value('Global_ini','WebUserName'))
    logging.info('test')