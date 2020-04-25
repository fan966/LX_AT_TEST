# coding = utf-8
from uu.read_ini import readini

class Read_elment(object):
    def get_ini_element(self):
        data = readini.get_ini_value()
        data_list = data.split(' ')
        # print(data_list) test
read_element = Read_elment()