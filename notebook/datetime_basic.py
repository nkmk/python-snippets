import datetime

dt_now = datetime.datetime.now()
print(dt_now)
# 2023-04-08 23:08:13.873520

print(type(dt_now))
# <class 'datetime.datetime'>

print(dt_now.year)
# 2023

print(type(dt_now.year))
# <class 'int'>

print(datetime.datetime(2023, 4, 1, 20, 15, 30, 2000))
# 2023-04-01 20:15:30.002000

print(datetime.datetime(2023, 4, 1))
# 2023-04-01 00:00:00

dt = datetime.datetime(2023, 4, 1, 20, 15, 30, 2000)

d = dt.date()
print(d)
# 2023-04-01

print(type(d))
# <class 'datetime.date'>

t = dt.time()
print(t)
# 20:15:30.002000

print(type(t))
# <class 'datetime.time'>

print(datetime.datetime.combine(d, t))
# 2023-04-01 20:15:30.002000

d_today = datetime.date.today()
print(d_today)
# 2023-04-08

print(type(d_today))
# <class 'datetime.date'>

print(d_today.month)
# 4

print(datetime.date(2023, 4, 1))
# 2023-04-01

t_now = datetime.datetime.now().time()
print(t_now)
# 23:08:13.919031

print(type(t_now))
# <class 'datetime.time'>

print(t_now.microsecond)
# 919031

print(datetime.time(20, 15, 30, 2000))
# 20:15:30.002000

print(datetime.time())
# 00:00:00

dt1 = datetime.datetime(2023, 4, 1, 20, 15, 30, 2000)
dt2 = datetime.datetime(2023, 7, 1, 10, 45, 15, 100)

td = dt2 - dt1
print(td)
# 90 days, 14:29:44.998100

print(type(td))
# <class 'datetime.timedelta'>

print(td.days)
# 90

print(td.seconds)
# 52184

print(td.microseconds)
# 998100

print(td.total_seconds())
# 7828184.9981

td_1w = datetime.timedelta(weeks=1)
print(td_1w)
# 7 days, 0:00:00

print(td_1w.days)
# 7

dt = datetime.datetime(2023, 4, 1, 20, 15, 30, 2000)
print(dt)
# 2023-04-01 20:15:30.002000

print(dt - datetime.timedelta(weeks=1))
# 2023-03-25 20:15:30.002000

print(dt + datetime.timedelta(days=10))
# 2023-04-11 20:15:30.002000

print(dt + datetime.timedelta(minutes=50))
# 2023-04-01 21:05:30.002000

d_target = datetime.date(2023, 5, 1)
td = d_target - dt.date()
print(td)
# 30 days, 0:00:00

print(td.days)
# 30

dt = datetime.datetime(2023, 4, 1, 20, 15, 30, 2000)
print(dt.strftime('%Y/%m/%d %H:%M:%S.%f'))
# 2023/04/01 20:15:30.002000

print(dt.strftime('%A, %B %d, %Y'))
# Saturday, April 01, 2023

d = dt.date()
print(d.strftime('%Y/%m/%d %H:%M:%S.%f'))
# 2023/04/01 00:00:00.000000

t = dt.time()
print(t.strftime('%Y/%m/%d %H:%M:%S.%f'))
# 1900/01/01 20:15:30.002000

d = datetime.date(2023, 4, 1)
td = datetime.timedelta(weeks=2)
n = 4
f = '%Y/%m/%d'

l = [(d + i * td).strftime(f) for i in range(n)]
print(l)
# ['2023/04/01', '2023/04/15', '2023/04/29', '2023/05/13']

print('\n'.join(l))
# 2023/04/01
# 2023/04/15
# 2023/04/29
# 2023/05/13

s = '2023/4/1 20:30'
s_format = '%Y/%m/%d %H:%M'
dt = datetime.datetime.strptime(s, s_format)
print(dt)
# 2023-04-01 20:30:00

print(type(dt))
# <class 'datetime.datetime'>

print(dt.strftime('%Y%m%d_%H%M'))
# 20230401_2030

s = '2023/4/1'
s_format = '%Y/%m/%d'
td_10d = datetime.timedelta(days=10)

dt = datetime.datetime.strptime(s, s_format) - td_10d
print(dt.strftime(s_format))
# 2023/03/22
