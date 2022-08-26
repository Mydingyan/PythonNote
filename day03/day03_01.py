


'''
选择结构
1. debug模式


三种结构就可以表述这个世界：
2. 顺序结构
3. 选择结构
4. 循环结构
'''


# 2.顺序结构
print("按行执行1")
print("按行执行2")
print("按行执行3")
print("按行执行4")
print("按行执行5")


# 3. 选择结构

print("=====if循环案例========")

'''
if expression(条件表达式）
   statements(执行语句）
   
选择结构的代码，当满足一个条件之后，后面的代码就不会在运行了
'''


num  =  -3

if num >0:
    print(num,"是正数")



print("=====if...else循环案例========")


'''
if expression:(条件表达式）
    statements of if  （满足条件表达式执行）
else:（否则）
    statements of eslf  （不满足条件表达式执行）
'''
num  =  -3

if num >0:
    print(num,"是正数")
else:
    print(num,"是非正数")


print("========if...elif...else循环案例========")

'''
if expression:(条件表达式）
    statements of if  （满足条件表达式执行）
elif:
    statements of elif
else:（否则）
    statements of eslf  （不满足条件表达式执行）
'''

#方式1：嵌套循环（if...elif循环解决嵌套）

num  =  100

if num >0:
    #大于0
    print(num,"是正数")
    if num >100:            #嵌套循环（嵌套里能继续嵌套）
        print(num,"是大于100")
    elif num == 100:
        print(num,"是等于100:")
    else:
        print(num,"是小于100")
else:
    #不大于0
    if num ==0:             #嵌套循环
        print(num,"是0")
    else:
        print(num, "是非正数")


#方式2：嵌套循环（if...elif...else循环）   更聪明的方案

num  =  111

#是否大于0
if num >0:
    #大于0
    print(num,"是正数")
elif num == 0:       # elif 是 else if的简写
    #等于0
    print(num, "是0")
else:
    #不等于0
    print(num, "是非正数")


print("========循环案例3：折扣========")

money = float(input("请输入消费金额:"))

if money >= 8000 :
    k = 0.7 #折扣
    print("vip消费的折扣为:",k*10,"折")
elif money >=7000: # and money <8000:
    k = 0.75
    print("vip消费的折扣为:",k*10,"折")
elif money >=6000:
    k =0.8
    print("vip消费的折扣为:",k*10,"折")
elif money >=5000:
    k =0.85
    print("vip消费的折扣为:",k*10,"折")
elif money >=4000:
    k =0.9
    print("vip消费的折扣为:",k*10,"折")
else:
    k =1
    print("普通客户，原价购买:")

print("消费金额为:",money,"应收:",money*k,"元")

