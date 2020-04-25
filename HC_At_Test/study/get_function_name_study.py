# -*-coding:utf-8-*-
import sys
import unittest

def test12121():
    # 运用sys模块获取当前方法名称
    print("当前方法名：{}".format(sys._getframe().f_code.co_name))
test12121()



class Case(unittest.TestCase):
    # unittest 里面获取方法名
    def test1_function_name(self):
        print("当前方法名：{}".format(self._testMethodName))

    def test2_function_name(self):
        print("当前模块名：{}".format(self._testMethodName))

    # 运用sys模块获取方法名
    def test3_f_name(self):
        print('【info】页面不存在充值入口：请检查：【{}】'.format(sys._getframe().f_code.co_name))





if __name__ == "__main__":
    unittest.main()