# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_13_03_父线程和子线程.py
@time: 2022/9/25 17:27
"""

# 主线程和子线程
import threading
from time import  sleep

'''
如果线程A中，启动了一个线程B，  那么A就是B的父线程

daemon属性：False 主线程退出 子线程不退
            True  主线程退出 子线程不退
            
每一个线程都有自己的 daemon属性，你默认是False
必须再start之前设置（必须在开始前设置线程）

# 线程同步：
通过 锁 来实现 资源共享
'''

print("=====案例=====")

def func(arg):
    print("func start")
    sleep(1)
    print("传入参数",arg)
    print("func end")

# 定义子线程
t = threading.Thread(name='王者荣耀线程1',target=func,args = ("para",))

# 退出主线程
t.setDaemon(True)

# 常用方法
print("线程是否活动",t.is_alive())  #返回False
print("线程的名字",t.name)

# 驱动子线程（启动线程）
t.start()
print("线程是否活动",t.is_alive())  #启动后，返回True

# 阻塞线程
t.join()

print("父线程已经运行结束")