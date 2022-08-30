# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day06_01_函数.py
@time: 2022/8/30 23:43
"""


# 函数语法格式
'''
def：表示关键字
function_name()：标识符，起名字用的，可以给变量、函数、类、对象起名字  ()也是必须的，可以为空
page:参数

def function_name(para):
    stataments（执行语句，可以有多行）
    
'''

# 函数案例  (如果没有调用，函数是不会执行的）
def print_msg():
    print("print 函数内部代码")

# print_msg()   #写函数名就可以调用函数，调用才会执行函数


## 函数的嵌套（方法中调用方法）
def pritn_int():
    print(str(99))
    print_msg()

pritn_int()
#print(pritn_int())   # None
