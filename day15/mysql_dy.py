# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: mysql_dy.py
@time: 2022/9/28 22:11
"""


'''
封装一个mysql工具类

功能:
mysql数据库操作


步骤:
1.连接数据库
2.通过连接对象,获取游标对象
3.增删改查具体操作


方法:
查
1.直接运行

增删改
2.commit/rullback



'''
import pymysql

# 连接参数
config = {
     "host": '49.233.39.160',
     "port": 3306,
     "database":"lebostudent",
     "charset":"utf8",
     "user":'lebostudent',
     "passwd":"lebo@22334455"
}


class MysqlDb():
     #初始化方法
     def __init__(self):
          self.conn = self.get_conn()   #新建数据库连接初始化方法
          self.cursor = self.get_cursor()   #新增游标初始化方法

     #连接数据库的方法
     def get_conn(self):
          conn = pymysql.connect(**config)
          return conn

     #获取游标
     def get_cursor(self):
          cursor = self.conn.cursor()
          return  cursor


     # 查询方法

     def select_all(self,sql):
          self.cursor.execute(sql)
          return self.cursor.fetchall()


     def select_one(self,sql):
          self.cursor.execute(sql)
          return self.cursor.fetchone()

     def select_many(self, sql ,num):
          self.cursor.execute(sql)
          return self.cursor.fetchmany(num)


     # 增删改方法
     def commit_data(self,sql):
          try:
               self.cursor.execute(sql)
               self.conn.commit()
               print("提交成功")

          except:
               print("提交出错")
               self.conn.rollback()


     def __del__(self):
          self.cursor.close()
          self.conn.close()

