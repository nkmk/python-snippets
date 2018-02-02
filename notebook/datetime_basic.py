import datetime

dt_now = datetime.datetime.now()
print(dt_now)
# 2018-02-02 18:31:13.271231

print(type(dt_now))
# <class 'datetime.datetime'>

print(dt_now.year)
# 2018

print(dt_now.hour)
# 18

dt = datetime.datetime(2018, 2, 1, 12, 15, 30, 2000)
print(dt)
# 2018-02-01 12:15:30.002000

print(dt.minute)
# 15

print(dt.microsecond)
# 2000

dt = datetime.datetime(2018, 2, 1)
print(dt)
# 2018-02-01 00:00:00

print(dt.minute)
# 0

print(dt_now)
print(type(dt_now))
# 2018-02-02 18:31:13.271231
# <class 'datetime.datetime'>

print(dt_now.date())
print(type(dt_now.date()))
# 2018-02-02
# <class 'datetime.date'>

d_today = datetime.date.today()
print(d_today)
# 2018-02-02

print(type(d_today))
# <class 'datetime.date'>

print(d_today.year)
# 2018

d = datetime.date(2018, 2, 1)
print(d)
# 2018-02-01

print(d.month)
# 2

t = datetime.time(12, 15, 30, 2000)
print(t)
# 12:15:30.002000

print(type(t))
# <class 'datetime.time'>

print(t.hour)
# 12

t = datetime.time()
print(t)
# 00:00:00

td = dt_now - dt
print(td)
# 1 day, 18:31:13.271231

print(type(td))
# <class 'datetime.timedelta'>

print(td.days)
# 1

print(td.seconds)
# 66673

print(td.microseconds)
# 271231

print(td.total_seconds())
# 153073.271231

td_1w = datetime.timedelta(weeks=1)
print(td_1w)
# 7 days, 0:00:00

print(td_1w.days)
# 7

d_1w = d_today - td_1w
print(d_1w)
# 2018-01-26

td_10d = datetime.timedelta(days=10)
print(td_10d)
# 10 days, 0:00:00

dt_10d = dt_now + td_10d
print(dt_10d)
# 2018-02-12 18:31:13.271231

td_50m = datetime.timedelta(minutes=50)
print(td_50m)
# 0:50:00

print(td_50m.seconds)
# 3000

dt_50m = dt_now + td_50m
print(dt_50m)
# 2018-02-02 19:21:13.271231

d_target = datetime.date(2020, 7, 24)
td = d_target - d_today
print(td)
# 903 days, 0:00:00

print(td.days)
# 903

print(dt_now.strftime('%Y-%m-%d %H:%M:%S'))
# 2018-02-02 18:31:13

print(d_today.strftime('%y%m%d'))
# 180202

print(d_today.strftime('%A, %B %d, %Y'))
# Friday, February 02, 2018

print(d_today.strftime('%Y年%m月%d日'))
# 2018年02月02日

print('日番号（1年の何日目か / 正月が001）:', d_today.strftime('%j'))
print('週番号（週の始まりは日曜日 / 正月が00）:', d_today.strftime('%U'))
print('週番号（週の始まりは月曜日 / 正月が00）:', d_today.strftime('%W'))
# 日番号（1年の何日目か / 正月が001）: 033
# 週番号（週の始まりは日曜日 / 正月が00）: 04
# 週番号（週の始まりは月曜日 / 正月が00）: 05

week_num_mon = int(d_today.strftime('%W'))
print(week_num_mon)
print(type(week_num_mon))
# 5
# <class 'int'>

d = datetime.date(2018, 2, 1)
td = datetime.timedelta(weeks=2)
n = 8
f = '%Y年%m月%d日'

l = []

for i in range(n):
    l.append((d + i * td).strftime(f))

print(l)
# ['2018年02月01日', '2018年02月15日', '2018年03月01日', '2018年03月15日', '2018年03月29日', '2018年04月12日', '2018年04月26日', '2018年05月10日']

print('\n'.join(l))
# 2018年02月01日
# 2018年02月15日
# 2018年03月01日
# 2018年03月15日
# 2018年03月29日
# 2018年04月12日
# 2018年04月26日
# 2018年05月10日

l = [(d + i * td).strftime(f) for i in range(n)]
print(l)
# ['2018年02月01日', '2018年02月15日', '2018年03月01日', '2018年03月15日', '2018年03月29日', '2018年04月12日', '2018年04月26日', '2018年05月10日']

date_str = '2018/2/1 12:30'
date_dt = datetime.datetime.strptime(date_str, '%Y/%m/%d %H:%M')
print(date_dt)
# 2018-02-01 12:30:00

print(type(date_dt))
# <class 'datetime.datetime'>

print(date_dt.strftime('%Y年%m月%d日 %H時%M分'))
# 2018年02月01日 12時30分

date_str = '2018年2月1日'
date_format = '%Y年%m月%d日'
td_10_d = datetime.timedelta(days=10)

date_dt = datetime.datetime.strptime(date_str, date_format)
date_dt_new = date_dt - td_10_d
date_str_new = date_dt_new.strftime(date_format)

print(date_str_new)
# 2018年01月22日
