# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_09_02_对象和类.py
@time: 2022/9/5 16:49
"""

'''
# 面向对象和类
# 把一系列相关的 变量 和 函数，卸载一起，进行封装（类）   类只是一个概念
# 供其他代码使用，这就是面对对象的思路

# 面向对象是旅行车旅游团（具体的需求已经实现了组合起来）， 面向过程是自驾游，门票酒店旅游的整个过程都需要自己准备
# 类在是实例化之前啥也没干

# 变量  -- 属性
# 函数 -- 方法

# 三大特性： 封装、继承、多态
'''

# 类和对象举例：

'''
# 对象指的是具体的一个场景

水果 -- 类 （因为很多种苹果，只要不是唯一的，就是类）
苹果 -- 类  
红苹果 -- 类
红富士苹果 --类
我上周唯一的那个苹果  --对象（具体到某一件事情、某一个东西）

造飞机
图纸  -- 类
做出来的每一架飞机 --对象

够 --- 类
黄狗 -- 类
我加的那只黄狗 --对象
'''


# 类的语法

# 关键字：class
# 类的名字：必须有，大驼峰命名法
# 属性：可以有,下划线命名法  (也可以是变量）
# 方法：可以有，下划线命名法  （函数）


# 美工类（1、 定义一个类）  类没有实例化之前，啥也干不了
# 封装
class ArtDesigner():
    salary =5000 #类属性
    department = '设计部'  #类属性

    def draw_picture(self):      # 类方法
        print("画一张图")
'''
# 创建对象，实例化对象

# 对象1 = 类名()
# 对象2 = 类名()
# 对象3 = 类名()

#在Python中，一切皆是对象
# 类实例化之后，就是对象

数据类型也是 对象
函数        也是对象
列表        也是对象，等等，所有的东西都是对象
'''

# 实例化对象 （2 、实例化）
# 美工 小王
art_wang = ArtDesigner()  # 实例化对象才能调用
print(type(art_wang))     # 类型是 class '__main__.ArtDesigner'
print(id(art_wang))       # 每个实例化之后，存储的位置都不一样（根据一个模子，做出来不同名字，相同属性的东西）
# 应用对象属性
# print(art_wang.salary)
# print(art_wang.department)

#调用对象的方法
art_wang.draw_picture()


# 美工 小李
art_li = ArtDesigner()
print(type(art_li))  #<class '__main__.ArtDesigner'>
print(id(art_li))  #2190401474464
print(art_li.salary)   # 5000
print(art_li.department) #设计部


# 美工 小孙
art_sun = ArtDesigner()
print(type(art_sun))  #<class '__main__.ArtDesigner'>
print(id(art_sun))   #2190401474416
print(art_sun.salary)  # 5000
print(art_sun.department)  #设计部

#调用对象的方法
art_sun.draw_picture()   # 画一张图
print(type(art_sun.salary))  # <class 'int'>
# print(id(art_sun.salary))
# print(type(art_sun.draw_picture()))
# print(id(art_sun.draw_picture()))


# 测试工程师类
# 封装
# class TestEngineer():
#     salary = 9000
#     department = "测试部"
#     def write_testcase(self):
#         print("writer testcase")
#     def run_testcase(self):
#         print("run testcase")
#
#
# #1.实例化对象（对象必须先实例化才能调用属性或者方法）
# test_wang = TestEngineer()
#
# # 方法一：调用对象的属性
# print(test_wang.salary)  #对象的属性   #9000
# print(test_wang.department)  #对象的属性     # 测试部

# 方法二：调用对象的方法
# test_wang.write_testcase()
# test_wang.run_testcase()
