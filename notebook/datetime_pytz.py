import datetime
import pytz

jst = pytz.timezone('Asia/Tokyo')

print(jst)
# Asia/Tokyo

eastern = pytz.timezone('US/Eastern')

print(eastern)
# US/Eastern

print(type(jst))
# <class 'pytz.tzfile.Asia/Tokyo'>

print(issubclass(type(jst), datetime.tzinfo))
# True

dt_aware = datetime.datetime(2018, 12, 31, 5, 0, 30, 1000,
                             tzinfo=datetime.timezone.utc)

print(dt_aware)
# 2018-12-31 05:00:30.001000+00:00

print(dt_aware.astimezone(jst))
# 2018-12-31 14:00:30.001000+09:00

print(dt_aware.astimezone(eastern))
# 2018-12-31 00:00:30.001000-05:00

print(dt_aware.replace(tzinfo=jst))
# 2018-12-31 05:00:30.001000+09:19

print(dt_aware.replace(tzinfo=eastern))
# 2018-12-31 05:00:30.001000-04:56

print(jst.localize(dt_aware.replace(tzinfo=None)))
# 2018-12-31 05:00:30.001000+09:00

print(eastern.localize(dt_aware.replace(tzinfo=None)))
# 2018-12-31 05:00:30.001000-05:00

dt_naive = datetime.datetime(2018, 12, 31, 5, 0, 30, 1000)

print(dt_naive)
# 2018-12-31 05:00:30.001000

print(dt_naive.replace(tzinfo=jst))
# 2018-12-31 05:00:30.001000+09:19

print(dt_naive.replace(tzinfo=eastern))
# 2018-12-31 05:00:30.001000-04:56

print(jst.localize(dt_naive))
# 2018-12-31 05:00:30.001000+09:00

print(eastern.localize(dt_naive))
# 2018-12-31 05:00:30.001000-05:00

print(datetime.datetime(2018, 12, 31, 5, 0, 30, 1000,
                        tzinfo=jst))
# 2018-12-31 05:00:30.001000+09:19

print(jst.localize(datetime.datetime(2018, 12, 31, 5, 0, 30, 1000)))
# 2018-12-31 05:00:30.001000+09:00

print(datetime.datetime.now(jst))
# 2019-01-21 00:00:42.540529+09:00

dt_dst = datetime.datetime(2018, 3, 11, 2, 0, 0, 0)

print(eastern.localize(dt_dst))
# 2018-03-11 02:00:00-05:00

print(eastern.normalize(eastern.localize(dt_dst)))
# 2018-03-11 03:00:00-04:00
