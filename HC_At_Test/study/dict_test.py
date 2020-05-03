# -*-coding:utf-8-*-
dic = {}
dict_key = '剩余投注时间'
# 添加数据 字典键值对
dic[dict_key] = 1
# 修改字典value
dic[dict_key] = 2


print(dic)
value = dic.values()
key = dic.keys()
print(value)
print(key)

temp = '剩余投注时间'
if temp in dic.keys():
    print('剩余头猪十几件在key里面')
else:
    print('不等于')
temp1 = 2
if dic['剩余投注时间'] == temp1:
    print('dayu')