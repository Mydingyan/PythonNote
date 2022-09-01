# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_03_函数传递.py
@time: 2022/9/1 20:14
"""


def a(x=5,y=5):
    print("x = ",x,"y = ",y)
    if x >y:
        return x,y
    else:
        return y,x
    print("a的最后一行")



# 函数参数的传递
# 1 位置参数：不能不传
# res = a()   #不传报错

# 不能少传 ：
# res = a(6)   #默认传给第一个参数

#不能多传
# res = a(3,5,6)  # 多传报错 IndentationError: unexpected indent

#位置不能错，一个萝卜一个坑


# 2 默认参数
# 不传值，默认展示原始值，只传一个参数，给第一位
res = a()
print("默认参数，不传展示原值：",res)  #  不传值时，取默认参数
res = a(7)
print("默认参数，不传",res) # 只传一个值时，默认给第一位
res = a(8888)
print("默认参数，不传",res)


# 3 关键字参数
# 参数的顺序：（位置参数,关键字参数,不定长参数)
def pople_msg(name,age,address):
    print("name:",name)
    print("age:",age)
    print("address:",address)

pople_msg(222,"张伟","李三")  #按顺序传参
pople_msg(age=20,name="张飞",address="中国")


# 4 不定长参数 （一个星号（*）表示不定长参数
# 格式：*args      args可以使用任意标识符，只是args表示参数的意思习惯用

def write_names(*args):
    print(args)    #多个元素传参给args,格式为元组格式
    print(type(args))
    for xunhaun in args:
        print(xunhaun)

write_names("三国","张飞","刘备","关羽")


# 前面卡位置,剩下的都给args
def write_names(address,kind = "英雄",*args):
    print("address:",address)
    print("kind:",kind)  #列表
    print("args:",args)  #元组
    print(type(args))
    for item_in in args:
        print(item_in)

write_names("中国","张飞","刘备","关羽")
write_names("中国",None,"张飞","刘备","关羽")
write_names("三国","桃园三结义","张飞","刘备","关羽")


"""
全局，局部变量
变量是只用范围
变量的生命周期
"""

# global g
# print("函数体外部的G值",g)
# print("函数体外部的g-地址："id(g))

def my_func():
    x = 10 #函数内的赋值属于局部变量  声明变量+赋值
    y = 100

    print("函数体内部的x值:",x)
    print("函数体内部的x-地址",id(x))

    g = 10000
    print("函数体内部的g值",g)
    print("函数体内部的g地址",id(g))

    # 全局变量关键字
    global z    #声明全局变量
    z = 500   # 赋值语句，不是声明变量
    print("函数体内部的z值",z)
    print("函数体内部的z-地址“",id(z))
    # global  Z = 1000


my_func()

x = 20
z = 200 #声明变量并赋值
print("函数体外部的x值是：",x)
print("函数体外部的x-地址",id(x))
print("函数体外部的x值是：",z)
print("函数体外部的x-地址",id(z))


# global关键字规则
'''
1.函数内部创建变量，默认情况下是局部变量
2.在函数外部创建变量，默认是全局变量

3.使用全局变量关键字 global ，函数体内创建读/写也是全局变量
4.使用global申明的关键字，在函数体之外使用不生效
'''