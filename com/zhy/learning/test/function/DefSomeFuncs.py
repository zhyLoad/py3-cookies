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
