# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: mysql_normal.py
@time: 2022/9/29 10:42
"""

# 相比mysql_dy ，这是更“正式”的MYSQL 连接方法
# 干货
import pymysql


class Database():   #Database表示连接任意数据库方法
    def __init__(self,config):
        try:
            self.__conn = pymysql.connect(**config)
            self.__cursor = self.__conn.cursor()

        except Exception as e:
            print("数据库连接失败\n",e)

    # # 参数：表名 和条件
    # def select_one(self,table,factor_str="",field="*"):
    #     if factor_str == " ":
    #         sql = f"select {field} from {table}"   #无条件查询
    #     else:
    #         sql = f"select {field} from {table} where {factor_str}"
    #
    #     self.__cursor.execute(sql)
    #     return self.__cursor.fetchone()

    def select_one(self,table,factor_str='',field="*"):
        if factor_str=='':
            sql = f"select {field} from {table} "
        else:
            sql = f"select {field} from {table}  where  {factor_str}  "

        self.__cursor.execute(sql)
        return self.__cursor.fetchone()

