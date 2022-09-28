# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_15_02_调用连接数据库类.py
@time: 2022/9/28 22:30
"""

from mysql_dy import MysqlDb


# 连接数据库
my_db = MysqlDb()

# 查询
sql = "select * from scores;"
# select_data = lebo = my_db.select_all(sql)  #查询全部数据
# select_data = lebo = my_db.select_one(sql)   #查询一条数据
select_data = lebo = my_db.select_many(sql,5)   #查询5条数据

print(select_data)




# 增
# value = "('036', '王昭君', '女', '北京', 20, '1班', '340322199001247654')"
# sql = f"insert into students value {value}"
# my_db.commit_data(sql)
#
# # 删
# sql = f"delete from students where studentNo  = '031'"
# my_db.commit_data(sql)
# #
# # # 改
# sql = f"update students set name = '修改后王昭君33332' where studentNo  = 031"

# my_db.commit_data(sql)