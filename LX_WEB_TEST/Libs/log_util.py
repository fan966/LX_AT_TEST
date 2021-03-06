# -*-coding:utf-8-*-
import logging
import time
from Config.Config import *

def set_log():
    """
    日志输出规范
    :return:
    """

    # 相对路径
    log_file_path = Config().log_path
    # 获取当前时间
    times = time.strftime("\%Y-%m-%d" + ".log")  # 以年月日的格式+文件后缀
    file_name = log_file_path + times

    # 获取logger对象，设置日志级别
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 判断文件夹是否存在，不存在则创建
    #mkdir(r'OutPut\Log\%s'%ym)

    # 创建FileHandler对象用于写入文件
    handler1 = logging.FileHandler(file_name, encoding='utf-8')
    # 设置文件日志级别
    handler1.setLevel(logging.INFO)
    # 设置文件日志格式
    fmt1 = logging.Formatter(fmt='%(levelname)-8s %(asctime)s %(filename)-20s line:[%(lineno)d:] %(message)s',
                             datefmt='%Y-%m-%d %H:%M:%S')
    handler1.setFormatter(fmt1)

    # 创建StreamHandler对象用于输出到控制台
    handler2 = logging.StreamHandler()
    # 设置控制台日志级别
    handler2.setLevel(logging.INFO)
    # 设置控制台日志格式
    fmt2 = logging.Formatter(fmt='%(filename)-20s line:[%(lineno)d:] %(message)s')
    handler2.setFormatter(fmt2)

    # 将handler1、handler2添加到logger
    logger.addHandler(handler1)
    logger.addHandler(handler2)

if __name__ == '__main__':
    set_log()
    logging.info('test')