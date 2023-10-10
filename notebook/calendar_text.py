import calendar

print(calendar.month(2023, 8))
#     August 2023
# Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6
#  7  8  9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30 31
# 

print(type(calendar.month(2023, 8)))
# <class 'str'>

print(calendar.month(2023, 8, w=3, l=2))
#         August 2023
# 
# Mon Tue Wed Thu Fri Sat Sun
# 
#       1   2   3   4   5   6
# 
#   7   8   9  10  11  12  13
# 
#  14  15  16  17  18  19  20
# 
#  21  22  23  24  25  26  27
# 
#  28  29  30  31
# 
# 

calendar.prmonth(2023, 8)
#     August 2023
# Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6
#  7  8  9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30 31

print(calendar.calendar(2023))
#                                   2023
# 
#       January                   February                   March
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#                    1             1  2  3  4  5             1  2  3  4  5
#  2  3  4  5  6  7  8       6  7  8  9 10 11 12       6  7  8  9 10 11 12
#  9 10 11 12 13 14 15      13 14 15 16 17 18 19      13 14 15 16 17 18 19
# 16 17 18 19 20 21 22      20 21 22 23 24 25 26      20 21 22 23 24 25 26
# 23 24 25 26 27 28 29      27 28                     27 28 29 30 31
# 30 31
# 
#        April                      May                       June
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#                 1  2       1  2  3  4  5  6  7                1  2  3  4
#  3  4  5  6  7  8  9       8  9 10 11 12 13 14       5  6  7  8  9 10 11
# 10 11 12 13 14 15 16      15 16 17 18 19 20 21      12 13 14 15 16 17 18
# 17 18 19 20 21 22 23      22 23 24 25 26 27 28      19 20 21 22 23 24 25
# 24 25 26 27 28 29 30      29 30 31                  26 27 28 29 30
# 
#         July                     August                  September
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#                 1  2          1  2  3  4  5  6                   1  2  3
#  3  4  5  6  7  8  9       7  8  9 10 11 12 13       4  5  6  7  8  9 10
# 10 11 12 13 14 15 16      14 15 16 17 18 19 20      11 12 13 14 15 16 17
# 17 18 19 20 21 22 23      21 22 23 24 25 26 27      18 19 20 21 22 23 24
# 24 25 26 27 28 29 30      28 29 30 31               25 26 27 28 29 30
# 31
# 
#       October                   November                  December
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#                    1             1  2  3  4  5                   1  2  3
#  2  3  4  5  6  7  8       6  7  8  9 10 11 12       4  5  6  7  8  9 10
#  9 10 11 12 13 14 15      13 14 15 16 17 18 19      11 12 13 14 15 16 17
# 16 17 18 19 20 21 22      20 21 22 23 24 25 26      18 19 20 21 22 23 24
# 23 24 25 26 27 28 29      27 28 29 30               25 26 27 28 29 30 31
# 30 31
# 

print(type(calendar.calendar(2023)))
# <class 'str'>

print(calendar.calendar(2023, c=3, m=4))
#                                            2023
# 
#       January                February                March                  April
# Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su
#                    1          1  2  3  4  5          1  2  3  4  5                   1  2
#  2  3  4  5  6  7  8    6  7  8  9 10 11 12    6  7  8  9 10 11 12    3  4  5  6  7  8  9
#  9 10 11 12 13 14 15   13 14 15 16 17 18 19   13 14 15 16 17 18 19   10 11 12 13 14 15 16
# 16 17 18 19 20 21 22   20 21 22 23 24 25 26   20 21 22 23 24 25 26   17 18 19 20 21 22 23
# 23 24 25 26 27 28 29   27 28                  27 28 29 30 31         24 25 26 27 28 29 30
# 30 31
# 
#         May                    June                   July                  August
# Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su
#  1  2  3  4  5  6  7             1  2  3  4                   1  2       1  2  3  4  5  6
#  8  9 10 11 12 13 14    5  6  7  8  9 10 11    3  4  5  6  7  8  9    7  8  9 10 11 12 13
# 15 16 17 18 19 20 21   12 13 14 15 16 17 18   10 11 12 13 14 15 16   14 15 16 17 18 19 20
# 22 23 24 25 26 27 28   19 20 21 22 23 24 25   17 18 19 20 21 22 23   21 22 23 24 25 26 27
# 29 30 31               26 27 28 29 30         24 25 26 27 28 29 30   28 29 30 31
#                                               31
# 
#      September               October                November               December
# Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su
#              1  2  3                      1          1  2  3  4  5                1  2  3
#  4  5  6  7  8  9 10    2  3  4  5  6  7  8    6  7  8  9 10 11 12    4  5  6  7  8  9 10
# 11 12 13 14 15 16 17    9 10 11 12 13 14 15   13 14 15 16 17 18 19   11 12 13 14 15 16 17
# 18 19 20 21 22 23 24   16 17 18 19 20 21 22   20 21 22 23 24 25 26   18 19 20 21 22 23 24
# 25 26 27 28 29 30      23 24 25 26 27 28 29   27 28 29 30            25 26 27 28 29 30 31
#                        30 31
# 

calendar.prcal(2023)
#                                   2023
# 
#       January                   February                   March
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#                    1             1  2  3  4  5             1  2  3  4  5
#  2  3  4  5  6  7  8       6  7  8  9 10 11 12       6  7  8  9 10 11 12
#  9 10 11 12 13 14 15      13 14 15 16 17 18 19      13 14 15 16 17 18 19
# 16 17 18 19 20 21 22      20 21 22 23 24 25 26      20 21 22 23 24 25 26
# 23 24 25 26 27 28 29      27 28                     27 28 29 30 31
# 30 31
# 
#        April                      May                       June
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#                 1  2       1  2  3  4  5  6  7                1  2  3  4
#  3  4  5  6  7  8  9       8  9 10 11 12 13 14       5  6  7  8  9 10 11
# 10 11 12 13 14 15 16      15 16 17 18 19 20 21      12 13 14 15 16 17 18
# 17 18 19 20 21 22 23      22 23 24 25 26 27 28      19 20 21 22 23 24 25
# 24 25 26 27 28 29 30      29 30 31                  26 27 28 29 30
# 
#         July                     August                  September
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#                 1  2          1  2  3  4  5  6                   1  2  3
#  3  4  5  6  7  8  9       7  8  9 10 11 12 13       4  5  6  7  8  9 10
# 10 11 12 13 14 15 16      14 15 16 17 18 19 20      11 12 13 14 15 16 17
# 17 18 19 20 21 22 23      21 22 23 24 25 26 27      18 19 20 21 22 23 24
# 24 25 26 27 28 29 30      28 29 30 31               25 26 27 28 29 30
# 31
# 
#       October                   November                  December
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#                    1             1  2  3  4  5                   1  2  3
#  2  3  4  5  6  7  8       6  7  8  9 10 11 12       4  5  6  7  8  9 10
#  9 10 11 12 13 14 15      13 14 15 16 17 18 19      11 12 13 14 15 16 17
# 16 17 18 19 20 21 22      20 21 22 23 24 25 26      18 19 20 21 22 23 24
# 23 24 25 26 27 28 29      27 28 29 30               25 26 27 28 29 30 31
# 30 31

calendar.setfirstweekday(calendar.SUNDAY)

print(calendar.month(2023, 8))
#     August 2023
# Su Mo Tu We Th Fr Sa
#        1  2  3  4  5
#  6  7  8  9 10 11 12
# 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26
# 27 28 29 30 31
# 

print(calendar.MONDAY)
# 0

print(calendar.SUNDAY)
# 6

calendar.setfirstweekday(0)

print(calendar.month(2023, 8))
#     August 2023
# Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6
#  7  8  9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30 31
# 

print(calendar.firstweekday())
# 0

ltc_de = calendar.LocaleTextCalendar(locale='de_de')

print(ltc_de.formatmonth(2023, 8))
#     August 2023
# Mo Di Mi Do Fr Sa So
#     1  2  3  4  5  6
#  7  8  9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30 31
# 

ltc_ja = calendar.LocaleTextCalendar(locale='ja_jp')

print(ltc_ja.formatmonth(2023, 8))
#       8月 2023
# 月  火  水  木  金  土  日
#     1  2  3  4  5  6
#  7  8  9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30 31
# 
