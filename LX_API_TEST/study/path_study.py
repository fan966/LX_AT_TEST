#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
def get_current_path():
    current_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(os.path.join(current_path,'Docs'),'report.html')
    return data_path



if __name__ == '__main__':
    # path = get_current_path()
    # print(path)
    # print(os.path.basename(__file__))
    # d = []
    # t = {1}
    # y = {5}
    # c = d+y+t
    # print(c)
    i = [{'age':18,'hieght':'test','kim':'qwe'},{'age':18,'hieght':'ffas'}]
    for j in i:
        for key in j:
            if key in ['hieght','kim']:
                j.update({key:'000000000000000000000'})
        k = i

    print(i)
    print('1')
    print(k)
    [{"FGameTypeId": 1, "FKickback": 0.09}, {"FGameTypeId": 2, "FKickback": 0.09},
     {"FGameTypeId": 3, "FKickback": 0.09}, {"FGameTypeId": 5, "FKickback": 0.09},
     {"FGameTypeId": 7, "FKickback": 0.09}, {"FGameTypeId": 8, "FKickback": 0.09},
     {"FGameTypeId": 9, "FKickback": 0.09}, {"FGameTypeId": 10, "FKickback": 0.09},
     {"FGameTypeId": 11, "FKickback": 0.09}, {"FGameTypeId": 13, "FKickback": 0.09},
     {"FGameTypeId": 15, "FKickback": 0.09}, {"FGameTypeId": 21, "FKickback": 0.09}]