import numpy as np

a_2d = np.arange(6).reshape(2, 3)
print(a_2d)
# [[0 1 2]
#  [3 4 5]]

a_2d_rot = np.rot90(a_2d)
print(a_2d_rot)
# [[2 5]
#  [1 4]
#  [0 3]]

print(np.shares_memory(a_2d, a_2d_rot))
# True

a_2d_rot[0, 0] = 100
print(a_2d_rot)
# [[100   5]
#  [  1   4]
#  [  0   3]]

print(a_2d)
# [[  0   1 100]
#  [  3   4   5]]

a_2d[0, 2] = 2
print(a_2d)
# [[0 1 2]
#  [3 4 5]]

print(a_2d_rot)
# [[2 5]
#  [1 4]
#  [0 3]]

a_2d_rot_copy = np.rot90(a_2d).copy()
print(a_2d_rot_copy)
# [[2 5]
#  [1 4]
#  [0 3]]

print(np.shares_memory(a_2d, a_2d_rot_copy))
# False

print(np.rot90(a_2d, 2))
# [[5 4 3]
#  [2 1 0]]

print(np.rot90(a_2d, 3))
# [[3 0]
#  [4 1]
#  [5 2]]

print(np.rot90(a_2d, 4))
# [[0 1 2]
#  [3 4 5]]

print(np.rot90(a_2d, 100))
# [[0 1 2]
#  [3 4 5]]

print(np.rot90(a_2d, -1))
# [[3 0]
#  [4 1]
#  [5 2]]

print(np.rot90(a_2d, -2))
# [[5 4 3]
#  [2 1 0]]

a_1d = np.arange(3)
print(a_1d)
# [0 1 2]

# print(np.rot90(a_1d))
# ValueError: Axes must be different.

a_2d_row = np.arange(3).reshape(1, 3)
print(a_2d_row)
# [[0 1 2]]

print(np.rot90(a_2d_row))
# [[2]
#  [1]
#  [0]]

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

print(np.rot90(a_3d))
# [[[ 8  9 10 11]
#   [20 21 22 23]]
# 
#  [[ 4  5  6  7]
#   [16 17 18 19]]
# 
#  [[ 0  1  2  3]
#   [12 13 14 15]]]

print(np.rot90(a_3d).shape)
# (3, 2, 4)

print(a_3d[:, :, 0])
# [[ 0  4  8]
#  [12 16 20]]

print(np.rot90(a_3d)[:, :, 0])
# [[ 8 20]
#  [ 4 16]
#  [ 0 12]]

print(np.rot90(a_3d, axes=(0, 1)))
# [[[ 8  9 10 11]
#   [20 21 22 23]]
# 
#  [[ 4  5  6  7]
#   [16 17 18 19]]
# 
#  [[ 0  1  2  3]
#   [12 13 14 15]]]

print(np.rot90(a_3d, axes=(1, 2)))
# [[[ 3  7 11]
#   [ 2  6 10]
#   [ 1  5  9]
#   [ 0  4  8]]
# 
#  [[15 19 23]
#   [14 18 22]
#   [13 17 21]
#   [12 16 20]]]

print(np.rot90(a_3d, axes=(1, 2)).shape)
# (2, 4, 3)

print(np.rot90(a_3d, axes=(2, 1)))
# [[[ 8  4  0]
#   [ 9  5  1]
#   [10  6  2]
#   [11  7  3]]
# 
#  [[20 16 12]
#   [21 17 13]
#   [22 18 14]
#   [23 19 15]]]

print(np.rot90(a_3d, axes=(2, 1)).shape)
# (2, 4, 3)

print(np.rot90(a_3d, 2, axes=(1, 2)))
# [[[11 10  9  8]
#   [ 7  6  5  4]
#   [ 3  2  1  0]]
# 
#  [[23 22 21 20]
#   [19 18 17 16]
#   [15 14 13 12]]]

print(np.rot90(a_3d, -1, axes=(1, 2)))
# [[[ 8  4  0]
#   [ 9  5  1]
#   [10  6  2]
#   [11  7  3]]
# 
#  [[20 16 12]
#   [21 17 13]
#   [22 18 14]
#   [23 19 15]]]
