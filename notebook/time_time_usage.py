import time
import datetime

ut = time.time()

print(ut)
# 1549094588.2293189

print(type(ut))
# <class 'float'>

print(datetime.datetime.fromtimestamp(ut))
# 2019-02-02 17:03:08.229319

print(datetime.datetime.now())
# 2019-02-02 17:03:08.259437

print(datetime.datetime.now(datetime.timezone.utc))
# 2019-02-02 08:03:08.266625+00:00

start = time.time()

time.sleep(3)

t = time.time() - start

print(t)
# 3.0013327598571777
