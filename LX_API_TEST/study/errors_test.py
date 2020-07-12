#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Desc    : 自定义异常类学习
from Libs.Errors import *
a = 0
try:
    if not a:
        raise InterfaceVerifyError('接口返回异常')
except InterfaceVerifyError:
    a=1
    print(a)
print('101')

# 捕获到异常则进行字段判断