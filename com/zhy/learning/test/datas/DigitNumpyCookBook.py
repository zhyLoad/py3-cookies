
"""
简介numpy操作数组和矩阵
"""

import  numpy as np


#numpy----操作二维数组
#注意：传统的数组操作，并不能实现对数组中每一项统一操作，使用numpy可以方便的实现这个效果
xn = np.array([1,2,3,4])
yn = np.array([5,6,7,8])
print('array xn is ',xn,'\n array yn is ',yn)

print('xn+2=',xn+2)  #数组中每一项加2
print('xn*2=',xn*2)  #数组中每一项乘以2
#当两个数组操作时，实现的是数组中对等位置的数据元素的操作计算
print('xn+yn=',xn+yn)  #两个数组中每一项相加
print('xn*yn=',xn*yn)  #两个数组中每一项相乘

#使用场景举例：计算多项式的值：数组中每一项都做同一运算
def f(x):
    return x*3/4-x*x +34
print('xn*3/4-xn*xn+34 = ',f(xn))

#使用场景举例：对数组进行数学运算
print('sin(xn)=',np.sin(xn)) #对数组中各元素做数学计算，就不用迭代逐项操作了

#使用场景举例：构造一个很大的二维浮点数组(10000*10000)
# g = np.zeros(shape=(10000,10000),dtype=float)
# print('np.zeros(shape=(10000,10000),dtype=float) :\n',g)
# #对这个很大数组做数学运算
# print('cos(g): \n',np.cos(g))


#二维数组操作
aa = np.array([[1,3,2,4],[3,4,5,2],[1,3,4,6]])
print('aa :\n',aa)
#检索二维数组很方便
print('aa[1]: ',aa[1])   #取第二行
print('aa[:,1]: ',aa[:,1]) # 取第二列
print('aa[1:3,1:3] :\n ',aa[1:3,1:3]) #子二维数组
print('aa+[100,100,100,100] :\n ',aa+[100,102,104,108]) #每一行加某个指定的值
print('np.where(aa<5,aa,10) :\n',np.where(aa<5,aa,0)) #过滤每一项，按条件转化最终值,生成一个新的二维数组
print('\n')

#numpy----操作矩阵
xm = np.matrix([[1,3,2,5],[4,7,5,2],[3,5,3,8]])
print('xm ; \n',xm)
print('xm transpose:\n',xm.T) #求矩阵的转置
print('xm inverse:\n',xm.I) #求矩阵的逆