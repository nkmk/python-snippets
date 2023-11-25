import numpy as np

print(np.__version__)
# 1.26.1

a_1d = np.arange(4)
print(a_1d)
# [0 1 2 3]

print(a_1d[[0, 2]])
# [0 2]

print(a_1d[[3, 3, 3, -3, 0]])
# [3 3 3 1 0]

print(a_1d[np.array([3, 3, 3, -3, 0])])
# [3 3 3 1 0]

a_2d = np.arange(12).reshape(3, 4)
print(a_2d)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a_2d[[0, 2]])
# [[ 0  1  2  3]
#  [ 8  9 10 11]]

print(a_2d[:, [0, 3]])
# [[ 0  3]
#  [ 4  7]
#  [ 8 11]]

print(a_2d[[0, 2], [0, 3]])
# [ 0 11]

print(a_2d[np.ix_([0, 2], [0, 3])])
# [[ 0  3]
#  [ 8 11]]

print(a_2d[np.ix_([2, 1, 1, -1, -1], [0, 2, 1, 3])])
# [[ 8 10  9 11]
#  [ 4  6  5  7]
#  [ 4  6  5  7]
#  [ 8 10  9 11]
#  [ 8 10  9 11]]

print(a_2d[:, [1]])
# [[1]
#  [5]
#  [9]]

print(a_2d[:, [1]].shape)
# (3, 1)

print(a_2d[:, 1])
# [1 5 9]

print(a_2d[:, 1].shape)
# (3,)
