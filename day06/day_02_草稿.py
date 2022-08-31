# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_02_草稿.py
@time: 2022/8/31 23:38
"""


### 两个数值大小排列
#同一个函数可以有多个return，一旦运行return，那么函数的代码就结束了

def a(x,y):
    if x<y:
        return  x,y   #返回的时候其实是元组，只是元组可以不用加括号（PYthon能省则省）
    else:
        return  y,x

res = a(1,10)
res_max = res[0]    #从元组中取数
res_min = res[1]
print(res)
print(type(res))  #元素类型
print("大数值是",res_max,"小数是",res_min)


# 列表排序
l_sort = [2,3,4,53,45,46,5,75,86,9,69,69,634,523,523,5,235,23,5353535]
l_sort.sort()  #sort函数，对列表从小到大排列
print(l_sort)
print("列表中最小的数是:",l_sort[0],"列表中最大是数是:",l_sort[-1])