# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_10_01_common.py.py
@time: 2022/9/8 22:50
"""


class ShopUser():

    '''
    类名：ShopUser
    说明：用户类
    初始化参数：用户名，密码     使用print(user_1.__doc__) 方法，获取此说明
    '''

    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password

    '''
    这里也是注释
    '''

    def login(self):
        if self.password == "123456":
            print("合法用户")
        else:
            print("非法用户")

    # 打印 该对象用来给用户的提示信息
    def __str__(self):
        return "我是一个用户类"

    def __del__(self):   #删除方法
        print("对象被删除，做收尾动作")




# __name__
print("day10.day_10_01_common.py中的值",__name__)   #本文件运行，获得__main__



if __name__ == "__main__":
    print('if __name__ = "__main__"":  之后的代码')