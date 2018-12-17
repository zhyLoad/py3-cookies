import math

def my_abs(a):
    """
    测试定义函数
    :param a:
    :return |a|:
    """
    checkInputDataType(a)

    if a < 0:
        return -a
    elif a == 0:
        return a
    else:
        return a

def nullMethod():
    """
    空函数
    :return None:
    """
    pass


def multiResultMethod(x,y):
    """
    返回多个值的函数
    :param x:
    :param y:
    :return :
    """
    checkInputDataType(x)
    checkInputDataType(y)
    x1 = x+3*math.sqrt(x)
    y1 = y-math.log(y,10)
    return x1,y1


def checkInputDataType(a):
    """
    校验录入参数类型为数字
    :param a:
    :return:
    """
    if not isinstance(a, (int, float)):   # mark this :how to check input param's type
        raise TypeError('bad operand type')
    pass



#返回多个值的函数如何使用
x = multiResultMethod(2,5)
a,b = multiResultMethod(2,5)
print('x= multiResultMethod(2,5) = ',x)  #返回多值的函数，用一个变量去接值，得到的是个元组
print('a,b = multiResultMethod(2,5) :','a=',a,',b=',b) #返回多值的函数，也可以用多个变量去接返回值---元组解包

#注意：(a,b)和a,b都能标识元组，一般省略括号直接用a,b代替(a,b)
m = 4,32
n = (4,32)
print('if m = 4,32 and n = (4,32) then:')
print('m=n?:',type(m)==type(n))
