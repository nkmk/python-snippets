import numpy as np

a_1d = np.arange(3)
print(a_1d)
# [0 1 2]

a_2d = np.arange(12).reshape((3, 4))
print(a_2d)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

a_3d = np.arange(24).reshape((2, 3, 4))
print(a_3d)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
# 
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

print(a_1d.ndim)
# 1

print(type(a_1d.ndim))
# <class 'int'>

print(a_2d.ndim)
# 2

print(a_3d.ndim)
# 3

print(a_1d.shape)
# (3,)

print(type(a_1d.shape))
# <class 'tuple'>

print(a_2d.shape)
# (3, 4)

print(a_3d.shape)
# (2, 3, 4)

print(a_2d.shape[0])
# 3

print(a_2d.shape[1])
# 4

row, col = a_2d.shape
print(row)
# 3

print(col)
# 4

print(a_1d.size)
# 3

print(type(a_1d.size))
# <class 'int'>

print(a_2d.size)
# 12

print(a_3d.size)
# 24

print(len(a_1d))
# 3

print(a_1d.shape[0])
# 3

print(a_1d.size)
# 3

print(len(a_2d))
# 3

print(a_2d.shape[0])
# 3

print(len(a_3d))
# 2

print(a_3d.shape[0])
# 2
