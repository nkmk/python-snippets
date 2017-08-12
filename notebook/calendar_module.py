# https://docs.python.jp/3/library/calendar.html

import calendar

print(calendar.calendar(2017))
#                                   2017
#       January                   February                   March
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#                    1             1  2  3  4  5             1  2  3  4  5
#  2  3  4  5  6  7  8       6  7  8  9 10 11 12       6  7  8  9 10 11 12
#  9 10 11 12 13 14 15      13 14 15 16 17 18 19      13 14 15 16 17 18 19
# 16 17 18 19 20 21 22      20 21 22 23 24 25 26      20 21 22 23 24 25 26
# 23 24 25 26 27 28 29      27 28                     27 28 29 30 31
# 30 31
#        April                      May                       June
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#                 1  2       1  2  3  4  5  6  7                1  2  3  4
#  3  4  5  6  7  8  9       8  9 10 11 12 13 14       5  6  7  8  9 10 11
# 10 11 12 13 14 15 16      15 16 17 18 19 20 21      12 13 14 15 16 17 18
# 17 18 19 20 21 22 23      22 23 24 25 26 27 28      19 20 21 22 23 24 25
# 24 25 26 27 28 29 30      29 30 31                  26 27 28 29 30
#         July                     August                  September
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#                 1  2          1  2  3  4  5  6                   1  2  3
#  3  4  5  6  7  8  9       7  8  9 10 11 12 13       4  5  6  7  8  9 10
# 10 11 12 13 14 15 16      14 15 16 17 18 19 20      11 12 13 14 15 16 17
# 17 18 19 20 21 22 23      21 22 23 24 25 26 27      18 19 20 21 22 23 24
# 24 25 26 27 28 29 30      28 29 30 31               25 26 27 28 29 30
# 31
#       October                   November                  December
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#                    1             1  2  3  4  5                   1  2  3
#  2  3  4  5  6  7  8       6  7  8  9 10 11 12       4  5  6  7  8  9 10
#  9 10 11 12 13 14 15      13 14 15 16 17 18 19      11 12 13 14 15 16 17
# 16 17 18 19 20 21 22      20 21 22 23 24 25 26      18 19 20 21 22 23 24
# 23 24 25 26 27 28 29      27 28 29 30               25 26 27 28 29 30 31
# 30 31

print(calendar.month(2100, 1))
#     January 2100
# Mo Tu We Th Fr Sa Su
#              1  2  3
#  4  5  6  7  8  9 10
# 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24
# 25 26 27 28 29 30 31

l = calendar.monthcalendar(2100, 1)
print(type(l))
print(l)
# <class 'list'>
# [[0, 0, 0, 0, 1, 2, 3], [4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30, 31]]

print(calendar.weekday(2001, 9, 11)) # Monday: 0, Sunday:6
# 1
