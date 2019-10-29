import numpy as np

a = np.arange(9).reshape((3, 3))
print(a)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

print(np.where(a < 4, -1, 100))
# [[ -1  -1  -1]
#  [ -1 100 100]
#  [100 100 100]]

print(np.where(a < 4, True, False))
# [[ True  True  True]
#  [ True False False]
#  [False False False]]

print(a < 4)
# [[ True  True  True]
#  [ True False False]
#  [False False False]]

print(np.where((a > 2) & (a < 6), -1, 100))
# [[100 100 100]
#  [ -1  -1  -1]
#  [100 100 100]]

print(np.where((a > 2) & (a < 6) | (a == 7), -1, 100))
# [[100 100 100]
#  [ -1  -1  -1]
#  [100  -1 100]]

print((a > 2) & (a < 6))
# [[False False False]
#  [ True  True  True]
#  [False False False]]

print((a > 2) & (a < 6) | (a == 7))
# [[False False False]
#  [ True  True  True]
#  [False  True False]]

print(np.where(a < 4, -1, a))
# [[-1 -1 -1]
#  [-1  4  5]
#  [ 6  7  8]]

print(np.where(a < 4, a, 100))
# [[  0   1   2]
#  [  3 100 100]
#  [100 100 100]]

a_org = np.arange(9).reshape((3, 3))
print(a_org)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

a_new = np.where(a_org < 4, -1, a_org)
print(a_new)
# [[-1 -1 -1]
#  [-1  4  5]
#  [ 6  7  8]]

print(a_org)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

a_org[a_org < 4] = -1
print(a_org)
# [[-1 -1 -1]
#  [-1  4  5]
#  [ 6  7  8]]

print(np.where(a < 4, a * 10, a))
# [[ 0 10 20]
#  [30  4  5]
#  [ 6  7  8]]

print(np.where(a < 4))
# (array([0, 0, 0, 1]), array([0, 1, 2, 0]))

print(type(np.where(a < 4)))
# <class 'tuple'>

print(list(zip(*np.where(a < 4))))
# [(0, 0), (0, 1), (0, 2), (1, 0)]

a_3d = np.arange(24).reshape(2, 3, 4)
print(a_3d)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
# 
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

print(np.where(a_3d < 5))
# (array([0, 0, 0, 0, 0]), array([0, 0, 0, 0, 1]), array([0, 1, 2, 3, 0]))

print(list(zip(*np.where(a_3d < 5))))
# [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 3), (0, 1, 0)]

a_1d = np.arange(6)
print(a_1d)
# [0 1 2 3 4 5]

print(np.where(a_1d < 3))
# (array([0, 1, 2]),)

print(list(zip(*np.where(a_1d < 3))))
# [(0,), (1,), (2,)]

print(np.where(a_1d < 3)[0])
# [0 1 2]

print(np.where(a_1d < 3)[0].tolist())
# [0, 1, 2]
