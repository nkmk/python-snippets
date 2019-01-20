import datetime

s = '2018-12-31T05:00:30.001000'

dt = datetime.datetime.fromisoformat(s)
print(dt)
# 2018-12-31 05:00:30.001000

print(dt.tzinfo)
# None

s = '2018-12-31T05:00:30.001000+09:00'

dt = datetime.datetime.fromisoformat(s)

print(dt)
# 2018-12-31 05:00:30.001000+09:00

print(dt.tzinfo)
# UTC+09:00

print(dt.isoformat())
# 2018-12-31T05:00:30.001000+09:00

s = '2018-12-31T05:00:30.001000Z'

# dt = datetime.datetime.fromisoformat(s)
# ValueError: Invalid isoformat string: '2018-12-31T05:00:30.001000Z'

print(s.replace('Z', '+00:00'))
# 2018-12-31T05:00:30.001000+00:00

dt_utc = datetime.datetime.fromisoformat(s.replace('Z', '+00:00'))

print(dt_utc)
# 2018-12-31 05:00:30.001000+00:00

print(dt_utc.tzinfo)
# UTC

print(s.replace('Z', ''))
# 2018-12-31T05:00:30.001000

dt_none = datetime.datetime.fromisoformat(s.replace('Z', ''))

print(dt_none)
# 2018-12-31 05:00:30.001000

print(dt_none.tzinfo)
# None
