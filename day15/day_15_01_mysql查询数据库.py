# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_15_01_mysql查询数据库.py
@time: 2022/9/25 18:04
"""


'''

Python 访问MySQL数据库
pip install pymysql

① 创建链接 ②获取游标 ③执行SQL  ④关闭游标 ⑤关闭链接
'''
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
            sql = "select * from scores"   #2、准备SQL语句（增删改查都可以）
            cursor.execute(sql)  #执行SQL语句

            print("=====读取数据的三种方法======")
            print("=====方法一：datas:SQL中获取全部数据=====")
            # datas = cursor.fetchall()   #从cursor中获取SQL语句查询的全部数据
            # print("datas:SQL获取全部数据：\n",datas)     # 返回结果为元组类型 (每一行都是元组）

            # print("=====方法二：datas2:SQL中获取单行数据=====")
            # datas2 =cursor.fetchone()   #从SQL中取出一行数据（每读取一行，光标后移动一行，也就是再次使用语句时，会查询第二行数据）
            # print("datas2:SQL中获取单行数据",datas2)

            print("=====方法三：datas3:SQL中获取指定行数=====")
            datas3 = cursor.fetchmany(3)  #从SQL中取数指定行数数据
            print("datas3:SQL中获取指定行数数据",datas3)


    except Exception as e:    #3、抛出异常
        print("数据库操作异常\n",e)

    finally:
        con.close()  # 4、关闭数据库链接



if __name__ == '__main__':
    mysql_db()
