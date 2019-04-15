import numpy as np

a = np.array([1, 100, 10])
print(a)
# [  1 100  10]

print(np.argmax(a))
# 1

a = np.array([1, 10, 10])
print(a)
# [ 1 10 10]

print(np.argmax(a))
# 1

a_2d = np.array([[20, 50, 30], [60, 40, 10]])
print(a_2d)
# [[20 50 30]
#  [60 40 10]]

print(np.argmax(a_2d))
# 3

print(a_2d.flatten())
# [20 50 30 60 40 10]

print(np.argmax(a_2d.flatten()))
# 3

print(np.argmax(a_2d, axis=0))
# [1 0 0]

print(np.max(a_2d, axis=0))
# [60 50 30]

print(np.argmax(a_2d, axis=1))
# [1 0]

print(np.max(a_2d, axis=1))
# [50 60]

idx = np.unravel_index(np.argmax(a_2d), a_2d.shape)
print(idx)
# (1, 0)

print(a_2d[idx])
# 60

print(np.max(a_2d))
# 60

a = np.array([1, 100, 10])
print(a)
# [  1 100  10]

print(a.argmax())
# 1

print(a.max())
# 100

a_2d = np.array([[20, 50, 30], [60, 40, 10]])
print(a_2d)
# [[20 50 30]
#  [60 40 10]]

print(a_2d.argmax())
# 3

print(a_2d.argmax(axis=0))
# [1 0 0]

print(a_2d.max(axis=0))
# [60 50 30]

print(a_2d.argmax(axis=1))
# [1 0]

print(a_2d.max(axis=1))
# [50 60]

print(np.unravel_index(a_2d.argmax(), a_2d.shape))
# (1, 0)
