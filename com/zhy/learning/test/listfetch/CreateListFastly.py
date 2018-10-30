

def print_list(list):
    for v in list:
        print('list_value_', v)




list_1 = list(range(1,11))  # range(1,11) create list [1,2,3,4,5,6,7,8,9,10]
print_list(list_1)
print('\n')


list_2 = [x*x for x in range(10)] # range(10) create list [0,1,2,3,4,5,6,7,8,9]
print_list(list_2)
print('\n')

list_3 = (x*x for x in range(10)) #注意："()"中生成的列表为generator 生成器 --- 适用于在循环中不断推算出列表的下一个元素的场景
print_list(list_3)
print('\n')


def fib(x):
    """ 简易的斐波那契函数"""
    x = 0
    a = 0
    b = 1
    while x<100:
       print(b)
       t = (b,a+b)
       a = t[0]
       b = t[1]   # 这三句等价于     a, b = b, a + b
       x = x +1
    return 'DONE'


def fib_1(x):
    """ 斐波那契Generator"""
    x = 0
    a = 0
    b = 1
    while x<100:
        yield b   # 注意这里：一旦函数中有yield返回，则该函数就不再是函数，而是个generator生成器。遇到yield就中断，下次又继续执行
        t = (b,a+b)
        a = t[0]
        b = t[1]   # 这三句等价于     a, b = b, a + b
        x = x +1
    return 'DONE'



# test fit function
print('fid(6) : ')
fib(6)
print('\n')


# test fit_1 function
f_1 = fib_1(6)
print('fib_1(6) : ')
print_list(f_1)
print('\n')


"""
generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
"""