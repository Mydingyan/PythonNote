
# 2022年8月25日23点04分


'''
# 4. 循环结构
# 列表、字典、元组、集合都可以在循环中使用


for 循环
有一个计数器（确定的循环次数）

while 循环
有一个判断条件（确定或者退出条件）
'''

print("======for循环格式=========")
'''
for var in seauence:
    for循环内的代码
for循环外的代码
'''

print("======for循环案例一=========")


numbers = [5,7,9,11,13,15]

for val in numbers:      #   val:每次从列表中取一个数字
    print("本次取出的是：",val)
print("循环之外的代码")


print("======for循环案例二：列表=========")

numbers = ['诸葛亮','张飞','关羽','刘备']

for val in numbers:
    print("本次取出的是:",val)
print("我是循环体之外的代码了")


print("======for循环案例三：列表中取数=========")
numbers = [1,2,3,4,5]
for val in numbers:
    print("本次取出的是：",val)
print("我是循环体之外的代码了")

print("======for循环案例三：函数中取数=========")
numbers = range(1,6)     #函数中取数
for val in numbers:
    print("本次取出的是：",val)
print("我是循环体之外的代码了")


print("======for循环案例三：range函数中取数=========")
for i in range(1,10,2):    #起點,范围，步长
    print(i*i)

print("======for循环案例三：字典中取数=========")

d = {
    "name":"诸葛亮",
    "age":20,
    "weight":120.5
    }

keys = d.keys()  #字典取出key
print("type(keys)",type(keys))   #类型为字典

for k in keys:  #从字典中取三个key值进行循环
    print(k)



print("======while循环格式=========")
'''
while expression:
    statements of while

break #退出循环语句
'''
print("======while循环案例一：输入正确答案才会停止循环=========")


name = ''
while name != '诸葛亮':
    print("name",name,"不是我要找的人")
    name = input("请输入姓名：")

print("找到了")



print("======while循环案例一：break=========")

password = input ("请输入密码：")
i = 1
while password != "芝麻开门":
    print("密码",password,"不正确")
    # 尝试次数
    if i >=5:
        break  #退出循环语句

    i+=1
    password = input("请输入密码:")
    print("剩余可尝试次数",5-i)


print("======while循环案例二：continue=========")
# continue
# 不执行本次循环 ,位于continue语句之后的代码

for val in "王者荣耀dasd3242142b14`/*":      #for循环依次取出字符串中每一个字符（包括中英文及特殊字符）
    print("本次取出:",val)
    if val == '3' or val == "b":   # 取出的数值进入该判断时，continue不再执行之下的语句（包括if之外的语句）
        continue        #不在运行后面的代码
    print("在continue语句之后打印的:",val)
    # print("在continue语句之后打印的:", val)
    # print("在continue语句之后打印的:", val)
    # print("在continue语句之后打印的:", val)