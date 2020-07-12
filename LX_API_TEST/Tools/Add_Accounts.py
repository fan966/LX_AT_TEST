#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 添加账户+修改密码+设置资金密码
# 资金密码统一为aaaa22
from Libs.log_util import set_log
from Verify.User.UserVerify import login_api
from Libs.http_requests import *
import logging
from Libs.CheckRresult_Util import check_result
set_log()
def add_account():
    account = 'atest1'
    password = 'aaaa2222'
    logging.info('---------调用登录接口--------------------')
    LoginSessionID = login_api(account,password)
    if not LoginSessionID:
        raise ('登录失败，请检查')
    logging.info('---------调用设置资金密码接口-------------')
    actual_result = http_api_requests('密码相关.重置/修改资金密码',Headers={'LoginSessionID':LoginSessionID},NewVerifParmsData={})
    expected_result = {"Status":True,"Info":"修改成功","Data":None,"Code":0}
    check_result(expected_result,actual_result)


if __name__ == '__main__':
    add_account()
