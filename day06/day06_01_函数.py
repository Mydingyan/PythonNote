# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day06_01_函数.py
@time: 2022/8/30 23:43
"""


# 函数语法格式
'''
def：表示关键字
function_name()：标识符，起名字用的，可以给变量、函数、类、对象起名字  ()也是必须的，可以为空
page:参数

def function_name(para):
    stataments（执行语句，可以有多行）
    
'''

# 函数案例  (如果没有调用，函数是不会执行的）
def print_msg():
    print("print 函数内部代码")

# print_msg()   #写函数名就可以调用函数，调用才会执行函数


## 函数的嵌套（方法中调用方法）
def pritn_int():
    print(str(99))
    print_msg()

pritn_int()
#print(pritn_int())   # None

'''
两个函数之间，不能相互调用
普通函数自己，不要调用自己

def function_name(para):
    statistics
    return 结果

function_name()

'''

# return语句

print("=====摄氏度转换为华氏度=====")
def converter999(c):  #c 形式参数
    f = c * 9/5 +32
    #返回结果
    return str(f) + "F"

ff = converter999(1111)
print("转换后的华氏度为:",ff)

# 角分计算器
def ceshi(a):
    j = a * 10  #转换角
    f = a * 100  #转换分
    return str(j) + "角", str(f) +"分"

aa = ceshi(10)
print("aa的值是：",aa)

#按照从大到小顺序排列两个数字
#函数可以又多个return
#一旦运行了return，那么函数代码就结束了
def a(x=5,y=5):
    print("x = ",x,"y = ",y)
    if x >y:
        return x,y
    else:
        return y,x
    print("a的最后一行")

res = a(11150,1111130)
res_max = res[0]
res_min = res[1]

print(res)
print(type(res))
print("大树是:",res_max,"小数是",res_min)


# 列表的方法取最大值和最小值
l_sort = [2,3,4,5,666,66666,777,333]
print(l_sort)
l_sort.sort()   #从小到大排序函数
print(l_sort)
print(l_sort[-1])  #取最后一位最大值
print(l_sort[0]) # 取第一位最小值

# 函数参数的传递
# 1 位置参数：不能不传
# res = a()

# 不能少传 ：
# res = a(3)

#不能多传
# res = a(3,5,6)

#位置不能错，一个萝卜一个坑


# 2 默认参数
res = a()
print("默认参数，不传",res)  #  不传值时，取默认参数

res = a(3)
print("默认参数，不传",res) # 只传一个值时，默认给小的一位
res = a(7)
print("默认参数，不传",res)  #
