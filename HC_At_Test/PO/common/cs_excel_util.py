# -*-coding:utf-8-*-
from Libs.excel_util import ExcelUtil
from PO.common.common_util import *
'''
测试case管理
'''
file_path = get_project_path() + '\\Data\\ClassMod_TestCase_info.xls'
def excel_test_classmod(mod_name):
    '''
    用例模块开关
    :return:
    '''
    flag = True
    ex = ExcelUtil(file_path).read_excel_addlist()
    for i in range(len(ex)):
        if ex[i]['classmod'] == mod_name:
            if ex[i]['temp'] == 'Y':
                flag = False
            else:
                flag = True
    return flag

def excel_test_case(sheet,method_name):
    '''
    case开关
    :return:
    '''
    flag = True
    ex = ExcelUtil(file_path,sheet).read_excel_addlist()
    for i in range(len(ex)):
        if ex[i]['classmethod'] == method_name:
            if ex[i]['temp'] == 'Y':
                flag = False
            else:
                flag = True
    return flag

if __name__ == "__main__":
    t = excel_test_case(2,'test3_offline_cel')
    print(t)
    m = excel_test_classmod('WebTopUpTestCase')
    print(m)