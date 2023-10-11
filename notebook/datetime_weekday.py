import datetime

dt = datetime.datetime(2023, 1, 1)
print(dt)
# 2023-01-01 00:00:00

print(dt.weekday())
# 6

print(type(dt.weekday()))
# <class 'int'>

print(dt.isoweekday())
# 7

print(type(dt.isoweekday()))
# <class 'int'>

d = datetime.date(2023, 1, 1)
print(d)
# 2023-01-01

print(d.weekday())
# 6

print(d.isoweekday())
# 7

dt = datetime.datetime(2023, 1, 1)

print(dt.strftime('%A'))
# Sunday

print(dt.strftime('%a'))
# Sun

import locale

locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
print(dt.strftime('%A'))
# Sunday

print(dt.strftime('%a'))
# Sun

locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')
print(dt.strftime('%A'))
# Sonntag

print(dt.strftime('%a'))
# So

locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
print(dt.strftime('%A'))
# 日曜日

print(dt.strftime('%a'))
# 日

w_list = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']

dt = datetime.datetime(2023, 1, 1)
d = datetime.date(2023, 1, 1)

print(w_list[dt.weekday()])
# Su

print(w_list[d.weekday()])
# Su
