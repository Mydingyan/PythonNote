# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: main_module.py
@time: 2022/9/3 21:55
"""



print("----------------1-------------------")

SYSTEM = 'WINDOWS'  #变量
print("----------------2-------------------")

def print_msg_001():
    print("-----这段代码来自main_module_001.py的rint_msg函数-----")
    print("----------------3------------------")

print("----------------4-------------------")


#判断语句
#用法：__name__ == '__main__': 在本文件执行时，__name__ = __main__(__name__是python设定的系统变量），所以if语句可以执行
#当其他文件调用时，__name等于文件名，文件名不等于__main__,所以if语句不能执行

print("__name__:",__name__)
# 类似卧室的门（从外面导入就不会运行这里的代码）
if __name__ == '__main__':    #判断__name__这个魔法变量是不是等于__main__这个字符串
    print_msg_001()
    print("----------------5-------------------")

print("----------------6-------------------")
