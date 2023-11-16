import numpy as np

print(np.__version__)
# 1.26.1

a_int64 = np.arange(3)
print(a_int64)
# [0 1 2]

print(a_int64.dtype)
# int64

a_float64 = np.arange(6).reshape(2, 3) / 10
print(a_float64)
# [[0.  0.1 0.2]
#  [0.3 0.4 0.5]]

print(a_float64.dtype)
# float64

print(np.zeros_like(a_int64))
# [0 0 0]

print(np.zeros_like(a_int64).dtype)
# int64

print(np.zeros_like(a_float64))
# [[0. 0. 0.]
#  [0. 0. 0.]]

print(np.zeros_like(a_float64).dtype)
# float64

print(np.zeros_like(a_int64, dtype=np.float64))
# [0. 0. 0.]

print(np.zeros_like(a_int64, dtype=np.float64).dtype)
# float64

print(np.ones_like(a_int64))
# [1 1 1]

print(np.ones_like(a_int64).dtype)
# int64

print(np.ones_like(a_float64))
# [[1. 1. 1.]
#  [1. 1. 1.]]

print(np.ones_like(a_float64).dtype)
# float64

print(np.ones_like(a_int64, dtype=np.float64))
# [1. 1. 1.]

print(np.ones_like(a_int64, dtype=np.float64).dtype)
# float64

print(np.full_like(a_int64, 100))
# [100 100 100]

print(np.full_like(a_int64, 100).dtype)
# int64

print(np.full_like(a_float64, 100))
# [[100. 100. 100.]
#  [100. 100. 100.]]

print(np.full_like(a_float64, 100).dtype)
# float64

print(np.full_like(a_int64, 0.123))
# [0 0 0]

print(np.full_like(a_int64, 0.123).dtype)
# int64

print(np.full_like(a_int64, 0.123, dtype=np.float64))
# [0.123 0.123 0.123]

print(np.full_like(a_int64, 0.123, dtype=np.float64).dtype)
# float64
