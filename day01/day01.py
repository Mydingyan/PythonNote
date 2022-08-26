


#!/usr/bin/python
# coding=utf-8
'''
Author:乐搏-知行
'''
'''
python数据类型:
1.数字 int  float  complex(复数) 
2.字符串 不可变
3.列表 
4.元祖 不可变
5.字典
6.集合 不可变






'''
# 1.数字类型
age = 20
print("age的值是:", age)
print("age的内存地址是:", id(age))
print("age的数据类型是:", type(age))

height = 135.5
print("height的值是:", height)
print("height的内存地址是:", id(height))
print("height的数据类型是:", type(height))

# 2.字符串
# 不可改变,可以切片

# name = "孔明"
# name = '孔明'
name = '''孔
        明'''
print('"name"的值是:' + name)
print("name的内存地址是:", id(name))
print("name的数据类型是:", type(name))

hellow = "0123456hellow kity"
print("切片", hellow[2:5])
hellow = "0123456hxllow kity"
print("切片", hellow[8])
# hellow[8]="x"
print(hellow)

# 3.列表 list
# 中括号,逗号
a = [1, 2.2, "python"]
print('"a"的值是:', a)
print("a的内存地址是:", id(a))
print("a的数据类型是:", type(a))
print("切片", a[1:3])

# 4元祖 tuple
# ()  ,
t = (2, 3.6, "java", [3, 4, 5], (2.3, "23"))
print('"t"的值是:', t)
print("t的内存地址是:", id(t))
print("t的数据类型是:", type(t))
print("切片", t[1:3])

# 5 字典类型 dict 自解释
# 键  值 对
d = {
    "name": "孔明",
    "age": 20,
    "weight": 158
}
print('"d"的值是:', d)
print("d的内存地址是:", id(d))
print("d的数据类型是:", type(d))
print("引用", d["name"])
print("引用", d["age"])
print(d.keys())
print(d.values())

# 6集合类型 set
#
s = {1, 2, 3, "set"}

print("集合类型", s)
print("空{}", type({}))
print("空set", type(set()))

'''
数据类型转变
'''
# 隐式转变
num_int = 123
num_float = 1.23
num_new = num_int + num_float

print("num_new的值:", num_new)
print("num_new的类型:", type(num_new))

# 显式转换
n_int = 998
s_str = "1000.9"

print("num_new:", n_int + float(s_str))
print("num_new:", n_int + int(float(s_str)))
print("num_new:", str(n_int) + s_str)

print("五大皆空")
print(type(list()))
print(type(tuple()))
print(type(dict()))
print(type(str()))
print(type(set()))