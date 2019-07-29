import calendar
import datetime

dt = datetime.datetime(2019, 1, 1, 10, 10, 10)
print(dt)
# 2019-01-01 10:10:10

print(calendar.isleap(dt.year))
# False

d = datetime.date(2020, 1, 1)
print(d)
# 2020-01-01

print(calendar.isleap(d.year))
# True

def isleap_datetime(dt):
    return calendar.isleap(dt.year)

print(dt)
# 2019-01-01 10:10:10

print(isleap_datetime(dt))
# False

print(d)
# 2020-01-01

print(isleap_datetime(d))
# True

def isleap_datetime2(dt):
    return dt.year % 4 == 0 and (dt.year % 100 != 0 or dt.year % 400 == 0)

print(dt)
# 2019-01-01 10:10:10

print(isleap_datetime2(dt))
# False

print(d)
# 2020-01-01

print(isleap_datetime2(d))
# True
