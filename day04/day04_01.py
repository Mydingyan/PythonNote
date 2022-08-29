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



# 字符串分切
#方法：split(sep,[maxsplit]) ，切完成后，字符串变成列表
#（只要输入点，出来的都是字符串对象的方法）

print("leboleboleboleboxueyuan".split('l'))   #方式1：l切后的字符消失
print("lebo,lebo,lebo,leboxueyuan".split(','))  #方式2：逗号间隔符消失
print("lebo,lebo,lebo,leboxueyuan".split(',',1)) #方式3:切割次数1次表示只匹配1次


#字符串删减
str_11 = '   124124 124124 5125125     '
print('++++'+str_11.strip()+'++++')   # 去除字符串前后的空格

print('++++'+str_11.lstrip()+'++++')   # 去除字符串左边的空格
print('++++'+str_11.rstrip()+'++++')   # 去除字符串右边的空格

print(len(str_11))  #除去空格之前29个字符
print(len(str_11.strip()))  #除去空格之后21个字符


#字符串填充
str_12 = 'leboautotest'
print(str_12.zfill(111))   #将字符串长度用0补充至111位

#字符串格式化输出
school  = '演讲学院'
name = '孙策'
age = 25

#格式化输出方法1
print("我叫"+name+',今年'+str(age)+"岁,我在"+school+"学习自动化测试")

#格式化输出方法2  (最新且最简单的方法）
print(f"我叫{name},今年{age}岁,我在{school}学习自动化测试")

#格式化输出方法3
print("我叫%s,今年%s岁,我在%s学习自动化测试"%(name,age,school))

#格式化输出方法4
print("我叫{},今年{}岁,我在{}学习自动化测试".format(name,age,school))

print("=====格式化输出精简小数点位数")
weight = 121.12456
print("商品的重量为:%f"%(weight))
print("商品的重量为:%10.3f"%(weight))  #%5.2 表示整数位可以占5个字符，小数点位可以占2个字符




#### 整数输出

'''
- % d

- 左补空格

% 3
d意思是打印结果为3位整数，当整数的位数不够3位时，在整数左侧补空格

- 右补空格

% -3
d意思是打印结果为3位整数，当整数的位数不够3位时，在整数右侧补空格

- 左侧补零

% 05
d意思是打印结果为5位整数，当整数的位数不够5位时，在整数左侧补0

'''

age = 9
print('格式化1结果:%d,格式化2结果:%3d,格式化3结果:%-3d,格式化4结果:%03d' % (age, age, age, age))


#列表
my_list = []   #创建列表
my_list = [1,2,3]
my_list = [1,[2,3,5,["python"],1.444],3,(3,5)]  # 列表中可以嵌套列表、元组

print(my_list[1][3])  #列表中的列表嵌套切片，注意从0开始
print(my_list[3])  #列表中的元组也可以切片


#列表切片
print(my_list[1:2])
print(my_list[1:4:2][0][3][0])  #切片后，从新的列表中继续切片，取出python字符串


#通过切片修改切片中的内容
my_list = [1,[2,3,5,["python"],1.444],3,(3,5)]
print(my_list)
my_list[2] = '乐博学院'   #修改列表中的元组
print(my_list)


# 列表中添加元素
print(my_list)
my_list.append("这是列表新增的字符串")  #新增1个元素
print(my_list)
my_list.append(["好好学习","天天向上"])  #新增一个列表
print(my_list)

my_list.insert(1,"指定位置新增") #新增至列表第一个元素
print(my_list)


#两个列表合并、串联

my_list4 = ['a','b','c']
my_list5 = [1,2,4]

my_list6 = my_list4 + my_list5   #合并两个列表为一个
print(my_list6)
print(my_list4,my_list5)     #列表串联，输出两个列表
print([my_list4,my_list5])   #将两个列表合并为新列表中的元素


#列表元素删除
my_list7 = [1,2,3,4,5,6,7,8,9,10]
print(my_list7)
del my_list7[2]  #删除指定位置的元素，从0开始
print("删除某个元素：",my_list7)

del my_list7[1:5]  #删除指定长度列表
print("删除指定长度列表:",my_list7)

del my_list7[1:5:2]  #删除指定长度列表
print("按步长删除:",my_list7)

del my_list7   #删除整个列表


#列表元素判断（判断元素在列表中是否存在，返回True和False

my_list9 = [1,[3,5,"python"],3,(3,6),888]
print(1 in my_list9)   #返回True
print("1" in my_list9)   #返回False
print([3,5,'python'] in my_list9)
print((3,6) in my_list9)   #True


### 遍历列表
for it in my_list9:    # it表示申明的变量，可以是任意自定义名称
    print(it)

### 列表推导式
# 从现有列表中 创建出新列表
list_old = [1,2,3,4,5,6,7,8,'3吖阿啊']

print("=====列表推导式方式一：直接输出原列表")
list_new = [it for it in list_old]  #两边的it必须相同，第一个it是引用（不懂的话看19节7分钟开始的位置）
print(list_new)

print("=====列表推导式方式二：运算符号")
list_new = [it*2 for it in list_old]  #it*2表示所有数字值*2，字符串就输出两边
print(list_new)

list_old = [1,2,3,4,5,6,7,8]
print("=====列表推导式方式三：if判断")
list_new = [it for it in list_old if it<3]  #输出小于5的值，不能有中文
print(list_new)


list_old = [1,2,3,4,5,6,7,8]
print("=====列表推导式方式三：if判断取出偶数")
list_new = [it for it in list_old if it%2 ==0]  #取数偶数
print(list_new)


print("=====此方法就是等价于列表推导式方法二")
list_new = []
for n in list_old:
    list_new.append(n*2)
print(list_new)


## 更多Python列表方法
'''
Python 有许多有用的列表方法，它们可以非常轻松地处理列表。
以下是一些常用的列表方法。
语法:
字符串.方法

| 方法      | 描述                                 |
| :-------- | :----------------------------------- |
| append()  | 在列表末尾添加一个元素               |
| extend()  | 将一个列表的所有元素添加到另一个列表 |
| insert()  | 在定义的索引处插入一个元素           |
| remove()  | 从列表中删除一个元素                 |
| pop()     | 返回并删除给定索引处的元素           |
| clear()   | 从列表中删除所有元素                 |
| index()   | 返回第一个匹配元素的索引             |
| count()   | 返回作为参数传递的元素数的计数       |
| sort()    | 按升序对列表中的元素进行排序         |
| reverse() | 颠倒列表中元素的顺序                 |
| copy()    | 返回列表的浅拷贝                     |

'''
