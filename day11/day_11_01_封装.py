# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_11_01_封装.py
@time: 2022/9/11 16:00
"""


'''
面向对象的三大特征
封装、继承、多态

封装：
1. 为什么？  数据的安全性，降低代码耦合度
2. 表现形式  将一组具有统一功能和相关的代码，抽象成一个函数或者一个类 或类的方法            --个人可以理解为API自动化中登录、加密写成固定方法，其他接口直接调用极客
三个基本权限：
共有、私有、保护

'''


class Human():
    arms = 2
    _addrss = "科技三鹿"  # 受保护的属性,可以调用(主要是提示看代码的人不要乱动)
    lega = 2

    def __init__(self,name,age,income):    #私有属性
        self.name = name
        self.age = age
        self.__income = income   #私有属性（不能直接调用）

    def eat(self):
        print("i eat something")

    def run(self):
        print("i run away")

    #私有属性访问，提供接口的形式
    def get_income(self):
        return  self.__income

    # 修改私有属性的接口
    def set_income(self,new_income):
        #校验之后
        if new_income < 1800:
            return "不能低于最低工资"
        elif new_income >10000:
            return "工资过高"
        else:
            self.__income = new_income
            return "修改成功"
        # 写入Log日志

    def change(self,na):
        self.__set_age(na)   # 通用公用方法调用私有方法

    def __writer_log(self,mag):  #举例,写私有方法(增删改的日志)
        pass

    def __set_age(self,na):  # __开头表示私有方法(一)  比如链接数据库\修改数据库数据的方法写成私有方法,提供接口给公共方法
        self.age  = na
# 实例化
one_man = Human("刘备",30,5000)


#公有属性调用 (会把所有值都修改了)
print("每个人的胳膊：",one_man.arms)
print("我的名字：",one_man.name)

#私有属性调用
# print("我的收入：",one_man.income)   # 直接使用私有属性会报错 AttributeError
print("通过get_income函数接口获取收入:",one_man.get_income())

# 私有属性的修改 (只修改自己的值,而且可以加上校验)
one_man.set_income(555)
print("通过接口修改私有属性函数:",one_man.get_income())


# 通过实例修改属性
# 公有属性能直接全部修改
# one_man.age = 100
#
# print("年龄改为:",one_man.age)


# 私有方法调用
one_man.change(600)         #私有方法调用:需要在类函数中通过公共方法调用
print("年龄改为:",one_man.age)


# 受保护的属性调用
print("受保护的属性:",one_man._addrss)  #可以调用