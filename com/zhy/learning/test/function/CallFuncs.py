from DefSomeFuncs import my_abs,nullMethod,multiResultMethod

print("test my_abs 1 ",my_abs(-3))
print("test my_abs 2 ",my_abs(123.123))
#print("test my_abs error ",my_abs('12341'))   # test the exception handler

print('null method return :',nullMethod())

x,y = multiResultMethod(12,34)
print('call the multiResultMethod 1:',x,y)
r = multiResultMethod(12,34)
print('call the multiResultMethod 2:',r)  #注意：多返回值的函数，如果用一个变量指向结果，类型是个tupe
r = multiResultMethod('qew',34)  # test the exception handler
