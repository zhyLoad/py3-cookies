




# fetch point one
def point_one(list,r):
    print('list[',r,']', list[r])


# fetch iterator
def iterate_list(list):
    for i in range(list.__len__()):
        print('list_', i, ' = ', list[i])




list = ['tom','jerry','kette','alex','sandeson']
point_one(list,0)
point_one(list,1)
point_one(list,-1)
point_one(list,-2)
print('\n')

print('show the list:')
iterate_list(list)
print('\n')




# fetch by slice （切片）
list_1 = list[:3]
print('show the list_1:')
iterate_list(list_1)
print('\n')

list_2 = list[1:3]
print('show the list_2:')
iterate_list(list_2)
print('\n')

list_3 = list[-3:]
print('show the list_3:')
iterate_list(list_3)
print('\n')

list_4 = list[:] # 复制一个列表
print('show the list_4:')
iterate_list(list_4)
print('\n')

list_5 = list[:5:2]#第二个"："后表示每隔2个截取一次
print('show the list_5:')
iterate_list(list_5)
print('\n')

#Tuple 与List类似
t1 = ('a','b','c','d','e')[:3]
print('show tuple 1:')
iterate_list(t1)
print('\n')

t2 = ('a','b','c','d','e')[:4:2]
print('show tuple 2:')
iterate_list(t2)
print('\n')

#字符串可以作为List被切片
print('show string slice :','ABCDEFGH'[:6:2])