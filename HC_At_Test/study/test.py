# -*-coding:utf-8-*-
from Libs.cnfg_util import config_ini
from Libs.excel_util import ExcelUtil
from PO.common.common_util import *
data_path = get_project_path() + '\\Data\\game\\hc_game.xls'
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


bet_list = []
bet = config_ini('game.ini','game','bet_longhu')
print(bet)
print(type(bet))
str1 = '第一球VS第三球'
if str1 in bet:
    print('在里面')
datas = ExcelUtil(data_path, 1).read_excel_addlist()
print(datas)
print(datas[0]['play2'])
if datas[0]['play2'] == '':
    print('空字符串')
elif datas[0]['play2'] == None:
    print('=None')