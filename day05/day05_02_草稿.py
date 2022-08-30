# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day05_02_草稿.py
@time: 2022/8/30 22:49
"""

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
# 输入dict，可以将元组中的列表转换成字典
my_d9 = dict([["hone10",500],["hone11",600],["hone12",700]])
print(my_d9)


### 字典访问元素
print('name',my_d['name']) #方法一：根据key,返回value，找不到就报错（KeyError: 'name88'）
print("name",my_d.get("name"))  #方法二：根据key,返回value,找不到就返回None   这种方法更好用，自带异常处理

# print("name",my_d["name88"])  # 查找不存在的key，返回报错
print("name",my_d.get("name88"))  #查找不存在的key，返回空 None


# 字典的嵌套
my_d1 = {"name":"刘备",
         "age":40,
         "high":170,
         "brother":{
             "二弟":"关云长",
             "三弟":"张飞"
         }}

print(my_d1)

#字典中的元素更新
my_d1["age"] = 44
print(my_d1)

## 字典中元素增加
my_d1['citys'] = 35  #默认增加在最后
print(my_d1)

#字典元素删除
my_d1.popitem()
print(my_d1)

my_d1.pop("name")
print(my_d1)
my_d1["brother"].pop("二弟")   #
print(my_d1)

# 字典的生成
# my_d4 = {x.upper():x.lower() fox x in "wangzhe"}
#
# print("字典生成式", my_d4)
# print("len", len(my_d4))


# 字典的遍历
# for itd in my_d4:
#     print("")

# 字典的内置函数
