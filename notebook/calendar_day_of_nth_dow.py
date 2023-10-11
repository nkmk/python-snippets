import calendar
import datetime

def get_day_of_nth_dow(year, month, nth, dow):
    '''dow: Monday(0) - Sunday(6)'''
    if nth < 1 or dow < 0 or dow > 6:
        return None

    first_dow, n = calendar.monthrange(year, month)
    day = 7 * (nth - 1) + (dow - first_dow) % 7 + 1

    return day if day <= n else None

print(calendar.month(2023, 8))
#     August 2023
# Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6
#  7  8  9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30 31
# 

print(get_day_of_nth_dow(2023, 8, 1, 1))  # 1st Tuesday(1)
# 1

print(get_day_of_nth_dow(2023, 8, 2, 0))  # 2nd Monday(0)
# 14

print(get_day_of_nth_dow(2023, 8, 3, 6))  # 3rd Sunday(6)
# 20

print(get_day_of_nth_dow(2023, 8, 5, 3))  # 5th Thursday(3)
# 31

print(get_day_of_nth_dow(2023, 8, 5, 4))
# None

print(get_day_of_nth_dow(2023, 8, 0, 4))
# None

print(get_day_of_nth_dow(2023, 8, 1, 10))
# None

print(get_day_of_nth_dow(2023, 8, 2, 1.8))
# 8.8

def get_date_of_nth_dow(year, month, nth, dow):
    day = get_day_of_nth_dow(year, month, nth, dow)
    return datetime.date(year, month, day) if day else None

print(get_date_of_nth_dow(2023, 8, 1, 1))
# 2023-08-01

print(get_date_of_nth_dow(2023, 8, 1, 10))
# None

# print(get_date_of_nth_dow(2023, 8, 2, 1.8))
# TypeError: 'float' object cannot be interpreted as an integer

print([(m, get_day_of_nth_dow(2023, m, 2, 0)) for m in range(1, 13)])
# [(1, 9), (2, 13), (3, 13), (4, 10), (5, 8), (6, 12), (7, 10), (8, 14), (9, 11), (10, 9), (11, 13), (12, 11)]

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
