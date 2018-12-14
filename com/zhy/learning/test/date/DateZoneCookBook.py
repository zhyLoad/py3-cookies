
"""
处理带有时区的时间，使用pytz
"""
from datetime import  datetime,timedelta
from pytz import timezone, UTC

d = datetime(2018,12,14,23,34,23)

print('d = datetime(2018,12,14,23,34,23) : ',d)
print('\n')


#1) datetime 本地化
central = timezone('US/Central')  #美国时间
local_d = central.localize(d)
print('US time : ',local_d)

#2) 本地化之后就可以转化为指定时区的时间
appoint_d = d.astimezone(timezone('Asia/Hong_Kong')) #香港时间
print('HongKong time : ',appoint_d)
print('\n')

#注意：先本地化后转化指定时区的用法有缺陷：例如美国时区在时间的计算上要考虑夏令时间转化。推荐时区问题的解决都基于UTC时区时间

#将时间转化为UTC时间
utc_d = d.astimezone(UTC)
print('UTC time : ',utc_d)

#UTC时区时进行计算，然后将计算后的结果转化为想要的时区时间
caculate_utc_d = utc_d + timedelta(minutes=30)
print(' caculate time : ',caculate_utc_d)

#指定UTC时区时间为指定时区的时间
appoint_caculate_utc_d = caculate_utc_d.astimezone(central)
print('transfer caculate time to Central time : ',appoint_caculate_utc_d)




