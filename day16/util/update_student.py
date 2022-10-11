# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: update_student.py
@time: 2022/10/7 13:18
"""
from day16.database.mysql_normal import db


def update_class():
    stu_num = input("请输入要修改的学生学号：")
    class_num = input("请输入要调换班级的编号：")
    set_dic = {
        "class":f"'{class_num}班'"
    }
    db.update("students",f"studentNo='{stu_num}'",set_dic)

def update_card():
    stu_num = input("请输出要修改的学生学号：")
    card_num = input("请输入要调换的卡号：")
    set_dic = {
        "card":f"'{card_num}'"
    }
    db.update("students",f"studentNo='{stu_num}'",set_dic)