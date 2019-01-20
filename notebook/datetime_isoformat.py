import datetime

d = datetime.date(2018, 12, 31)

print(d)
# 2018-12-31

print(type(d))
# <class 'datetime.date'>

print(d.isoformat())
# 2018-12-31

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

dt = datetime.datetime(2018, 12, 31, 5, 0, 30, 1000)

print(dt)
# 2018-12-31 05:00:30.001000

print(type(dt))
# <class 'datetime.datetime'>

print(dt.isoformat())
# 2018-12-31T05:00:30.001000

print(type(dt.isoformat()))
# <class 'str'>

print(dt.isoformat(' '))
# 2018-12-31 05:00:30.001000

print(dt.isoformat('x'))
# 2018-12-31x05:00:30.001000

# print(dt.isoformat('xx'))
# TypeError: isoformat() argument 1 must be a unicode character, not str

print(dt.isoformat(timespec='hours'))
# 2018-12-31T05

print(dt.isoformat(timespec='minutes'))
# 2018-12-31T05:00

print(dt.isoformat(timespec='seconds'))
# 2018-12-31T05:00:30

print(dt.isoformat(timespec='milliseconds'))
# 2018-12-31T05:00:30.001

print(dt.isoformat(timespec='microseconds'))
# 2018-12-31T05:00:30.001000

print(dt.isoformat(' ', 'seconds'))
# 2018-12-31 05:00:30

print(dt.date())
# 2018-12-31

print(type(dt.date()))
# <class 'datetime.date'>

print(dt.date().isoformat())
# 2018-12-31

print(type(dt.date().isoformat()))
# <class 'str'>

print(dt.time())
# 05:00:30.001000

print(type(dt.time()))
# <class 'datetime.time'>

print(dt.time().isoformat())
# 05:00:30.001000

print(type(dt.time().isoformat()))
# <class 'str'>

print(dt.time().isoformat('seconds'))
# 05:00:30
