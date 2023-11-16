import numpy as np

print(np.__version__)
# 1.26.1

print(np.zeros(3))
# [0. 0. 0.]

print(np.zeros((2, 3)))
# [[0. 0. 0.]
#  [0. 0. 0.]]

print(np.zeros(3).dtype)
# float64

print(np.zeros(3, dtype=np.int64))
# [0 0 0]

print(np.zeros(3, dtype=np.int64).dtype)
# int64

print(np.ones(3))
# [1. 1. 1.]

print(np.ones((2, 3)))
# [[1. 1. 1.]
#  [1. 1. 1.]]

print(np.ones(3).dtype)
# float64

print(np.ones(3, dtype=np.int64))
# [1 1 1]

print(np.ones(3, dtype=np.int64).dtype)
# int64

print(np.full(3, 100))
# [100 100 100]

print(np.full((2, 3), 0.123))
# [[0.123 0.123 0.123]
#  [0.123 0.123 0.123]]

print(np.full(3, 100).dtype)
# int64

print(np.full(3, 100.0).dtype)
# float64

print(np.full(3, 0.123).dtype)
# float64

print(np.full(3, 100, dtype=np.float64))
# [100. 100. 100.]

print(np.full(3, 0.123, dtype=np.int64))
# [0 0 0]
