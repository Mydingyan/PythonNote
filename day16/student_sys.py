# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: student_sys.py
@time: 2022/10/7 12:56
"""


## 创建一个学生系统，要有一个总体的规划


# 菜单(print input两个功能)
from day16.util.delete_student import delete_name, delete_studentNo
from day16.util.insert_student import insert_student  #在函数上，按住ait+回车，可以直接导入
from day16.util.select_student import select_all_student, select_class_student, select_student_name, select_studentNo
from day16.util.update_student import update_class, update_card


# 打印菜单
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

        menu()  # 打印print菜单
        choice = int(input("请选择操作(0-9):"))

        if choice == 1:  #新增学生记录
            insert_student()

        elif choice == 2:  #列出所有学生
            select_all_student()

        elif choice == 3:  #按班级查询学生
            select_class_student()

        elif choice == 4:  #按姓名查询学生
            select_student_name()

        elif choice == 5:   #按学号查询学生
            select_studentNo()

        elif choice == 6:  #按姓名删除学生
            delete_name()

        elif choice == 7:  #按学号删除学生
            delete_studentNo()

        elif choice == 8:  #修改学生班级
            update_class()

        elif choice == 9:  #修改学生卡号
            update_card()

        elif choice == 0:
            exit()  #退出操作









        input("按任意键继续...")