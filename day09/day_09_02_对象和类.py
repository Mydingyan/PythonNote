# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_09_02_对象和类.py
@time: 2022/9/5 16:49
"""

'''
# 面向对象和类
# 把一系列相关的 变量 和 函数，卸载一起，进行封装  ---类
# 供其他代码使用，这就是面对对象的思路

# 变量  -- 属性
# 函数 -- 方法

# 三大特性： 封装、继承、多态
'''

# 类和对象举例：

'''
# 对象指的是具体的一个场景

水果 -- 类
苹果 -- 类
红苹果 -- 类
红富士苹果 --类
我上周唯一的那个苹果  --对象

造飞机
图纸  -- 类
做出来的每一架飞机 --对象

够 --- 类
黄狗 -- 类
我加的那只黄狗 --对象
'''



# 类实例化之后，生成的对象
# 关键字 class
# 类的名字（必须有，大驼峰命名法）
# 属性(可以有,下划线命名法）
# 方法(可以有，下划线命名法）


# 美工类
# 封装
class ArtDesigner():
    salary =5000 #类属性
    department = '设计部'  #类属性

    # 类方法
    def draw_picture(self):
        print("画一张图")
'''
# 创建对象，实例化对象

# 对象1 = 类名()
# 对象2 = 类名()
# 对象3 = 类名()

#在Python中，一切皆为对象

数据类型也是 对象
函数        也是对象
列表        也是对象.
'''

# 实例化对象
# 美工 小王
art_wang = ArtDesigner()  # 实例化对象才能调用
print(type(art_wang))
print(id(art_wang))
# 应用对象属性
# print(art_wang.salary)
# print(art_wang.department)

#调用对象的方法
art_wang.draw_picture()


# 美工 小李
art_li = ArtDesigner()
print(type(art_li))
print(id(art_li))
print(art_li.salary)
print(art_li.department)


# 美工 小孙
art_sun = ArtDesigner()
print(type(art_sun))
print(id(art_sun))
print(art_sun.salary)  # 5000
print(art_sun.department)  #设计部
#调用对象的方法
art_sun.draw_picture()
print(type(art_sun.salary))
print(id(art_sun.salary))
print(type(art_sun.draw_picture()))
print(id(art_sun.draw_picture()))


# 测试工程师类
# 封装
class TestEngineer():
    salary = 9000
    department = "测试部"
    def write_testcase(self):
        print("writer testcase")
    def run_testcase(self):
        print("run testcase")


#1.实例化对象（对象必须先实例化才能调用属性或者方法）
test_wang = TestEngineer()

# 2.引用对象的属性
print(test_wang.salary)  #对象的属性
print(test_wang.department)  #对象的属性

# 3.调用对象的方法
test_wang.write_testcase()
test_wang.run_testcase()
