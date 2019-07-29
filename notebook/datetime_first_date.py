import datetime

def get_first_date(dt):
    return dt.replace(day=1)

dt = datetime.datetime(2019, 1, 10, 10, 10, 10)
print(dt)
# 2019-01-10 10:10:10

print(get_first_date(dt))
# 2019-01-01 10:10:10

d = datetime.date(2019, 1, 10)
print(d)
# 2019-01-10

print(get_first_date(d))
# 2019-01-01

print(datetime.date.today())
# 2019-07-29

print(get_first_date(datetime.date.today()))
# 2019-07-01

def get_first_date2(year, month):
    return datetime.date(year, month, 1)

print(get_first_date2(2019, 1))
# 2019-01-01
