#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
json_1 = {
    "Status": True,
    "Info": "test",
    "Data": {
        "VRUrl": "http://fe.vrbetdemo.com/Account/LoginValidate?version=1.0&id=HC1&data=8o%2bosq%2fXeXWywk89TAQcftW8BduHh4Dof%2bI%3d"
    },
    "Code": 0
}

json_2 = {
    "Status": False,
    "Info": "",
    "Data": {
        "VRUrl": "http://fe.vrbetdemo.com/Account/LoginValidate?version=1.0&id=HC1&data=8o%2bosq%2fXeXWywk89TAQcftW8BduHh4Dof%2bI%3d"
    },
    "Code": 0
}

print(isinstance(True,type(False)))
print(isinstance(True,dict))
print(isinstance(True,list))
print('test')


class qaErroe(Exception):
    pass
y = 1
try:
    if y:
        raise qaErroe('3123')
except qaErroe:
    raise
finally:
    print('0')
    print('0')
    print('0')
    print('11111')
print('0000000000000000000000000000')
print(json_1['Info'])
print(type(json_2['Info']))
print('1')
#print(isinstance(json_1['Info'],))


# def get_value(diff):
#     if diff:
#         return False,(json.dumps(diff,ensure_ascii=False,indent=4))
#
#
#
# if __name__ == '__main__':
#     diff = ['字段Code值不一致：预期结果值：0，实际结果值：1']
#     gg = get_value(diff)
#     print(type(gg))
#     print(gg)




