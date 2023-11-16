import numpy as np

print(np.__version__)
# 1.26.1

a = np.arange(6).reshape(2, 3)
print(a)
# [[0 1 2]
#  [3 4 5]]

b = np.zeros_like(a)
print(b)
# [[0 0 0]
#  [0 0 0]]

print(a)
# [[0 1 2]
#  [3 4 5]]

a[:, :] = 0
print(a)
# [[0 0 0]
#  [0 0 0]]

a[:] = 1
print(a)
# [[1 1 1]
#  [1 1 1]]

print(a.dtype)
# int64

a[:] = 0.123
print(a)
# [[0 0 0]
#  [0 0 0]]

a = a.astype(np.float64)
a[:] = 0.123
print(a)
# [[0.123 0.123 0.123]
#  [0.123 0.123 0.123]]
