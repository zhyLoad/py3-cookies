

# 一、数字的四舍五入
#保留1位小数
from decimal import Decimal, localcontext

import math

print('round(1.23,1) = ',round(1.23,1))
print('round(1.27,1) = ',round(1.27,1))
print('round(1.25,1) = ',round(1.25,1)) #注意：四舍五入操作，当值为5时舍掉
print('round(-1.23,1) = ',round(-1.23,1))
print('round(-1.27,1) = ',round(-1.27,1))
print('round(-1.25,1) = ',round(-1.25,1))

print('round(1.2537,3) = ',round(1.2537,3)) #保留三位小数

print('round(12323,-3) = ',round(12323,-3))#第二个参数标识要舍入的位数，当为负数时，依次从十位、百位、千位往前推算。本例中-3标识精确到小数点之前的千位
print('round(12523,-3) = ',round(12523,-3)) #注意：边界值5被进位
print('round(12483,-3) = ',round(12483,-3)) #注意：只看边界值4，不看4后面有没有被进位
print('\n\n')





# 二、数字的精度
#使用浮点数做计算的前提是容忍微小的误差，不要企图用round函数去求出精确值。
#即： 要想保证精确值的计算和结果（例如钱数的计算）,几乎不允许有大的误差。则请不要使用round，而是使用decimal等数据类型
a = 2.1
b = 3.2
c =a + b
print('a+b = ',c)
print('round(a+b)',round(c,2)) #这是错误做法，并不能所有情况下都得到想要的值(不要企图用round函数去求出精确值)

#用Decimal替代上步的浮点计算，表面上看没什么区别
aa = Decimal('1.3')
bb = Decimal('1.7')
cc = aa+bb
print('in decimal, aa + bb = ',cc)
dd = aa/bb
print('in decimal, aa/ bb = ',dd)

# 但是Decimal最大的用途在下方，你可以得到任意精度的准确计算结果，没有任何舍入
with localcontext() as ctx:   #指定Decimal的上下文
    ctx.prec = 3
    print('ctx 1 : aa/ bb = ', aa/bb)

with localcontext() as ctx:
    ctx.prec = 50          # prec可以指定要精确到几位
    print('ctx 2 : aa/ bb = ', aa/bb)

# 注意:Decimal 最宜使用在金融计算等领域，这些场景下用户不允许任何细微的误差出现

#下方的例子计算错误：
nums = [1.23e+18,1,-1.23e+18]
print('[1.23e+18,1,-1.23e+18] get sums = ',sum(nums))
#解决办法是使用更精确的fsum来计算
print('[1.23e+18,1,-1.23e+18] get fsum = ',math.fsum(nums))
print('\n\n')








