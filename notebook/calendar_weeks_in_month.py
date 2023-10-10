import calendar
import pprint

print(calendar.month(2023, 1))
#     January 2023
# Mo Tu We Th Fr Sa Su
#                    1
#  2  3  4  5  6  7  8
#  9 10 11 12 13 14 15
# 16 17 18 19 20 21 22
# 23 24 25 26 27 28 29
# 30 31
# 

pprint.pprint(calendar.monthcalendar(2023, 1))
# [[0, 0, 0, 0, 0, 0, 1],
#  [2, 3, 4, 5, 6, 7, 8],
#  [9, 10, 11, 12, 13, 14, 15],
#  [16, 17, 18, 19, 20, 21, 22],
#  [23, 24, 25, 26, 27, 28, 29],
#  [30, 31, 0, 0, 0, 0, 0]]

print(len(calendar.monthcalendar(2023, 1)))
# 6

calendar.setfirstweekday(calendar.SUNDAY)

print(calendar.month(2023, 1))
#     January 2023
# Su Mo Tu We Th Fr Sa
#  1  2  3  4  5  6  7
#  8  9 10 11 12 13 14
# 15 16 17 18 19 20 21
# 22 23 24 25 26 27 28
# 29 30 31
# 

pprint.pprint(calendar.monthcalendar(2023, 1))
# [[1, 2, 3, 4, 5, 6, 7],
#  [8, 9, 10, 11, 12, 13, 14],
#  [15, 16, 17, 18, 19, 20, 21],
#  [22, 23, 24, 25, 26, 27, 28],
#  [29, 30, 31, 0, 0, 0, 0]]

print(len(calendar.monthcalendar(2023, 1)))
# 5

print(calendar.MONDAY)
# 0

print(calendar.SUNDAY)
# 6

calendar.setfirstweekday(0)

print(calendar.firstweekday())
# 0
