# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day05_01.py
@time: 2022/8/29 17:04
"""


'''
元祖定义及进阶操作操作
1. 不同数据类型,使用 元祖.      相似数据类型 ,使用列表
2. 元祖的 遍历,比列表 快
3. 常量,可以放在 元祖中. 

'''

# 创建元组
my_type = ()
print(type(my_type))
print(my_type)  # 输出空()

# 只有一个元素的元组，后面需要加逗号，否则就是字符串格式
print('=====元组特殊情况：一个元素的元组，后面需要加一个逗号，否则就是字符串格式的')
my_type = ("王者",)
print(type(my_type))    # <class 'str'>
print(my_type)

my_t1 = (1,2,3,4,5)
my_t2 = (1,'啦啦啦啦',[1,2,3,4,5],('python',12,['自动化']))
print("my_t1:",my_t1)
print("my_t2:",my_t2)

# 元祖打包，不输入括号，默认输出的元组格式
my_t3 = "python",1,2,3,[1,2,3],("python",3213,'自动化')
print(my_t3)

# 访问元祖元素
print("访问元祖元素",my_t3[2])
# 必须用 int
# print("访问元祖元素",my_t3[2.0])  #元组的索引只能为整形，使用浮点会报错
print("访问元祖嵌套元素",my_t3[4][2])
print("负数索引访问元祖元素",my_t3[-2][-1])  #负数取列表中的数还是按右开始

#元组切片
print("元组切片",my_t3[1:5])  #左包右开，右边的5不取数
print("元组切片",my_t3[1:5][1:5])  #意思是先取数，然后从取出的数中中切片

ind = 1
print("元组引用单个元素，是切片的一种简写",my_t3[ind])  # 相当于设置变量的效果，切片中一个数字只引用一个元素，切出来的结果为索引值本身，不再是列表
print("元组设置变量引用",my_t3[ind:ind+1])    #这二种方式取出来的值与上一种值的区别是，这个值为元组


#元组的更改
print('=====元组中元素不可删除或修改，只能删除元组=====')

# my_t3[1] = "fix"   #报错  TypeError: 'tuple' object does not support item assignment
print("元组任意数值都不可更改")

# 删除元组元素（不支持）
# del my_t3[1]
print(my_t3)   #TypeError: 'tuple' object doesn't support item deletion

# del my_t3  # 可以删除元组，不能删除元组中的元素
print(my_t3)   #删除后，找不到变量  NameError: name 'my_t3' is not defined    元组可能会存储整篇文章，如果不销毁会占用较大内存


# 元组的方法
print('=====元组的方法：案例=====')

my_t4 = ('l','e','a','b','c','d','www')
print("my_t4元素个数",len(my_t4))     # 计算元组中元素的个数
print("'my_t4'元素个数",len("my_t4"))  #len函数,使用引号后，计算括号中的元素个数
print(my_t4.count('b'))  #count 计数方法，计算b在元组中的个数

# 查找字符串起始索引值（找不到控制台报错）
print(my_t4.index('www'))   #ValueError: 'wwww' is not in list

print('======注释======')
#index与if此方法相同,相当于省写
if "www" in my_t4:
    print(my_t4.index("www"))  #a存在元组中，返回起始索引值2
else:
    print('"sss" not in my_t4')


# 元组的遍历
for ball in my_t4:
    print("遍历元组中的元素:",ball)   #元组是可迭代对象

for ball in "123456789":
    print("遍历字符串中的元素:",ball)  #字符串也是可迭代对象


a = ["10","12","14","16","18",]
print('a的长度',len(a))     #字符串列表也是可迭代对象

for ball in ["10",'12','14','16','18']:
    print("遍历列表中的元素:",ball)

print("列表推导式",["元组字符是:"+ x for x in ('l','o','v','e','y','o','u')])   #只有列表推导式，没有元组推导式
print("元组推导式",("元组字符是:"+ x for x in ('l','o','v','e','y','o','u')))  #输出<generator object <genexpr> at 0x000001CB2CA28AC0>

# 元组取最大值和最小值（可以判定数字、字母）
my_t5 = (-10,2,-30,4,5555,666667)
print("max:",max(my_t5))
print("min:",min(my_t5))

print("max:",max(my_t4))
print("min:",min(my_t4))


# 元组内的可变元素
print('=====元组内只能修改元组中的可变的元素（比如列表，修改后元组的内存地址不变），但不能修改元组内的值======')
my_t6 = ('loveme',[1,2,3,4,5],("python",'345','自动化'))
# my_t6[1] = [1,2,3]   #  修改元组的元素会报错，（元祖的元素不可改变） TypeError: 'tuple' object does not support item assignment

print('=====案例一：元组内元素不可改变，但元素中的列表可以修改======')
print("修改之前的列表地址",id(my_t6[1]))
my_t6[1][2] = 'fix'    #元组中的值不可修改，但元组中的列表可以修改
print("修改后的 列表 地址",id(my_t6[1]))   # 修改后的元组，内存地址不变
print("元组内的可变元素",my_t6)

print('=====案例二：元组内元素不可删除案例======')
my_t6 = ('loveme',[1,2,3,4,5],("python",'345','自动化'))
after_pop = my_t6[1].pop   #.pop表示删除最后一个元素      产生了新的列表，而元组记录的是原来的列表
print("after_pop:删除后",after_pop)
print("元组内的可变元素",my_t6)    # 删除前与删除后无变化，内存地址也无变化
print("after_pop:",after_pop)


# 元组定义及进阶操作
# 1. 不同数据类型使用元组， 相似数据类型使用列表
# 2. 元组的遍历速度比列表快
# 3. 常量，可以放在元组中


