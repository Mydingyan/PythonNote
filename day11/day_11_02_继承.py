# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_11_02_继承.py
@time: 2022/9/11 18:36
"""


'''
继承
类是可以相互继承的
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


class ArtDesigner(Human):    # 继承Human
    pass



# 实例化
one_man = ArtDesigner("刘备",30,5000)

# 子类如何调用父类的

# 1>子类继承父类属性案例
one_art = ArtDesigner("刘备",30,5000)
print("继承来的属性: ",one_art.name)

# 2> 子类继承父类属性案例
print("继承来的方法")
one_art.eat()


# 3>子类修改父类实例属性的案例
one_art.set_income(9000)
print("修改后的实例私有属性:",one_art.get_income())

# 查看继承关系的魔法方法
print(ArtDesigner.__mro__)   # 层级继承关系  (<class '__main__.ArtDesigner'>, <class '__main__.Human'>, <class 'object'>)


