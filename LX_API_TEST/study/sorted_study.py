#!/usr/bin/env python
# -*- coding: utf-8 -*-
# sorted() 可以对可迭代对象进行排序
dic = {'Headers': {'ValidateToken': '_fb6feb46f67f4139b077ee0e9c0ad58c'}, 'NewVerifParmsData': {'UserName': 'hctest001'},'age':'tets'}
d = sorted(dic)
print(d)


t =  {'ValidateToken': '_fb6feb46f67f4139b077ee0e9c0ad58c'}
tt = sorted(t)
print(tt)



str1 = 'test'
str2 = sorted(str1)
print(str2)