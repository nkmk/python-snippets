import datetime

d = datetime.date(2023, 4, 1)
print(d)
# 2023-04-01

print(type(d))
# <class 'datetime.date'>

print(d.isoformat())
# 2023-04-01

print(type(d.isoformat()))
# <class 'str'>

t = datetime.time(5, 0, 30, 1000)
print(t)
# 05:00:30.001000

print(type(t))
# <class 'datetime.time'>

print(t.isoformat())
# 05:00:30.001000

print(type(t.isoformat()))
# <class 'str'>

print(t.isoformat('hours'))
# 05

print(t.isoformat('minutes'))
# 05:00

print(t.isoformat('seconds'))
# 05:00:30

print(t.isoformat('milliseconds'))
# 05:00:30.001

print(t.isoformat('microseconds'))
# 05:00:30.001000

dt = datetime.datetime(2023, 4, 1, 5, 0, 30, 1000)
print(dt)
# 2023-04-01 05:00:30.001000

print(type(dt))
# <class 'datetime.datetime'>

print(dt.isoformat())
# 2023-04-01T05:00:30.001000

print(type(dt.isoformat()))
# <class 'str'>

print(dt.isoformat(' '))
# 2023-04-01 05:00:30.001000

print(dt.isoformat('x'))
# 2023-04-01x05:00:30.001000

# print(dt.isoformat('xx'))
# TypeError: isoformat() argument 1 must be a unicode character, not str

print(dt.isoformat(timespec='hours'))
# 2023-04-01T05

print(dt.isoformat(timespec='minutes'))
# 2023-04-01T05:00

print(dt.isoformat(timespec='seconds'))
# 2023-04-01T05:00:30

print(dt.isoformat(timespec='milliseconds'))
# 2023-04-01T05:00:30.001

print(dt.isoformat(timespec='microseconds'))
# 2023-04-01T05:00:30.001000

print(dt.isoformat(' ', 'seconds'))
# 2023-04-01 05:00:30

print(dt.date().isoformat())
# 2023-04-01

print(dt.time().isoformat())
# 05:00:30.001000
