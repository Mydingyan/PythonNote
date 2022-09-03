# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: read_file.py
@time: 2022/9/3 13:50
"""

# 相对路径打开方式演示


print("=====文件打开方式案例一：相对路径：打开同级目录 =======")
# 相对路径（相对于 启动模块 的路径） 意思就是需要相同目录下才行
# ./ 打开同目录下文件   (左右斜杠都可以使用）
# f = open(r"./微信小程序.txt",mode="r", encoding="utf-8")


print("=====文件打开方式案例一：相对路径：打开上级目录 =======")
# 相对路径  ../ 打开上级目录的文件
# f = open(r"../微信小程序.txt",mode="r", encoding="utf-8")


print("=====文件打开方式案例一：相对路径：打开兄弟目录 =======")
# f = open(r"../文件操作附件/微信小程序.txt",mode="r", encoding="utf-8")
# print(f.read())
