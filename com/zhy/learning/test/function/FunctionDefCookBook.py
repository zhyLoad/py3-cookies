
#简单一句话的函数定义，不用传统的def语句定义，可以直接用lambda表达式来定义函数
add_func = lambda x,y:x+y   #注意：用lambda表达式定义的函数叫匿名函数

print('3+4 = ',add_func(3,4))

#lambda表达式的妙用：排序或者reduce
names=['David Beazley','Brian Jones','Raymond Hettinger','Ned Batchelder']
print('names: ',names)
print('after sorted ,names: ',sorted(names,key=lambda name:name.split()[-1].lower()))

print('\n')

#注意：易错点：匿名函数中的变量值并不是在声明时绑定，而是在运行时决定的！
x = 20
a = lambda y:x+y

x = 30
b = lambda y:x+y

#由于x变量的值在最后x=30处确定，所以两个匿名函数a和函数b中的x值都是30
print('a(10) = ',a(10))
print('b(10) = ',b(10))

print('\n')

#继续修改x的值，匿名函数的结果会跟着x的不同值而产生相应结果
x=10
print('when x = 10,then a(3) = ',a(3))
x=21
print('when x = 21,then  a(3) = ',a(3))

print('\n')

#强制实现匿名函数在声明时就确定参数的值
x = 20
c = lambda y,x=x:x+y  #将当前x的值定义成x变量的默认参数值

x = 30
d = lambda y,x=x:x+y
print('c(10) = ',c(10))
print('d(10) = ',d(10))

print('\n')

#注意：易错点，Lambda表达式用在循环中时，不能想当然的期待程序记住每一次迭代的结果
funcs = [lambda x:x+n for n in range(5)]  #根据“匿名函数的变量都在运行时才绑定值”这一原理，每次迭代都不缓存上一次结果，而是每次迭代的值都是最后一次的值
for f in funcs:
    print(f(0))
print('')
#正确实现方式如下：
funcs = [lambda x,n=n:x+n for n in range(5)]  #为中间变量指定默认值，可以保证循环中，上一次迭代的结果被记住且使用在下一次
for f in funcs:
    print(f(0))
