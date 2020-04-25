# coding = utf-8
import unittest
class Firstcase(unittest.TestCase):
    # #装饰器
    # @classmethod # 类方法
    # def setUpClass(cls):
    #     print('所有case执行前的前置条件')
    # # 装饰器
    # @classmethod
    # def tearDownClass(cls):
    #     print('所有case执行后的后置条件')
    # unittest前置条件
    def setUp(self):
        print('执行case的前置条件')

     # unittest后置条件
    def tearDown(self):
        print('执行case的后置条件')
    @unittest.skipIf()
    def test_first_case(self): # case方法名必须以tets开头才能执行
        print('第一条case执行成功')
    def test_secend_case(self):# case方法名必须以tets开头才能执行
        print('第二条case执行成功')


if __name__ == '__main__':
    suite = unittest.TestSuite() # unittest执行套件
    suite.addTest(Firstcase('test_first_case')) # 添加case 类名（case方法名）
    unittest.TextTestRunner().run(suite)
