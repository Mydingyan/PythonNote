# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: delete_student.py
@time: 2022/10/7 13:17
"""
from day16.database.mysql_normal import db


def delete_name():
    name = input("请输出要删除的学生姓名：")
    db.delete("students",f"name = '{name}'")    #疑问：在SQL中删除0行也是返回成功，如何判断删除值为空时提示


def delete_studentNo():
    stu_num = input("请输出要删除的学生编号：")
    db.delete("students",f"studentNo = '{stu_num}'")




