

"""
数字与二进制、八进制、十六进制的转化
"""


#整数  -> 二进制
print('bin(1234)=',bin(1234))
print('after format :',format(1234,'b')) #不输出0b前缀，直接输出完整二进制数
#整数  -> 八进制
print('oct(1234)=',oct(1234))
print('after format :',format(1234,'o'))#不输出0o前缀，直接输出八进制数
#整数  -> 十六进制
print('hex(1234)=',hex(1234))
print('after format :',format(1234,'x'))#不输出0x前缀，直接输出十六进制数

#指定最大位数长度，例如显示32位长的值
print('format(2**32+(-1234),"b")',format(2**32+(-1234),'b')) #二进制
print('format(2**32+(-1234),"x")',format(2**32+(-1234),'x')) #十六进制

#二进制  -> 整数
print('int("10011010010",2)=',int('10011010010',2))
print('int("0b10011010010",2)=',int('0b10011010010',2))
#八进制  ->  整数
print('int("0o2322",8)=',int('0o2322',8))
print('int("2322",8)=',int('2322',8))
#十六进制 -> 整数
print('int("0x4d2",8)=',int('0x4d2',16))
print('int("4d2",8)=',int('4d2',16))
print('\n\n')