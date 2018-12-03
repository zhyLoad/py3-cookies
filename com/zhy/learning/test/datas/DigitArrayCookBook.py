"""
处理数组
"""
import random

x = [1,2,3,4]
y = [5,6,7,8]
print('array x is ',x,'\n array y is ',y)

print('x*2=',x*2) #注意，数组乘以2表示每一项又出现一次，并没有逐项乘以2
print('x+y=',x+y) #注意，数组相加表示把两个数据各项对接起来，并没有逐项相加
#注意：要处理对数组中每一项元素逐项操作，请参考numpy的使用

a = [2,5,32,5,776,23,21,17]
print('a : \n',a)
print('choice some one in array a  = ',random.choice(a)) #随机选取数组中的一个数
print('choice some one in array a = ',random.choice(a)) #随机选取数组中的一个数
print('choice some one in array a = ',random.choice(a)) #随机选取数组中的一个数

print('random.sample(a,2) : ',random.sample(a,2)) #随机提取一个长度为2的样本
print('random.sample(a,2) : ',random.sample(a,2))#随机提取一个长度为2的样本
print('random.sample(a,4) : ',random.sample(a,4))#随机提取一个长度为4的样本

random.shuffle(a)
print('after random.shuffle(a) a : ',a) #打乱数组元素次序

#补充：关于random的其他用法
#1.生成随机整数
print('generate int : ',random.randint(0,10))
print('generate int : ',random.randint(0,10))
print('generate int : ',random.randint(0,10))

#2.生成0到1范围内均匀分布的浮点数
print('generate a float number : ',random.random())
print('generate a float number : ',random.random())
print('generate a float number : ',random.random())

#3.N位随机位（二进制）的整数
print('random.getrandbits(200)) : ',random.getrandbits(200))

# 注意：密码学应用中若要生成随机数，请不要使用Random，请使用带有安全性的ssl模块中的随机数生成器 ssl.RAND_bytes()





























