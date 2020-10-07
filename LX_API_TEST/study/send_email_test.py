# !/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from Config.Config import *
path = Config().report_path
# 连接163邮箱服务器
mailserver = "smtp.163.com"
# 163邮箱的端口号
mailPort = 25
# 163邮箱的用户名
mailUsername = "niefan_it@163.com"
# 使用163邮箱的授权 密码
mailPasswd = "XKXCOUSQLDJJLWRP"
# 接收方的邮件地址
to_mail = "664340382@qq.com"
# 连接邮箱服务器,
smtpServer = smtplib.SMTP(mailserver,mailPort)
# 登陆邮箱服务器, 注意: 密码是邮箱的授权密码,    登陆前必须先授权
smtpServer.login(mailUsername,mailPasswd)
# 写邮件-发件人,收件人,内容
# 创建MIMEtext(),并设置内容
# msg = MIMEText('python_email_test')
# 设置主题内容
msg = email.mime.multipart.MIMEMultipart()
msg["From"] = mailUsername
msg["To"] = to_mail
msg["Subject"] = "Python"
# 添加附件，从本地路径读取。如果添加多个附件，可以定义part_2,part_3等，然后使用part_2.add_header()和msg.attach(part_2)即可。
part = MIMEApplication(open(path, 'rb').read())
part.add_header('Content-Disposition', 'attachment', filename="html_report.html")  # 给附件重命名,一般和原文件名一样,改错了可能无法打开.
msg.attach(part)


# 发送邮件
smtpServer.sendmail(mailUsername,to_mail,str(msg))
# 关闭连接
smtpServer.close()
