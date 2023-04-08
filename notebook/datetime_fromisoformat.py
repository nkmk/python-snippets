import datetime

d = datetime.date.fromisoformat('2023-04-01')
print(d)
# 2023-04-01

print(type(d))
# <class 'datetime.date'>

# print(datetime.date.fromisoformat('2023-04'))
# ValueError: Invalid isoformat string: '2023-04'

# print(datetime.date.fromisoformat('2023-4-1'))
# ValueError: Invalid isoformat string: '2023-4-1'

t = datetime.time.fromisoformat('05:00:30.001000')
print(t)
# 05:00:30.001000

print(type(t))
# <class 'datetime.time'>

print(datetime.time.fromisoformat('05'))
# 05:00:00

# print(datetime.time.fromisoformat('5:00:30'))
# ValueError: Invalid isoformat string: '5:00:30'

dt = datetime.datetime.fromisoformat('2023-04-01T05:00:30.001000')
print(dt)
# 2023-04-01 05:00:30.001000

print(type(dt))
# <class 'datetime.datetime'>

print(datetime.datetime.fromisoformat('2023-04-01x05:00:30.001000'))
# 2023-04-01 05:00:30.001000

# print(datetime.datetime.fromisoformat('2023-04-01xx05:00:30.001000'))
# ValueError: Invalid isoformat string: '2023-04-01xx05:00:30.001000'

print(datetime.datetime.fromisoformat('2023-04-01T05'))
# 2023-04-01 05:00:00

print(datetime.datetime.fromisoformat('2023-04-01'))
# 2023-04-01 00:00:00

# print(datetime.datetime.fromisoformat('2023-4-1T5:00'))
# ValueError: Invalid isoformat string: '2023-4-1T5:00'

s = '2023-04-01T05:00:30.001000'

# print(datetime.date.fromisoformat(s))
# ValueError: Invalid isoformat string: '2023-04-01T05:00:30.001000'

d = datetime.datetime.fromisoformat(s).date()
print(d)
# 2023-04-01

print(type(d))
# <class 'datetime.date'>

t = datetime.datetime.fromisoformat(s).time()
print(t)
# 05:00:30.001000

print(type(t))
# <class 'datetime.time'>

print(datetime.date.fromisoformat('20230401'))
# 2023-04-01

print(datetime.time.fromisoformat('050030.001000'))
# 05:00:30.001000

print(datetime.datetime.fromisoformat('20230401T050030.001000'))
# 2023-04-01 05:00:30.001000

print(datetime.datetime.strptime('20230401T050030.001000', '%Y%m%dT%H%M%S.%f'))
# 2023-04-01 05:00:30.001000

s = '2023-04-01T05:00:30.001000'
print(s.replace('-', '').replace(':', ''))
# 20230401T050030.001000

print(s.split('.')[0].replace('-', '').replace(':', ''))
# 20230401T050030

s_basic = '20230401T050030.001000'
print(datetime.datetime.fromisoformat(s_basic).isoformat())
# 2023-04-01T05:00:30.001000
