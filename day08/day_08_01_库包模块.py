# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_08_01_库包模块.py
@time: 2022/9/3 15:08
"""

'''
本章：库、包、模块详解
-- 模块： module:一个Python文件，就是一个模块，一般由函数和类组成
-- 包：package:多个模块，放在一个文件夹里，就是一个包。 其中必须有一个 __init.py__ 

++ 库：逻辑概念,具有一定的功能，可以是模块，也可以是包 
 

#  包和文件夹的区别
1. 包里面 必须有 __init__.py
2. python只能导入包中的对象，不能导入directory(目录）


导入方法
用  import 关键字来导入
'''

# 导入关键字具体方法
# 从模块中导入
# 从包中导入

#1. 同目录下导入
# 方法一:直接导入，导入同目录下模块中的对象
# import  util.main_module
# util.main_module.print_msg()   #调用函数
# print(util.main_module.LANGUAGE)  #调用变量


# 方法二： 导入同目录下的对象
# 这种方法导入时，会运行导入文件中的所有代码
import main_modul_001 as mm   #导入文件名可以重命名
# mm.print_msg_001()
# print(mm.SYSTEM)  #可以使用导入对象中的变量

# 2. 用from 方法导入函数和变量
# 方法一：导入同目录下模块中的对象
# from  main_modul_001 import  print_msg_001   #导入具体函数，调用时就更方便
# from  main_modul_001 import  print_msg_001 as p1  #导入具体函数，调用时就更方便
# from main_modul_001 import SYSTEM
# print_msg_001()   #导入函数
# print(SYSTEM)  #这种方法也可以导入具体的变量


# 方法二：导入同目录下的对象
# from util import main_module as mm   #方导入法一：
# mm.print_msg()   #调用函数
# print(mm.LANGUAGE)  #调用变量


# main 函数  假的main函数

# __name__，python系统设置的变量
# 导入的模块运行  __name__ 等于模块名
# 模块内运行，__name__ 等于__main__
import main_modul_001 as mm   #导 入是，会运行除了__name__函数下的所有代码
#if __name__ == '__main__':  判断语句，防止被导入时运行

