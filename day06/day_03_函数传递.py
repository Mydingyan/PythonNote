# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_03_函数传递.py
@time: 2022/9/1 20:14
"""


print("=====位置参数案例：不能不传，不能少传，不能多传，位置不能错，一个萝卜一个坑")
# 函数参数的传递
#位置参数总结：不能不传，不能少传，不能多传，位置不能错，一个萝卜一个坑

def aa(x,y):
    print("x = ",x,"y = ",y)
    if x >y:
        return x,y
    else:
        return y,x
    print("a的最后一行")

# 1.位置参数：不能不传
# res = aa()   #不传报错,位置参数，TypeError: aa() missing 2 required positional arguments: 'x' and 'y'

# 2.不能少传 ：
# res = aa(6)   #默认传给第一个参数  TypeError: aa() missing 1 required positional argument: 'y'

#3.不能多传
# res = aa(3,5,6)  # 多传报错 TypeError: aa() takes 2 positional arguments but 3 were given



# 2 三种参数①：默认参数
print("=====默认参数案例：不传值，默认展示原始值，只传一个参数，给第一位======")

def a(x=5,y=5):
    print("x = ",x,"y = ",y)
    if x >y:
        return x,y
    else:
        return y,x
    print("a的最后一行")

res = a()
print("默认参数，不传展示原值：",res)  #  不传值时，取默认参数
res = a(7)
print("默认参数，不传",res) # 只传一个值时，默认给第一位
res = a(8888,9999)
print("默认参数，不传",res)


# 3  三种参数②：关键字参数
print("=====关键字参数：按顺序传参，位置参数可以不输入参数名======")
def pople_msg(name,age,address):
    print("name:",name)
    print("age:",age)
    print("address:",address)

pople_msg(222,"张伟","李三")  #按顺序传参
pople_msg(age=20,name="张飞",address="中国")

# 参数的顺序：（位置参数,关键字参数,不定长参数)    多种参数时，位置参数一定要放在最前，关键字参数在中间，不定长参数在最后。顺序不能乱



# 4 三种参数③：不定长参数 （一个星号（*）表示不定长参数
# 格式：*args      args可以使用任意标识符，只是args表示参数的意思习惯用
print("=====不定长参数案例一：======")

def write_names(*args):
    print(args)    #多个元素传参给args,格式为元组
    print(type(args))
    for xunhaun in args:
        print(xunhaun)

write_names("三国","张飞","刘备","关羽")


print("=====不定长参数案例二：多种参数的使用======")
# 前面卡位置,剩下的都给args
def write_names(address,kind = "英雄",*args):
    print("address:",address)
    print("kind:",kind)  #列表
    print("args:",args)  #元组
    print(type(args))
    for item_in in args:
        print(item_in)

write_names("中国","张飞","刘备","关羽")
write_names("中国",None,"张飞","刘备","关羽")   #None可以覆盖kind中的默认参数，kind有默认值，如果需要原来的值，还是得写上
write_names("三国","桃园三结义","张飞","刘备","关羽")




