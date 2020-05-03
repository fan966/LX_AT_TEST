# -*-coding:utf-8-*-
import os
import random
import re
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
    pass


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
