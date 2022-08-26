# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day04_01.py
@time: 2022/8/25 23:11
"""

# 创建字符串

str_1 = 'abc de'

# 字符串切片

str_4 = 'avcvzcfd456451'
print(str_4[1])  #切一个字符

print("=====切片的语法======")
# [开始:结束:步长]   左闭右开

print(str_4[3:])   #打印第四个字符之后的所有
print(str_4[:4])


str_5 = 'abcde'
str_6 = '12345'
print(str_5+" "+str_6)   #两种方法等价
print(str_5,str_6)

print(str_5 * 10)