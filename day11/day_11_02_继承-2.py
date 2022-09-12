# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_11_02_继承-2.py
@time: 2022/9/12 15:16
"""

# 子类调用父类的内容


#父类
class Human():

    def __init__(self,name,age,gender):
        self.name= name
        self.age = age
        self.gender = gender

    def eat(self):
        print("i eat something")

    def run(self):
        print("i run away")


# 子类(调用父类)
class ArtDesigner(Human):    # 继承Human

    # 重写子类自己的初始化方法
    def __init__(self,name,age,gender,salary):  #增加了一个方法
        #通过显式调用父类的初始化方法
        Human.__init__(Human,name,age,gender)   #调用父类的初始化方法
        #增加一个子类的实例属性
        self.salary = salary



    def deaw_pictur(self):   #子类特有的"技能"
        print("draw a picture")

#实例化子类
# one_art = ArtDesigner("小雅",26,"female")   #继承了父类的初始化方法(必须带初始化方法)
# print("子类的name:",one_art.name)

# 实例化子类并增加属性
one_art = ArtDesigner("小雅",26,"female",6666)   #子类增加了一个salary属性吗,需要增加子类属性的初始化
print("子类的salary:",one_art.salary)


# 子类中调用父类的方法
one_art.eat()
one_art.run()
one_art.deaw_pictur()   # 也可以调用子类自己的方法



# 继承

'''
1.子类可以继承多个父类,父类可以被多个子类继承
2.父类的私有属性,不能直接用
3.子类有用父类的私有属性,但可以引用的方法比较特殊      --一般不常用

'''