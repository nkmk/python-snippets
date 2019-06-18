import numpy as np

a_2d = np.arange(6).reshape(2, 3)
print(a_2d)
# [[0 1 2]
#  [3 4 5]]

a_2d_T = a_2d.T
print(a_2d_T)
# [[0 3]
#  [1 4]
#  [2 5]]

print(np.shares_memory(a_2d, a_2d_T))
# True

a_2d_T[0, 1] = 100
print(a_2d_T)
# [[  0 100]
#  [  1   4]
#  [  2   5]]

print(a_2d)
# [[  0   1   2]
#  [100   4   5]]

a_2d[1, 0] = 3
print(a_2d)
# [[0 1 2]
#  [3 4 5]]

print(a_2d_T)
# [[0 3]
#  [1 4]
#  [2 5]]

a_2d_T_copy = a_2d.T.copy()
print(a_2d_T_copy)
# [[0 3]
#  [1 4]
#  [2 5]]

print(np.shares_memory(a_2d, a_2d_T_copy))
# False

a_2d_T_copy[0, 1] = 100
print(a_2d_T_copy)
# [[  0 100]
#  [  1   4]
#  [  2   5]]

print(a_2d)
# [[0 1 2]
#  [3 4 5]]

a_2d = np.arange(6).reshape(2, 3)
print(a_2d)
# [[0 1 2]
#  [3 4 5]]

print(a_2d.transpose())
# [[0 3]
#  [1 4]
#  [2 5]]

print(np.shares_memory(a_2d, a_2d.transpose()))
# True

print(np.transpose(a_2d))
# [[0 3]
#  [1 4]
#  [2 5]]

print(np.shares_memory(a_2d, np.transpose(a_2d)))
# True

a_1d = np.arange(3)
print(a_1d)
# [0 1 2]

print(a_1d.T)
# [0 1 2]

print(a_1d.transpose())
# [0 1 2]

print(np.transpose(a_1d))
# [0 1 2]

a_row = a_1d.reshape(1, -1)
print(a_row)
# [[0 1 2]]

print(a_row.shape)
# (1, 3)

print(a_row.ndim)
# 2

a_col = a_1d.reshape(-1, 1)
print(a_col)
# [[0]
#  [1]
#  [2]]

print(a_col.shape)
# (3, 1)

print(a_col.ndim)
# 2

print(a_row.T)
# [[0]
#  [1]
#  [2]]

print(a_col.T)
# [[0 1 2]]

a_3d = np.arange(24).reshape(2, 3, 4)
print(a_3d)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
# 
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

print(a_3d.T)
# [[[ 0 12]
#   [ 4 16]
#   [ 8 20]]
# 
#  [[ 1 13]
#   [ 5 17]
#   [ 9 21]]
# 
#  [[ 2 14]
#   [ 6 18]
#   [10 22]]
# 
#  [[ 3 15]
#   [ 7 19]
#   [11 23]]]

print(a_3d.T.shape)
# (4, 3, 2)

print(a_3d.transpose())
# [[[ 0 12]
#   [ 4 16]
#   [ 8 20]]
# 
#  [[ 1 13]
#   [ 5 17]
#   [ 9 21]]
# 
#  [[ 2 14]
#   [ 6 18]
#   [10 22]]
# 
#  [[ 3 15]
#   [ 7 19]
#   [11 23]]]

print(a_3d.transpose().shape)
# (4, 3, 2)

print(a_3d.transpose(2, 1, 0))
# [[[ 0 12]
#   [ 4 16]
#   [ 8 20]]
# 
#  [[ 1 13]
#   [ 5 17]
#   [ 9 21]]
# 
#  [[ 2 14]
#   [ 6 18]
#   [10 22]]
# 
#  [[ 3 15]
#   [ 7 19]
#   [11 23]]]

print(a_3d.transpose(2, 1, 0).shape)
# (4, 3, 2)

print(a_3d.transpose((2, 1, 0)).shape)
# (4, 3, 2)

print(np.transpose(a_3d, (2, 1, 0)))
# [[[ 0 12]
#   [ 4 16]
#   [ 8 20]]
# 
#  [[ 1 13]
#   [ 5 17]
#   [ 9 21]]
# 
#  [[ 2 14]
#   [ 6 18]
#   [10 22]]
# 
#  [[ 3 15]
#   [ 7 19]
#   [11 23]]]

print(np.transpose(a_3d, (2, 1, 0)).shape)
# (4, 3, 2)

# print(np.transpose(a_3d, 2, 1, 0))
# TypeError: transpose() takes from 1 to 2 positional arguments but 4 were given

# print(a_3d.transpose(0, 1))
# ValueError: axes don't match array

# print(a_3d.transpose(0, 1, 2, 3))
# ValueError: axes don't match array

# print(a_3d.transpose(0, 1, 3))
# AxisError: axis 3 is out of bounds for array of dimension 3

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

print(a_3d.transpose(0, 2, 1))
# [[[ 0  4  8]
#   [ 1  5  9]
#   [ 2  6 10]
#   [ 3  7 11]]
# 
#  [[12 16 20]
#   [13 17 21]
#   [14 18 22]
#   [15 19 23]]]

print(a_3d.transpose(0, 2, 1).shape)
# (2, 4, 3)

print(a_3d.transpose(1, 0, 2))
# [[[ 0  1  2  3]
#   [12 13 14 15]]
# 
#  [[ 4  5  6  7]
#   [16 17 18 19]]
# 
#  [[ 8  9 10 11]
#   [20 21 22 23]]]

print(a_3d.transpose(1, 0, 2).shape)
# (3, 2, 4)

print(a_3d[:, :, 0])
# [[ 0  4  8]
#  [12 16 20]]

print(a_3d.transpose(1, 0, 2)[:, :, 0])
# [[ 0 12]
#  [ 4 16]
#  [ 8 20]]
