#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Libs.http_requests import *
from Config.Config import *
import logging
from Libs.log_util import set_log
from Libs.Db_Sql_Util import *
'''
用户通用前置检查
'''
def login_api(account,password):
    """
    用户登录公告接口
    :param account: 账户 ttt1
    :param password: 密码 aaaa2222
    """
    res_msg = http_api_requests('登录注册.获取全局Token值', NewVerifParmsData={})
    ValidateToken = None
    if not res_msg:
        logging.error('获取全局Token失败')
    else:
        ValidateToken = get_json_value(res_msg, '/Data/Value')
    res_msg = http_api_requests('登录注册.获取图片验证码', Headers={'ValidateToken': ValidateToken}, NewVerifParmsData={})
    if not res_msg:
        logging.error('获取图片验证码失败')
    logging.info('======================调用：用户登录接口=======================')
    res_msg = http_api_requests('登录注册.用户登录', Headers={'ValidateToken': ValidateToken},NewVerifParmsData={"UserName":account,"Password":pwd_md5_encryption(password,'9999')})
    res_msg_stasus = get_json_value(res_msg,'/Status')

    if not  res_msg_stasus:
        logging.error('登录失败 ： {}'.format(res_msg))
    else:
        LoginSessionID = get_json_value(res_msg,'/Data/LoginSessionID')
        return LoginSessionID

def ag_login_api(account,password):
    '''
    后台登录通用接口
    :param account:
    :param password:
    :return:
    '''
    import re
    logging.info('======================调用：用户登录接口=======================')
    res_msg = http_api_requests('后台相关.用户登录',server_host=Config().ag_host,return_result=False,NewVerifParmsData={"username": account,"password":md5_encryption(md5_encryption(password))})
    str1 = res_msg.request.headers['Cookie']
    p = re.compile('LoginSessionID=.*; ', re.I)
    LoginSessionID = p.findall(str1)[0].split(';')[0].split('=')[1]
    if not LoginSessionID:
        logging.error('后台登录失败，请检查')
    return LoginSessionID


def from_db_get_user_ID(username):
    '''
    username;用户名
    数据库查询用户user_ID
    :return:
    '''
    db = DB_Util(Config().db_config_name)
    sql = '''select a.FID,a.FAccount,a.FCompanyID from 
    TAccounts as a 
    where a.FAccount='{}' and a.FCompanyID in 
    (select a.FCompanyID from TAccounts as a where a.FAccount='{}')'''.format(username,Config().ag_account)
    sql_result = db.excute_sql(sql)
    sql_result = db.sql_result_to_json(sql_result,['id','name','cid'])
    return sql_result

def from_db_TCredits_get_user_FBalance(FUserID):
    '''
    根据用户ID查询用户余额
    :return:
    '''
    db = DB_Util(Config().db_config_name)
    sql = '''select t.FUserID,t.FBalance from TCredits as t where FUserID='{}';'''.format(FUserID)
    sql_result = db.excute_sql(sql)
    sql_result = db.sql_result_to_json(sql_result, ['id','Balance'])
    return sql_result


if __name__ == '__main__':
    # data = from_db_get_user_ID('ttt11')
    # print(data[0]['id'])
    set_log()
    temp = login_api('ttt1','aaaa2222')
    print(temp)