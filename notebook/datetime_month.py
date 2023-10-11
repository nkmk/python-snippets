import datetime

dt = datetime.datetime(2023, 1, 1)

print(dt.strftime('%B'))
# January

print(dt.strftime('%b'))
# Jan

import locale

locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
print(dt.strftime('%B'))
# January

print(dt.strftime('%b'))
# Jan

locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')
print(dt.strftime('%B'))
# Januar

print(dt.strftime('%b'))
# Jan

locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
print(dt.strftime('%B'))
# 1月

print(dt.strftime('%b'))
#  1

dt = datetime.datetime(2023, 1, 1)
print(dt.month)
# 1

print(type(dt.month))
# <class 'int'>

m_list = ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'June', 'July', 'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.']

print(m_list[dt.month - 1])
# Jan.

d = datetime.date(2023, 1, 1)
print(d.month)
# 1

print(m_list[d.month - 1])
# Jan.
