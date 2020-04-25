# coding = utf-8
import unittest
class Firstcase02(unittest.TestCase):
    #装饰器
    @classmethod # 类方法
    def setUpClass(cls):
        print('所有case执行前的前置条件')
    # 装饰器
    @classmethod
    def tearDownClass(cls):
        print('所有case执行后的后置条件')
    # unittest前置条件
    def setUp(self):
        print('执行case的前置条件')

     # unittest后置条件
    def tearDown(self):
        print('执行case的后置条件')

    def test_first_case1(self): # case方法名必须以tets开头才能执行
        print('第一条case执行成功00002')

    @unittest.skip('不执行此条case')
    # 此条用例不执行
    def test_first_case3(self):# case方法名必须以tets开头才能执行
        print('第三条case执行成功000002')

    def test_first_case2(self):# case方法名必须以tets开头才能执行
        print('第二条case执行成功00002')


if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite() # unittest执行套件
    # suite.addTest(Firstcase02('test_first_case3')) # 添加case 类名（case方法名）
    # #suite.addTest(Firstcase('test_first_case1'))
    # suite.addTest(Firstcase02('test_first_case2'))
    # unittest.TextTestRunner().run(suite)
