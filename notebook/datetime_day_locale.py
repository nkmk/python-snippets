import datetime
import locale

dt = datetime.datetime(2018, 1, 1)
print(dt)
# 2018-01-01 00:00:00

print(dt.strftime('%A, %a, %B, %b'))
# Monday, Mon, January, Jan

print(locale.getlocale(locale.LC_TIME))
# (None, None)

locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
print(locale.getlocale(locale.LC_TIME))
# ('ja_JP', 'UTF-8')

print(dt.strftime('%A, %a, %B, %b'))
# 月曜日, 月, 1月,  1

locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
print(dt.strftime('%A, %a, %B, %b'))
# Monday, Mon, January, Jan

locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')
print(dt.strftime('%A, %a, %B, %b'))
# Montag, Mo, Januar, Jan

locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')

s = '2018-01-01'
s_dow = datetime.datetime.strptime(s, '%Y-%m-%d').strftime('%A')

print(s_dow)
# 月曜日
