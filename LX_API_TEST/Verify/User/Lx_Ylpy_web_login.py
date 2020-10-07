#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 娱乐平台前台登录/随机下注
from Libs.http_requests import *
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from Libs.log_util import *
from Libs.Time_Util import *
import logging
import sys
sys.path.append('..')
def lx_ylpt_login():


    import json
    server_host = Config().ag_api_host
    logging.info('=======================调用【用户登录】接口====================================')
    actual_result = http_api_requests('娱乐平台.前台登录', Headers={"ASP.NET_SessionId":"453kmaiyd0flctslrmyoan0d","DROCQ.ISAPI":"False","DROCQ.ISGUEST":"False","GAMEID":"30","multiSelect":"true","DROCQ.FFORCESCHANGEPWD":"False"}, NewVerifParmsData={"username":"huiy07","password":"f09caad93c556216048595de602044b0","validateCode":"9999","sid":"453kmaiyd0flctslrmyoan0d"},return_result=False)
    cookie = actual_result.request.headers['Cookie']
    cookie = cookie.split('; ')
    cookie_dict = {}
    for i in cookie:
        list1 = i.split('=')
        cookie_dict.update({list1[0]:list1[1]})
    cookie_dict.update()



    logging.info('=======================调用【获取游戏玩法】接口====================================')
    actual_result = http_api_requests('娱乐平台.获取六合彩玩法',
                                      Headers=cookie_dict,
                                      NewVerifParmsData={"username": "huiy07",
                                                         "password": "f09caad93c556216048595de602044b0",
                                                         "validateCode": "9999", "sid": "453kmaiyd0flctslrmyoan0d"},
                                      return_result=False)

    # while True:
    #     try:
    #         logging.info('=======================调用【获取游戏玩法】接口====================================')
    #         res = requests.get(url=server_host + '/WS/GetBallData',Headers=cookie_dict)
    #         play_data = res.text
    #         play_data = json.loads(play_data) # 玩法数据
    #         logging.info('游戏玩法获取成功：{}'.format(play_data))
    #
    #         logging.info('=======================调用【获取游戏期数】接口====================================')
    #         res = requests.get(url=server_host + '/Shared/GetNewPeriod', cookies=cookie_dict,data={"_":get_time_stamp()})
    #         perid = res.text
    #         perid = json.loads(perid)
    #         perid = perid['fid'] # 期数ID
    #         logging.info('游戏期数获取成功：{}'.format(perid))
    #
    #         logging.info('=======================调用【获取玩法赔率】接口====================================')
    #         datas = {"periodId":perid,"ids":"457,462,461,464,463,466,469,468,465,470,460,876,877,632,633","handicap":1,"_":get_time_stamp()}
    #         res = requests.get(url=server_host + '/Shared/GetOdd', cookies=cookie_dict, data=datas)
    #         odd_data = res.json()
    #         odd_data = get_json_value(odd_data,'/odds')
    #         odd_data = json.loads(odd_data) # 转换有序列表类型
    #         odd_data = random.choice(odd_data) # 随机获取玩法赔率
    #         logging.info('游戏玩法赔率成功：{}'.format(odd_data))
    #
    #
    #         logging.info('=======================调用【六合彩下注接口】接口====================================')
    #         from Libs.Random_util import RandomUtil
    #         r = RandomUtil()
    #         amount = r.get_random_int(200,1000)
    #         list_data = [{"id":odd_data['cid'],"pid":odd_data['pid'],"amount":amount,"goal":odd_data['cid'],"odds":odd_data['odds']}]
    #         datas = {"force":False,"orderlist":'{}'.format(list_data),"handicap":1,"periodID":perid}
    #         res = requests.post(url=server_host + '/AddOrders/SixOrder', cookies=cookie_dict, data=datas)
    #         logging.info('游戏成功：{}'.format(res.text))
    #
    #         time.sleep(1)
    #     except Exception as error:
    #         logging.info(error)


def get_ylpt_login_id(NET_SessionId):
    import re
    p = re.compile('ASP.NET_SessionId=.*;', re.I)
    LoginSessionID = p.findall(NET_SessionId)[0].replace(';', '')
    LoginSessionID = LoginSessionID.split('=')
    LoginSessionID = LoginSessionID[1].split(' ')
    return LoginSessionID[0]


if __name__ == '__main__':
    set_log()
    lx_ylpt_login()

    # str = 'ASP.NET_SessionId=453kmaiyd0flctslrmyoan0d; DROCQ.ID=403859; DROCQ.USERID=huiy07; DROCQ.USERNAME=huiy07; DROCQ.GRADEID=975; DROCQ.GRADENAME=%e4%bc%9a%e5%91%98; DROCQ.COMPANYID=38171; DROCQ.ROLE=User; DROCQ.LOGINSTATUS=1; DROCQ.AUTHORITYID=403859; DROCQ.AUTHORITYGRADEID=975; DROCQ.PARENTID=403849; DROCQ.SUPACCOUNTS=38171%2c403845%2c403846%2c403847%2c403849; DROCQ.ISAPI=False; DROCQ.ISGUEST=False; DROCQ.FFORCESCHANGEPWD=False'
    # str2 = str.split(';')
    # datas1 = {}
    # for i in str2:
    #     list1 = i.split('=')
    #     datas1.update({list1[0]:list1[1]})
    # print(datas1)