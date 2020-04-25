# coding = utf-8
import ddt
import unittest
@ddt.ddt # 装饰器ddt类
class Datatest(unittest.TestCase):
    def setUp(self) :
        print('case前置条件')
    def tearDown(self) :
        print('case后置条件')

    # 组织data格式数据
    @ddt.data(
        [1,2],
        [3,4],
        [5,6]
    )

    @ddt.unpack # 解包数据用来运行下面案例
    def test_case_01(self,a,b):
        print(a+b)

if __name__ == '__main__':
    unittest.main()
