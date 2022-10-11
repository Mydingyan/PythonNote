# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: insert_student.py
@time: 2022/10/7 13:18
"""

from day16.database.mysql_normal import db


# def insert_student():
#     stu_num = db.get_new_studentNo()
#     card = db.get_new_card()
#     name = input("请输出学生姓名:")
#     gender = input("请输出学生性别：")
#     hometown = input("请输入籍贯：")
#     age = input("请输入年龄：")
#     class_name = input("请输出班级编号") + "班"
#
#     stu = {
#         "studentNo":f"{stu_num}",
#         "name":f"'{name}'",
#         "sex":f"'{gender}'",
#         "hometown":f"'{hometown}'",
#         "age":f"{age}",
#         "class":f"'{class_name}'",
#         "card":f"'{card}'"
#     }
#     stustr = f"({stu_num},'{name}','{gender}','{hometown}',{age},'{class_name}',{card})"
#     db.insert('students',stustr)

def insert_student():
    stu_num = db.get_new_studentNo()
    card = db.get_new_card()
    name = input("请输入学生姓名:")
    gender = input("请输入学生性别:")
    hometown = input("请输入籍贯:")
    age = input("请输入年龄:")
    class_name = input("请输入班级编号") + "班"

    stu = {
        "studentNo": f"{stu_num}",
        "name": f"'{name}'",
        "sex": f"'{gender}'",
        "hometown": f"'{hometown}'",
        "age": f"{age}",
        "class": f"'{class_name}'",
        "card": f"'{card}'"
    }
    db.insert_dic("students",stu)

    # stustr=F"({stu_num},'{name}','{gender}','{hometown}',{age},'{class_name}',{card})"
    # db.insert("students",stustr)
