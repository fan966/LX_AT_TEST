#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Libs.excel_util import ExcelUtil
from Libs.log_util import set_log
import logging
from Config.Config import *
def get_case_from_excel(file_path,sheet_name_list,run_rules_dic,sheet_name=''):
    '''
    excel文件获取case数据
    :param file_path: 文件路径
    :param sheet_name_list: 指定sheet名
    :param run_rules_dic: 过滤规则字典
    :return:
    '''
    data_result = None
    ex = ExcelUtil(file_path,sheet_name)
    if isinstance(sheet_name_list,list):
        data_result = ex.excel_case_data_info(sheet_name_list,run_rules=run_rules_dic)
    else:
        logging.error('【提供的sheet名必须是list格式】')
    if not data_result:
        logging.error('【Excel接口用例数据文件中未找到待匹配的接口用例！】')
    return data_result

def write_result_data_to_excel(file_path,sheet_name,row_name,row_value,result):
    '''
    写入excel实际结果
    :param file_path:文件路径
    :param sheet_name: sheet名
    :param row_name:
    :param row_value:
    :param result:
    :return:
    '''
    excel = ExcelUtil(file_path,sheet_name)
    row_number = excel.get_excel_num(row_name,row_value)
    excel.write_result_to_excel(row_number,excel.get_cols(),result)

if __name__ == '__main__':
    file_path = Config().case_data_file_path
    write_result_data_to_excel(file_path,'User','ID','A003','dsadasdasd')

