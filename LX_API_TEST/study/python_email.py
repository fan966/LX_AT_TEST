# coding: utf-8
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText

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
if __name__ == '__main__':
    from Config.Config import *
    path = Config().case_data_file_path
    send_mail(username='niefan_it@163.com',passwd='XKXCOUSQLDJJLWRP',recv='664340382@qq.com',title='python_test',content='python_test_report',file=path)