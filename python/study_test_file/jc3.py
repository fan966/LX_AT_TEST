
class Webdriver(object):
    def __init__(self,driver):
        self.driver = driver
        self.age = 18
    def get_url(self,url):
        self.driver.get(url)
    def test3(self):
        print('Webdriver')