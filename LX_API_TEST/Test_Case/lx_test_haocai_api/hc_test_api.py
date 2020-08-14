#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests
from Libs.common import *
import logging
from Libs.http_requests import *
from Config.Config import *
import logging
from Libs.Db_Sql_Util import *
# import re
# url = 'http://gshcweb.add177.com/Home/login'
# datas = {
#     "username":"ttt1",
#     "password":md5_encryption(md5_encryption('aaaa2222')),
#     "validateCode":""
# }
#
# res = requests.post(url=url,data=datas,verify=False)
# res = res.headers
# print(res['Set-Cookie'])
# str1 = res['Set-Cookie']
# p =re.compile('LoginSessionID=.*;',re.I)
# print(p.findall(str1)[0].replace(';',''))
#print([p.findall(str1)][0].replace(';',''))


# def login_api(account,password):
#     """
#     用户登录公告接口
#     :param account: 账户 ttt1
#     :param password: 密码 aaaa2222
#     """
#     logging.info('======================调用：用户登录接口=======================')
#     res_msg = http_api_requests('登录注册.用户登录',NewVerifParmsData={"UserName":account,"Password":md5_encryption(md5_encryption('aaaa2222'))})
#     res_msg_stasus = get_json_value(res_msg,'/Status')
#
#     if not  res_msg_stasus:
#         logging.error('登录失败 ： {}'.format(res_msg))
#     else:
#         LoginSessionID = get_json_value(res_msg,'/Data/LoginSessionID')
#         return LoginSessionID
#rl"2","mp":1594387700},{"amount":1,"goal":"1361","id":1361,"name":"19","odds":43.61,"odds1":-1.0,"parentName":"特码","sId":457,"timestamp":1594387700},{"amount":1,"goal":"1362","id":1362,"name":"20","odds":43.61,"odds1":-1.0,"parentName":"特码","sId":457,"timestamp":1594387700},{"amount":1,"goal":"1363","id":1363,"name":"21","odds":43.61,"odds1":-1.0,"parentName":"特码","sId":457,"timestamp":1594387700},{"amount":1,"goal":"1364","id":1364,"name":"22","odds":43.61,"odds1":-1.0,"parentName":"特码","sId":457,"timestamp":1594387700},{"amount":1,"goal":"1365","id":1365,"name":"23","odds":43.61,"odds1":-1.0,"parentName":"特码","sId":457,"timestamp":1594387700},{"amount":1,"goal":"1366","id":1366,"name":"24","odds":43.61,"odds1":-1.0,"parentName":"特码","sId":457,"timestamp":1594387700},{"amount":1,"goal":"1367","id":1367,"name":"25","odds":43.61,"odds1":-1.0,"parentName":"特码","sId":457,"timestamp":1594387700},{"amount":1,"goal":"1368","id":1368,"name":"26","odds":43.61,"odds1":-1.0,"parentName":"特码","sId":457,"timestamp":1594387700},{"amount":1,"goal":"1369","id":1369,"name":"27","odds":43.61,"odds1":-1.0,"parentName":"特码","sId":457,"timestamp":1594387700},{"amount":1,"goal":"1370","id":1370,"name":"28","odds":43.61,"odds1":-1.0,"parentName":"特码","sId":457,"timestamp":1594387700},{"amount":1,"goal":"1371","id":1371,"name":"29","odds":43.61,"odds1":-1.0,"parentName":"特码","sId":457,"timestamp":1594387700},{"amount":1,"goal":"1372","id":1372,"name":"30","odds":43.61,"odds1":-1.0,"parentName":"特码","sId":457,"timestamp":1594387700},{"amount":1,"goal":"1373","id":1373,"name":"31","odds":43.61,"odds1":-1.0,"parentName":"特码","sId":457,"timestamp":1594387700},{"amount":1,"goal":"1374","id":1374,"name":"32","odds":43.61,"odds1":-1.0,"parentName":"特码","sId":457,"timestamp":1594387700},{"amount":1,"goal":"1375","id":1375,"name":"33","odds":43.61,"odds1":-1.0,"parentName":"特码","sId":457,"timestamp":1594387700},{"amount":1,"goal":"1376","id":1376,"name":"34","odds":43.61,"odds1":-1.0,"parentName":"特码","sId":457,"timestamp":1594387700},{"amount":1,"goal":"1377","id":1377,"name":"35","odds":43.61,"odds1":-1.0,"parentName":"特码","sId":457,"timestamp":1594387700},{"amount":1,"goal":"1378","id":1378,"name":"36","odds":43.61,"odds1":-1.0,"parentName":"特码","sId":457,"timestamp":1594387700},{"amount":1,"goal":"1379","id":1379,"name":"37","odds":43.61,"odds1":-1.0,"parentName":"特码","sId":457,"timestamp":1594387700},{"amount":1,"goal":"1380","id":1380,"name":"38","odds":43.61,"odds1":-1.0,"parentName":"特码","sId":457,"timestamp":1594387700},{"amount":1,"goal":"1381","id":1381,"name":"39","odds":43.61,"odds1":-1.0,"parentName":"特码","sId":457,"timestamp":1594387700},{"amount":1,"goal":"1382","id":1382,"name":"40","odds":43.61,"odds1":-1.0,"parentName":"特码","sId":457,"timestamp":1594387700},{"amount":1,"goal":"1383","id":1383,"name":"41","odds":43.61,"odds1":-1.0,"parentName":"特码","sId":457,"timestamp":1594387700},{"amount":1,"goal":"1384","id":1384,"name":"42","odds":43.61,"odds1":-1.0,"parentName":"特码","sId":457,"timestamp":1594387700},{"amount":1,"goal":"1385","id":1385,"name":"43","odds":43.61,"odds1":-1.0,"parentName":"特码","sId":457,"timestamp":1594387700},{"amount":1,"goal":"1386","id":1386,"name":"44","odds":43.61,"odds1":-1.0,"parentName":"特码","sId":457,"timestamp":1594387700},{"amount":1,"goal":"1387","id":1387,"name":"45","odds":43.61,"odds1":-1.0,"parentName":"特码","sId":457,"timestamp":1594387700},{"amount":1,"goal":"1388","id":1388,"name":"46","odds":43.61,"odds1":-1.0,"parentName":"特码","sId":457,"timestamp":1594387700},{"amount":1,"goal":"1389","id":1389,"name":"47","odds":43.61,"odds1":-1.0,"parentName":"特码","sId":457,"timestamp":1594387700},{"amount":1,"goal":"1390","id":1390,"name":"48","odds":43.61,"odds1":-1.0,"parentName":"特码","sId":457,"timestamp":1594387700},{"amount":1,"goal":"1391","id":1391,"name":"49","odds":43.61,"odds1":-1.0,"parentName":"特码","sId":457,"timestamp":1594387700}],"periodID":"43686131","selectBack":0.0}