# -*-coding:utf-8-*-
dic = {}
dict_key = '剩余投注时间'
# 添加数据 字典键值对
dic[dict_key] = 1
print(dic)
# 修改字典value
dic[dict_key] = 2
print(dic)
# updata更新键值对进字典
dic.update({'age':18})
dic['age'] = 18
dic['age'] = 'tets'
print(dic)
# print(dic)
# value = dic.values()
# key = dic.keys()
# print(value) # dict_values([2]) 此方法打印结果 重点
# print(key)
#
# temp = '剩余投注时间'
# if temp in dic.keys(): # dict_keys(['剩余投注时间']) 方法打印结果 重点
#     print('剩余头猪十几件在key里面')
# else:
#     print('不等于')
# temp1 = 2
# if dic['剩余投注时间'] == temp1:
#     print('dayu')
#
# print(dic)