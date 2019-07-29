import calendar
import datetime

def get_day_of_nth_dow(year, month, nth, dow):
    '''dow: Monday(0) - Sunday(6)'''
    if nth < 1 or dow < 0 or dow > 6:
        return None
    
    first_dow, n = calendar.monthrange(year, month)
    day = 7 * (nth - 1) + (dow - first_dow) % 7 + 1
    
    return day if day <= n else None

print(calendar.month(2019, 1))
#     January 2019
# Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6
#  7  8  9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30 31
# 

print(get_day_of_nth_dow(2019, 1, 1, 1))  # 1st Tuesday(1)
# 1

print(get_day_of_nth_dow(2019, 1, 2, 0))  # 2nd Monday(0)
# 14

print(get_day_of_nth_dow(2019, 1, 3, 6))  # 3rd Sunday(6)
# 20

print(get_day_of_nth_dow(2019, 1, 5, 3))  # 5th Thursday(3)
# 31

print(get_day_of_nth_dow(2019, 1, 5, 4))
# None

print(get_day_of_nth_dow(2019, 1, 0, 4))
# None

print(get_day_of_nth_dow(2019, 1, 1, 10))
# None

print(get_day_of_nth_dow(2019, 1, 2, 1.8))
# 8.8

def get_date_of_nth_dow(year, month, nth, dow):
    day = get_day_of_nth_dow(year, month, nth, dow)
    return datetime.date(year, month, day) if day else None

print(get_date_of_nth_dow(2019, 1, 1, 1))
# 2019-01-01

print(get_date_of_nth_dow(2019, 1, 1, 10))
# None

# print(get_date_of_nth_dow(2019, 1, 2, 1.8))
# TypeError: integer argument expected, got float

print([(m, get_day_of_nth_dow(2019, m, 2, 0)) for m in range(1, 13)])
# [(1, 14), (2, 11), (3, 11), (4, 8), (5, 13), (6, 10), (7, 8), (8, 12), (9, 9), (10, 14), (11, 11), (12, 9)]

for y in range(2020, 2030):
    print(get_date_of_nth_dow(y, 1, 2, 0))
# 2020-01-13
# 2021-01-11
# 2022-01-10
# 2023-01-09
# 2024-01-08
# 2025-01-13
# 2026-01-12
# 2027-01-11
# 2028-01-10
# 2029-01-08
