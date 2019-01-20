import datetime

dt_now = datetime.datetime.now()

print(dt_now)
# 2019-01-20 23:53:16.711783

print(dt_now.tzinfo)
# None

dt_now_utc = datetime.datetime.now(datetime.timezone.utc)

print(dt_now_utc)
# 2019-01-20 14:53:16.735097+00:00

print(dt_now_utc.tzinfo)
# UTC

dt_now_jst = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))

print(dt_now_jst)
# 2019-01-20 23:53:16.758037+09:00

print(dt_now_jst.tzinfo)
# UTC+09:00

dt_utcnow = datetime.datetime.utcnow()

print(dt_utcnow)
# 2019-01-20 14:53:16.802029

print(dt_utcnow.tzinfo)
# None
