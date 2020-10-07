#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 学习路径   https://www.cnblogs.com/hester/p/6025489.html    configparser  重点
# https://www.jianshu.com/p/d9774cf1fea5    pandas库学习路径
import os
import configparser
import logging

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
        self.config_path = os.path.join(self.current_path,'Config')
        self.data_path = os.path.join(self.current_path,'Data')
        self.verify_path = os.path.join(self.current_path, 'Verify')
        self.report_path = os.path.join(os.path.join(os.path.join(self.current_path,'Report'),'html_report'),'html_report.html')
        self.log_path = os.path.join(os.path.join(self.current_path,'Report'),'log')
        self.ini_config_path = os.path.join(self.config_path,'config.ini')
        self.ini_global_path = os.path.join(self.config_path,'global_config.ini')
        self.db_config_path = os.path.join(self.config_path,'db_sqlserver.ini')
        self.game_bet_path = os.path.join(self.config_path,'game.ini')
        self.test_case_dirname_path = os.path.join(self.current_path,'Test_Case')
        self.user_case_file_path = os.path.join(os.path.join(self.current_path,'Test_Case'),'User')
        self.game_case_file_path = os.path.join(os.path.join(self.current_path,'Test_Case'),'Game')
        self.game_bet_yaml_path = os.path.join(os.path.join(self.verify_path,'Game'),'game_bet_play_data.yaml')
        # 实例化对象
        self.C = MyConfig()
        self.C.read(self.ini_config_path,encoding='utf-8')
        self.case_data_from_type = self.C.getint('default','case_data_from_type')
        self.IsRun = self.C.get('rules','IsRun')
        self.ApplyEnv = self.C.get('rules','ApplyEnv')
        self.RunResult = self.C.get('rules','RunResult')
        self.report_filename = self.C.get('default','report_file')
        self.case_report_html_path = os.path.join(self.report_path,self.report_filename)
        self.case_data_file_path = os.path.join(self.data_path,self.C.get('default','case_data_file'))
        self.interface_path = os.path.join(self.data_path,self.C.get('default','interface_file'))
        # 请求全局参数获取
        self.Global = MyConfig()
        self.Global.read(self.ini_global_path,encoding='utf-8')
        self.api_type = self.Global.getint('Global_ini','Api_Type')
        self.config_sections_list = self.C.sections()
        self.db_config_name = self.C.get(self.config_sections_list[self.api_type],'env_db_cfg_item')
        self.ag_host = self.C.get(self.config_sections_list[self.api_type],'ag_host') # 对应环境api后台地址
        self.ag_api_host = self.C.get(self.config_sections_list[self.api_type],'api_host') # 对应环境api前台地址
        self.ag_account = self.C.get(self.config_sections_list[self.api_type],'FAcount')
        self.key = self.C.get(self.config_sections_list[self.api_type],'key')
        self.requests_retry_num = self.C.getint('default','requests_retry')
        self.Game = MyConfig()
        self.Game.read(self.game_bet_path,encoding='utf-8')
        self.test_game_id = self.Game.get('game','test_game_id')
        self.test_account = self.Game.get('game','test_account')
        self.test_password = self.Game.get('game','test_password')
        self.bet_num = self.Game.get('game','bet_num')
        self.bet_note = self.Game.get('game','bet_note')
        self.game_per_info = self.Game.getint('game','game_period_info')



        #print(self.case_data_file_path)

    def get_ini_value(self,sections,options):
        '''
        返回全局变量配置数据
        :return:
        '''
        return_data = self.Global.get(sections,options)
        return return_data

    def set_options_value(self,options,set_value,setions = 'Global_ini'):
        '''
        回写全局变量值
        :return:
        '''
        self.Global.set(setions,options,set_value)
        try:
            with open(self.ini_global_path, 'w+', encoding='utf-8') as f:
                self.Global.write(f)
        except Exception as err:
            logging.error(err)
            logging.error('配置文件回写数据报错，请检查')

    def set_game_period_info_options_value(self,options,set_value,setions = 'game'):
        '''
        六合彩期数回写，用于特定场景
        :return:
        '''
        self.Game.set(setions,options,set_value)
        try:
            with open(self.game_bet_path, 'w+', encoding='utf-8') as f:
                self.Game.write(f)
        except Exception as err:
            logging.error(err)
            logging.error('配置文件回写数据报错，请检查')





    def get_run_rules_config(self):
        '''
        获取全局运行过滤规则字典
        :return:
        '''
        run_rules ={}
        if self.ApplyEnv:
            run_rules['ApplyEnv'] = self.ApplyEnv
        if self.RunResult:
            run_rules['RunResult'] = self.RunResult
        if self.IsRun:
            run_rules['IsRun'] = self.IsRun

        return run_rules



if __name__ == '__main__':

    c = Config()
    # #c.get_run_rules_config()
    # account = c.get_ini_value('Global_ini','WebUserName')
    # password = c.get_ini_value('Global_ini','WebPwd')
    # print(account)
    # print(password)
    #Config().set_options_value('amount_pwd','test11')
    #c.set_game_period_info_options_value('game_period_info','152487')


