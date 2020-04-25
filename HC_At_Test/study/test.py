# -*-coding:utf-8-*-
from Libs.cnfg_util import config_ini
online_top = config_ini('financial.ini','web','pmtp') # 配置文件支付方式
data = online_top.split(',')
print(type(online_top))
print(data)
temp = '百度'
for i in range(len(data)):
    if temp == data[i]:
        print(data[i])
    # 调用方法传入data[i]

if temp in data:
    print('1')
onlne_top = ['支付宝', '在线支付', 'QQ钱包', '财付通', '京东', '百度']
if temp in onlne_top:
    print(temp +'zailimian ')