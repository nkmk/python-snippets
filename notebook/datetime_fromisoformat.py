import datetime

s = '2018-12-31'

d = datetime.date.fromisoformat(s)

print(d)
# 2018-12-31

print(type(d))
# <class 'datetime.date'>

# print(datetime.date.fromisoformat('2018-12'))
# ValueError: Invalid isoformat string: '2018-12'

print(datetime.date.fromisoformat('2018-01-01'))
# 2018-01-01

# print(datetime.date.fromisoformat('2018-1-1'))
# ValueError: Invalid isoformat string: '2018-1-1'

s = '05:00:30.001000'

t = datetime.time.fromisoformat(s)

print(t)
# 05:00:30.001000

print(type(t))
# <class 'datetime.time'>

print(datetime.time.fromisoformat('05'))
# 05:00:00

# print(datetime.time.fromisoformat('5:00:30'))
# ValueError: Invalid isoformat string: '5:00:30'

s = '2018-12-31T05:00:30.001000'

dt = datetime.datetime.fromisoformat(s)

print(dt)
# 2018-12-31 05:00:30.001000

print(type(dt))
# <class 'datetime.datetime'>

print(datetime.datetime.fromisoformat('2018-12-31x05:00:30.001000'))
# 2018-12-31 05:00:30.001000

# print(datetime.datetime.fromisoformat('2018-12-31xx05:00:30.001000'))
# ValueError: Invalid isoformat string: '2018-12-31xx05:00:30.001000'

print(datetime.datetime.fromisoformat('2018-12-31T05'))
# 2018-12-31 05:00:00

print(datetime.datetime.fromisoformat('2018-12-31'))
# 2018-12-31 00:00:00

# print(datetime.datetime.fromisoformat('2018-12-31T5:00'))
# ValueError: Invalid isoformat string: '2018-12-31T5:00'

s = '2018-12-31T05:00:30.001000'

# print(datetime.date.fromisoformat(s))
# ValueError: Invalid isoformat string: '2018-12-31T05:00:30.001000'

# print(datetime.time.fromisoformat(s))
# ValueError: Invalid isoformat string: '2018-12-31T05:00:30.001000'

d = datetime.datetime.fromisoformat(s).date()

print(d)
# 2018-12-31

print(type(d))
# <class 'datetime.date'>

t = datetime.datetime.fromisoformat(s).time()

print(t)
# 05:00:30.001000

print(type(t))
# <class 'datetime.time'>

s = '2018-12-31T05:00:30'

s_basic = s.replace('-', '').replace(':', '')

print(s_basic)
# 20181231T050030

s = '2018-12-31T05:00:30.001000'

s_basic = s.split('.')[0].replace('-', '').replace(':', '')

print(s_basic)
# 20181231T050030

s_ex = datetime.datetime.strptime(s_basic, '%Y%m%dT%H%M%S').isoformat()

print(s_ex)
# 2018-12-31T05:00:30
