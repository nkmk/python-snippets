import numpy as np

a_2d = np.arange(12).reshape(3, 4)
print(a_2d)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a_2d[1, 1:3])
# [5 6]

print(a_2d[1, [False, True, True, False]])
# [5 6]

print(a_2d[1, [1, 2]])
# [5 6]

print(a_2d[1:3, 1:3])
# [[ 5  6]
#  [ 9 10]]

print(a_2d[1:3, [False, True, True, False]])
# [[ 5  6]
#  [ 9 10]]

print(a_2d[1:3, [1, 2]])
# [[ 5  6]
#  [ 9 10]]

print(a_2d[np.ix_([1, 2], [False, True, True, False])])
# [[ 5  6]
#  [ 9 10]]

a_3d = np.arange(24).reshape(2, 3, 4)
print(a_3d)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
# 
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

print(a_3d[:, :2, [True, False, True, False]])
# [[[ 0  2]
#   [ 4  6]]
# 
#  [[12 14]
#   [16 18]]]

print(a_3d[:, :2, [0, 2]])
# [[[ 0  2]
#   [ 4  6]]
# 
#  [[12 14]
#   [16 18]]]

print(a_3d[:, [0, 2], [0, 2]])
# [[ 0 10]
#  [12 22]]

# print(a_3d[np.ix_(:, [0, 2], [0, 2])])
# SyntaxError: invalid syntax

print(a_3d[np.ix_(range(2), [0, 2], [0, 2])])
# [[[ 0  2]
#   [ 8 10]]
# 
#  [[12 14]
#   [20 22]]]

print(a_3d[np.ix_(range(a_3d.shape[0]), [0, 2], [0, 2])])
# [[[ 0  2]
#   [ 8 10]]
# 
#  [[12 14]
#   [20 22]]]

# print(a_3d[np.ix_(0, [0, 2], [0, 2])])
# ValueError: Cross index must be 1 dimensional

print(a_3d[np.ix_([0], [0, 2], [0, 2])])
# [[[ 0  2]
#   [ 8 10]]]
