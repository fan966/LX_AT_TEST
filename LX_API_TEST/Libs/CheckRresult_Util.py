#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import logging
from Libs.Errors import *

class Diff(object):
    def __init__(self, first, second, with_values=False, ignore_value_of_keys=[]):

        self.difference = []
        self.with_values = with_values
        self.ignore_value_of_keys = ignore_value_of_keys

        self.check(first, second, with_values=self.with_values)

    def check(self, first, second, path='', with_values=False):

        if with_values and not isinstance(first, type(second)):
            message = '%s - 值类型--预期结果：%s, 实际结果：%s' % (path, type(first).__name__, type(second).__name__)
            self.save_diff(message)
        if isinstance(first, dict):
            for key in first:
                #print(key)
                if key not in self.ignore_value_of_keys:
                    #print('tets')
                    if len(path) == 0:
                        #print(len(path))
                        new_path = key
                    else:
                        new_path = "%s.%s" % (path, key)

                    if isinstance(second, dict):
                        if key in second:
                            sec = second[key]
                        else:
                            compare_result = "实际结果没有路径：%s" % new_path
                            self.save_diff(compare_result)
                            sec = None
                        self.check(first[key], sec, path=new_path, with_values=self.with_values)
                    else:
                        message = "实际结果没有路径：%s" % new_path
                        #print(message)
                        self.save_diff(message)
                        self.check(first[key], second, path=new_path, with_values=self.with_values)

        elif isinstance(first, list):
            print('==================================')
            for (index, item) in enumerate(first):
                new_path = "%s[%s]" % (path, index)
                sec = None
                if second:
                    try:
                        sec = second[index]
                    except (IndexError, KeyError):
                        compare_result = '%s - 类型：%s' % (new_path, type(item).__name__)
                        self.save_diff(compare_result)
                self.check(first[index], sec, path=new_path, with_values=self.with_values)
        else:
            if with_values:
                if first != second:
                    comapre_result = '字段%s值不一致：预期结果值：%s，实际结果值：%s' % (path, first, second)
                    self.save_diff(comapre_result)
            return

    def save_diff1(self, diff_message, type_):
        if diff_message not in self.difference:
            self.difference.append((type_, diff_message))

    def save_diff(self, diff_message, path=''):
        if diff_message not in self.difference:
            self.difference.append(diff_message)
def check_result(expect_result, actual_result, with_values=True, ignore_list_order_recursively=False, ignore_value_of_keys=[], assert_msg=''):
    """
          结果比较（以预期结果为准）
          :param expect_result:  预期结果
          :param actual_result: 实际结果
          :param with_values: True-比较值,False-不比较值
          :param ignore_list_order_recursively: 是否忽略递归排序  当为True 时，将会进行比较前的json字段排序
          :param ignore_value_of_keys: 过滤的字段key （列表）
          :param assert_msg: 用户自定义断言错误提示
          :return:
          """
    if isinstance(expect_result, str):
        logging.info('预期结果:\n' + expect_result)
        expect_result = json.loads(expect_result)
    else:
        logging.info('预期结果:\n' + json.dumps(expect_result, indent=2, ensure_ascii=False))
        expect_result = json.loads(json.dumps(expect_result))

    try:
        if isinstance(actual_result, str):
            actual_result = json.loads(actual_result)
        else:
            logging.info('实际结果:\n' + json.dumps(actual_result, indent=2, ensure_ascii=False))
            actual_result = json.loads(json.dumps(actual_result))
    except Exception:
        raise Exception('出现异常！实际结果格式错误！\n{}'.format(actual_result))

    result, reason = compare(expect_result, actual_result, with_values=with_values,
                                        ignore_list_order_recursively=ignore_list_order_recursively,
                                        ignore_value_of_keys=ignore_value_of_keys)
    if not result:
        logging.error('出现错误！接口校验时发现预期结果与实际结果不一致！原因： \t\n' + reason)
        raise InterfaceVerifyError('接口校验错误！原因： \t\n' + reason + '\t\n' + assert_msg)




def compare(expect_location, actual_location, with_values=True, ignore_list_order_recursively=False, ignore_value_of_keys=[]):
    """
    对象比较方法
    :param expect_location: 预期结果
    :param actual_location: 实际结果
    :param with_values: True-比较值,False-不比较值-只比较json格式
    :param ignore_list_order_recursively: 是否忽略递归排序  当为True 时，将会进行比较前的json字段排序
    :param ignore_value_of_keys: 过滤的字段key （列表）
    :return:
    """

    json1 = expect_location
    json2 = actual_location

    if ignore_list_order_recursively:

        json1 = _bottom_up_sort(json1)
        json2 = _bottom_up_sort(json2)


    diff1 = Diff(json1, json2, with_values, ignore_value_of_keys).difference


    if not diff1:
        return True, json.dumps(diff1, ensure_ascii=False, indent=4)
    else:
        return False, json.dumps(diff1, ensure_ascii=False, indent=4)



def _bottom_up_sort(unsorted_json):
    '''
    进行字典/列表排序整理-最终还是放入Diff进行比对
    :param unsorted_json:
    :return:
    '''

    if isinstance(unsorted_json, list):
        new_list = []
        for i in range(len(unsorted_json)):
            new_list.append(_bottom_up_sort(unsorted_json[i]))
        return sorted(new_list)

    elif isinstance(unsorted_json, dict):
        new_dict = {}

        for key in sorted(unsorted_json):
            new_dict[key] = _bottom_up_sort(unsorted_json[key])
        return new_dict
    else:
        return unsorted_json


if __name__ == '__main__':
    expected_dic = {'Headers': {'ValidateToken': '_fb6feb46f67f439b077ee0e9c0ad58c'}}
    au_dic1 = {'Headers': {'ValidateToken': '_fb6feb46f67f4139b077ee0e9c0ad58c'},'NewVerifParmsData': {'UserName': 'hctest001'}, "age": "test"}
    check_result(expected_dic,au_dic1)
