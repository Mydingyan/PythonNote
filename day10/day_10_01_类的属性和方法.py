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
    def draw_picture(self):   #方法 （函数）
        print("draw a picture")
    def draw_video(self):  #方法
        print("make a video")


# 实例化
art_wang = ArtDesigner()
art_li = ArtDesigner()

art_li.draw_picture()

# 类的属性
# 1 类属性的访问
# 类属性可以直接访问，无需实例化
print("=====类属性调用方法一：类名.属性  不会被修改")
print("类属性Post无需实例化也可以访问:",ArtDesigner.post)  # 美工  类属性修改

# 类属性也可以通过实例来访问
print("=====类属性调用方法二：实例名.属性  会被修改")
print("实例属性post也可以通过实例来访问:",art_wang.post)  #  美工

# 实际上，所有的实例，是 共享 类属性的。   （我的理解为多对一的关系， 所有人（实例）都在黑板上写相同的名字）

print("类属性的修改方法一：类名.属性  会修改所有实例化出来的对象")
# 类属性的修改   会修改所有实例化出来的实例（对象）
ArtDesigner.post = '美工部'
print("修改后类属性Post无需实例化也可以访问:",ArtDesigner.post)  #美工部
print("修改后实例属性post也可以通过实例来访问:",art_wang.post)   #美工部
print("修改后实例属性post也可以通过实例来访问:",art_li.post)     #美工部


print("类属性的新增方法一：实例化.属性  可以理解为新增了同名的一个实例化属性，并不能修改原来的值")
# 增加实例的属性案例一       （实例属性第一次赋值并不是修改类属性，而是增加了一个同名的实例属性，不会影响其他实例的同名属性）
art_wang.salary = 7000
print("修改后类属性salary无需实例化也可以访问:",ArtDesigner.salary)  #5000
print("修改后实例属性salary也可以通过实例来访问:",art_wang.salary)   #7000
print("修改后实例属性salary也可以通过实例来访问:",art_li.salary)     #5000


# 增加实例的属性案例一    （第一次新增并赋值属性，属于新增）
art_wang.salary_wang = 8000
print("类属性ArtDesigner.salary无需实例化也可以访问:",ArtDesigner.salary)  #5000  ，为对象中原本的属性
print("实例属性art_wang.salary也可以通过实例来访问:",art_wang.salary)   #7000   # 为对象中新增的属性
print("实例属性art_wang.salary_wang也可以通过实例来访问:",art_wang.salary_wang)   #8000  ,为实例中新增加的属性
print("实例属性art_li.salary也可以通过实例来访问:",art_li.salary)   #5000  为对象中实例化的属性


# 修改实例属性    （第二次赋值，可以理解为继续为art_wang.salary = 7000重新赋值，所以算修改实例属性，就类似局部变量重新赋值  = = ）
art_wang.salary_wang = 9000
print("类属性ArtDesigner.salary无需实例化也可以访问:",ArtDesigner.salary)  #5000  ，为对象中原本的属性
print("实例属性art_wang.salary也可以通过实例来访问:",art_wang.salary)   #7000   # 为对象中新增的属性
print("实例属性art_wang.salary_wang也可以通过实例来访问:",art_wang.salary_wang)   #8000  ,为实例中新增加的属性
print("实例属性art_li.salary也可以通过实例来访问:",art_li.salary)   #5000  为对象中实例化的属性


# 类属性的增加   增加后，无论是类属性直接访问，还是
ArtDesigner.company = "荣耀工作室"
print("======类属性的增加  类方法.属性   新增company属性 =====")
print("类属性增加compay的访问:",ArtDesigner.company)  #类属性直接访问
print("类属性增加compay的访问:",art_wang.company)  # 实例化方法来访问
print("类属性增加compay的访问:",art_li.company)    # 实例化方法来访问


# 总结：
# 如果实例 不具有此属性，就是新增
# 如果实例 具有此属性，就是修改

# 新知识点：初始化方法
print("=====实例的修改（重新赋值）=====")
# 真正的实例修改  （用init 初始化方法来创建）
class ArtDesigner():
    post = '美工'  #类属性
    salary = 5000  #类属性

    # 使用初始化init方法来创建  实例属性
    # 在实例化时，自动运行
    def __init__(self,name88):
        print(f"在实例化{name88}时，自动运行...")
        self.name = name88   #name是变量名    self 表示会增加一个属性，可以是任意值

    def draw_picture(self):   #方法 （函数）
        print("draw a picture")
    def draw_video(self):  #方法
        print("make a video")

print("=====实例属性的修改（重新赋值）=====")
art_wang = ArtDesigner("王富贵")
art_li = ArtDesigner("李富荣")    #实例化对象并重新赋值

print("art_wang 的 name 属性:",art_wang.name)  #查看类的属性
print("art_li 的 name 属性:",art_li.name)

print("=====实例属性的新增=====")
print("动态增加 wang_salary")
art_wang.wang_salary = 8888  #具体给某一个赋值
print("这是新增的属性 wang_salary",art_wang.wang_salary)  # 8888  wang_salary属性只赋给art_wang实例
# print("这是新增的属性 art_li",art_li.wang_salary)  #AttributeError报错，并没有新增art_li的属性



print("=====增加实例属性======")
art_wang.salary = 5555
print("类属性ArtDesigner.salary:",ArtDesigner.salary)  #5000
print("实例属性art_wang.salary:",art_wang.salary)       #5555   # 这个增加了实例属性
print("类属性art_wang.salary也可以通过实例来访问:",art_li.salary)  #这个没有增加实例属性，还是用的类属性，所以还是属于类属性


# 新只是： 类方法调用函数
# 类方法 未实例化事前，不能被调用
# ArtDesigner.draw_picture()  #报错，TypeError

# 类方法可以返回值

res = art_wang.draw_picture()
print(type(res))


# 类方法重写   类里面主要存的都是指针
def draw_pictur(self):
    print("我不会画图，买一张去")

ArtDesigner.draw_picture = draw_pictur
art_wang.draw_picture()