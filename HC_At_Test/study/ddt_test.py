# -*-coding:utf-8-*-
from PO.common.common_util import get_project_path
import unittest
yaml_file_path = get_project_path() + "\\Data\\touup_online.yaml"
print(yaml_file_path)
from ddt import ddt,file_data
@ddt
class dataTest(unittest.TestCase):

    @file_data(yaml_file_path)
    def test1_yaml1(self,data):
        d = data.split(',')
        print(d[0],d[1])
        #print(type(d[0]),type(d[1]))




if __name__ == "__main__":
    unittest.main()
    pass
