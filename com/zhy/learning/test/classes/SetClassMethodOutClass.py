from types import MethodType

"""
定义某个类，为这个类动态的绑定某个方法
"""
class AAA(object):
    pass

print('now we create new methd ,then give it to the class \' instances :')
print('\n')

aaa = AAA()

# 1.为类的某个实例设置一个函数/方法---这种设置方法仅作用于某一个实例，其他实例不起作用
def set_amethod(self):  #  做法是先定义一个方法
    print('You called set_amethod! ')

aaa.set_amethod = MethodType(set_amethod,aaa) # 将该方法赋值给指定的类实例

print('call the new method for aaa instance : ...')
aaa.set_amethod()
print('\n')

# 该代码会报异常
# bbb = AAA()
# print('call the new method for another instance : ...')
# bbb.set_amethod()   # 验证MethodType为某个列的实例设置的方法，对于别的实例不起作用
# print('\n')

print('now we create new methd ,then give it to the class')
print('\n')

# 2.为某个类设置一个函数/方法，该类的任何实例都可以使用
def set_bmethod(self):  #  做法是先定义一个方法
    print('You called set_bmethod! ')

AAA.set_bmethod = set_bmethod # 定义的函数直接赋值给类的某个方法

ccc = AAA()
ddd = AAA()
print('call the new method for one instance : ...')
ccc.set_bmethod()
print('\n')
print('call the new method for another instance : ...')
ddd.set_bmethod()
print('\n')




