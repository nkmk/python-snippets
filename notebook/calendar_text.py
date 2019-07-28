import calendar

print(calendar.month(2019, 1))
#     January 2019
# Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6
#  7  8  9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30 31
# 

print(type(calendar.month(2019, 1)))
# <class 'str'>

print(calendar.month(2019, 1, w=3, l=2))
#         January 2019
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

calendar.prmonth(2019, 1)
#     January 2019
# Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6
#  7  8  9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30 31

print(calendar.calendar(2019))
#                                   2019
# 
#       January                   February                   March
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6                   1  2  3                   1  2  3
#  7  8  9 10 11 12 13       4  5  6  7  8  9 10       4  5  6  7  8  9 10
# 14 15 16 17 18 19 20      11 12 13 14 15 16 17      11 12 13 14 15 16 17
# 21 22 23 24 25 26 27      18 19 20 21 22 23 24      18 19 20 21 22 23 24
# 28 29 30 31               25 26 27 28               25 26 27 28 29 30 31
# 
#        April                      May                       June
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#  1  2  3  4  5  6  7             1  2  3  4  5                      1  2
#  8  9 10 11 12 13 14       6  7  8  9 10 11 12       3  4  5  6  7  8  9
# 15 16 17 18 19 20 21      13 14 15 16 17 18 19      10 11 12 13 14 15 16
# 22 23 24 25 26 27 28      20 21 22 23 24 25 26      17 18 19 20 21 22 23
# 29 30                     27 28 29 30 31            24 25 26 27 28 29 30
# 
#         July                     August                  September
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#  1  2  3  4  5  6  7                1  2  3  4                         1
#  8  9 10 11 12 13 14       5  6  7  8  9 10 11       2  3  4  5  6  7  8
# 15 16 17 18 19 20 21      12 13 14 15 16 17 18       9 10 11 12 13 14 15
# 22 23 24 25 26 27 28      19 20 21 22 23 24 25      16 17 18 19 20 21 22
# 29 30 31                  26 27 28 29 30 31         23 24 25 26 27 28 29
#                                                     30
# 
#       October                   November                  December
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6                   1  2  3                         1
#  7  8  9 10 11 12 13       4  5  6  7  8  9 10       2  3  4  5  6  7  8
# 14 15 16 17 18 19 20      11 12 13 14 15 16 17       9 10 11 12 13 14 15
# 21 22 23 24 25 26 27      18 19 20 21 22 23 24      16 17 18 19 20 21 22
# 28 29 30 31               25 26 27 28 29 30         23 24 25 26 27 28 29
#                                                     30 31
# 

print(type(calendar.calendar(2019)))
# <class 'str'>

print(calendar.calendar(2019, c=3, m=4))
#                                            2019
# 
#       January                February                March                  April
# Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6                1  2  3                1  2  3    1  2  3  4  5  6  7
#  7  8  9 10 11 12 13    4  5  6  7  8  9 10    4  5  6  7  8  9 10    8  9 10 11 12 13 14
# 14 15 16 17 18 19 20   11 12 13 14 15 16 17   11 12 13 14 15 16 17   15 16 17 18 19 20 21
# 21 22 23 24 25 26 27   18 19 20 21 22 23 24   18 19 20 21 22 23 24   22 23 24 25 26 27 28
# 28 29 30 31            25 26 27 28            25 26 27 28 29 30 31   29 30
# 
#         May                    June                   July                  August
# Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su
#        1  2  3  4  5                   1  2    1  2  3  4  5  6  7             1  2  3  4
#  6  7  8  9 10 11 12    3  4  5  6  7  8  9    8  9 10 11 12 13 14    5  6  7  8  9 10 11
# 13 14 15 16 17 18 19   10 11 12 13 14 15 16   15 16 17 18 19 20 21   12 13 14 15 16 17 18
# 20 21 22 23 24 25 26   17 18 19 20 21 22 23   22 23 24 25 26 27 28   19 20 21 22 23 24 25
# 27 28 29 30 31         24 25 26 27 28 29 30   29 30 31               26 27 28 29 30 31
# 
#      September               October                November               December
# Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su   Mo Tu We Th Fr Sa Su
#                    1       1  2  3  4  5  6                1  2  3                      1
#  2  3  4  5  6  7  8    7  8  9 10 11 12 13    4  5  6  7  8  9 10    2  3  4  5  6  7  8
#  9 10 11 12 13 14 15   14 15 16 17 18 19 20   11 12 13 14 15 16 17    9 10 11 12 13 14 15
# 16 17 18 19 20 21 22   21 22 23 24 25 26 27   18 19 20 21 22 23 24   16 17 18 19 20 21 22
# 23 24 25 26 27 28 29   28 29 30 31            25 26 27 28 29 30      23 24 25 26 27 28 29
# 30                                                                   30 31
# 

calendar.prcal(2019)
#                                   2019
# 
#       January                   February                   March
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6                   1  2  3                   1  2  3
#  7  8  9 10 11 12 13       4  5  6  7  8  9 10       4  5  6  7  8  9 10
# 14 15 16 17 18 19 20      11 12 13 14 15 16 17      11 12 13 14 15 16 17
# 21 22 23 24 25 26 27      18 19 20 21 22 23 24      18 19 20 21 22 23 24
# 28 29 30 31               25 26 27 28               25 26 27 28 29 30 31
# 
#        April                      May                       June
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#  1  2  3  4  5  6  7             1  2  3  4  5                      1  2
#  8  9 10 11 12 13 14       6  7  8  9 10 11 12       3  4  5  6  7  8  9
# 15 16 17 18 19 20 21      13 14 15 16 17 18 19      10 11 12 13 14 15 16
# 22 23 24 25 26 27 28      20 21 22 23 24 25 26      17 18 19 20 21 22 23
# 29 30                     27 28 29 30 31            24 25 26 27 28 29 30
# 
#         July                     August                  September
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#  1  2  3  4  5  6  7                1  2  3  4                         1
#  8  9 10 11 12 13 14       5  6  7  8  9 10 11       2  3  4  5  6  7  8
# 15 16 17 18 19 20 21      12 13 14 15 16 17 18       9 10 11 12 13 14 15
# 22 23 24 25 26 27 28      19 20 21 22 23 24 25      16 17 18 19 20 21 22
# 29 30 31                  26 27 28 29 30 31         23 24 25 26 27 28 29
#                                                     30
# 
#       October                   November                  December
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6                   1  2  3                         1
#  7  8  9 10 11 12 13       4  5  6  7  8  9 10       2  3  4  5  6  7  8
# 14 15 16 17 18 19 20      11 12 13 14 15 16 17       9 10 11 12 13 14 15
# 21 22 23 24 25 26 27      18 19 20 21 22 23 24      16 17 18 19 20 21 22
# 28 29 30 31               25 26 27 28 29 30         23 24 25 26 27 28 29
#                                                     30 31

calendar.setfirstweekday(calendar.SUNDAY)

print(calendar.month(2019, 1))
#     January 2019
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

print(calendar.month(2019, 1))
#     January 2019
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

print(ltc_de.formatmonth(2019, 1))
#     Januar 2019
# Mo Di Mi Do Fr Sa So
#     1  2  3  4  5  6
#  7  8  9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30 31
# 

ltc_ja = calendar.LocaleTextCalendar(locale='ja_jp')

print(ltc_ja.formatmonth(2019, 1))
#       1月 2019
# 月  火  水  木  金  土  日
#     1  2  3  4  5  6
#  7  8  9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30 31
# 
