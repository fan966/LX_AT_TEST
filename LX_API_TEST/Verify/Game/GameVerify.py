#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Libs.http_requests import *
from Config.Config import *
import logging
from Libs.Db_Sql_Util import *
import random
from Libs.Time_Util import *
import yaml
import os
from Libs.common import *
from Verify.User.UserVerify import login_api
from Libs.Random_util import RandomUtil
from Libs.log_util import set_log
'''
游戏模块通用方法
'''
r = RandomUtil()
def get_official_game_id(retrun_all_id = False):
   '''
   调用获取首页游戏分类接口获取游戏ID
   获取官方游戏ID
   :param retrun_all_id: 返回数据（retrun_all_id为false时返回一个ID，当为trun时，返回所有ID）
   :return:
   '''
   logging.info('=======================调用【获取首页游戏列表接口】接口====================================')
   actual_result = http_api_requests('游戏相关.获取首页游戏列表', NewVerifParmsData={})
   data = get_json_value(actual_result, '/Data/GameData')
   game_id_list = []
   for game_data in data:
      for game_list in game_data['GameCateList']:
         if game_list['FCategoryName'] not in ['真人视讯', 'VR彩', '体育竞技', '电子游戏', '棋牌']:
            # 过滤掉信用游戏
            if game_list['FGroupID'] == 3:
               # 获取游戏分类
               #print(game_list)
               FCategoryName = game_list['FCategoryName']
               if FCategoryName in ['11选5']: # 筛选彩种大类

                  for game_info in game_list['GameInfoList']:
                     game_list =[]

                     game_list.append(game_info['FGameName'])
                     game_list.append(game_info['FGameID'])
                     game_id_list.append(game_list)
   #print(game_id_list)
   return game_id_list if retrun_all_id else random.choice(game_id_list)

def get_game_period_info(LoginSessionID,datas,istemp=True):
   '''
   获取游戏最新期数信息
   istemp;为True获取官方游戏期数信息/False则获取信用游戏期数信息
   :return:
   '''
   while True:

      logging.info('=======================调用【获取游戏最新开盘期数】接口====================================')
      actual_result = http_api_requests('游戏相关.获取游戏最新开盘期数', Headers={"LoginSessionID": LoginSessionID},NewVerifParmsData=datas)
      json_data = get_json_value(actual_result, '/Data')
      json_period_data = json.loads(json_data, encoding='utf-8')
      # 本期期数
      current_period = json_period_data['fnumberofperiod']
      # 本期开盘时间
      start_time = json_period_data['fstarttime']
      # 期数状态 （0未开盘，1开盘中，2已封盘，3已开奖，4、已结算，5、返还金额）
      period_status = json_period_data['fstatus']
      # 游戏是否停售 ：false代表开售中，true代表停售中
      is_off_stop = json_period_data['fisstopseles']
      # 期数ID
      fid = json_period_data['fid']
      # 游戏ID
      game_id = json_period_data['gameID']
      # 通过ID获取彩种信息是否为秒秒彩/true则返回期数为0
      if istemp:
         game_info = from_game_id_get_game_info_official(game_id)
      else:
         game_info = from_game_id_get_game_info_credit(game_id)
      logging.info('获取游戏信息：{}'.format(game_info))
      # 本期封盘时间
      if '低频彩' in list(game_info.keys())[0]:
         end_time = json_period_data['fspecialcodeclosetime']
      else:
         end_time = json_period_data['fclosetime']
      logging.info('最新开盘期数信息：【期数状态：{}，本期期数：{}，本期开盘时间：{}，本期封盘时间：{}，游戏是否停售：{}，期数ID：{}】'
                   .format(period_status,current_period,start_time,end_time,is_off_stop,fid))
      # 判断游戏是否停售
      if is_off_stop:
         logging.error('游戏停售，不可下注！')

      if '秒秒彩' in list(game_info.keys())[0]:
         logging.info('此彩种为秒秒彩,返回期数ID：0')
         return fid
      # 判断期数状态
      if period_status != 1:
         logging.error('游戏未开盘，没有期数信息')
         return {}
      # 封盘时间-当前时间是否大于6秒

      now_time = get_now_time()

      end_time = end_time

      count_times = count_datatime(now_time,end_time,type='secods')

      if count_times < 10:
         logging.info('期数时间接近封盘，等待下一期期数')
      # 以上满足条件即可返回期数ID
      else:
         logging.info('获取游戏期数信息成功！')
         return fid

def get_officia_gam_bet_data(LoginSessionID = None,game_id = None,return_all_data=False):
   '''
   获取官方游戏下注数据
   :return:
   '''

   Radix = None
   moneyModel = None
   LoginSessionID = login_api(Config().test_account,Config().test_password) if not LoginSessionID else LoginSessionID
   game_id = Config().test_game_id if not game_id else game_id
   game_info = from_game_id_get_game_info_official(int(game_id))
   # 获取游戏赔率/禁用玩法数据
   logging.info('=======================调用【获取游戏最新开盘期数】接口====================================')
   actual_result = http_api_requests('游戏相关.获取游戏赔率数据', Headers={"LoginSessionID": LoginSessionID},NewVerifParmsData={"GameID":game_id})
   try:
      DisablePlay = get_json_value(actual_result, '/Data/DisablePlay')# 禁用玩法ID
      DisablePlay_item = get_json_value(actual_result, '/Data/DisablePlayItem') # 禁用玩法项ID
      DisablePlay_list = [] # 禁用玩法ID list
      for i in DisablePlay:
         if isinstance(i, str) and i:
            DisablePlay_list.append(int(i))
      odds_List = get_json_value(actual_result,'/Data/OddsList') # 获取玩法反水/赔率数据
      data = get_json_value(actual_result,'/Data')
      Radix = data['Radix']  # 单注下注金额基数
      moneyModel = data['moneyModel'] # 投注模式
   except Exception as err:
      logging.error(err)
   # 获取游戏玩法数据
   logging.info('=======================调用【获取游戏玩法数据】接口====================================')
   actual_result = http_api_requests('游戏相关.获取游戏玩法数据', Headers={"LoginSessionID": LoginSessionID},NewVerifParmsData={"GameID":game_id})
   game_data = get_json_value(actual_result,'/Data')
   game_data_path = Config().game_bet_yaml_path
   with open(game_data_path,'r',encoding='utf-8') as f:
      game_bet_data = yaml.safe_load(f.read())
      #print(game_bet_data)
   game_bet_list = []
   for data in game_data:
      for data_dict in data['Child']:
         for data_play_dict in data_dict['C']:
            #print(data_play_dict)
            if data_play_dict['Id'] not in DisablePlay_list:  # 过滤禁用玩法
               print(data_play_dict)
               for game_data_dict in data_play_dict['Child']:
                  # 此条查看匹配玩法名称
                  #print(game_data_dict)
                  if game_bet_data.__contains__(data_play_dict['Name']):
                     #print(data_play_dict['Name'])
                     game_play_item_name = data_play_dict['Name']
                     flag = ''
                     if '单式' in game_play_item_name:
                        flag = ','
                     elif '复式' in game_play_item_name or '组选' in game_play_item_name or '单双' in game_play_item_name or '定位胆' in game_play_item_name:
                        flag = '|'
                     if isinstance(game_bet_data[game_play_item_name],int):
                        if '分分彩'or '时时彩' in list(game_info.keys())[0]:
                           c = r.random_number_list1(game_bet_data[game_play_item_name],flag)
                        else:
                           c = r.random_number_list(game_bet_data[game_play_item_name],flag)
                     elif  isinstance(game_bet_data[game_play_item_name],dict):
                        # 获取字典value判断类型
                        if isinstance(list(game_bet_data[game_play_item_name].values())[0],list):
                           # 获取字典的key值，传入key和value获取玩法排列组合项
                           play_value_item = list(game_bet_data[game_play_item_name].keys())[0]
                           data = get_new_sort_data(play_value_item,list(game_bet_data[game_play_item_name].values())[0])
                           c = flag.join(data)
                     i = game_data_dict['Id']  # 玩法项ID
                     k = 0
                     t = int(Config().bet_num)
                     n = int(Config().bet_note)
                     moneyModel_list = []
                     for j in moneyModel:
                        if isinstance(j,str) and j and j != ',':
                           moneyModel_list.append(int(j))
                     m = moneyModel_list[0]
                     a = None
                     if m == 1:
                        a = Radix * n * t
                     elif m == 2:
                        a = Radix * n * t /10
                     elif m == 3:
                        a = Radix * n * t / 100
                     elif m == 4:
                        a = Radix * n * t / 1000
                     else:
                        logging.debug('投注模式有误，请检查')
                     game_bet_list.append([{"i":i,"c":c,"n":n,"t":t,"k":k,"m":m,"a":a,"ts":15}])

   return game_bet_list if return_all_data else random.choice(game_bet_list)


def from_game_id_get_game_info_official(game_id):
   '''
   根据游戏ID返回游戏信息（官方）
   :param game_id:
   :return:
   '''
   logging.info('=======================调用【获取首页游戏列表接口】接口====================================')
   actual_result = http_api_requests('游戏相关.获取首页游戏列表', NewVerifParmsData={})

   data = get_json_value(actual_result, '/Data/GameData')
   game_id_list = []
   for game_data in data:
      # print(game_data)
      for game_list in game_data['GameCateList']:
         if game_list['FCategoryName'] not in ['真人视讯', 'VR彩', '体育竞技', '电子游戏', '棋牌']:
            # 过滤掉信用游戏
            if game_list['FGroupID'] == 3:
               FCategoryName = game_list['FCategoryName']
               for game_info in game_list['GameInfoList']:
                  game_dic = {}
                  # print(FCategoryName,game_info)
                  game_dic.update({FCategoryName: {game_info['FGameName']: game_info['FGameID']}})
                  game_id_list.append(game_dic)

   for game in game_id_list:
      if list(list(game.values())[0].values())[0] == game_id:
         return game









def from_game_id_get_game_info_credit(game_id):
   '''
   根据游戏ID返回游戏信息（信用）
   :param game_id:
   :return:
   '''
   logging.info('=======================调用【获取首页游戏列表接口】接口====================================')
   actual_result = http_api_requests('游戏相关.获取首页游戏列表', NewVerifParmsData={})

   data = get_json_value(actual_result, '/Data/GameData')
   game_id_list = []
   for game_data in data:
      # print(game_data)
      for game_list in game_data['GameCateList']:
         if game_list['FCategoryName'] not in ['真人视讯', 'VR彩', '体育竞技', '电子游戏', '棋牌']:
            # 过滤掉信用游戏
            if game_list['FGroupID'] == 0:
               FCategoryName = game_list['FCategoryName']
               for game_info in game_list['GameInfoList']:
                  game_dic = {}
                  # print(FCategoryName,game_info)
                  game_dic.update({FCategoryName: {game_info['FGameName']: game_info['FGameID']}})
                  game_id_list.append(game_dic)

   for game in game_id_list:
      if list(list(game.values())[0].values())[0] == game_id:
         return game



def get_credit_gam_bet_data(LoginSessionID = None,game_id = None,return_all_data=False):
   '''
   获取六合彩/信用游戏玩法数据
   :return:
   '''
   Radix = None
   moneyModel = None
   LoginSessionID = login_api(Config().test_account, Config().test_password) if not LoginSessionID else LoginSessionID
   game_id = Config().test_game_id if not game_id else game_id

   game_info = from_game_id_get_game_info_official(int(game_id))
   # 获取游戏赔率/禁用玩法数据
   logging.info('=======================调用【获取游戏最新开盘期数】接口====================================')
   actual_result = http_api_requests('游戏相关.获取游戏赔率数据', Headers={"LoginSessionID": LoginSessionID},NewVerifParmsData={"GameID": game_id})
   DisablePlay_list = None
   try:
      DisablePlay = get_json_value(actual_result, '/Data/DisablePlay')# 禁用玩法ID
      DisablePlay_item = get_json_value(actual_result, '/Data/DisablePlayItem') # 禁用玩法项ID
      DisablePlay_list = [] # 禁用玩法ID list
      for i in DisablePlay:
         if isinstance(i, str) and i:
            DisablePlay_list.append(int(i))
      odds_List = get_json_value(actual_result,'/Data/OddsList') # 获取玩法反水/赔率数据
      data = get_json_value(actual_result,'/Data')
      Radix = data['Radix']  # 单注下注金额基数
      moneyModel = data['moneyModel'] # 投注模式
   except Exception as err:
      logging.error(err)
   # 获取游戏玩法项数据
   logging.info('=======================调用【获取游戏玩法数据】接口====================================')
   actual_result = http_api_requests('游戏相关.获取游戏玩法数据', Headers={"LoginSessionID": LoginSessionID},NewVerifParmsData={"GameID": game_id})
   game_data = get_json_value(actual_result, '/Data')
   game_data_path = Config().game_bet_yaml_path
   with open(game_data_path, 'r', encoding='utf-8') as f:
      game_bet_data = yaml.safe_load(f.read())
   # print(game_data)
   # print(game_bet_data)

   play_id_list = []
   for gamer_play in game_data:
      #print(gamer_play)
      for game_play_child in gamer_play['Child']:
         #print(game_play_child)
         if game_play_child['Id'] in DisablePlay_list: # 过滤禁用玩法
            continue
         if game_play_child['Name'] == '特码':
            #print(game_play_child)
            for tema_game_play_data in game_play_child['Child']:
               flag_list = []
               #print(tema_game_play_data)
               flag_list.append(tema_game_play_data['Id'])
               flag_list.append(tema_game_play_data['Name'])
               flag_list.append(tema_game_play_data['SId'])
               play_id_list.append(flag_list)

   return play_id_list if return_all_data else random.choice(play_id_list)


if __name__ == '__main__':
   # game_id = get_official_game_id()
   # print(game_id)
   set_log()
   #print(get_officia_gam_bet_data(return_all_data=True))
   #print(from_game_id_get_game_info(51))
   # data = get_credit_gam_bet_data(return_all_data=True)
   # print(data)
   # orderlist = []
   # orderlist1 = []
   # gamelist = []
   # for game_data in data:
   #    orderdata = {"amount": 301, "goal": str(game_data[0]), "id": game_data[0], "name": game_data[1], "odds": 43.61,"odds1": -1.0, "parentName": "特码", "sId": game_data[2], "timestamp": get_time_stamp()}
   #    gamelist.append(orderdata)
   # for i in range(0,48):
   #    orderlist.append(gamelist[i])
   # print(orderlist)
   # for i in range(48,49):
   #    orderlist1.append(gamelist[i])
   # orderlist1[0].update({"amount":300})
   # print(orderlist1)
   get_officia_gam_bet_data(game_id=612)


