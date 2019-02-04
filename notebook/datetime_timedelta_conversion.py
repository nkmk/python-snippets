import datetime

td = datetime.timedelta(weeks=1, days=1, hours=1, minutes=1,
                        seconds=1, milliseconds=1, microseconds=1)

print(td)
# 8 days, 1:01:01.001001

print(type(td))
# <class 'datetime.timedelta'>

print(datetime.timedelta(days=0.5, hours=-6, minutes=120))
# 8:00:00

td = datetime.timedelta(weeks=1, days=1, hours=1, minutes=1,
                        seconds=1, milliseconds=1, microseconds=1)

print(td)
# 8 days, 1:01:01.001001

print(type(td))
# <class 'datetime.timedelta'>

print(td.days)
# 8

print(type(td.days))
# <class 'int'>

print(td.seconds)
# 3661

print(type(td.seconds))
# <class 'int'>

print(td.microseconds)
# 1001

print(type(td.microseconds))
# <class 'int'>

print(td.total_seconds())
# 694861.001001

print(type(td.total_seconds()))
# <class 'float'>

print(td.days * 24 * 60 * 60 + td.seconds + td.microseconds / 1000000)
# 694861.001001

s = str(td)

print(s)
# 8 days, 1:01:01.001001

print(type(s))
# <class 'str'>

td = datetime.timedelta(days=1, hours=1, milliseconds=100)

sec = td.total_seconds()

print(sec)
# 90000.1

print(type(sec))
# <class 'float'>

sec = datetime.timedelta(days=1, hours=1, milliseconds=100).total_seconds()

print(sec)
# 90000.1

td = datetime.timedelta(seconds=123456.789)

print(td)
# 1 day, 10:17:36.789000

s = str(td)

print(s)
# 1 day, 10:17:36.789000

print(type(s))
# <class 'str'>

print(td.days)
# 1

print(td.seconds)
# 37056

print(td.microseconds)
# 789000

def get_h_m_s(td):
    m, s = divmod(td.seconds, 60)
    h, m = divmod(m, 60)
    return h, m, s

print(get_h_m_s(td))
# (10, 17, 36)

print(type(get_h_m_s(td)))
# <class 'tuple'>

h, m, s = get_h_m_s(td)

print(h)
# 10

print(m)
# 17

print(s)
# 36

def get_d_h_m_s_us(sec):
    td = datetime.timedelta(seconds=sec)
    m, s = divmod(td.seconds, 60)
    h, m = divmod(m, 60)
    return td.days, h, m, s, td.microseconds

print(get_d_h_m_s_us(123456.789))
# (1, 10, 17, 36, 789000)

print(get_d_h_m_s_us(123.456789))
# (0, 0, 2, 3, 456789)

td_m = datetime.timedelta(seconds=-123456.789)

print(td_m)
# -2 days, 13:42:23.211000

print(td_m.days)
# -2

print(td_m.seconds)
# 49343

print(td_m.microseconds)
# 211000

print(td_m.total_seconds())
# -123456.789

print(get_h_m_s(td_m))
# (13, 42, 23)

print(get_d_h_m_s_us(-123456.789))
# (-2, 13, 42, 23, 211000)

print(abs(td_m))
# 1 day, 10:17:36.789000

print(get_h_m_s(abs(td_m)))
# (10, 17, 36)

print(get_d_h_m_s_us(abs(-123456.789)))
# (1, 10, 17, 36, 789000)
