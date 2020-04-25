import HTMLTestRunnerCN
import unittest
import os
import logging
from log.log_util import set_log
set_log()
logging.info('.....测试开始.....')
case_path = os.getcwd()
suite = unittest.defaultTestLoader.discover(case_path,'unittest_*.py') # 匹配该路径下所有unittest_*.py的case文件，得到case集合
#unittest.TextTestRunner().run(suite)
#report_path = os.path.join(os.getcwd(),"\\python\\report\\first_test_report.html")
report_path = "..//report//first_test_report.html"
f = open(report_path,'wb')
runner = HTMLTestRunnerCN.HTMLTestRunner(stream=f,title='yolo傻逼！！！测试报告',tester='Fan',verbosity=1,description='刀哥牛逼牛逼牛逼')
runner.run(suite)
logging.info('.....测试结束.....')