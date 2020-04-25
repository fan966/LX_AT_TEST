from selenium import webdriver
from study_test_file.jc2 import Idenx
driver = webdriver.Chrome()
class Usercenter(Idenx):
    def __init__(self,driver):
        super(Usercenter,self).__init__(driver)
        self.name = "ttt1"
    def tets1(self):
        print('1')

if __name__ == "__main__":
    user = Usercenter(driver)
    user.tets1()
    user.test2()
    user.test3()


