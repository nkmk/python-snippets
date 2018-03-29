import numpy as np

l_1d = [0, 1, 2]

arr_1d = np.array(l_1d)

print(arr_1d)
print(arr_1d.dtype)
# [0 1 2]
# int64

arr_1d_f = np.array(l_1d, dtype=float)

print(arr_1d_f)
print(arr_1d_f.dtype)
# [0. 1. 2.]
# float64

l_2d = [[0, 1, 2], [3, 4, 5]]

arr_2d = np.array(l_2d)

print(arr_2d)
# [[0 1 2]
#  [3 4 5]]

l_2d_error = [[0, 1, 2], [3, 4]]

arr_2d_error = np.array(l_2d_error)

print(arr_2d_error)
# [list([0, 1, 2]) list([3, 4])]

print(arr_2d_error.dtype)
# object

print(arr_2d_error.shape)
# (2,)

arr_1d = np.arange(3)

print(arr_1d)
# [0 1 2]

l_1d = arr_1d.tolist()

print(l_1d)
# [0, 1, 2]

arr_2d = np.arange(6).reshape((2, 3))

print(arr_2d)
# [[0 1 2]
#  [3 4 5]]

l_2d = arr_2d.tolist()

print(l_2d)
# [[0, 1, 2], [3, 4, 5]]

arr_3d = np.arange(24).reshape((2, 3, 4))

print(arr_3d)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

l_3d = arr_3d.tolist()

print(l_3d)
# [[[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]], [[12, 13, 14, 15], [16, 17, 18, 19], [20, 21, 22, 23]]]

print(l_3d[0])
# [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]

print(l_3d[0][0])
# [0, 1, 2, 3]

print(l_3d[0][0][0])
# 0
