import datetime

s = '2018/12/31 05:00:30+0900'

dt = datetime.datetime.strptime(s, '%Y/%m/%d %H:%M:%S%z')

print(dt)
# 2018-12-31 05:00:30+09:00

print(dt.tzinfo)
# UTC+09:00

s = '2018-12-31T05:00:30+09:00'

dt = datetime.datetime.fromisoformat(s)

print(dt)
# 2018-12-31 05:00:30+09:00

print(dt.tzinfo)
# UTC+09:00
