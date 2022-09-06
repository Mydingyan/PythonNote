# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_09_02_对象练习.py
@time: 2022/9/6 23:18
"""

#1、定义一个类 :类在实例化之前，啥也干不了

class ArtDesigner():
    salary =5000 #类属性
    department = '设计部'  #类属性

    def draw_picture(self):      # 类方法
        print("111")


#2、 实例化
# 小王
art_wang = ArtDesigner()

#3、 实例化后，就可以调用实例和方法
# 既可以调用对象的属性，也可以调用对象的方法
print(type(art_wang.salary))  #调用属性
print(art_wang.draw_picture())  #调用方法

# 调用方法
art_wang.draw_picture()
print(type(art_wang))



#



