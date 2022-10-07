#!/usr/bin/python
# coding=utf-8

import pymysql
# import yaml
# pip3 install pyyaml

class MysqlDatabase():
    connected = False

    def __init__(self, **conf):
        try:
            self.__conn = pymysql.connect(**conf)
            self.connected = True
        except Exception as e:
            print("数据库连接失败:\n", e)

    def get_new_studentNo(self):
        sql = "select max(studentNo) from class"
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
                return cursor.fetchone()[0] + 1

        except Exception as e:
            print("get_new_studentNo 失败:\n", e)

    def get_new_card(self):
        sql = "select max(card) from class"
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
                card = cursor.fetchone()
                new_card = str( int(card[0]) + 1 )
                return  new_card

        except Exception as e:
            print("get_new_card 失败:\n", e)

    def select_one(self, table, filter_str, field=" * "):
        sql = f"select {field} from {table} where {filter_str}"
        try:
            with self.__conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(sql)
                return cursor.fetchone()
        except Exception as e:
            print("select_one 失败:\n", e)

    def select_all(self, table, filter_str, field=" * "):
        sql = f"select {field} from {table} where {filter_str}"
        try:
            with self.__conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(sql)
                return cursor.fetchall()
        except Exception as e:
            print("select_all 失败:\n", e)

    def insert(self, table, val):
        sql = f"insert into {table} values {val}  "
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
            self.__conn.commit()
            print("insert success")

        except Exception as e:
            self.__conn.rollback()
            print("insert 失败:\n", e)

    def insert_dic(self, table, val_dic):

        str_val = ''
        for val in val_dic.values():
            str_val = str_val + "'" + val + "',"

        sql = f"insert into {table} values ({str_val[0:-1]})"

        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
            self.__conn.commit()
            print("insert success")

        except Exception as e:
            self.__conn.rollback()
            print("insert 失败:\n", e)

    def delete(self, table, filter_str):
        sql = f"delete from {table} where {filter_str}  "
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
            self.__conn.commit()
            print("delete success")

        except Exception as e:
            self.__conn.rollback()
            print("delete 失败:\n", e)

    def update(self,table,filter_str,key_val):
        str_val = ''
        for key,val in key_val.items():
            str_val = f" {key} = {val} "

        sql = f"update {table} set {str_val} where {filter_str} "
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
            self.__conn.commit()
            print("update success")

        except Exception as e:
            self.__conn.rollback()
            print("update 失败:\n", e)

    def get_new_card(self):
        sql = "select max(card) from class"
        cursor = self.__conn.cursor()
        cursor.execute(sql)
        card = cursor.fetchone()
        new_card = str(int(card[0])+1)
        return new_card

    def get_new_studentNo(self):
        sql = "select max(studentNo) from class"
        cursor = self.__conn.cursor()
        cursor.execute(sql)
        studentNo = cursor.fetchone()
        new_studentNo = str(int(studentNo[0]) + 1)
        return new_studentNo



    def __del__(self):
        self.__conn.close()



config = {
    "host": '49.233.39.160',
    "port": 3306,
    "database": "lebostudent",
    "charset": "utf8",
    "user": "lebostudent",
    "passwd": "lebo@22334455"
}

db = MysqlDatabase(**config)

'''
yaml_file = "../config/DbConfig.yaml"

with open(yaml_file,'r') as f:
    cfg = yaml.safe_load(f)
    print(cfg["mysql_lebo"]["config"])

db = MysqlDatabase(**cfg["mysql_lebo"]["config"])

'''
