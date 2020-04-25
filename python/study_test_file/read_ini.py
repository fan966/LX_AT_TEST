import configparser
class Read_ini(object):
    def __init__(self):
        self.data = self.laod_ini()
    def laod_ini(self):
        cf = configparser.ConfigParser()

        cf.read('../config/localElement.ini') # ..是从上级目录开始查找文件 如果是同级目录可直接查找文件
        return cf
    def get_ini_value(self,sections,key):
        return self.data.get(sections,key)



# if __name__ == '__main__':
#     readini =Read_ini()
#     t = readini.get_ini_value('element','selec')
#     t_list = t.split('-') # 以>切割字符串
#     print(t_list)
readini = Read_ini()