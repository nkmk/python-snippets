import numpy as np

a = np.arange(12).reshape((3, 4))
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a < 5)
# [[ True  True  True  True]
#  [ True False False False]
#  [False False False False]]

print(a[a < 5])
# [0 1 2 3 4]

print(a < 10)
# [[ True  True  True  True]
#  [ True  True  True  True]
#  [ True  True False False]]

print(a[a < 10])
# [0 1 2 3 4 5 6 7 8 9]

b = a[a < 10]
print(b)
# [0 1 2 3 4 5 6 7 8 9]

print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a[a < 5].sum())
# 10

print(a[a < 5].mean())
# 2.0

print(a[a < 5].max())
# 4

print(a[a < 10].min())
# 0

print(a[a < 10].std())
# 2.8722813232690143

print(a < 5)
# [[ True  True  True  True]
#  [ True False False False]
#  [False False False False]]

print(np.all(a < 5))
# False

print(np.all(a < 5, axis=0))
# [False False False False]

print(np.all(a < 5, axis=1))
# [ True False False]

print(a < 10)
# [[ True  True  True  True]
#  [ True  True  True  True]
#  [ True  True False False]]

print(np.all(a < 10, axis=0))
# [ True  True False False]

print(np.all(a < 10, axis=1))
# [ True  True False]

print(a[:, np.all(a < 10, axis=0)])
# [[0 1]
#  [4 5]
#  [8 9]]

print(a[np.all(a < 10, axis=1), :])
# [[0 1 2 3]
#  [4 5 6 7]]

print(a[np.all(a < 10, axis=1)])
# [[0 1 2 3]
#  [4 5 6 7]]

print(a[:, np.all(a < 5, axis=0)])
# []

print(a[np.all(a < 5, axis=1)])
# [[0 1 2 3]]

print(a[np.all(a < 5, axis=1)].ndim)
# 2

print(a[np.all(a < 5, axis=1)].shape)
# (1, 4)

print(a < 5)
# [[ True  True  True  True]
#  [ True False False False]
#  [False False False False]]

print(np.any(a < 5))
# True

print(np.any(a < 5, axis=0))
# [ True  True  True  True]

print(np.any(a < 5, axis=1))
# [ True  True False]

print(a[:, np.any(a < 5, axis=0)])
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a[np.any(a < 5, axis=1)])
# [[0 1 2 3]
#  [4 5 6 7]]

print(a[~(a < 5)])
# [ 5  6  7  8  9 10 11]

print(a[:, np.all(a < 10, axis=0)])
# [[0 1]
#  [4 5]
#  [8 9]]

print(a[:, ~np.all(a < 10, axis=0)])
# [[ 2  3]
#  [ 6  7]
#  [10 11]]

print(a[np.any(a < 5, axis=1)])
# [[0 1 2 3]
#  [4 5 6 7]]

print(a[~np.any(a < 5, axis=1)])
# [[ 8  9 10 11]]

print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(np.delete(a, [0, 2], axis=0))
# [[4 5 6 7]]

print(np.delete(a, [0, 2], axis=1))
# [[ 1  3]
#  [ 5  7]
#  [ 9 11]]

print(a < 2)
# [[ True  True False False]
#  [False False False False]
#  [False False False False]]

print(np.where(a < 2))
# (array([0, 0]), array([0, 1]))

print(np.where(a < 2)[0])
# [0 0]

print(np.where(a < 2)[1])
# [0 1]

print(np.delete(a, np.where(a < 2)[0], axis=0))
# [[ 4  5  6  7]
#  [ 8  9 10 11]]

print(np.delete(a, np.where(a < 2)[1], axis=1))
# [[ 2  3]
#  [ 6  7]
#  [10 11]]

print(a == 6)
# [[False False False False]
#  [False False  True False]
#  [False False False False]]

print(np.where(a == 6))
# (array([1]), array([2]))

print(np.delete(a, np.where(a == 6)))
# [ 0  3  4  5  6  7  8  9 10 11]

print(np.delete(a, np.where(a == 6)[0], axis=0))
# [[ 0  1  2  3]
#  [ 8  9 10 11]]

print(np.delete(a, np.where(a == 6)[1], axis=1))
# [[ 0  1  3]
#  [ 4  5  7]
#  [ 8  9 11]]

print(a[(a < 10) & (a % 2 == 1)])
# [1 3 5 7 9]

print(a[np.any((a == 2) | (a == 10), axis=1)])
# [[ 0  1  2  3]
#  [ 8  9 10 11]]

print(a[:, ~np.any((a == 2) | (a == 10), axis=0)])
# [[ 0  1  3]
#  [ 4  5  7]
#  [ 8  9 11]]
