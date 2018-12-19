import  html

#位置参数：只关心某个位置的参数值，参数叫什么名称并不关注
def avg_1(first, *rest):
    """
    :param first:
    :param rest: 可传入任意数量的参数
    :return:
    """
    return (first + sum(rest)) / (1 + len(rest))  #rest 位置参数的值为一个元组数据类型

print('avg_1(1,2) = ',avg_1(1,2))
print('avg_1(1,2,3,4) = ',avg_1(1,2,3,4))
print('\n')


#关键字参数：不仅使用参数的值，还关注参数的名称
def make_elements(name,value,**attrs):
    """
    :param name:
    :param value:
    :param attrs: 任意数量的关键字参数，用**标识
    :return:
    """
    keyvals = ['%s = "%s"' % item for item in attrs.items()]  #attrs是包含所有关键字参数的字典,即关键字参数接收到的是个关键字参数的字典数据类型
    attr_str = ''.join(keyvals)
    element = '<{name} {attrs}>{value}</{name}>'.format(name=name,attrs=attr_str,value=html.escape(value))
    return element

element_1 = make_elements('item','Albatross',size='large',quantity=6)
element_2 = make_elements('p','<spam>')
print('element_1 = ',element_1)
print('element_2 = ',element_2)
print('\n')


#位置参数和关键字参数的函数总结
def anyargs(*args,**attrs):
    print('位置参数：',args,' 类型为：isinstance(args,tuple) = ',isinstance(args,tuple))  # 位置参数实质是传入一个元组作为函数的入参
    print('关键字参数：',attrs,' 类型为：isinstance(attrs,dict) = ',isinstance(attrs,dict))   # 关键字参数实质是传入一个字典作为函数的入参
print('for function anyargs(*args,**attrs) :')
anyargs(1,'today',23*2,name='Tim',age=23,six='man',phone='23912332')
print('\n')

def test_1(a,b,*args):
    pass
def test_2(a,*args,b): #注意，一个函数只能定义一次位置参数，例如：def test_3(a,*args,b,*args_1):是不允许的。位置参数后面还可以定义其他参数，如本例
    pass
def test_3(a,b,**attrs): #注意：关键字参数只能出现在函数参数列表的最后一位，例如：def test_4(a,b,**attrs,c,d):是不允许的
    pass
def test_4(a,b,*args,d,**attrs): #位置参数和关键字参数同时存在时
    pass


#强制使用关键字参数的办法
def recv(maxsize,*,block):
    pass
recv(23,block=True) #本例中，*后面的block参数必须使用关键字参数方法使用，即传入值时必须是block='value',若写成recv(23,True)则会报错
#尽量强制使用关键字参数，因为这样会使程序可读性强，使用函数的人从函数定义中可以更好理解函数参数的作用

#位置参数后面可以指定关键字参数
def test_5(*args,type=None): #本函数定义将type作为了关键字参数，使用时test_5(1,2,3,4,5)或者test_5(1,2,3,4,5,type='add')
    pass


#给函数增加元信息：元信息即对函数用途的解释，加与不加对函数的执行不产生影响，只是为了阅读函数的人更易懂
def add_1(x:int,y:int)->int:
    return x+y
#print(help(add_1))


#在函数声明的时候指定参数的默认值   ----- 1）普通类型的参数变量
def spam(a,b=43):
    print('test spam : ',' a =',a,',b = ',b)

spam(23) #调用时不传有默认值的参数，则默认按照声明时指定的那个默认值
spam(20,34)
spam(20,None) #注意：调用函数时参数值为None和不传该参数值的结果不一样


#在函数声明的时候指定参数的默认值   ----- 2）当默认参数为列表、集合、字典等类型的参数时，一般用None/True/False等不可变的变量来指定默认值。
#注意：当默认参数为列表、集合、字典等类型的参数时，千万不要写成可变的变量，例如定义为：spam(a,b=[])是错误的
def spam(a,b=None):
    if b is None:   #注意：判断对象是不是None必须用 b is None ，不能用 if not b
        b = [12,323,453]
    print('test spam : ',' a =',a,',b = ',b)

spam(23)  # 调用时不传有默认值的参数，则默认按照声明时指定的那个默认值
spam(20, [34,23,44])

print('\n')

#函数指定默认值只在指定时有效，指定之后再修改就不起作用了：
x = 43
def spam_1(a,b=x):
    print('test spam : ', ' a =', a, ',b = ', b)
print('before change x : ')
spam_1(32)

x = 22
print('after change x : ')
spam_1(32)

print('\n')

#验证一下如果集合类型的指定默认变量如果指定为非不可变的值会产生错误结果：
def spam_2(a,b=[]):
    print(b)
    return b
x = spam_2(1)   #print out : []
x.append('AAA')
x.append(99)
print('after change the x value: ')
spam_2(1) # print out ['AAA', 99]
#注意：以上两次都调用spam_2(1)得到的结果反而不一样，因为b变量默认值为可变数组[],它的值被修改了会引起函数返回值修改。所以要尽量指定b的默认值为None等不可变值

print('\n')

#一个函数想在定义的时候判断一下某个指定默认值的参数在用户调用时有没有传值
no_value = object()   #no_value是在函数声明时创建的变量，用户在调用时不可能知道这个变量.所以如果b没有传值，b的默认值肯定是no_value
def spam_3(a,b=no_value):
    if b is no_value:
        print('b parameter value is null')
        print('test spam : ',' a =', a, 'b is no value')
    else:
        #... when b is not null ,do this ...
        print('test spam : ',' a =', a, ',b  = ',b)

spam_3(4)
spam_3(4,5)
spam_3(4,None)
