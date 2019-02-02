import datetime

dt = datetime.datetime.fromtimestamp(0)

print(dt)
# 1970-01-01 09:00:00

print(type(dt))
# <class 'datetime.datetime'>

print(dt.tzinfo)
# None

dt_utc_aware = datetime.datetime.fromtimestamp(0, datetime.timezone.utc)

print(dt_utc_aware)
# 1970-01-01 00:00:00+00:00

print(dt_utc_aware.tzinfo)
# UTC

dt_jst_aware = datetime.datetime.fromtimestamp(0, datetime.timezone(datetime.timedelta(hours=9)))

print(dt_jst_aware)
# 1970-01-01 09:00:00+09:00

print(dt_jst_aware.tzinfo)
# UTC+09:00

dt_utc_naive = datetime.datetime.utcfromtimestamp(0)

print(dt_utc_naive)
# 1970-01-01 00:00:00

print(dt_utc_naive.tzinfo)
# None

print(dt)
# 1970-01-01 09:00:00

print(dt.timestamp())
# 0.0

print(type(dt.timestamp()))
# <class 'float'>

print(dt_utc_aware)
# 1970-01-01 00:00:00+00:00

print(dt_utc_aware.timestamp())
# 0.0

print(dt_jst_aware)
# 1970-01-01 09:00:00+09:00

print(dt_jst_aware.timestamp())
# 0.0

print(dt_utc_naive)
# 1970-01-01 00:00:00

print(dt_utc_naive.timestamp())
# -32400.0
