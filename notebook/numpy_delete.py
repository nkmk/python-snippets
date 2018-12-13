import numpy as np

a = np.arange(12).reshape(3, 4)
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

a_del = np.delete(a, 1, 0)
print(a_del)
# [[ 0  1  2  3]
#  [ 8  9 10 11]]

print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(np.delete(a, 0, 0))
# [[ 4  5  6  7]
#  [ 8  9 10 11]]

print(np.delete(a, 2, 0))
# [[0 1 2 3]
#  [4 5 6 7]]

# print(np.delete(a, 3, 0))
# IndexError: index 3 is out of bounds for axis 0 with size 3

print(np.delete(a, 1, 0))
# [[ 0  1  2  3]
#  [ 8  9 10 11]]

print(np.delete(a, 1, 1))
# [[ 0  2  3]
#  [ 4  6  7]
#  [ 8 10 11]]

# print(np.delete(a, 1, 2))
# AxisError: axis 2 is out of bounds for array of dimension 2

print(np.delete(a, 1, None))
# [ 0  2  3  4  5  6  7  8  9 10 11]

print(np.delete(a, 1))
# [ 0  2  3  4  5  6  7  8  9 10 11]

print(np.delete(a, [0, 3], 1))
# [[ 1  2]
#  [ 5  6]
#  [ 9 10]]

print(np.delete(a, [0, 1, 3], 1))
# [[ 2]
#  [ 6]
#  [10]]

print(np.delete(a, slice(2), 1))
# [[ 2  3]
#  [ 6  7]
#  [10 11]]

print(np.delete(a, slice(1, 3), 1))
# [[ 0  3]
#  [ 4  7]
#  [ 8 11]]

print(np.delete(a, slice(None, None, 2), 1))
# [[ 1  3]
#  [ 5  7]
#  [ 9 11]]

print(np.delete(a, np.s_[:2], 1))
# [[ 2  3]
#  [ 6  7]
#  [10 11]]

print(np.delete(a, np.s_[1:3], 1))
# [[ 0  3]
#  [ 4  7]
#  [ 8 11]]

print(np.delete(a, np.s_[::2], 1))
# [[ 1  3]
#  [ 5  7]
#  [ 9 11]]

print(np.delete(np.delete(a, 1, 0), 1, 1))
# [[ 0  2  3]
#  [ 8 10 11]]

a_3d = np.arange(24).reshape(2, 3, 4)
print(a_3d)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
# 
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

print(a_3d.shape)
# (2, 3, 4)

print(np.delete(a_3d, 1, 0))
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]]

print(np.delete(a_3d, 1, 1))
# [[[ 0  1  2  3]
#   [ 8  9 10 11]]
# 
#  [[12 13 14 15]
#   [20 21 22 23]]]

print(np.delete(a_3d, 1, 2))
# [[[ 0  2  3]
#   [ 4  6  7]
#   [ 8 10 11]]
# 
#  [[12 14 15]
#   [16 18 19]
#   [20 22 23]]]

print(np.delete(a_3d, [0, 3], 2))
# [[[ 1  2]
#   [ 5  6]
#   [ 9 10]]
# 
#  [[13 14]
#   [17 18]
#   [21 22]]]

print(np.delete(a_3d, np.s_[::2], 2))
# [[[ 1  3]
#   [ 5  7]
#   [ 9 11]]
# 
#  [[13 15]
#   [17 19]
#   [21 23]]]
