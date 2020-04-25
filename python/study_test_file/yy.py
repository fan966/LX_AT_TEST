# conding = tuf-8
import time
# from study_test_file.test import get_project_path
# # class Findelememt(object):
# #     def __init__(self,driver):
# #         self.driver = driver
# #     def get_element(self):
# #         self.driver.find
# file_path = get_project_path()
#
# file_name = file_path+'\\config\\localElement.ini'
# print(file_name)
# from study_test_file.test import *
# from util.read_exce_data import Excel_data
# file_name = get_project_path()+'\\libs\\登录信息.xlsx'
# ec = Excel_data(file_name)
# data = ec.read_excel_data_list()
# #print(len(data))
#
# for i in range(len(data)):
#     if data[i]['skin'] == "豪彩":
#         if data[i]['uid'] == "ttt1":
#             print("1")
#
#         else:
#             print("2")
url = 'http://csdqthcweb.lx901.com'

if "/login" not in url.lower(): # url.lower() 把字符串里面大写字母变为小写
    # rstrip('/')去掉字符串尾部的/ （不带参数默认为空格）
    # strip()  去掉首尾的空格 不带参数默认为空格
    url = url.rstrip('/').strip() + '/login'
    print(url)


