#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import datetime
import logging

def get_time_stamp(level=1):
    '''
    获取当前时间秒级别时间戳
    :return:
    '''

    t = time.time()
    if level == 1:
        t = int(t)
    elif level == 2:
        t = int(round(t * 1000))
    else:
        logging.error('时间级别传参有误，请检查！')
    return t


def count_datatime(start_time,end_time,type='day'):
    '''
    计算两个日期差/限定格式/2020/06/28 13:49:59
    end_time:结束时间
    start_time:起始时间
    type：day;计算天数差 min；计算分差 secods；计算秒差
    :return:
    '''
    start = datetime.datetime.strptime(start_time,"%Y/%m/%d %H:%M:%S")
    end = datetime.datetime.strptime(end_time,"%Y/%m/%d %H:%M:%S")
    if type == 'day':
        num = (end-start).days
    elif type == 'min':
        num = (end-start).microseconds
    elif type == 'secods':
        num = (end-start).seconds
    else:
        logging.error('计算格式有误，请检查传参！')
    return num

def get_now_time(type='/'):
    '''
    获取当前时间/已指定格式返回
    :return:
    '''
    now_tim = datetime.datetime.now()
    if type == '/':
        time = now_tim.strftime("%Y/%m/%d %H:%M:%S")
    elif type == '-':
        time = now_tim.strftime("%Y-%m-%d %H:%M:%S")
    else:
        logging.error('时间格式错误，请检查传参！')
    return  time

def get_nowday_and_yestday():
    '''
    获取当前日期和前一天日期
    :return:
    '''
    now = datetime.datetime.now()
    yes = now + datetime.timedelta(days=-1)
    now = now.strftime("%Y-%m-%d %H:%M:%S")
    yes = yes.strftime("%Y-%m-%d %H:%M:%S")
    return now,yes

if __name__ == '__main__':
    # print(count_datatime('2020/06/28 13:49:59','2020/06/28 13:54:53','day'))
    # now = datetime.datetime.now()
    # now = now.strftime("%Y/%m/%d %H:%M:%S")
    # print(now)
    #print(get_now_time(''))
    #print(get_nowday_and_yestday())
    # l = {"PeriodId":"179621970","OrderList":"[{\"a\":2.0,\"c\":\"01\",\"i\":21053,\"k\":\"0\",\"m\":1,\"n\":1,\"t\":1,\"ts\":1593360463}]","GameId":"320"}
    # print(l)
    # s_time = '2020/07/02 01:44:20'
    # en_time = '2020/07/02 01:44:53'
    # print(count_datatime(s_time,en_time,type='secods'))
    print(get_time_stamp(level=1))
