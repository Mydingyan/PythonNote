# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day07_01_拆包.py
@time: 2022/9/1 18:45
"""

'''
拆包：
解压序列（元组、列表、字典），分别赋值给多个变量

个人注释： 可以用于接口参数化、参数传递、读取外部文件
'''

## 获取变量的原始方法
pack = (1,5)
a = pack[0]
b = pack[1]
print("获取ab变量值的原始方法：",a,b)

#新获取变量的方法
#拆包的过程

print("=====拆包的方法1：元组拆包=====")
pack = (1,5)
apple = 1,6,6,7,8,9  #不加括号的元组，也可以拆包
liebiao = [412,"adffs",'fdsfa']

a,b = pack
a,b,c,d,e,f = apple  #等号后的变量名称一一对应即可  ，元组中有多少变量，也要声明多有变量
print("a的值：",str(a)+"。b的值：",b)
print("a,b,c,e,d,f的值：",a,b,c,d,e,f)

print("=====拆包的方法1：列表拆包=====")
# 列表拆包
aa,bb,cc = liebiao
print("列表的拆包:",aa,bb,cc)


print("=====拆包的方法1：字典拆包=====")
dic = {"user":"abc123",
     "pwd":"123456",
     "level":8}
a,b,c = dic
print("字典的拆包",a,b,c)   #拆出的是字典的Key


# 已拆包的形式，给多个变量赋值
print("=====元组拆包方法2：已拆包的形式，给多个变量赋值=====")
a,b,c = 5,6,7
print("a:",a,"   b:",b,"    c:",c)


## 通过return返回多个值的函数进行拆包
print("=====元组、列表拆包方法3：回多个值的函数进行拆包=====")
def get_my_info():
    high = 178
    weight = 100
    age =18
    return high,weight,age   #返回的多个值是元组
    #return [high,weight,age]   #中括号括起来就是列表


#res = get_my_info()
h,w,a = get_my_info()   #通过方法2得知，可以给多个变量进行赋值，元组正好可以直接赋值
#print(type(res))
print(h,w,a)


print("=====字典拆包方法3：回多个值的函数进行拆包=====")
def get_my_info():
    r = {
    'high' : 178,
    'weight' : 100,
    'age' : 18
    }

    # eturn r   #拆出来key
    return r.values()  # 拆出来的是值

h,w,a = get_my_info()
print(h,w,a)




# 新知识点：通配符
print("=====通配符： 格式：*字符串,字符串（可以为多个）=====")
order = ("computer",2,8000,(2022,4,10))

print("=====通配符标准格式：方式一=====")
*_,date_str = order    # 标准格式，可以把元组中的日期拆出来
print("拆出来的是元组日期：",date_str)  # 拆出来元组中的日期

print("=====通配符标准格式：方式二=====")
*head,date_str = order
print("head方法中拆出来的值：",head)  # 拆出来元组中的日期

print("=====通配符标准格式：方式三=====")
*head,price,date_str = order
print("拆出来的是价格：",head)  # 拆出8000

print("=====通配符标准格式：方式四(星号是必须的）=====")
name,*lost,price,date_str = order    #四个元素位置必须对应（类似不定长参数）
print("拆除剩下的参数：",lost)  # 拆除剩下的参数


# 不定长参数中，







# name,*lost,price,date_str = order

# print(type(order))   #元组
#
#
# # 位置必须对应
# name,*lost,date_str,price = order
#
# # 不定长参数中 可变参数 必须放在最后
#
# print("name",name)
# print("price:",price)
# print("date_str",date_str)



