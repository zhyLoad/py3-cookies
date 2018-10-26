#Test：数据类型相互转化
#str--> float
print("change 1:",float('234'))
#str--> int
print("change 2:",int('123'))
#str--> boolean
print("change 3-1:",bool('abcd'))
print("change 3-2:",bool(''))
print("change 3-3:",bool(' '))
print("change 3-4:",bool())
#float--> str
print("change 4:",str(123.43))
#float--> int
print("change 5:",int(123.43))
#float--> boolean
print("change 6-1:",bool(123.43))
print("change 6-2:",bool(0))
print("change 6-3:",bool(-123.34))
#int--> str
print("change 7:",str(123))
#int--> float
print("change 8:",float(123))
#int--> boolean
print("change 9-1:",bool(123))
print("change 9-2:",bool(-123))
