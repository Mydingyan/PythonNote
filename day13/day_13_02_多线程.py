# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_13_02_多线程.py
@time: 2022/9/24 18:34
"""


# 多线程
# ![1664017626874.png](https://cdn.loveloveme.cn/2022/09/24/632ee4dce6d71.png)

# 每一个程序启动以后，就会有一个进程，
# 线程是再进程内开辟一个线程（一个进程可以有多个线程）
# （四核CPU ，相当于就是把四个CPU做在一起，每一个核心

'''
进程和线程的区别

1.复用CPU，可以并发执行
2.区别：
（1）地址空间，一个进程，至少有一个线程，他们共享进程的地址空间
            每一个进程，是有独立的地址空间
（2）资源拥有：进程是资源配分和拥有的单位，而同一个进程内的线程  共享资源
（3）线程是处理器调度的基本单位，进程不是

总之：一个程序至少有一个进程，一个进程至少有一个线程

Python中实现多线程的方式：用threading模块实现多线程
'''

import threading #内置模块
from time import  sleep



# 多线程方法一：通过threading.Thread()创建
def test(msg,x,y):
    for i in range(x,y):
        print(msg,"num:",i)
        sleep(1)

# 并发运行
thread1 = threading.Thread(name = "t1",target=test,args=("thread1----",0,5))   #提示：test函数可以作为其他函数的参数
thread2 = threading.Thread(name = "t2",target=test,args=("thread2----",2000,2005))   #threading.Thread() 方法实现多线程

thread1.start()   #启动多线程
thread2.start()

""" 
输出结果：
thread1---- thread2---- num: num: 0     #同时运行
2000
thread1---- num: 1
thread2---- num: 2001
thread2----thread1---- num: 2002 
num: 2
thread2----thread1---- num:  2003
num: 3
thread1----thread2----  num:num:  2004
4

进程已结束，退出代码为 0
"""


print("=====多线程方法二：=====")
# 多线程方法二：通过继承threading.Thread()类实现
class mythread(threading.Thread):
    #重写run方法（Thread中有run方法）
    def run(self):
        for i in  range(1,5):
            print("num的值是：",i)
            sleep(1)

thread3 = mythread()
thread4 = mythread()

# thread3.run()
# thread4.run()

thread3.start()
thread4.start() # 备注：不太理解start与run启动多线程的区别
