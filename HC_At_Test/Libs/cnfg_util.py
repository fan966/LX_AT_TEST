# -*-coding:utf-8-*-
import configparser
from PO.common.common_util import get_project_path
# ini配置文件目录路径 + 传入ini文件名即可
ini_path = get_project_path() + '\\Config\\'

def config_ini(ini_name,sections,key):
    # 实例化第项
    cf =configparser.ConfigParser()
    # 读取文件内容
    cf.read(ini_path + ini_name,encoding='utf8')
    # 返回获取值
    return cf.get(sections,key)

if __name__ == "__main__":
    value = config_ini('config.ini','default','browesr_name')
    print(value)
    value1 = config_ini('financial.ini','web','pmtp')
    print(value1)
