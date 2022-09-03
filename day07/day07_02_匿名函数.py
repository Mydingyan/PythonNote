# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day07_02_匿名函数.py
@time: 2022/9/2 23:06
"""


# # 匿名函数
# def add(x,y):
#     return x + y
#
# print(add(100,200))

# 简单写法的匿名函数
# def add(x,y): return x + y
# print(add(100,200))

print("=====lambda函数（匿名函数的方法）======")
# 匿名函数语法(也叫lambda函数）
# lambda:x,y:x + y    #lambda代替了def 、return两个函数

"""
匿名函数的调用方法：
1.创建一个匿名函数
2.使用一个变量，来保存这个匿名函数
3.通过这个变量，来调用匿名函数
"""

l_1 = lambda x,y:x+y
print(l_1(500,611))

l_2 = lambda x,y:(x+y,x-y)
xsy,xpy = l_2(500,1000)
print(xsy)



# 匿名函数的作用：作为高阶函数的参数
# 高阶函数：就是以函数为参数的函数  （可以理解为函数套娃）
# 使用格式： 函数名（匿名函数，其他参数）：
# 或者 函数名（其他参数，匿名函数）：


# 匿名函数在 列表推导式中的应用
print("=====匿名函数案例=====")
f = lambda x: x * 1000

list_l =  [ f(i) for i in range(10)]   #f(i)表示在函数中调用函数， 例如range取值为1时，i =1 ,f(i) = i*1000=1000
print(list_l)


print("=====lambda（过滤函数）的应用=====")
# python中 内置filter 函数中的应用: max() ,min(),len()
# filter 函数中的应用（过滤函数）
# filter 可以用在复杂函数中
list_2 = [1,2,3,4,5,6,7,8]
res_2 = list(filter(lambda x : x%2 == 0 ,list_2))   #（用什么函数过滤或者过滤方法，对谁进行过滤）   x%2 == 0 %表示取余，偶数%2 = 0

print(type(res_2))  #函数返回为filter类型
print(res_2)   #直接输出为内存地址,需要在filter外加一层强制转换列表函数


print("=====map函数的应用=====")
# map 函数的应用
# 使用Lambda拼接字符串，必须要用map函数
list_3 = [1,2,3,4,5,6]
res_3 = list(map(lambda x : "元素是：" + str(x),list_3))
print(res_3)
