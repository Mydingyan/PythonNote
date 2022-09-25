# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_15_01_mysql访问数据库.py
@time: 2022/9/25 18:04
"""


'''

Python 访问MySQL数据库
pip install pymysql

① 创建链接 ②获取游标 ③执行SQL  ④关闭游标 ⑤关闭链接
'''
import pymysql

def mysql_db():
    con = pymysql.connect(
        host = '49.233.39.160',
        port = 3306,
        database= "lebostudent",
        charset="utf-8",
        user = 'lebostudent',
        password="lebo@22334455"
    )

if __name__ == "__main__":
    mysql_db()

