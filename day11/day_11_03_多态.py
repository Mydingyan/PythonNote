# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_11_03_多态.py
@time: 2022/9/12 15:32
"""

#多态
# 子类与父类中同名方法, 重写父类方法,就是多态


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

    def work(self):
        print("do something get money")


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

    #相同名称,重写父类方法
    def work(self):
        print("artdesgner's work is deaw a picture -artdesgner 的作品是一幅画 ")


# 子类
class TestEngineer(Human):
    def work(self):
        print("TestEnginner's work is run test -TestEngineer 的工作是运行测试")



# 实例化子类并增加属性
one_art = ArtDesigner("小雅",26,"female",6666)   #子类增加了一个salary属性吗,需要增加子类属性的初始化
one_art.work()

# 实例化TestEngineer子类
one_art  = TestEngineer("王者",27,"male")
one_art.work()