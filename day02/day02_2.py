

# python数据类型:
# 1.数字 int  float  complex(复数)
# 2.字符串 不可变
# 3.列表
# 4.元祖 不可变
# 5.字典
# 6.集合 不可变
#  数字int,float、列表[]和字典{"键":"值"}属于简单数据类型，可变的
# 字符串str、元组（）、集合{}相对复杂，不可变的

# 1.数字类型 int
age = 111
print("age的值是:", age)
print("age的内存地址是：", id(age))
print("age的数据类型是:", type(age))

# 浮点类型 float
height = 111.111
print("age的值是:", height)
print("age的内存地址是：", id(height))
print("age的数据类型是:", type(height))


# 2.字符串 str
# 数据不可改变，但可以切片

name = '文' \
       '章'
print("name的值是:", name)
print("name的内存地址是：", id(name))
print("name的数据类型是:", type(name))

hellow = '12321321321hellow kity'
print("切片的内容：", hellow[1:5])
print("切片的内容是：",hellow[8])

# hellow[8] = "1"   # 切片内容不能修改字符串
# print(hellow)

print("------")

# 3.列表  list
# 中括号，逗号，列表是可变的

a = [111,222,333,4444,'python']
print("'a'的值是：",a)
print("a的内存地址是:",id(a))
print("a的数据类型是:",type(a))
print("a切片的值是:",a[1:5])


print("------")

# 4.元组 tuple
# 括号（）,可以嵌套列表和元组，元素用逗号隔开
# 元组也是不可变的

t = (2,3.1,"java",[1,2,3,4,"列表"],("21.1","元组嵌套元组"))
print("'t'的值是：",t)
print("t的内存地址是:",id(t))
print("t的数据类型是:",type(t))
print("t切片的值是:",t[0:5])

# 5. 字典类型 dict 自解释
# 键 值 对   ，字典是可变的
d = {
    "name":"张晓明",
    "age":22,
    "weight":"111",
    "height":"168"
}

print("'d'的值是：",d)
print("d的内存地址是:",id(d))
print("d的数据类型是:",type(d))
print("引用d的数值:",d["name"])
print("引用d的数值:",d["weight"])
print("打印d的所有key",d.keys())
print("打印d的所有values",d.values())


#6.集合类型 set
# 大括号{}  字典和集合的区别是 ,字典有key和value,集合只有value
# 不可变类型


s = {1,2,3,4,5,'set','我是集合'}
print("打印集合所有数据",s)
print("空集合{}",type(s))   #集合类型
print("空集合{}",type({}))  #字典dict
print("空set",type(set()))

print("===========")
# 数据类型转变
# 隐式转变
num_int = 123
num_float = 1.24
num_new = num_int + num_float
print("num_new的值：",num_new)
print("num_new的类型",type(num_new))  #float


print("===========")

# 显式转换
n_int = 1111
s_str = "111.1111"

print("num_new:",n_int+float(s_str))
print("num_new",n_int+int(float(s_str)))  #字符串转成数字类型，会舍弃小数点后数字


print("五大皆空")
print(type(list()))     #空列表
print(type(tuple()))    #空元组
print(type(dict()))     #空字典
print(type(str()))      #空字符串
print(type(set()))      #空集合



