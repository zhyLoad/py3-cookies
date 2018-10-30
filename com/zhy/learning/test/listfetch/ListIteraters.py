from collections import Iterable

# 1. 测试迭代Dict

dict_1 = {'a':1234,'b':332,'c':843,'d':3024,'e':952}

# print key one by one
for key in dict_1:
    print('key_',key)

# print value one by one
for value in dict_1.values():
    print('value_',value)

# print key and value one by one
for k,v in dict_1.items():
    print(k,':',v)

# print word in string one by one
for w in 'ABCDEFGHIJKLMN':
    print('word_',w)

# check a strut can be iterable
print('isinstance((12,32,434,123),Iterable) : ',isinstance((12,32,434,123),Iterable))
print('isinstance(123456,Iterable) : ',isinstance(123456,Iterable))

# to implements like 'for(i=0;i<xxx;i++)'
for i,v in enumerate(['tom','jerry','diff','wolf','duckTang']):
    print('i = ',i , ',the value = ',v)


# 2.测试迭代列表

def print_list(list):
    for v in list:
        print('list_value_', v)


list_1 = (1,2,3,4,5,6,7,8,9,10)
list_2 = [x*x for x in list_1]  # list 中每一项都平方计算
print_list(list_2)
print('\n')

list_3 = [m+n for m in 'ABC' for n in 'EFF'] # 双层循环实现全排列
print_list(list_3)
print('\n')

list_4 = [x*x for x in list_1 if x%2==0] # list中每一项平方计算，并且在结果列表中过滤偶数
print_list(list_4)
print('\n')

list_5 = ['adaf','qwerD','qewQ','tyaegfr']
list_6 = [t.upper() for t in list_5] # 将列表中字符串全部转化大写
print_list(list_6)
print('\n')

d = {'x': 'A', 'y': 'B', 'z': 'C' }
list_7 = [k+' = '+v for k,v in d.items()]  # 迭代Dict的又一种写法
print_list(list_7)