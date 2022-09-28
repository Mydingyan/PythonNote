# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_15_01_数据库插入数据.py
@time: 2022/9/27 14:46
"""

# 插入数据（单行）
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

            # 插入1条数据
            # value = "('030','王昭君','女','北京',20,'1班','340322199001247654')"

            # 插入多条数据
            value = '''
            ('023','王昭君1','女','北京',20,'1班','340322199001247654'),
            ('024','后裔','女','北京',20,'2班','340322199001247655'),
            ('025','妲己','女','北京',20,'3班','340322199001247656'),
            ('026','凯','男','广州',20,'4班','340322199001247657')
            '''
            sql = f"insert into students value {value}"   #2、准备SQL语句（增删改查都可以）
            cursor.execute(sql)  #执行SQL语句

            # 提交SQL
            con.commit()
            print("数据插入成功")

    except Exception as e:    #3、抛出异常
        # 回滚到上次commit的地方
        con.rollback()
        print("数据库操作异常\n",e)

    finally:
        con.close()  # 4、关闭数据库链接



if __name__ == '__main__':
    mysql_db()
