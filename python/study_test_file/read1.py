__all__ = ["test2"] # 里面写入字符串tets2后，导入该模块则只能调用test2 --
def test1():
    print("---test1---")
    #print(__name__)

def test2():
    print('---test2---')

if __name__ == '__main__':
    test1()
