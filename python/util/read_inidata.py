#coding = utf-8
import configparser
class Read_inidata(object):
    def __init__(self,path):
        self.data = self.laod_ini(path)
    def laod_ini(self,path):
        cf = configparser.ConfigParser()
        cf.read(path) # ..是从上级目录开始查找文件 如果是同级目录可直接查找文件
        return cf
    def get_ini_value(self,sections,key):
        return self.data.get(sections,key)
if __name__ == "__main__":
    # rd = Read_ini('../config/localElement.ini')
    # data = rd.get_ini_value("element","login")
    # data_list = data.split(":")
    # print(data_list)
    rd = Read_inidata("../config/localElement.ini") # 同级目录下路径直接输入不用加/
    data = rd.get_ini_value("element","selec")
    print(data)


