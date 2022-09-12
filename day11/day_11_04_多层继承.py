# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_11_04_多层继承.py
@time: 2022/9/12 15:46
"""

# 多层继承(多重继承)

#父类
class Human():

    def __init__(self,name,age,gender):
        self.name= name
        self.age = age
        self.gender = gender

    def eat(self):
        print("i eat something")

    def run(self):
        print("i run away  --Human父函数")

    def work(self):
        print("do something get money")

# 员工子类
class Staff(Human):
    def __init__(self,name,age,gender,department,salary_dep):  #增加多个方法
        Human.__init__(Human,name,age,gender)  #显示调用父类方法    固定语法
        self.department = department
        self.salary_dep = salary_dep

    def come_to_work(self):
        print("我来上班了  --员工Staff子类")

# 个人薪资(新增美工属性)
class ArtDesigner(Staff):    # 继承Human

    def __init__(self,name,age,gender,department,salary_dep,salary):
        Staff.__init__(Staff,name,age,gender,department,salary_dep)
        #增加一个子类的实例属性
        self.salary = salary

    def draw_pictur(self):   #子类特有的"技能"
        print("draw a picture  --个人薪资类ArtDesigner")

    #相同名称,是重写父类方法  (这就是多态)
    def work(self):
        print("artdesgner's work is deaw a picture -artdesgner 的作品是一幅画 ")


# 测试部方法
class TestEngineer(Staff):
    # def work(self):
    #     print("run test")

    def run_test(self):
        print("run test")


# 初始化时需要传所有非私有属性值
one_test = TestEngineer("王大力",25,"male","测试部",8888)   # 私有属性不会继承,   从Staff中继承name,age,gender,department,salary_dep 5个属性
print("one_test.name:",one_test.name)

# 初始化
# name,age,gender,department,salary_dep,salary
one_art = ArtDesigner("小雅",26,"female","美工部",6000,6666)

print("one_art.name:",one_art.name)  #小雅   来自父类

print("one_art.department:",one_art.department)  #美工部     来自员工子类
print("one_art.salary_dep:",one_art.salary_dep)  #部门工资6000       来自员工子类

print("one_art.salary",one_art.salary)   #个人工资6666       来自个人薪资

# 实例化方法
one_art.come_to_work()   #我来上班了
one_art.work()




#新知识点:多重继承
class Master(ArtDesigner,TestEngineer):
    def __init__(self,name,age,gender,department,salary_dep,salary):
        ArtDesigner.__init__(ArtDesigner,name,age,gender,department,salary_dep,salary)   #salary是ArtDesigner的私有属性,TestEngineer不可直接使用
        TestEngineer.__init__(TestEngineer,name,age,gender,department,salary_dep)

# name,age,gender, department,salary_dep,salary

print("=====多重继承打印=======")
one_master = Master("多重继承",30,"male","乐博学院",10000,15000)   #多重函数初始化
print(one_master.name,one_master.department,one_master.salary_dep)

one_master.run_test()   # TestEngineer测试部子类方法
one_master.come_to_work()   #Staff员工子类
one_master.draw_pictur()   #  个人薪资子函数
one_master.run()   #调用Human父函数

