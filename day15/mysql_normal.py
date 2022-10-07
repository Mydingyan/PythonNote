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
    def __init__(self,**config):
        try:
            self.__conn = pymysql.connect(**config)
            self.__cursor = self.__conn.cursor()

        except Exception as e:
            print("数据库连接失败\n",e)


    # # 参数：表名 和条件
    # 查询
    def select_one(self,table,factor_str='',field="*"):
        if factor_str=='':
            sql = f"select {field} from {table} "
        else:
            sql = f"select {field} from {table}  where  {factor_str}  "

        self.__cursor.execute(sql)
        return self.__cursor.fetchone()

    # 插入数据
    def insert(self,table,val):
        sql = f'insert into {table} values {val}'
        try:
            self.__cursor.execute(sql)
            self.__conn.commit()
            print("插入成功！")
        except Exception as e:
            self.__conn.rollback()
            print("插入失败",e)


    # 修改数据
    #参数: table, set值的字典
    # def update(self,table,val_obj,tange_str):
    #
    #     sql = f'update {table} set'
    #     for key,val in val_obj.items():
    #         sql += f" {key} = {val},"
    #
    #     sql = sql[:-1] + "where" + tange_str  #从最左边到最后一个的前面，目的是为了切掉最后一个逗号
    #     try:
    #         self.__cursor.execute(sql)
    #         self.__conn.commit()
    #         print("修改成功！")
    #     except Exception as e:
    #         self.__conn.rollback()
    #         print("修改失败",e)


    def update(self,table,val_obj,tange_str):
        sql = f"update {table} set "
        for key,val in val_obj.items():
            sql += f" {key} = {val},"
        sql_head = sql[:-1]
        sql_f =sql_head + " where " + tange_str
        try:
            self.__cursor.execute(sql_f)
            self.__conn.commit()
            print("修改成功")
        except Exception as e:
            self.__conn.rollback()
            print("修改失败\n",e)
