

class Animal(object):
    def run(self):
        print("Animal is running ...")

class Dog(Animal):
    def run(self):
        print("Dog is running ...")



def run_twice(animal):
    animal.run()
    animal.run()


class Other(object):
    def run(self):
        print("other class's Running ...");





dog = Dog()  # 继承
dog.run() # 覆盖父类的方法
print("Dog is Animal :", isinstance(dog, Animal), '\n')

# 多态
print("begin to run twice:")
run_twice(Dog())
print("end to run twice!", '\n')

# Python 语言的动态语言特性：动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
# 只要有相同方法，不用继承类，也可以多态使用
print("begin to dark's  run twice:")
run_twice(Other())
print("end to run  dark'stwice!", '\n')

