# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: func.py
@time: 2023/5/16 22:55
"""

# 可变参数
# 字典类型的可变参数

d_1 = {

    "name":"李待",
    "age":30
}

d_2 = {

    "name": "张飞",
    "address":"中国",
    "type":"武将",
    "age": 31
}


def func(**kwargs):
    print(kwargs)



func(**d_1)
func(**d_2)