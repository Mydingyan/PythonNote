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
#print(str_4[50])  # IndexError: string index out of range  字符串索引超出范围


print("=====切片的语法======")
# [开始:结束:步长]   左闭右开

str_4 = '0123456789abcdefghijklmnopqrst'

print(str_4[3:])   #打印第四个字符之后的所有
print(str_4[:4])
print(str_4[1:4])
print(str_4[1:10:2])
print(str_4[::3])  #从开始到末尾间隔3位的数据

print("=====切片的语法：负数======")
#可以取负数，从右往左数
#print(str_4[::-1])   #倒序输出
print(str_4[-10:-2:-1])

print("=====切片的语法：字符串不可使用切片改变======")


print("=====字符串的拼接和重复======")

# 字符串的拼接和重复
str_5 = 'abcde'
str_6 = '12345'
print(str_5+" "+str_6)   #两种方法等价
print(str_5,str_6)

print(str_5 * 10)

print("=====jion 连接其他 字符串 ======")

# join  用自己来连接其他 字符串

# 案例
print(" ".join(["Hello","Python","world!"]))
print("_".join(["Hello","Python","world!"]))
print("-".join(["Hello","Python","world!"]))
print("lebo".join(["Hello","Python","world!"]))

# 字符串性质判断
age = input("请输入年龄：")
if age.isdigit():
    print("您输入的年龄是:",age)
else:
    print("年龄只能输入纯数字！")