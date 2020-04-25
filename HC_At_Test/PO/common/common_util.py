# -*-coding:utf-8-*-
import os
import random
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



