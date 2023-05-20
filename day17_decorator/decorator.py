# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: decorator.py
@time: 2023/5/18 22:48
"""


# 装饰器


# 1.函数作为参数传递给另外一个函数
# def strong(f):
#     print("strong函数内运行传入函数",f.__name__)   #（函数的名字）
#     f()
#
# def a():
#     print("fun_a are working")
#
# strong(a)



# 2.函数的嵌套
## 函数可以在 函数内 定义另外一个函数

# def strong(f):
#     def inner():
#         print("strong函数内运行传入函数",f.__name__)   #（函数的名字）
#         #f()
#     inner()  #
#
# def a():
#     print("fun_a are working")
#
# strong(a)

# 函数里可以继续调用新调用新定义的函数


# 3.函数内部定义的函数，可以作为内部返回值
def strong(f):
    def inner():
        print("strong函数内运行传入函数",f.__name__)   #（函数的名字）
        f()
    return inner  #此处不能加括号，否则就不是返回函数，而是返回函数的返回结果过了     #inner 是一个函数对象，而 return inner 是将这个函数对象作为结果返回

def a():
    print("fun_a are working")

# new_a = strong(a)     # 表示重新定义的函数，所以没有结果
# #返回运行结果
# new_a()

def b():
    print("我是函数b")

new_b = strong(b)
new_b()


# 我们可以给原有函数增加新功能个，还不用改写原有函数的代码



