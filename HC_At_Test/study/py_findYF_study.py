# -*-conding:utf-8-*-
import sys
#python find()方法语法：学习
# 检查字符串是否包含该字符串
# str -- 指定检索的字符串
# beg -- 开始索引，默认为0。
# end -- 结束索引，默认为字符串的长度。 检测到自己想要的字符则返回索引，没检测到则返回-1
from Libs.cnfg_util import config_ini
pmtpa = config_ini('financial.ini','web','pmtp')
str = '微信转账，支付宝转账'
# print(str.find(','))
print(pmtpa)
print(pmtpa.find('0',0,50)) # 参数直接输入数字就好，输入关键字则回报错
# -1  因为该字符串里面没有0这个字符，返回-1
print(pmtpa.find('通')) # 一般都是默认参数
# 38 返回索引值

# 一般用法  ： 用来确认字符串里面是否包含自己想要的字符串
if pmtpa.find(',') != -1:
    print('判断为真，字符串里面包含检查字符')

# list = [1,"qwasd",'微信']
# print(list.find('微信')) # 列表没有这个方法属性
print(str.find('8'))
