
"""
分数
"""
from fractions import Fraction

#1/3
print('Fraction(1,3) = ',Fraction(1,3))
print('Fraction(1,3) numerator =  ',Fraction(1,3).numerator) #分子
print('Fraction(1,3) denominator =  ',Fraction(1,3).denominator) #分母

a = Fraction(1,3)
b = Fraction(2,5)
print('a = ',a,'  b = ',b)
#分数的加减乘除
print('a+b=',a+b)
print('a-b=',a-b)
print('a*b=',a*b)
print('a/b=',a/b)

#分数 -> 浮点数
print('float(a) = ',float(a))

#浮点数 ->  分数
print('Fraction(*3.75.as_integer_ratio())=',Fraction(*3.75.as_integer_ratio()))