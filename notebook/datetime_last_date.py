import datetime
import calendar

print(calendar.monthrange(2023, 8))
# (1, 31)

print(calendar.monthrange(2023, 8)[1])
# 31

def get_last_date(dt):
    return dt.replace(day=calendar.monthrange(dt.year, dt.month)[1])

dt = datetime.datetime(2023, 8, 10, 10, 10, 10)
print(dt)
# 2023-08-10 10:10:10

print(get_last_date(dt))
# 2023-08-31 10:10:10

d = datetime.date(2023, 8, 10)
print(d)
# 2023-08-10

print(get_last_date(d))
# 2023-08-31

print(datetime.date.today())
# 2023-10-10

print(get_last_date(datetime.date.today()))
# 2023-10-31

def get_last_date2(year, month):
    return datetime.date(year, month, calendar.monthrange(year, month)[1])

print(get_last_date2(2023, 8))
# 2023-08-31
