import datetime

dt_jst = datetime.datetime(2018, 12, 31, 5, 0, 30, 1000,
                           tzinfo=datetime.timezone(datetime.timedelta(hours=9)))

print(dt_jst)
# 2018-12-31 05:00:30.001000+09:00

print(dt_jst.tzinfo)
# UTC+09:00

dt_jst_to_utc = dt_jst.astimezone(datetime.timezone.utc)

print(dt_jst_to_utc)
# 2018-12-30 20:00:30.001000+00:00

print(dt_jst_to_utc.tzinfo)
# UTC

dt_jst_to_m5h = dt_jst.astimezone(datetime.timezone(datetime.timedelta(hours=-5)))

print(dt_jst_to_m5h)
# 2018-12-30 15:00:30.001000-05:00

print(dt_jst_to_m5h.tzinfo)
# UTC-05:00

dt_jst_to_utc_replace = dt_jst.replace(tzinfo=datetime.timezone.utc)

print(dt_jst_to_utc_replace)
# 2018-12-31 05:00:30.001000+00:00

print(dt_jst_to_utc_replace.tzinfo)
# UTC

dt_jst_to_naive = dt_jst.replace(tzinfo=None)

print(dt_jst_to_naive)
# 2018-12-31 05:00:30.001000

print(dt_jst_to_naive.tzinfo)
# None

dt_naive = datetime.datetime(2018, 12, 31, 5, 0, 30, 1000)

print(dt_naive)
# 2018-12-31 05:00:30.001000

print(dt_naive.tzinfo)
# None

dt_naive_to_utc_replace = dt_naive.replace(tzinfo=datetime.timezone.utc)

print(dt_naive_to_utc_replace)
# 2018-12-31 05:00:30.001000+00:00

print(dt_naive_to_utc_replace.tzinfo)
# UTC

dt_naive_to_jst_replace = dt_naive.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=9)))

print(dt_naive_to_jst_replace)
# 2018-12-31 05:00:30.001000+09:00

print(dt_naive_to_jst_replace.tzinfo)
# UTC+09:00

dt_naive_to_utc = dt_naive.astimezone(datetime.timezone.utc)

print(dt_naive_to_utc)
# 2018-12-30 20:00:30.001000+00:00

print(dt_naive_to_utc.tzinfo)
# UTC
