import numpy as np

print(np.__version__)
# 1.26.1

print(np.arange(3))
# [0 1 2]

print(np.arange(3, 10))
# [3 4 5 6 7 8 9]

print(np.arange(3, 10, 2))
# [3 5 7 9]

print(np.arange(0.3, 1.0, 0.2))
# [0.3 0.5 0.7 0.9]

print(np.arange(-3, 3))
# [-3 -2 -1  0  1  2]

print(np.arange(10, 3))
# []

print(np.arange(10, 3, -2))
# [10  8  6  4]

a = np.arange(3, 10)
print(a)
# [3 4 5 6 7 8 9]

print(a.dtype)
# int64

a_float = np.arange(3, 10, dtype=float)
print(a_float)
# [3. 4. 5. 6. 7. 8. 9.]

print(a_float.dtype)
# float64

print(np.arange(3, 10, 2))
# [3 5 7 9]

print(np.arange(9, 2, -2))
# [9 7 5 3]

print(np.arange(3, 10, 2)[::-1])
# [9 7 5 3]

print(np.flip(np.arange(3, 10, 2)))
# [9 7 5 3]

print(np.arange(12).reshape(3, 4))
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(np.arange(24).reshape(2, 3, 4))
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
# 
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]
