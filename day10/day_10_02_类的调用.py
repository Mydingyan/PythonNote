# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_10_02_类的调用.py
@time: 2022/9/8 22:52
"""
from day10.day_10_01_common import ShopUser


user_1 = ShopUser("张飞","123456")   #按住alt,再按回车，能够直接导入同路径方法
user_1.login()


## 新知识：魔法方法
'''
Python 的类中，所有双下划线 包起来的方法  就叫魔法方法（也叫魔术方法）
在类和对象 发生某些事件的时候，可以自动与运行，让类具有了神奇的魔力

'''

#1.初始化方法
# __init__
# 实例化时自动运行
# 该方法定义的属性，即为实例的属性
# 自动开辟了一个内存空间，保存该实例对象的属性 和 类方法的指针（指针可以理解为内存地址）
#
# class A():
#     pass
#
# class B(A):
#     pass
#
# class C():
#     pass
# b = B()
#
#
# # 判断 实例是否为类创建出来的 (判断类和类的关系）
# print(isinstance(b,A))   # True
# print(isinstance(b,B))   # True
# print(isinstance(b,C))   # False   b不是C的方法中创建出来的
#
#
# #判断子类  issubclass表示是子类
# print(issubclass(B,A))  #B是A的子类，返回True
# print(issubclass(A,B))  #A不是B的子类，返回False
#
#
#
# # __str__ 方法的调用：
# print(user_1.__str__())   # 我是一个用户类  # 调用day10.day_10_01_common 中的str类
#
# # __doc__() 方法的调用
# print(user_1.__doc__)     #返回day10.day_10_01_common 中头部注释部分
#
#
# # __module__ 当前对象的所在模块
# print("__module",user_1.__module__)    # 返回类的模块位置__module day10.day_10_01_common
#
#
# # __class__ 获取实例化原方法位置
# print(user_1.__class__)   #   <class 'day10.day_10_01_common.ShopUser'>
#
#
# # __name__
# print("day10-2_类的调用.py中的值",__name__)   #__main__
# print(__name__)

# __del__
# 当对象被删除时自动运行
# del user_1

# __dict__
# 以字典的形式，输出实例属性
# 属性转换为字典
print(user_1.__dict__)   # {'user_name': '张飞', 'password': '123456'}



# 反射  （内置函数的一种）

# hasattr   是否有...（返回True或False)

print(user_1.user_name)   #返回张飞
print(hasattr(user_1,"user_name"))   # user_1中有user_name属性，返回True
print(hasattr(user_1,"user_code"))   # user_1中没有user_code属性，返回False
print(hasattr(user_1,"login"))       #user_1中没有login方法，返回True
print(hasattr(user_1,"login_out"))    #user_1中没有login_out方法，返回False


# getattr  获取对象属性值
print(user_1.user_name)   #返回张飞
print(getattr(user_1,"user_name"))   #返回张飞， 与.的方法一直
print(getattr(user_1,"user_code","属性不存在"))   #如类中没有user_code，返回属性不存在


#set 修改对象属性
print(getattr(user_1,"user_name"))  #修改前，关羽
setattr(user_1,"user_name","关羽")  #修改user_name元素
print(getattr(user_1,"user_name"))  #修改后，user_naem为关羽

#delattr 删除属性
print(getattr(user_1,"user_name","属性不存在"))    #删除前，返回关羽
delattr(user_1,"user_name")                        #删除user_name元素
print(getattr(user_1,"user_name","属性不存在"))    #删除后，返回属性不存在
