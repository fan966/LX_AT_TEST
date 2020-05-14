# # -*-coding:utf-8-*-
import logging
from Libs.log_util import set_log
import HTMLTestRunnerCN
import unittest
from PO.common.common_util import *

def main():
    '''
    主程序入口
    :return:
    '''
    while 1:
        set_log()
        logging.info("开始执行测试......")

        case_path = get_project_path() + '\\TestCase'
        suite = unittest.defaultTestLoader.discover(case_path,'*test_case.py')
        report_path = get_project_path() + '\\Report\\test_report\\Auto_test_reporting.html'
        f = open(report_path,'wb')
        runner = HTMLTestRunnerCN.HTMLTestRunner(stream=f, title='Lx自动化测试报告', tester='Fan', description='首次测试报告',verbosity=2)
        try:
            runner.run(suite)
        except Exception as err:
            f.close()
            logging.error(err)
            logging.error('【INFO】执行异常，请检查文件数据')

        logging.info("测试结束......")


if __name__ == "__main__":
    main()
