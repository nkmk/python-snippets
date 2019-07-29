import datetime
import calendar

print(calendar.monthrange(2019, 1))
# (1, 31)

print(calendar.monthrange(2019, 1)[1])
# 31

def get_last_date(dt):
    return dt.replace(day=calendar.monthrange(dt.year, dt.month)[1])

dt = datetime.datetime(2019, 1, 10, 10, 10, 10)
print(dt)
# 2019-01-10 10:10:10

print(get_last_date(dt))
# 2019-01-31 10:10:10

d = datetime.date(2019, 1, 10)
print(d)
# 2019-01-10

print(get_last_date(d))
# 2019-01-31

print(datetime.date.today())
# 2019-07-29

print(get_last_date(datetime.date.today()))
# 2019-07-31

def get_last_date2(year, month):
    return datetime.date(year, month, calendar.monthrange(year, month)[1])

print(get_last_date2(2019, 1))
# 2019-01-31
