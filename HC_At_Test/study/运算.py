# -*-coding:utf-8-*-
# print(3//3)
# print(1/2)
# print(1//2)
# print(3%3)
# print(1%3)
# 取余 能除尽的取余都是0
list=[]
for i in range(100):
    if i%3 == 0:
       list.append(i)
print(list)