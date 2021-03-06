
"""
测试 Type函数，它可以作用于普通变量，也可以作用于类，还可以作用于方法
"""

print(" type(123)= ",type(123))

print(" type(123.134) = ",type(123.134))

print(" type('abc')= ",type('abc'))

print(" isinstance('abc',str) = ",isinstance('abc',str))

print(" isinstance(123.134,(str,float)) = ",isinstance(123.134,(str,float)))


class A(object):
    pass
print(" type(A)= ",type(A))

a = A()
print(" type(a)= ",type(a))

print(" isinstance(A,(str,float,type)) = ",isinstance(A,(str,float,type)))


def funcB():
    pass

print("type(funcB) = ",type(funcB))

print(" type(abs)= ",type(abs))

print(" type(lambda x: x)= ",type(lambda x: x))

print(" type((x for x in range(10))) = ",type((x for x in range(10))))