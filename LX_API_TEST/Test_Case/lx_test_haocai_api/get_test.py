#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json,jsonpatch,jsonpointer
from Config.Config import *
from Libs.excel_util import ExcelUtil
import hashlib
import logging
import json
from Libs.common import *
# from Verify.User.test_web_login import login
# LoginSessionID = login('ttt1','aaaa2222')
# url = 'http://gshcweb.add177.com/Shared/GetPlayMoneyLimit'
# data = {"GameId":63}
# headers = {"LoginSessionID":LoginSessionID}
# res = requests.get(url=url,params=data,headers=headers,verify=False)
# print(res.json())
