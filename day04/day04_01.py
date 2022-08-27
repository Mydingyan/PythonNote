# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day04_01.py
@time: 2022/8/25 23:11
"""

# 创建字符串

str_1 = 'abc de'

# 字符串切片

str_4 = 'avcvzcfd456451'
print(str_4[1])  #切一个字符
#print(str_4[50])  # IndexError: string index out of range  字符串索引超出范围


print("=====切片的语法======")
# [开始:结束:步长]   左闭右开

str_4 = '0123456789abcdefghijklmnopqrst'

print(str_4[3:])   #打印第四个字符之后的所有
print(str_4[:4])
print(str_4[1:4])
print(str_4[1:10:2])
print(str_4[::3])  #从开始到末尾间隔3位的数据

print("=====切片的语法：负数======")
#可以取负数，从右往左数
#print(str_4[::-1])   #倒序输出
print(str_4[-10:-2:-1])

print("=====切片的语法：字符串不可使用切片改变======")


print("=====字符串的拼接和重复======")

# 字符串的拼接和重复
str_5 = 'abcde'
str_6 = '12345'
print(str_5+" "+str_6)   #两种方法等价
print(str_5,str_6)

print(str_5 * 10)

print("=====join 连接其他 字符串 ======")

# join  用自己来连接其他 字符串

# 案例
print(" ".join(["Hello","Python","world!"]))
print("_".join(["Hello","Python","world!"]))
print("-".join(["Hello","Python","world!"]))   #.join表示给前面的字符串赋值
print("lebo".join(["Hello","Python","world!"]))


print("=====字符串性质判断 ======")

# 字符串性质判断

print("=====字符串性质判断案例一：判断是不是纯数字 ======")

# age = input("请输入年龄：")
# if age.isdigit():
#     print("您输入的年龄是:",age)
# else:
#     print("年龄只能输入纯数字！")

print("=====字符串性质判断案例二：判断是不是纯字母 ======")

print("leaaa".isalpha())    #判断是不是纯字母，返回True

print("=====字符串性质判断案例三：判断字符串是不是全小写 ======")
# 只要不包含大写，就返回True
print("leaaa111".islower())  # 返回True
print("leaaa".islower())  # 返回True

print("=====字符串性质判断案例四：判断字符串是不是全大写 ======")
print("WZRTYFSD".isupper())   # 返回True
print("WZRTYFSDawe".isupper())   # False

print("=====字符串性质判断案例五：判断是不是某字符串开头 ======")

print("www.a.yansay.cn".startswith('www'))  # True
print("www.a.yansay.cn".startswith('http'))    # False


print("=====字符串性质判断案例五：判断是不是某字符串结尾 ======")

print("www.a.yansay.cn".endswith('.cn'))    # True
print("www.a.yansay.cn".endswith('.ca'))    # False


# 字符串查找与替换
str_8 = 'wangzherongyaoautotest'


print("=====案例一：字符串出现的次数：======")
print(str_8.count("a"))  #3次
print(str_8.count("t"))

print("=====案例二：查找字符串起始索引值（找不到就是-1）======")
str_8 = 'wangzherongyaoautotest'

print(str_8.find("auto"))   #14，起始索引
print(str_8.find("autoa"))   #找不到返回-1

print("=====案例二：查找字符串起始索引值（找不到控制台报错）======")
print(str_8.index("auto"))   #14，起始索引
# print(str_8.index("auto1"))   # 这个方法找不到时控制台报错ValueError: substring not found


print("=====案例三：字符串替换======")
print(str_8.replace("a","A"))  #替换所有A的字符，返回替换后的字符串
print(str_8.replace("auto","Auto"))



# 分切与连接
