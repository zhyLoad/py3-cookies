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








print("test my_abs 1 ",my_abs(-3))
print("test my_abs 2 ",my_abs(123.123))
#print("test my_abs error ",my_abs('12341'))   # test the exception handler

print('null method return :',nullMethod())

x,y = multiResultMethod(12,34)
print('call the multiResultMethod 1:',x,y)
r = multiResultMethod(12,34)
print('call the multiResultMethod 2:',r)  #注意：多返回值的函数，如果用一个变量指向结果，类型是个tupe
# r = multiResultMethod('qew',34)  # test the exception handler
