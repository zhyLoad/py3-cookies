
"""
日期和时间
"""

from datetime import  timedelta,datetime


#1.时间长度
a = timedelta(days=2,hours=6)   #两天零6小时
print('a = timedelta(days=2,hours=6)')
print('a.days = ',a.days)  #两天
print('a.seconds = ',a.seconds) #六小时
print('a.microseconds = ',a.microseconds)
print('a.total_seconds() = ',a.total_seconds())

b = timedelta(hours=4.5)
print('b = timedelta(hours=4.5)')
c = a+b
print('c = a+b')
print('c.days = ',c.days)
print('c.seconds = ',c.seconds)
print('c.total_seconds() = ',c.total_seconds())
print('\n')


#2.具体日期
aa = datetime(2018,12,4,12,35,33)  #2018-12-04 12:35:33
print('aa = datetime(2018,12,4,12,35,33)')
print('aa = ',aa)
print('aa.year = ',aa.year)
print('aa.month = ',aa.month)
print('aa.day = ',aa.day)
print('aa.hour = ',aa.hour)
print('aa.minute = ',aa.minute)
print('aa.second = ',aa.second)
print('aa.timestamp() = ',aa.timestamp())
print('aa.timetuple() = ',aa.timetuple())
print('aa.timetz() = ',aa.timetz())
print('aa.tzname() = ',aa.tzname())
print('aa.time() = ',aa.time())
print('aa.ctime() = ',aa.ctime())
print('aa.date() = ',aa.date())
print('aa.dst() = ',aa.dst())
print('aa.isocalendar() = ',aa.isocalendar())
print('aa.isoweekday() = ',aa.isoweekday())
print('aa.weekday() = ',aa.weekday())
print('aa.utcoffset() = ',aa.utcoffset())
print('aa.utctimetuple() = ',aa.utctimetuple())
print('aa.toordinal() = ',aa.toordinal())
print('aa+timedelta(days=2) = ',aa+timedelta(days=2)) #加两天
bb = datetime(2018,12,6,11,32,33)
cc = bb-aa
print('cc = datetime(2018,12,6,11,32,33) - datetime(2018,12,4,12,35,33) = ',cc) #时间相减
print('cc.days',cc.days)
print('cc.total_seconds()',cc.total_seconds())
now = datetime.today()
print('current = ',now)
print('current + 10 minutes = ',now+timedelta(minutes=10))  #当前日期加10分钟
print('current - 1 day = ',now-timedelta(days=1))  #当前日期往前推一天（减一天）
#注意，日期的加减已经考虑了闰年的情况
print('part 1 : ',(datetime(2012,3,1)-datetime(2012,2,28)).days)
print('part 2 : ',(datetime(2013,3,1)-datetime(2013,2,28)).days)






