# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: select_student.py
@time: 2022/10/7 13:18
"""

from day16.database.mysql_normal import db   # day16.可以在外部调用

def select_all_student():
    all = db.select_all("students","age >0 ")
    for one_s in all:
        print(one_s)


def select_class_student():  # 按班级查询
    class_stu = input("请输入要查询的班级编号:")
    all = db.select_all("students",f"class = '{class_stu}班'")
    if all:
        for one_s in all:
            print(one_s)
    else:
        print(f"没查到{class_stu}班的学生")

def select_student_name():  # 按姓名查
    name = input("请输入要查询的姓名:")
    stu = db.select_all("students",f"name = '{name}'")
    if stu:
        for one_s in stu:
            print(one_s)
    else:
        print(f"未查到{name}的信息")


def select_studentNo():  # 按学号查
    sty_no = input("请输入要查询的学号:")
    stu = db.select_one("students",f"studentNo = '{sty_no}'")
    if stu:   #打印单行数据
        print(stu)
    else:
        print(f"没查到{sty_no}学号的学生")
