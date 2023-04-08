import datetime

s = '2023-04-01T05:00:30.001000'
dt = datetime.datetime.fromisoformat(s)
print(dt)
# 2023-04-01 05:00:30.001000

print(dt.tzinfo)
# None

s = '2023-04-01T05:00:30.001000+09:00'
dt = datetime.datetime.fromisoformat(s)
print(dt)
# 2023-04-01 05:00:30.001000+09:00

print(dt.tzinfo)
# UTC+09:00

print(dt.isoformat())
# 2023-04-01T05:00:30.001000+09:00

s = '2023-04-01T05:00:30.001000Z'
dt = datetime.datetime.fromisoformat(s)
print(dt)
# 2023-04-01 05:00:30.001000+00:00

print(dt.tzinfo)
# UTC

s = '2023-04-01T05:00:30.001000Z'
dt_utc = datetime.datetime.fromisoformat(s.replace('Z', '+00:00'))
print(dt_utc)
# 2023-04-01 05:00:30.001000+00:00

print(dt_utc.tzinfo)
# UTC

dt_none = datetime.datetime.fromisoformat(s.replace('Z', ''))
print(dt_none)
# 2023-04-01 05:00:30.001000

print(dt_none.tzinfo)
# None
