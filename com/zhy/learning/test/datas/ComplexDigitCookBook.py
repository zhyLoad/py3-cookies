"""
 处理复数 ai+bj
"""

import cmath

print('complex(2,4)=',complex(2,4))
print('2+4j=',2+4j)
f = complex(2,4)
print('2+4j的实部：',f.real)
print('2+4j的虚部：',f.imag)
print('2+4j的共轭：',f.conjugate())
f1 = 2+4j
f2 = 3-5j
print('f1 = ',f1,'  ,f2 = ',f2)
print('f1+f2=',f1+f2)
print('f1-f2=',f1-f2)
print('f1*f2=',f1*f2)
print('f1/f2=',f1/f2)
print('|f2|=',abs(f2))
print('sin(f1)=',cmath.sin(f1))
print('cos(f1)=',cmath.cos(f1))
#注意，实际计算中不会返回负数值，要想得到复数值结果，需要显示调用
print('cmath.sqrt(-1)=',cmath.sqrt(-1)) #注意：若使用math.sqrt(-1)则会报错