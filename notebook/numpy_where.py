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
