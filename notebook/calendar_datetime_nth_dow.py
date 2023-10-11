import calendar
import datetime

print(calendar.month(2023, 8))
#     August 2023
# Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6
#  7  8  9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30 31
# 

def get_nth_week(day):
    return (day - 1) // 7 + 1

def get_nth_dow(year, month, day):
    return get_nth_week(day), calendar.weekday(year, month, day)

print(get_nth_dow(2023, 8, 7))
# (1, 0)

print(get_nth_dow(2023, 8, 20))
# (3, 6)

def get_nth_dow_datetime(year, month, day):
    return get_nth_week(day), datetime.date(year, month, day).weekday()

print(get_nth_dow_datetime(2023, 8, 7))
# (1, 0)

print(get_nth_dow_datetime(2023, 8, 20))
# (3, 6)

def get_nth_dow_datetime_dt(dt):
    return get_nth_week(dt.day), dt.weekday()

dt = datetime.datetime(2023, 8, 20)
print(get_nth_dow_datetime_dt(dt))
# (3, 6)

d = datetime.date(2023, 8, 20)
print(get_nth_dow_datetime_dt(d))
# (3, 6)

print(datetime.date.today())
# 2023-10-11

print(get_nth_dow_datetime_dt(datetime.date.today()))
# (2, 2)

print(calendar.month(2023, 8))
#     August 2023
# Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6
#  7  8  9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30 31
# 

calendar.setfirstweekday(6)
print(calendar.month(2023, 8))
#     August 2023
# Su Mo Tu We Th Fr Sa
#        1  2  3  4  5
#  6  7  8  9 10 11 12
# 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26
# 27 28 29 30 31
# 

def get_nth_week2(year, month, day, firstweekday=0):
    first_dow = calendar.monthrange(year, month)[0]
    offset = (first_dow - firstweekday) % 7
    return (day + offset - 1) // 7 + 1

print(get_nth_week2(2023, 8, 20))
# 3

print(get_nth_week2(2023, 8, 20, 6))
# 4

def get_nth_week2_datetime(year, month, day, firstweekday=0):
    first_dow = datetime.date(year, month, 1).weekday()
    offset = (first_dow - firstweekday) % 7
    return (day + offset - 1) // 7 + 1

print(get_nth_week2_datetime(2023, 8, 20))
# 3

print(get_nth_week2_datetime(2023, 8, 20, 6))
# 4

def get_nth_week2_datetime_dt(dt, firstweekday=0):
    first_dow = dt.replace(day=1).weekday()
    offset = (first_dow - firstweekday) % 7
    return (dt.day + offset - 1) // 7 + 1

dt = datetime.datetime(2023, 8, 20)
print(get_nth_week2_datetime_dt(dt))
# 3

print(get_nth_week2_datetime_dt(dt, 6))
# 4

d = datetime.date(2023, 8, 20)
print(get_nth_week2_datetime_dt(d))
# 3

print(get_nth_week2_datetime_dt(d, 6))
# 4

print(datetime.date.today())
# 2023-10-11

print(get_nth_week2_datetime_dt(datetime.date.today()))
# 3

print(get_nth_week2_datetime_dt(datetime.date.today(), 6))
# 2
