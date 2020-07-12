#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import datetime
# 获取当前时间戳-数字格式 time.time()
temp = time.time()
print(temp) # 1591600390.050816
print(int(temp))

# 获取当前时间-元组格式 time.localtime()
now_time = time.localtime()
print(now_time) # time.struct_time(tm_year=2020, tm_mon=6, tm_mday=8, tm_hour=15, tm_min=14, tm_sec=41, tm_wday=0, tm_yday=160, tm_isdst=0)

# 格式化当前时间格式- 按照字符串格式输出当前时间格式
time_value = time.strftime("%Y-%m-%d %H:%M:%S----%A---%w---%j")
print(time_value)

# 获取当前时间和前一天时间
now = datetime.datetime.now()
yes = now + datetime.timedelta(days=-1)
print('test')
print(now)
print(yes)
now = now.strftime("%Y-%m-%d %H:%M:%S")
yes = yes.strftime("%Y-%m-%d %H:%M:%S")
print(now,'nowtype',type(now))
print(yes,'nowtype',type(yes))
t = (now,yes)
print(t)
