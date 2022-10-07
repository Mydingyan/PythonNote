# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: student_sys.py
@time: 2022/10/7 12:56
"""


## 创建一个学生系统，要有一个总体的规划



# 菜单(print input)


# 打印菜单
from day16.util.insert_student import insert_student
from day16.util.select_student import select_all_student


def menu():
    print("************主菜单*************")
    print("         1.新增学生记录")
    print("         2.列出所有学生")
    print("         3.按班级查询学生")
    print("         4.按姓名查询学生")
    print("         5.按学号查询学生")
    print("         6.按姓名删除学生")
    print("         7.按学号删除学生")
    print("         8.修改学生班级")
    print("         9.修改学生卡号")
    print("         0.退出系统")
    print("******************************")

if __name__ == '__main__':

    while True:

        menu()
        choice = int(input("请选择操作（0-9）："))

        if choice == 1:
            insert_student()

        elif choice ==2:
            select_all_student()

        elif choice ==3:


        elif choice == 3:





        else