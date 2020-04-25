import time
from selenium import webdriver
try:
    driver = webdriver.Chrome()
    driver.get('https://www.imooc.com/article/be')
    driver.maximize_window()
    time.sleep(2)
    js = "document.documentElement.scrollTop=10000" # 执行这句话将页面滚动条滑动到底部
    while True:
        element_lisi = driver.find_elements_by_class_name('article-lwrap')
        print('1')
        for element in element_lisi:
            print('2')
            element_name = element.text
            print('3')
            print(element_name)
            print('4')
            if element_name == '刷掉 90% 候选人的互联网大厂海量数据面试题（附题解+方法总结）':
                print('5')
                element.click()
                break
        driver.execute_script(js) # 执行滚动条滑动到底部
except Exception as er:
    print(er)
finally:
    driver.quit()