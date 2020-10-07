# !/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests
url = 'http://6rtj0qib.qaz2032.com/Login'


# res = requests.get(url=url)
# print(res)
# print(res.headers)

datas = {"username":"huiy07","password":"f09caad93c556216048595de602044b0","validateCode":"9999","sid":"453kmaiyd0flctslrmyoan0d"}
header = {"ASP.NET_SessionId":"453kmaiyd0flctslrmyoan0d"}
cookie = {"ASP.NET_SessionId":"453kmaiyd0flctslrmyoan0d"}

res = requests.post(url=url,data=datas,cookies=cookie)
heard = res.headers
print(heard)
print(res)
