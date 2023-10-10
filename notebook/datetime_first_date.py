import datetime

def get_first_date(dt):
    return dt.replace(day=1)

dt = datetime.datetime(2023, 8, 10, 10, 10, 10)
print(dt)
# 2023-08-10 10:10:10

print(get_first_date(dt))
# 2023-08-01 10:10:10

d = datetime.date(2023, 8, 10)
print(d)
# 2023-08-10

print(get_first_date(d))
# 2023-08-01

print(datetime.date.today())
# 2023-10-10

print(get_first_date(datetime.date.today()))
# 2023-10-01

def get_first_date2(year, month):
    return datetime.date(year, month, 1)

print(get_first_date2(2023, 8))
# 2023-08-01
