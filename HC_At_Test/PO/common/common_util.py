# -*-coding:utf-8-*-
import os
import random
import re
import time
def get_project_path():
    """
    获取项目根目录
    :return: 项目根目录
    """
    path = os.path.dirname(__file__).replace("\PO\common",'')

    return path

def get_random_int(miu_num,max_num):
    '''
    两个数值内随机取一个整数型
    :param miu_num:
    :param max_num:
    :return:
    '''
    num = random.randint(miu_num,max_num)
    return num

def get_random_str():
    '''
    获取随机字符串
    :return:
    '''
    text = 1


def re_sub(pattern, rep, string, count=0, flags=0):
    """
    使用正则表达式替换匹配的内容
    :param pattern: 正则中的模式字符串
    :param rep: 替换的字符串，也可为一个函数
    :param string: 要被查找替换的原始字符串
    :param count: 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配
    :param flags: 开始位置， 默认 0 从第1个字符开始
    :return: 替换后的字符串
    """
    return re.sub(pattern, rep, string, count, flags)


def re_findall(pattern, string, flags=0):
    """
    使用正则表达式查找字符串,忽略大小写
    :param pattern: 正则中的模式字符串
    :param string: 要被查找的原始字符串
    :param flags: 开始位置， 默认 0 从第1个字符开始
    :return: 匹配的内容集合
    """
    _pattern = re.compile(pattern, re.I)
    return _pattern.findall(string, flags)

def get_time_str():
    '''
    获取当前时间以字符串格式输出
    :return:
    '''
    time_str = time.strftime('%m%d%H%M%S')
    return time_str

def util_str_convert_tupledata(str1,str_split='/',data_split = ','):
    '''
    通用字符串转换数据组 例如：V1,10,1/V2,100,10  转换后为 {'1': ['V1', '10', '1'], '2': ['V2', '100', '10']} 再排序得到元组数据列表 [('1', ['V1', '10', '1']), ('2', ['V2', '100', '10'])]
    :param str1:需转换的字符串
    :param str_split:字符串中的分隔符，用来切割为多条数据
    :param data_split:转换字符串切割符，用来切割多条数据
    :return:返回的元组列表中key值为从1开始依次递增的数值字符串
    '''
    dic = {}
    num = 1
    for i in str1.split(str_split): # 字符串以’/‘切割为多条数据
        dic1 = {'{}'.format(num):i.split(data_split)} # 循环单条数据以’,‘切割为多条数据为字典键值对
        dic.update(dic1) # 字典更新键值对数据 num作为建，切割的列表数据作为值
        num += 1
    return sorted(dic.items(),key=lambda x:x[0],reverse=False) # 字典items()以列表返回可遍历的(键, 值) 元组数组,降序排序



if __name__ == '__main__':
    # text = get_time_str()
    # print(text)
    text1 = '3|100,1000,2,5'

    test2 = text1.split('|')
    print(test2[1])
    t = util_str_convert_tupledata(test2[1])
    print(t)
    for num,value in t:
        print(num)
        print(value)