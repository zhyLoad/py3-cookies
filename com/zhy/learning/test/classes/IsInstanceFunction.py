
"""
测试 isinstance方法
"""

"""
继承体系：object->Animal->Dog->Jeky
"""
class Animal(object):
    pass

class Dog(Animal):
    pass

class Jeky(Dog):
    pass


a = Animal()
d = Dog()
j = Jeky()


print(" isinstance(j,Dog)= ",isinstance(j,Dog))

print(" isinstance(j,Animal)= ",isinstance(j,Animal))

print(" isinstance(j,Jeky) = ",isinstance(j,Jeky))

print(" isinstance(d,Dog)= ",isinstance(d,Dog))

print(" isinstance(d,Animal)= ",isinstance(d,Animal))

print(" isinstance(d,Jeky)= ",isinstance(d,Jeky))

print(" isinstance('abc',str)= ",isinstance('abc',str))

print(" isinstance(123,int)= ",isinstance(123,int))

print(" isinstance(1234.23,float)= ",isinstance(1234.23,float))

print(" isinstance([1, 2, 3], (list, tuple))= ",isinstance([1, 2, 3], (list, tuple)))

print(" isinstance((1, 2, 3), (list, tuple))= ",isinstance((1, 2, 3), (list, tuple)))



class ABC(object):
    def fun1(self):
        print('fun1 ...')
    def __init__(self):
        pass
    def setAbc(self,abc):
        self.__abc = abc

print('dir(ABC) = ',dir(ABC)) #获取一个类的所有属性和方法详情
#d打印结果：dir(ABC) =  ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'fun1', 'setAbc']

aaaClass = ABC()
aaaClass.x =1.3
print('hasattr(aaaClass,\'x\') = ',hasattr(aaaClass,'x')) #判断类是否有某个属性
print('hasattr(aaaClass,\'y\') = ',hasattr(aaaClass,'y'))

setattr(aaaClass,'zz',234)     #为某个对象设置属性和值
print('hasattr(aaaClass,\'zz\') = ',hasattr(aaaClass,'zz'))
print('getattr(aaaClass,\'zz\') = ',getattr(aaaClass,'zz')) #获取某个对象的指定属性值

print('hasattr(aaaClass,\'setAbc\') = ',hasattr(aaaClass,'setAbc')) #判断类是否有某个方法
print('getattr(aaaClass,\'setAbc\') = ',getattr(aaaClass,'setAbc')) #获取类某个方法