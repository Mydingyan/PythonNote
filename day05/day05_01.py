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

my_type = ("王者")
print(type(my_type))
print(my_type)

my_t1 = (1,2,3,4,5)
my_t2 = (1,'啦啦啦啦',[1,2,3,4,5],('python',12,['自动化']))
print("my_t1:",my_t1)
print("my_t2:",my_t2)

# 元祖打包，默认输出元组格式
my_t3 = "python",1,2,3,[1,2,3],("python",3213,'自动化')
print(my_t3)

# 访问元祖元素
# print("访问元祖元素",my_t3[2])
# 必须用 int
# print("访问元祖元素",my_t3[2.0])  #使用浮点会报错
print("访问元祖嵌套元素",my_t3[4][2])
print("负数索引访问元祖元素",my_t3[-2][-1])  #负数取列表中的数还是按右开始

#元组切片
print("元组切片",my_t3[1:5])  #左包右开，右边的5不取数
print("元组切片",my_t3[1:5][1:5])  #意思是先取数，然后从取出的数中中切片

ind = 1
print("元组引用单个元素，是切片的一种简写",my_t3[ind])  # 相当于设置变量的效果
print("元组设置变量引用",my_t3[ind:ind+3])


#元组的更改
print('=====元组中元素不可删除或修改，只能删除元组=====')

# my_t3[1] = "fix"   #报错  TypeError: 'tuple' object does not support item assignment
print("元组任意数值都不可更改")

# 删除元组元素（不支持）
# del my_t3[1]
print(my_t3)   #TypeError: 'tuple' object doesn't support item deletion

# del my_t3  # 可以删除元组，不能删除元组中的元素
print(my_t3)   #删除后，找不到变量  NameError: name 'my_t3' is not defined


# 元组的方法
print('=====元组的方法：案例=====')

my_t4 = ['l','e','a','b','c','d','www']
print("my_t4元素个数",len(my_t4))
print("'my_t4'元素个数",len("my_t4"))  #len函数,使用引号后，计算括号中的元素个数
print(my_t4.count('b'))  #计算b的元素个数

# 查找字符串起始索引值（找不到控制台报错）
print(my_t4.index('www'))   #ValueError: 'wwww' is not in list

#index与if此方法相同,相当于省写
if "aa" in my_t4:
    print(my_t4.index("a"))  #a存在元组中，返回起始索引值2
else:
    print("aa" not in my_t4)   #返回True或Flase


# 元组的遍历
for ball in my_t4:
    print("遍历元组中的元素:",ball)

for ball in "123456789":
    print("遍历字符串中的元素:",ball)


a = ["10","12","14","16","18",]
print('a的长度',len(a))

for ball in ["10",'12','14','16','18']:
    print("遍历列表中的元素:",ball)

print("列表推导式",["元组字符是:"+ x for x in ('l','o','v','e','y','o','u')])
print("元组推导式",("元组字符是:"+ x for x in ('l','o','v','e','y','o','u')))  #输出<generator object <genexpr> at 0x000001CB2CA28AC0>

# 元组取最大值和最小值（可以判定数字、字母）
my_t5 = (-10,2,-30,4,5555,666667)
print("max:",max(my_t5))
print("min:",min(my_t5))

print("max:",max(my_t4))
print("min:",min(my_t4))


print('=====元组内可变的元素======')
# 元组内的可变元素
my_t6 = ('loveme',[1,2,3,4,5],("python",'345','自动化'))

# 元祖的元素不可改变
# my_t6[1] = [1,2,3]   #TypeError: 'tuple' object does not support item assignment

print("修改之前的列表地址",id(my_t6[1]))
my_t6[1][2] = 'fix'    #元组中的值不可修改，但元组中的列表可以修改
print("修改后的 列表 地址",id(my_t6[1]))   # 修改后的元组，内存地址不变
print("元组内的可变元素",my_t6)

my_t6 = ('loveme',[1,2,3,4,5],("python",'345','自动化'))
after_pop = my_t6[1].pop   #.pop表示删除
print("after_pop:",after_pop)
print("元组内的可变元素",my_t6)    # 删除前与删除后无变化，内存地址也无变化
print("after_pop:",after_pop)


'''
字典
自解释数据类型
json 格式 

| 方法                   | 描述                                                         |
| :--------------------- | :----------------------------------------------------------- |
| clear()                | 从字典中删除所有项                                           |
| copy()                 | 返回字典的浅拷贝副本                                         |
| fromkeys(seq[, value]) | 返回一个新字典，以序列 **seq** 中元素做字典的键，**value** 为字典所有键对应的初始值。 |
| get(key[,d])           | 返回键的值。如果键不存在，则返回**d**(默认为 **None**)       |
| items()                | 以**(keys,value)**格式返回字典中的每一项                     |
| keys()                 | 返回字典中的所有键key                                        |
| pop(key[,d])           | 删除带有key的项并返回其值或如果未找到key，则返回 d如果未提供d且未找到key，则会引发错误KeyError。 |
| popitem()              | 删除并返回任意项**(key,value)**。如果字典为空，则引发错误KeyError。 |
| setdefault(key[,d])    | 如果key在字典中，则返回相应的值value。如果没有，则插入值为d的key并返回d（默认为None）。 |
| update([other])        | 使用其他键/值对更新字典，覆盖现有键。                        |
| values()               | 返回字典中的所有值value                                      |

'''

my_d = {"name":"刘备",
        "age":44,
        "high":177
        }

print("=====列表与字典的转换：案例1")
# 输入dict，可以将列表嵌套的元组转换成字典
my_d8 = dict(
    [("iphone10",5000),
     ("iphone11",6000),
     ("iphone12",7000)])
print(my_d8)

print("=====列表与字典的转换：案例2")
# 输入dict，可以将列表嵌套的元组转换成字典
my_d9 = dict([
    ["hone10",500],
    ["hone11",600],
    ["hone12",700]])
print(my_d9)
