import datetime

dt_naive = datetime.datetime(2018, 12, 31, 5, 0, 30, 1000)

print(dt_naive)
# 2018-12-31 05:00:30.001000

print(dt_naive.tzinfo)
# None

dt_aware = datetime.datetime(2018, 12, 31, 5, 0, 30, 1000,
                             tzinfo=datetime.timezone.utc)

print(dt_aware)
# 2018-12-31 05:00:30.001000+00:00

print(dt_aware.tzinfo)
# UTC

print(type(dt_aware.tzinfo))
# <class 'datetime.timezone'>

print(datetime.timezone.utc)
# UTC

print(type(datetime.timezone.utc))
# <class 'datetime.timezone'>

print(issubclass(type(datetime.timezone.utc), datetime.tzinfo))
# True

tz_jst = datetime.timezone(datetime.timedelta(hours=9))

print(tz_jst)
# UTC+09:00

print(type(tz_jst))
# <class 'datetime.timezone'>

tz_jst_name = datetime.timezone(datetime.timedelta(hours=9), name='JST')

print(tz_jst_name)
# JST

dt_utc = datetime.datetime(2018, 12, 31, 5, 0, 30, 1000,
                           tzinfo=datetime.timezone.utc)

print(dt_utc)
# 2018-12-31 05:00:30.001000+00:00

print(dt_utc.tzinfo)
# UTC

dt_jst = datetime.datetime(2018, 12, 31, 5, 0, 30, 1000,
                           tzinfo=datetime.timezone(datetime.timedelta(hours=9)))

print(dt_jst)
# 2018-12-31 05:00:30.001000+09:00

print(dt_jst.tzinfo)
# UTC+09:00
