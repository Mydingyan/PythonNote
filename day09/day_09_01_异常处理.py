# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_09_01_异常处理.py
@time: 2022/9/4 16:49
"""

# 异常处理

# print("======before======")
# open("tyerer.txt")   #打开不存在的文件，报错FileNotFoundError
# print("======after======")

# 所有语法可以单独使用，也可以组合使用
print("=====异常处理基础语法======")
try:
    print("======before======")
    # open("tyerer.txt")    #不存在的文件
    print(1/0)   #这里会报错
    open(r"../day07/文件操作附件/产品.txt")  # 存在的文件
    print("======after======")
except(TypeError,KeyError):
    print("TypeError字符类型,KeyError键 错误")
except (IOError,NameError):   #错误分组，可以写已知报错，被except接收异常（也可以写单个）
    print("IOError,NameError错误，文件路径未找到，请检查文件路径")
except:    #除了IOError这种错误，其他异常都提示这个
    print("打开文件出错")
finally:  #不管是否出错，都运行
    print("finally表示不管是否出错，都会运行")
# else:
#     print("没有发生任何错误")
print("打开文件后的操作")



print("=====捕获异常的常用写法，报错后会写入日志里======")
#处理一切异常常用写法
try:
    print("======before======")
    open(r"../day07/文件操作附件/产品aa.txt")  #不存在的文件
    print("======after======")
    print(1/0)   #这里会报错
except Exception as msg:
    print("程序出错，报错信息位：\n",msg)

print("打开文件后的操作")



#自定义抛出异常
#1 异常的传递
#用途：1 防备调用其他程序报错，try嵌套中不会影响外部代码
print("=====方法一：try嵌套")

try:
    f = open(r"../day08/day_08_02_OS模块.py")
    try:    #try 嵌套
        while True:
            content = f.readline()
            if content == "":
                break
            print(content)
    except:  #打开文件后，就捕获异常，如果没有这一句，会影响外部代码
        print("读取文件发生异常！")
    finally:
        f.close()
        print("关闭文件")

except Exception as msg:
    print("程序出错，报错信息位：\n",msg)
else:
    print("程序运行正常，没有报错")




#2 函数嵌套调用
print("=====函数嵌套调用=====")


def test1():    #发生异常的函数
    print("test--1")
    print(num)   #使用没有定义的变量报错


def test2():
    print("test--2   start")
    test1()
    print("test--2   end")


def test3():    #调用test1
    try:
        test1()
    except Exception as result:
        print("捕获到异常，异常为\n",result)
    print("test--3")


test3()
