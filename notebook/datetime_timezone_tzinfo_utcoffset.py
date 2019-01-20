import datetime

dt_utc = datetime.datetime(2018, 12, 31, 5, 0, 30, 1000,
                           tzinfo=datetime.timezone.utc)

print(dt_utc.tzinfo)
# UTC

print(type(dt_utc.tzinfo))
# <class 'datetime.timezone'>

print(dt_utc.utcoffset())
# 0:00:00

print(type(dt_utc.utcoffset()))
# <class 'datetime.timedelta'>

dt_jst = datetime.datetime(2018, 12, 31, 5, 0, 30, 1000,
                           tzinfo=datetime.timezone(datetime.timedelta(hours=9)))

print(dt_jst.tzinfo)
# UTC+09:00

print(type(dt_jst.tzinfo))
# <class 'datetime.timezone'>

print(dt_jst.utcoffset())
# 9:00:00

print(type(dt_jst.utcoffset()))
# <class 'datetime.timedelta'>
