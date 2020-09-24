# !/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
url = 'http://csdqthcweb.lx901.com/'
data = {"param":'{"includeG1Sport":true}'}
res = requests.get(url=url,params=data,verify=False)
print(res.json())