import datetime

dt1 = datetime.datetime(year=2017, month=10, day=10, hour=15)

print(dt1)
# 2017-10-10 15:00:00

print(type(dt1))
# <class 'datetime.datetime'>

dt2 = datetime.datetime(year=2019, month=1, day=1, hour=12)

print(dt2)
# 2019-01-01 12:00:00

td = dt2 - dt1

print(td)
# 447 days, 21:00:00

print(type(td))
# <class 'datetime.timedelta'>

print(td.days)
# 447

print(td.seconds)
# 75600

print(td.microseconds)
# 0

print(td.total_seconds())
# 38696400.0

td_m = dt1 - dt2

print(td_m)
# -448 days, 3:00:00

print(td_m.days)
# -448

print(td_m.seconds)
# 10800

print(td_m.total_seconds())
# -38696400.0

td_abs = abs(dt1 - dt2)

print(td_abs)
# 447 days, 21:00:00

print(td_abs.days)
# 447

print(td_abs.seconds)
# 75600

print(td_abs.total_seconds())
# 38696400.0

d1 = datetime.date(year=2017, month=10, day=10)

print(d1)
# 2017-10-10

print(type(d1))
# <class 'datetime.date'>

d2 = datetime.date(year=2019, month=1, day=1)

print(d2)
# 2019-01-01

td = abs(d1 - d2)

print(td)
# 448 days, 0:00:00

print(type(td))
# <class 'datetime.timedelta'>

# print(dt2 - d1)
# TypeError: unsupported operand type(s) for -: 'datetime.datetime' and 'datetime.date'

print(dt2.date())
# 2019-01-01

print(type(dt2.date()))
# <class 'datetime.date'>

print(dt2.date() - d1)
# 448 days, 0:00:00

print(datetime.datetime.combine(d1, datetime.time()))
# 2017-10-10 00:00:00

print(type(datetime.datetime.combine(d1, datetime.time())))
# <class 'datetime.datetime'>

print(dt2 - datetime.datetime.combine(d1, datetime.time()))
# 448 days, 12:00:00

print(datetime.datetime.now() - dt2)
# 34 days, 9:30:07.362784

print(datetime.date.today() - d2)
# 34 days, 0:00:00

td = datetime.timedelta(weeks=1, hours=20)

print(td)
# 7 days, 20:00:00

print(type(td))
# <class 'datetime.timedelta'>

print(dt1)
# 2017-10-10 15:00:00

print(dt1 + td)
# 2017-10-18 11:00:00

print(dt1 - td)
# 2017-10-02 19:00:00

print(d1)
# 2017-10-10

print(d1 + td)
# 2017-10-17

print(d1 - td)
# 2017-10-03
