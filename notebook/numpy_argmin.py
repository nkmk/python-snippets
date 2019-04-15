import numpy as np

a = np.array([1, 100, 10])
print(a)
# [  1 100  10]

print(np.argmin(a))
# 0

print(a.argmin())
# 0

a_2d = np.array([[20, 50, 30], [60, 40, 10]])
print(a_2d)
# [[20 50 30]
#  [60 40 10]]

print(np.argmin(a_2d))
# 5

print(a_2d.argmin())
# 5

print(np.argmin(a_2d, axis=0))
# [0 1 1]

print(a_2d.argmin(axis=0))
# [0 1 1]

print(np.min(a_2d, axis=0))
# [20 40 10]

print(a_2d.min(axis=0))
# [20 40 10]

print(np.argmin(a_2d, axis=1))
# [0 2]

print(a_2d.argmin(axis=1))
# [0 2]

print(np.min(a_2d, axis=1))
# [20 10]

print(a_2d.min(axis=1))
# [20 10]

idx = np.unravel_index(np.argmin(a_2d), a_2d.shape)
print(idx)
# (1, 2)

print(a_2d[idx])
# 10

print(np.min(a_2d))
# 10

print(np.unravel_index(a_2d.argmin(), a_2d.shape))
# (1, 2)
