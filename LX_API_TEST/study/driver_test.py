from selenium import webdriver
import sys
import os
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(path)
# def lx_ylpt_login():
#     # UI刷新页面获取sid值
#     pass
#
# if __name__ == '__main__':
#     cookie = 'ASP.NET_SessionId=453kmaiyd0flctslrmyoan0d; DROCQ.FFORCESCHANGEPWD=False; DROCQ.ISAPI=False; DROCQ.ISGUEST=False; GAMEID=30; multiSelect=true'
#     cookie = cookie.split('; ')
#     # print(cookie)
#     # print(type(cookie))
#     cookie_dict = {}
#     for i in cookie:
#         list1 = i.split('=')
#         cookie_dict.update({list1[0]: list1[1]})
#     cookie_dict.update()
#     print(cookie_dict)