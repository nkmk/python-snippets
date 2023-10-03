import datetime

dt_now = datetime.datetime.now()
print(dt_now)
# 2023-10-03 21:12:49.683787

print(dt_now.tzinfo)
# None

dt_now_utc = datetime.datetime.now(datetime.timezone.utc)
print(dt_now_utc)
# 2023-10-03 12:12:49.689641+00:00

print(dt_now_utc.tzinfo)
# UTC

dt_now_jst = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
print(dt_now_jst)
# 2023-10-03 21:12:49.693979+09:00

print(dt_now_jst.tzinfo)
# UTC+09:00

dt_utcnow = datetime.datetime.utcnow()
print(dt_utcnow)
# 2023-10-03 12:12:49.697851

print(dt_utcnow.tzinfo)
# None
