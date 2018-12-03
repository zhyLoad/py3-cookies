
"""
 数字的格式化
"""

#想要得到一定长度格式的小数，不要使用round，只需要format即可
x=1.2345
print('x = ',x)
print('format(x,"0.3f") = ',format(x,'0.3f'))

y=1234.56789
print('y = ',y)
print('format(y,">10.1f")=',format(y,'>10.1f'))  #四舍五入保留一位小数，一共显示10个字符，且向右调整
#以上格式化可以用%简写如下：
print('format(y,">10.1f") equals to "%10.1f" % y =','%10.1f' % y)
print('format(y,"<10.1f")=',format(y,'<10.1f'))  #四舍五入保留一位小数，一共显示10个字符，且向左调整
#以上格式化可以用%简写如下：
print('format(y,"<10.1f") equals to "%-10.1f" % y =','%-10.1f' % y)
print('format(y,"^10.1f")=',format(y,'^10.1f'))  #四舍五入保留一位小数，一共显示10个字符，且居中
print('format(y,",")=',format(y,','))              #在千位处加上逗号
print('format(y,"0,.1f")=',format(y,'0,.1f'))     #四舍五入保留一位小数，且在千位加逗号
#注意：以上操作可以等价于如下代码
print('the equal value {:0,.1f}'.format(y))  #同时制定精度和宽度的格式形如：'[<>^]?width[,]?(.digits)?'

#注意：'f'标识格式化浮点数，E或e可以格式化指数
print('format(y,"e")=',format(y,'e'))
print('format(y,"0.2e")=',format(y,'0.2e'))
print('\n\n')