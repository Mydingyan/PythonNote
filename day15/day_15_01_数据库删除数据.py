# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_15_01_数据库删除数据.py
@time: 2022/9/28 17:08
"""


# 删除数据
import pymysql

def mysql_db():
    try:
        con = pymysql.connect(    # 1.连接数据库
            host = '49.233.39.160',
            port = 3306,
            database= "lebostudent",
            charset="utf8",
            user = 'lebostudent',
            passwd="lebo@22334455"
        )
        with con.cursor() as cursor:   #游标

            sql = f"delete from students where studentNo  = '032'"   #2、准备SQL语句（增删改查都可以）
            cursor.execute(sql)  #执行SQL语句

            # 提交SQL
            con.commit()
            print("数据删除成功")                 #疑问：delete删除0行时，如何抛出异常

    except Exception as e:    #3、抛出异常
        # 回滚到上次commit的地方
        con.rollback()
        print("数据库操作异常\n",e)

    finally:
        con.close()  # 4、关闭数据库链接



if __name__ == '__main__':
    mysql_db()