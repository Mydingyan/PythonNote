# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_10_01_类的属性和方法.py
@time: 2022/9/5 19:44
"""

# 类的属性和方法
# 类的定义

class ArtDesigner():
    post = '美工'  #类属性
    salary = 5000  #类属性
    def draw_picture(self):   #方法
        print("draw a picture")
    def draw_video(self):  #方法
        print("make a video")



art_wang = ArtDesigner()
art_li = ArtDesigner()

art_li.draw_picture()

# 类的属性
# 1 类属性的访问

# 类属性可以直接访问，无需实例化
print("类属性Post的访问:",ArtDesigner.post)

# 类属性也可以通过实例来访问
print((""))