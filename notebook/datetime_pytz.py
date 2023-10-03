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

dt_aware = datetime.datetime(2022, 12, 31, 5, 0, 30, 1000,
                             tzinfo=datetime.timezone.utc)
print(dt_aware)
# 2022-12-31 05:00:30.001000+00:00

print(dt_aware.astimezone(jst))
# 2022-12-31 14:00:30.001000+09:00

print(dt_aware.astimezone(eastern))
# 2022-12-31 00:00:30.001000-05:00

print(dt_aware.replace(tzinfo=jst))
# 2022-12-31 05:00:30.001000+09:19

print(dt_aware.replace(tzinfo=eastern))
# 2022-12-31 05:00:30.001000-04:56

print(jst.localize(dt_aware.replace(tzinfo=None)))
# 2022-12-31 05:00:30.001000+09:00

print(eastern.localize(dt_aware.replace(tzinfo=None)))
# 2022-12-31 05:00:30.001000-05:00

dt_naive = datetime.datetime(2022, 12, 31, 5, 0, 30, 1000)
print(dt_naive)
# 2022-12-31 05:00:30.001000

print(dt_naive.replace(tzinfo=jst))
# 2022-12-31 05:00:30.001000+09:19

print(dt_naive.replace(tzinfo=eastern))
# 2022-12-31 05:00:30.001000-04:56

print(jst.localize(dt_naive))
# 2022-12-31 05:00:30.001000+09:00

print(eastern.localize(dt_naive))
# 2022-12-31 05:00:30.001000-05:00

print(datetime.datetime(2022, 12, 31, 5, 0, 30, 1000,
                        tzinfo=jst))
# 2022-12-31 05:00:30.001000+09:19

print(jst.localize(datetime.datetime(2022, 12, 31, 5, 0, 30, 1000)))
# 2022-12-31 05:00:30.001000+09:00

print(datetime.datetime.now(jst))
# 2023-10-03 21:22:22.497686+09:00

dt_dst = datetime.datetime(2023, 3, 12, 2, 0, 0, 0)

print(eastern.localize(dt_dst))
# 2023-03-12 02:00:00-05:00

print(eastern.normalize(eastern.localize(dt_dst)))
# 2023-03-12 03:00:00-04:00
