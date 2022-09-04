# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_08_02_OS模块.py
@time: 2022/9/4 13:46
"""

'''
文件  OS模块
OS： opreate system
Python标准库中的  用户访问操作系统的模块
'''

import  os

#查看操作系统类型
print(os.name)   #打印NT：表示Windows   ；打印posix：表示Linux 、unix 系统

#查看当前路径（运行WINDOWS CMS中的dir系统命令）
os.system("dir")

#启动程序
# os.system(r"C:\Windows\System32\calc.exe")    #打开计算器

#获取已经配置应用程序的系统变量
print(os.environ)


#获取当前Python的运行路径
print(os.getcwd())


#罗列目录下的所有文件名（非隐藏文件）
names = os.listdir(os.getcwd())
print(names)


#修改文件名
src = r"./test_case/test_001.py"  #修改前的文件名
dst = r"./test_case/test_101.py"  #修改后的文件名
os.rename(src,dst)  #调用rename改名方法


# 删除文件
os.remove(r"./")