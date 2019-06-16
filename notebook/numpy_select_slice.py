import numpy as np

a_1d = np.arange(10)
print(a_1d)
# [0 1 2 3 4 5 6 7 8 9]

print(a_1d[2:7])
# [2 3 4 5 6]

print(a_1d[:7])
# [0 1 2 3 4 5 6]

print(a_1d[2:])
# [2 3 4 5 6 7 8 9]

print(a_1d[2:7:2])
# [2 4 6]

a_2d = np.arange(12).reshape(3, 4)
print(a_2d)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a_2d[:2, 1:3])
# [[1 2]
#  [5 6]]

print(a_2d[:2, :])
# [[0 1 2 3]
#  [4 5 6 7]]

print(a_2d[:2])
# [[0 1 2 3]
#  [4 5 6 7]]

print(a_2d[1:2])
# [[4 5 6 7]]

print(a_2d[1:2].shape)
# (1, 4)

print(a_2d[1])
# [4 5 6 7]

print(a_2d[1].shape)
# (4,)

print(a_2d[:, 2:3])
# [[ 2]
#  [ 6]
#  [10]]

print(a_2d[:, 2:3].shape)
# (3, 1)

print(a_2d[:, 2])
# [ 2  6 10]

print(a_2d[:, 2].shape)
# (3,)

print(a_2d[1:2, 2:3])
# [[6]]

print(a_2d[1:2, 2:3].shape)
# (1, 1)

print(a_2d[1, 2])
# 6

print(type(a_2d[1, 2]))
# <class 'numpy.int64'>

a_3d = np.arange(24).reshape(2, 3, 4)
print(a_3d)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
# 
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

print(a_3d[0, 0, 0])
# 0

print(a_3d[0, 0])
# [0 1 2 3]

print(a_3d[0])
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a_3d[0:1, 0:1, 0:1])
# [[[0]]]

print(a_3d[0:1, 0:1])
# [[[0 1 2 3]]]

print(a_3d[0:1])
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]]
