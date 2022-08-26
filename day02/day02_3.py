


# 运算符

# 1. 算数运算符
print(1+1)
print(2-1)
print(2*2)
print(2/5)
print(5%2)  # 取模，求余数（例：100/500=0余100，2/4=0余2，5/2=2余1，不要整数，只要余数         ）
print(10//4) # 向下取整（例：100/5=20，10/4=2，取整数数，不要余）
print(2**3) # 幂运算

# 2. 赋值运算符
x =1
print(x)

x = 5
x += 5   #表示x+5=10
print(x)

x = 10
x -= 1   #表示x-1=9
print(x)

x = 5
x *= 5  #表示x*5=25
print(x)

x = 5
x /= 5
print(x)

# 3比较运算符，结果类型为布尔值（bool)，值为 True，False
x = 10
y = 12
res = x > y     #结果为false
print("res的数据类型是：",type(res))
print("x>y的结果res:",res)

res = x < y    #结果为True
print("res的数据类型是：",type(res))
print("x>y的结果res:",res)

res = x == y   #结果为False
print("res的数据类型是：",type(res))
print("x>y的结果res:",res)

res = x != y   #结果为True
print("res的数据类型是：",type(res))
print("x>y的结果res:",res)

# 大于或者等于
res = x>=y    #结果为False
print("res的数据类型是：",type(res))
print("x>y的结果res:",res)

#小于或者等于
res = x <= y   #结果为True
print("res的数据类型是：",type(res))
print("x>y的结果res:",res)


#4. 逻辑运算

# and 与运算（并且）
#只要有一个条件不满足，就为Flase
# 串联电路  三个连续的桥，过桥需要三个桥都联通
aa = True
bb = False
print("x and y",aa and bb )


age  = 18
name = '王者'
gender = '女'
print("年龄是18岁吗？",age == 18)
print("名字是叫王者吗？",name == '王者')
print("性别是男性吗？",gender == "男")
print("年龄是18岁，并且名字叫王者，并且是男性吗？",age ==18 and name =='王者' and gender == '男')


print("=================")
# or 或运算
#只要有一个满足条件，就为True
#并联电路  三条并列的桥，任意一条都能联通

age  = 18
name = '王者111'
gender = '女'
print("年龄是18岁吗？",age == 18)
print("名字是叫王者吗？",name == '王者')
print("性别是男性吗？",gender == "男")
print("年龄是18岁，并且名字叫王者，并且是男性吗？",age ==18 or name =='王者' or gender == '男')


print("=================")
# not 逻辑运算
print("年龄不是18岁吗？",not age == 18 ) #逻辑运算，对比较的结果取反
print("年龄不是18岁吗？" ,age != 18)  #比较运算，进行比较
print("年龄不是18岁吗？", not age != 1)  #比较运算，进行比较

