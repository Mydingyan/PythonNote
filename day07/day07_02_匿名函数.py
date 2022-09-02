# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day07_02_匿名函数.py
@time: 2022/9/2 23:06
"""


# # 匿名函数
# def add(x,y):
#     return x + y
#
# print(add(100,200))

# 简单写法的匿名函数
# def add(x,y): return x + y
# print(add(100,200))

print("=====lambda函数（匿名函数的方法）======")
# 匿名函数语法(也叫lambda函数）
# lambda:x,y:x + y    #lambda代替了def 、return两个函数

l_1 = lambda x,y:x+y
print(l_1(500,611))

l_2 = lambda x,y:(x+y,x-y)
xsy,xpy = l_2(500,1000)
print(xsy)
