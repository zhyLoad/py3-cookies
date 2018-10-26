

"""
测试类和类的属性值
"""

"""
Test1 ：class and class's properties -------为类的实例对象赋予新的属性
"""
class Student(object):
    """
    Test class
    """
    def __init__(self,name,age,scope):
        self.name = name
        self.age = age
        self.scope = scope
        self.__country = 'US' #以__开头的变量标识私有变量，类的外部不能访问

    def get_scope(self):
        if self.scope >= 90:
            return 'A'
        elif self.scope >= 80:
            return 'B'
        else:
            return 'C'


    def say_detail(self):
        self.name='wangwang'
        self.age=44
        print('my name is {0}:'.format(self.name))
        print('my age is {0}:'.format(self.age))

    def say_detail_again(self):
         print('my name is {0}:'.format(self.name))
         print('my age is {0}:'.format(self.age))

    def get_country(self):    #类的外部想访问私有变量时，通过调用类的方法来获取 .修改私有变量的方法类似，也通过调用类的方法实现 。注意：在类外部以 'xxx.__country=xxx_value'形式修改私有变量不会得到正确结果，反而给类新增了另外一个变量
        return self.__country


std = Student('Tom',23,87)
std.say_detail() #这个函数中尝试修改self.xxx 的变量值，结果可以成功修改
std.say_detail_again() #验证了值已经被上一步修改
print('my scope result =',std.get_scope(),'\n')

std1 = Student('Jerry',13,95)
std1.say_detail_again()
print('my scope result =',std1.get_scope(),'\n')

#此处尝试修改对象的属性值，成功修改了
std1.name = 'DD'
std1.age = 32
std1.say_detail_again()
print('--------------------------------------------------------------------','\n')
print('--------------------------------------------------------------------','\n')




"""
Test2 test limit the class's properties----------slots
"""
class Teacher(object):
    __slots__ = ('name','sex')  # 限制了这个类只能有括号中的几个属性
    pass

t1 = Teacher()
t1.name = '张三'
t1.sex = 'man'
#t1.phone = '143323213'  # 这句会报错：AttributeError: 'Teacher' object has no attribute 'phone'
print('t1 \'s properties : ','name=',t1.name,',set = ',t1.sex)

# 在继承体系下，父类的 slots并不能限制子类的属性设置
class CollegeTeacher(Teacher):
    pass

t2 = CollegeTeacher()
t2.phone = '12321' # 虽然父类 Teacher限制了只能定义name和age，但是子类只遵照子类的__slots__设置，父类Teacher的__slots__限制对他不起作用，所以子类CollegeTeacher仍然能顺利定义phone属性
print('t2 \'s properties : ',' phone=',t2.phone)




print('--------------------------------------------------------------------','\n')
print('--------------------------------------------------------------------','\n')


"""
Test3 test class's static properties ------类级别变量
"""
class CollegeStudent(object):
    name = 'college student'   #类级别的属性，归类所有，对象也可以访问
    def __init__(self):
        pass

a = CollegeStudent()
print('a.name = ',a.name)
print('CollegeStudent.name = ',CollegeStudent.name,'\n')

a.name = 'Jone'  #对象只能修改对象的属性，并不能修改类级别属性
print('after change ,a.name = ',a.name)
print('after change ,CollegeStudent.name = ',CollegeStudent.name,'\n')

del(a.name) #对象只能修改对象的属性，并不能修改类级别属性
print('after delete ,a.name = ',a.name)
print('after delete ,CollegeStudent.name = ',CollegeStudent.name,'\n')

#del(a.name) #报错：AttributeError: name 已经将该实例对象的属性 name 删除了
#print('after again delete ,a.name = ',a.name)

#结论：类级别的变量和实例化后的对象的变量，尽量不要重名，否则会混乱得不到想要的值

print('--------------------------------------------------------------------','\n')
print('--------------------------------------------------------------------','\n')


"""
Test 4: @Property  
"""
class Bird(object):
    pass

bird = Bird()
bird.color = 'blue'            # setter method

print('bird \' property: color = ',bird.color,'\n')  # getter method

# 以上类的定义和实例的赋值等价于以下property用法

class Bird_1(object):
    @property
    def color(self):                # 这样相当于定义属性的一个getter方法
        return self._color

    @color.setter                    # 这样相当于定义属性的一个setter方法
    def color(self,color_value):
        if not isinstance(color_value,str):  # 对属性值的校验一般放在Setter方法中做，这样保证了实例化类再赋值的时候必须满足一定条件，而不是随便赋值
            raise ValueError('color must be an str!')
        self._color = color_value



bird_1 = Bird_1()
bird_1.color = 'Yellow'  # setter method

print('bird_1 \' property: color = ',bird_1.color,'\n')  # getter method








