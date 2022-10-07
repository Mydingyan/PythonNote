# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_15_03_调用normal数据库连接方法.py
@time: 2022/9/29 11:33
"""

from mysql_normal import Database





config = {
    "host": "49.233.39.160",
    "port": 3306,
    "database": "lebostudent",
    "charset": "utf8",
    "user": "lebostudent",
    "passwd": "lebo@22334455"
}

db = Database(**config)   ## 配置参数与类脱离

# 查询
# select_one = db.select_one("students")
# select_one = db.select_one("students","age>20")  #有查询条件
# print(select_one)


# # 新增
# value = ("('049','修改字段','女','北京',20,'1班','340322199001247677')")
# db.insert("students",value)

# 修改
db.update("students",{"card":"‘340322199001247688’"},"name = ‘修改字段’")     # 执行报错，后期跟进优化  (1054, "Unknown column '‘修改字段’' in 'where clause'")  （视频第60讲）

