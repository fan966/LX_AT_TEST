#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import getopt
from Libs.log_util import set_log
import unittest
from Config.Config import *
import logging
import HTMLTestRunnerCN
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText
def main(argv):

    try:
        report_type = 1 # 测试报告类型
        opts,args = getopt.getopt(argv[1:],"hu:e:r:x")

        for op,value in opts:
            if op == '-u':
                account = value.strip() # 当前执行的用户

            elif op == '-e':
                evn_type = value.strip() # 当前执行脚本环境

            elif op == '-r':
                report_type = value.strip()

    except Exception as err:
        #print('test')
        pass



def send_mail(username, passwd, recv, title, content, mail_host='smtp.163.com', port=25, file=None):
    '''
    发送邮件函数，默认使用163smtp
    :param username: 邮箱账号 xx@163.com
    :param passwd: 邮箱密码
    :param recv: 邮箱接收人地址，多个账号以逗号隔开
    :param title: 邮件标题
    :param content: 邮件内容
    :param mail_host: 邮箱服务器
    :param port: 端口号
    :return:
    '''
    if file:
        msg = MIMEMultipart()

        # 构建正文
        part_text = MIMEText(content)
        msg.attach(part_text)  # 把正文加到邮件体里面去

        # 构建邮件附件
        part_attach1 = MIMEApplication(open(file, 'rb').read())  # 打开附件
        part_attach1.add_header('Content-Disposition', 'attachment', filename=file)  # 为附件命名
        msg.attach(part_attach1)  # 添加附件
    else:
        msg = MIMEText(content)  # 邮件内容
    msg['Subject'] = title  # 邮件主题
    msg['From'] = username  # 发送者账号
    msg['To'] = recv  # 接收者账号列表
    smtp = smtplib.SMTP(mail_host, port=port)
    smtp.login(username, passwd)  # 登录
    smtp.sendmail(username, recv, msg.as_string())
    smtp.quit()

def run():
    set_log()
    logging.info('开始执行测试.......')
    f = open(Config().report_path,'wb')
    runner = HTMLTestRunnerCN.HTMLTestRunner(stream=f,title='LX接口自动化测试报告',tester='Fan',description='首次报告',verbosity=2)
    all_test_case = add_case_suite()
    try:
        runner.run(all_test_case)
    except Exception as err:
        f.close()
        logging.error(err)
        logging.error('执行异常，请检查测试数据！')
    path = Config().report_path
    send_mail(username='niefan_it@163.com',passwd='XKXCOUSQLDJJLWRP',recv='664340382@qq.com',title='python_test',content='python_test_report',file=path)

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
    # if len(sys.argv) == 1:
    #     sys.argv.append('-u Fan')
    #     sys.argv.append('-e test')
    #     sys.argv.append('-r 1')
    # main(sys.argv)
    #add_case_suite()
    # test_suite()
    run()
