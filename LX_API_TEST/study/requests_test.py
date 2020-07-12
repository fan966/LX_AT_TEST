#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import requests
import json
from Libs.common import *
test = 'aaaa2222'
md5 = hashlib.md5() # 实例化MD5加密对象
md5.update(test.encode('utf-8')) # 字符串必须转码
res1 = md5.hexdigest() # 获取加密数据
test2 = res1+'9999'
md5.update(test2.encode('utf-8'))
temp = md5.hexdigest()
# print(temp)
#
#
# url = 'http://csdqthcapi.lx901.com/api/ValidateCode'
# tok_url = 'http://csdqthcapi.lx901.com/api/GetValidateTokenKey'
#
#
#datas = {"UserName":"ttt1","ValidateCode":"","ClientFlag":"Android","OnlyFlag":"99be1d7f5f0d930a8a65ec1124179012","Password":"aaaa2222"}
# datas = {'param': '{"UserName":"ttt1","ValidateCode":"","ClientFlag":"Android","OnlyFlag":"99be1d7f5f0d930a8a65ec1124179012","Password":"8196658ecaeceb870d0ad3053dd579d2"}'}
# print(datas)
#res = requests.post(url=url,data=datas,headers=headers).json()
#print(res)
# res = requests.get(url=url)
# print(res.json())
# print(res.headers)
# print(res.cookies)
# print(res.status_code)
# print(type(res.status_code))

# tok = res['Data']['Value']
# print(tok)
# header = {"ValidateToken":tok}
# res = requests.post(url=url,data=datas,headers=header)
# print(res.text)
# print(type(res.json()))
# LoginSessionID = res.json()["Data"]["LoginSessionID"]
# print(LoginSessionID)
# add_url = 'http://csdqthcapi.lx901.com/api/AddAccount'
# header = {"LoginSessionID":LoginSessionID}
# datas = {'param':'{"FIsMsgHigherups":false,"IsAgent":true,"PassWrod":"aaaa1111","NickName":"vcx","UserKickbacks":[],"AccountName":"e12wdaww"}'}
# lll = {"param":"{\"FIsMsgHigherups\":false,\"IsAgent\":true,\"PassWrod\":\"aaaa1111\",\"NickName\":\"dhy8\",\"UserKickbacks\":[],\"AccountName\":\"dhy8495\"}"}
# # res = requests.post(url=add_url,data=datas,headers = header).json()
# # print(res)
# print(lll)
datas = {'param': '{"UserName":"ttt1","ValidateCode":"","ClientFlag":"Android","OnlyFlag":"99be1d7f5f0d930a8a65ec1124179012","Password":"8196658ecaeceb870d0ad3053dd579d2"}'}
tk_url = 'http://csdqthcapi.lx901.com/api/GetValidateTokenKey'
url = 'http://csdqthcapi.lx901.com/api/Login'
res = requests.get(url=tk_url)
print(res.json())
token = res.json()['Data']['Value']
headers = {'ValidateToken':token}
res = requests.post(url=url,data=datas,headers=headers).json()
print(res)
