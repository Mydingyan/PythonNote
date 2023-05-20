# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: 增加函数新功能.py
@time: 2023/5/19 22:49
"""


# 原函数 （可以理解为这部分代码前人写的）
import random
import time



def strong(f):
    def inner():
        print("strong函数内 的inner 函数内 运行传入函数",f.__name__)
        print(f.__name__,"函数开始运行时间",time.asctime())
        start_time = time.time()

        f()


        print(f,__name__,"函数结束运行时间",time.asctime())
        end_time = time.time()
        print("运行持续时间：",int(end_time - start_time))

    return inner #此处不能加括号

# 装饰器，就是用来增强原来函数（代码）功能，而且不用改写函数代码
@strong   #装饰器  （ 主要目的就在于，给前任写的代码中增加新功能，而且不需要改动原有的代码   人家的屎山代码不改动的情况下还能开发新功能）
def a():
    print("fun_b are working---")
    # 随机暂定几秒
    time.sleep(random.uniform(0, 10))

def b():
    print("fun_b are working---")
    #随机暂定几秒
    time.sleep(random.uniform(0, 10))

# 调用方式1：如果没有添加装饰器，那么调用个a函数，需要定义一个新的函数使用
# new_a = strong(a)
# new_a()

# 调用方式2：如果使用装饰器，可以直接这么调用（直接使用)
a()