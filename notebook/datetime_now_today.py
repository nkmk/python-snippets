import datetime

dt_now = datetime.datetime.now()

print(dt_now)
# 2019-02-04 21:04:15.412854

print(type(dt_now))
# <class 'datetime.datetime'>

print(dt_now.tzinfo)
# None

print(dt_now.strftime('%Y年%m月%d日 %H:%M:%S'))
# 2019年02月04日 21:04:15

print(type(dt_now.strftime('%Y年%m月%d日 %H:%M:%S')))
# <class 'str'>

print(dt_now.isoformat())
# 2019-02-04T21:04:15.412854

print(type(dt_now.isoformat()))
# <class 'str'>

print(dt_now.year)
# 2019

print(dt_now.month)
# 2

print(dt_now.day)
# 4

print(dt_now.hour)
# 21

print(dt_now.minute)
# 4

print(dt_now.second)
# 15

print(dt_now.microsecond)
# 412854

print(type(dt_now.year))
# <class 'int'>

dt_now_utc_aware = datetime.datetime.now(datetime.timezone.utc)

print(dt_now_utc_aware)
# 2019-02-04 12:04:15.561748+00:00

print(dt_now_utc_aware.tzinfo)
# UTC

dt_now_jst_aware = datetime.datetime.now(
    datetime.timezone(datetime.timedelta(hours=9))
)

print(dt_now_jst_aware)
# 2019-02-04 21:04:15.591827+09:00

print(dt_now_jst_aware.tzinfo)
# UTC+09:00

dt_now_utc_naive = datetime.datetime.utcnow()

print(dt_now_utc_naive)
# 2019-02-04 12:04:15.621472

print(dt_now_utc_naive.tzinfo)
# None

d_today = datetime.date.today()

print(d_today)
# 2019-02-04

print(type(d_today))
# <class 'datetime.date'>

d_today_utc = datetime.datetime.utcnow().date()

print(d_today_utc)
# 2019-02-04

print(type(d_today_utc))
# <class 'datetime.date'>

t_now = datetime.datetime.now().time()

print(t_now)
# 21:04:15.782546

print(type(t_now))
# <class 'datetime.time'>

print(t_now.tzinfo)
# None

dt_now_utc_aware = datetime.datetime.now(datetime.timezone.utc)

print(dt_now_utc_aware)
# 2019-02-04 12:04:15.838464+00:00

print(dt_now_utc_aware.tzinfo)
# UTC

print(dt_now_utc_aware.time())
# 12:04:15.838464

print(dt_now_utc_aware.time().tzinfo)
# None

print(dt_now_utc_aware.timetz())
# 12:04:15.838464+00:00

print(dt_now_utc_aware.timetz().tzinfo)
# UTC
