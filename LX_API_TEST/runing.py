#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import getopt
from Libs.log_util import set_log
import unittest
from Config.Config import *
import logging
import HTMLTestRunnerCN
from Libs.data_util import get_case_from_excel
set_log()
def run():
    while True:
        logging.info('开始执行测试.......')
        #case_file_path = Config().case_file_path
        #suite = unittest.defaultTestLoader.discover(case_file_path,'*Case*.py')
        f = open(Config().report_path,'wb')
        runner = HTMLTestRunnerCN.HTMLTestRunner(stream=f,title='LX接口自动化测试报告',tester='Fan',description='首次报告',verbosity=2)
        all_test_case = add_case_suite()
        try:
            runner.run(all_test_case)
        except Exception as err:
            f.close()
            logging.error(err)
            logging.error('执行异常，请检查测试数据！')

        logging.info('测试结束.......')


def add_case_suite():
    '''
    添加测试集
    :return:
    '''
    case_path = Config().test_case_dirname_path
    suite = unittest.TestSuite()
    case_list = []
    for dirpath,dirname,filename in os.walk(case_path):

        for file in filename:
            # 匹配文件起始和结尾字符
            if file.endswith('.py') and not file.startswith('__'):
                case_list.append(file)

    for case in case_list:
        discover = unittest.defaultTestLoader.discover(case_path,pattern=case)
        suite.addTest(discover)
    return suite





if __name__ == '__main__':
    run()