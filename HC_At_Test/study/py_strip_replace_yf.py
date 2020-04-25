# -*-coding:utf-8-*-
# 1. strip(str)
#
# 基本用法：ss.strip(rmStr)
#
# ss.strip()参数为空时，默认去除ss字符串中头尾\r, \t, \n, 空格等字符
#
# ss.lstrip()删除ss字符串开头处的指定字符，ss.rstrip()删除ss结尾处的指定字符
#
# 2. replace(old, new[, max])
#
# 基本用法：ss.replace(rgExp, replaceText, max)

str1 = '00'
s = str1.strip('0')
print(s)
