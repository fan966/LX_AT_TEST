# !/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests
url = 'http://6rtj0qib.qaz2032.com/Login'
datas = {"username":"huiy07","password":"f09caad93c556216048595de602044b0","validateCode":"9999","sid":"doqtx0uj11ih2cqn4ulbhq2u"}
header = {"Content-Type":"application/x-www-form-urlencoded",
          "Referer":"http://6rtj0qib.qaz2032.com/Login",
          "Connection":"keep-alive",
          "Host":"6rtj0qib.qaz2032.com",
          "Cache-Control":"no-cache",
          "Pragma":"no-cache",
          "Origin":"http://6rtj0qib.qaz2032.com",
          "Upgrade-Insecure-Requests":"1",
          "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
          "Accept-Encoding":"gzip, deflate",
          "Accept-Language":"zh-TW,zh;q=0.9",
          "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}
cookie = {"ASP.NET_SessionId":"doqtx0uj11ih2cqn4ulbhq2u","DROCQ.ISAPI":"False","DROCQ.ISGUEST":"False","GAMEID":"30","multiSelect":"true","DROCQ.FFORCESCHANGEPWD":"False"}

res = requests.post(url=url,data=datas,headers=header,cookies=cookie,allow_redirects=True)
heard = res.headers
print(heard)
print(res)
