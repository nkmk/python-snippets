import numpy as np

print(np.__version__)
# 1.26.1

a = np.arange(12).reshape((3, 4))
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(np.count_nonzero(a))
# 11

print(a < 4)
# [[ True  True  True  True]
#  [False False False False]
#  [False False False False]]

print(a % 2 == 0)
# [[ True False  True False]
#  [ True False  True False]
#  [ True False  True False]]

print(np.count_nonzero(a < 4))
# 4

print(np.count_nonzero(a % 2 == 0))
# 6

print(np.sum(a < 4))
# 4

print(np.sum(a % 2 == 0))
# 6

print(np.count_nonzero(a < 4))
# 4

print(np.count_nonzero(a < 4, axis=0))
# [1 1 1 1]

print(np.count_nonzero(a < 4, axis=1))
# [4 0 0]

print(np.count_nonzero(a < 4, keepdims=True))
# [[4]]

print(np.count_nonzero(a < 4, axis=0, keepdims=True))
# [[1 1 1 1]]

print(np.count_nonzero(a < 4, axis=1, keepdims=True))
# [[4]
#  [0]
#  [0]]

print(np.any(a < 4))
# True

print(np.any(a > 100))
# False

print(np.any(a < 4, axis=0))
# [ True  True  True  True]

print(np.any(a < 4, axis=1))
# [ True False False]

print(np.all(a < 4))
# False

print(np.all(a < 100))
# True

print(np.all(a < 4, axis=0))
# [False False False False]

print(np.all(a < 4, axis=1))
# [ True False False]

print((a < 4) | (a % 2 == 0))
# [[ True  True  True  True]
#  [ True False  True False]
#  [ True False  True False]]

print(np.count_nonzero((a < 4) | (a % 2 == 0)))
# 8

print(np.count_nonzero((a < 4) | (a % 2 == 0), axis=0))
# [3 1 3 1]

print(np.count_nonzero((a < 4) | (a % 2 == 0), axis=1))
# [4 2 2]
