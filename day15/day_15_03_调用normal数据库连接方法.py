# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_15_03_调用normal数据库连接方法.py
@time: 2022/9/29 11:33
"""

from mysql_normal import Database


config = {
     "host": '49.233.39.160',
     "port": 3306,
     "database":"lebostudent",
     "charset":"utf8",
     "user":'lebostudent',
     "passwd":"lebo@22334455"
}

db = Database(**config)
select_one = db.select_one("scores")