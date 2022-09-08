# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_10_01_实例化练习.py
@time: 2022/9/8 22:38
"""


class ArtDesigner():
    post = '美工'  #类属性
    salary = 5000  #类属性

    def __init__(self,name88,income):
        print(f"在实例化{name88}时，自动运行...")
        self.name = name88   #name是变量名
        self.income = income  # 每一次实例化都和运行


print("=====实例属性的修改（重新赋值）=====")
art_wang = ArtDesigner("王富贵",6000)
art_li = ArtDesigner("李富荣",6500)    #实例化对象并重新赋值


art_wang.salary = 6000
print("art_wang 的 name 属性:",art_wang.name)  #查看类的属性
print("art_li 的 name 属性:",art_wang.income)
print("art_li 的 name 属性:",art_wang.salary)