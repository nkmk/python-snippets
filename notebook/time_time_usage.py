import time

ut = time.time()

print(ut)
# 1549281692.9876952

print(type(ut))
# <class 'float'>

start = time.time()

time.sleep(3)

t = time.time() - start

print(t)
# 3.001929998397827
