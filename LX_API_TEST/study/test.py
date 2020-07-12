#!/usr/bin/env python
# -*- coding: utf-8 -*-
from study.path_study import *
import os
import hashlib
import pandas
import json
import jsonpointer
current_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(current_path,'Data\\Test_Case.xlsx')
print(file_path)

data = pandas.read_excel(file_path,['User'])
print(type(data))

dic = {'filter_field': {'IsRegression': 'YES', 'IsSmoke': 'YES', 'ApplyEnv': '全部', 'ScriptName': 'Api_User_IT_AddAccount_001.py'}}
result_data = []
for i in data:
    query_str = ''
    datas = data[i]
    print(type(datas))
    #print(datas)
    print('test')
    #print(datas)
    if dic:
        for key,value in dic.items():# items() 方法把字典的键值对转换为元组排列展示
            print(dic.items())
            print(key,'    ',value)
            print(type(key)) # 字符串
            print(type(value))  # 字典
            print('111')
            print(type(dic[key]))
            print(dic[key])
            for key_,value_ in dic[key].items():# items() 方法把字典的键值对转换为元组排列展示
                print(key_,'   ',value_)
                query_str += str(key_) + ' == "' + str(value_) + '" & '
                print(query_str)
            query_str = query_str.rstrip(' &') # 去掉字符串首尾指定字符，默认空格
            print(query_str)
            print(datas.query(query_str).empty)
            if not datas.query(query_str).empty:
                data1 = datas.query(query_str)
                print('222')
                print(data1)
                result_data += json.loads(data1.to_json(orient='records')) #
                print(result_data)
                print(result_data[0])
                print(type(result_data[0]))
                print(result_data[0]['NewVerifParmsData']) # 从文件里匹配取出的数据都是字符串格式的
                print(type(result_data[0]['NewVerifParmsData']))
                temp = json.loads(result_data[0]['NewVerifParmsData']) # 转换为json字典格式，因为传参时需要格式为json字典格式
                print(type(temp))
    #print(result_data)



