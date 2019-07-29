import calendar
import datetime

def get_day_of_last_week(year, month, dow):
    '''dow: Monday(0) - Sunday(6)'''
    n = calendar.monthrange(year, month)[1]
    l = range(n - 6, n + 1)
    w = calendar.weekday(year, month, l[0])
    w_l = [i % 7 for i in range(w, w + 7)]
    return l[w_l.index(dow)]

print(calendar.month(2019, 1))
#     January 2019
# Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6
#  7  8  9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30 31
# 

print(get_day_of_last_week(2019, 1, 0))
# 28

print(get_day_of_last_week(2019, 1, 3))
# 31

print(get_day_of_last_week(2019, 1, 4))
# 25

year = 2019
month = 1
dow = 0

n = calendar.monthrange(year, month)[1]
print(n)
# 31

l = range(n - 6, n + 1)
print(list(l))
# [25, 26, 27, 28, 29, 30, 31]

w = calendar.weekday(year, month, l[0])
print(w)
# 4

w_l = [i % 7 for i in range(w, w + 7)]
print(w_l)
# [4, 5, 6, 0, 1, 2, 3]

print(l[w_l.index(dow)])
# 28

def get_date_of_last_week(dt, dow):
    '''dow: Monday(0) - Sunday(6)'''
    return dt.replace(day=get_day_of_last_week(dt.year, dt.month, dow))

dt = datetime.datetime(2019, 1, 10, 10, 10, 10)
print(dt)
# 2019-01-10 10:10:10

print(get_date_of_last_week(dt, 0))
# 2019-01-28 10:10:10

print(get_date_of_last_week(dt, 3))
# 2019-01-31 10:10:10

d = datetime.date(2019, 1, 10)
print(d)
# 2019-01-10

print(get_date_of_last_week(d, 0))
# 2019-01-28

print(get_date_of_last_week(d, 3))
# 2019-01-31

def get_date_of_last_week2(year, month, dow):
    '''dow: Monday(0) - Sunday(6)'''
    return datetime.date(year, month, get_day_of_last_week(year, month, dow))

print(get_date_of_last_week2(2019, 1, 0))
# 2019-01-28
