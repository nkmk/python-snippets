import datetime

d1 = datetime.date(2010, 10, 1)
print(d1)
print(type(d1))
print(d1.year, d1.month, d1.day)
# 2010-10-01
# <class 'datetime.date'>
# 2010 10 1

d1_tt = d1.timetuple()
print(d1_tt)
print(type(d1_tt))
print(d1_tt.tm_year)
print(d1_tt[0])
# time.struct_time(tm_year=2010, tm_mon=10, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=4, tm_yday=274, tm_isdst=-1)
# <class 'time.struct_time'>
# 2010
# 2010

d2 = datetime.date.today()
print(d2)
# 2017-08-12

t = datetime.time(10, 5, 45)
print(t)
print(type(t))
print(t.hour, t.minute, t.second)
# 10:05:45
# <class 'datetime.time'>
# 10 5 45

dt1 = datetime.datetime(2001, 5, 10, 14, 10, 5)
print(dt1)
print(type(dt1))
print(dt1.year, dt1.month, dt1.day, dt1.hour, dt1.minute, dt1.second)
print(dt1.date())
print(dt1.time())
# 2001-05-10 14:10:05
# <class 'datetime.datetime'>
# 2001 5 10 14 10 5
# 2001-05-10
# 14:10:05

dt2 = datetime.datetime.now()
print(dt2)
print(dt2.microsecond)
# 2017-08-12 09:42:45.329713
# 329713

td1 = dt2 - dt1
print(td1)
print(type(td1))
print(td1.days, td1.seconds, td1.microseconds)
print(td1.total_seconds())
print(td1.days * 24 * 60 * 60 + td1.seconds + td1.microseconds / 1000000)
# 5937 days, 19:32:40.329713
# <class 'datetime.timedelta'>
# 5937 70360 329713
# 513027160.329713
# 513027160.329713

dt = datetime.datetime(2015, 3, 20, 20, 0, 10)
td = datetime.timedelta(days=100)
dt_a = dt + td
print(dt)
print(dt_a)
# 2015-03-20 20:00:10
# 2015-06-28 20:00:10

# https://docs.python.jp/3/library/datetime.html#strftime-strptime-behavior
dt = datetime.datetime(2015, 3, 20, 20, 0, 10)
print(dt)
print(dt.strftime('%Y/%m/%d(%a) %H:%M:%S'))
print(dt.strftime('%d %b. %Y'))
print(dt.strftime('%x %X'))
# 2015-03-20 20:00:10
# 2015/03/20(Fri) 20:00:10
# 20 Mar. 2015
# 03/20/15 20:00:10

s = '2010/4/1'
dts = datetime.datetime.strptime(s, '%Y/%m/%d')
print(dts)
print(dts.year, dts.hour)
print(type(dts))
# 2010-04-01 00:00:00
# 2010 0
# <class 'datetime.datetime'>
