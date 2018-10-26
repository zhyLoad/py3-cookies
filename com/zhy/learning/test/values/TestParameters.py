

#Test1 ： Set集合的交集和并集
set1 = set([1,2,3])
set2 = set([2,4])

print('set1 & set2',set1 & set2) #交集
print('set1 | set2',set1 | set2)  #并集



#Test2:可变和不可变的变量如何理解
list1 = [1,4,2,3]
list1.sort()
print('list :',list1)   #List是可变变量，当然可以被修改

a = 'abc'
a.replace('a','A')
print('a = ',a)
print('replace a : ',a.replace('a','A')) #字符串是不可变的，对字符串的操作只是创建了新的对象，原来的指向并没有变














