#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import random
def md5_encryption(text):
    '''
    加密处理字符串
    :param text:加密字符串
    :return:
    '''
    md5 = hashlib.md5()  # 实例化MD5加密对象
    md5.update(text.encode('utf-8'))  # 字符串必须转码
    data = md5.hexdigest()  # 获取加密数据
    return data


def pwd_md5_encryption(text,key):
    '''
    密码加密处理
    :param text: 加密字符串
    :param key:验证码
    :return:
    '''
    return md5_encryption(md5_encryption(text)+key)

def json_convert_to_key_value(json_object, split_str='&'):
    """
    json对象转换为字符串键值对
    :param json_object: json 对象
    :param split_str: 字符串切片字符
    """
    key_value_str = ''
    for key, value in json_object.items():
        key_value_str += key + '=' + str(value) + split_str

    return key_value_str.rstrip(split_str)

def get_new_sort_data(item,temp):
    '''
    获取可迭代对象值进行排列
    :return:
    '''
    new_data = []
    data = []
    for i in temp:

        if i and i != ',':
            new_data.append(i)
    while True:
        data.append(random.choice(new_data))
        if len(data) == item:
            break
    return data


if __name__ == '__main__':
    #print(pwd_md5_encryption('aaaa2222','9999'))
    y = ['大', '小', '单', '双']
    t = (1,2,3,4,5)
    d = {"age":18,"name":'laowang',"height":175}
    print(get_new_sort_data(2,d))


