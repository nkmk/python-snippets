import numpy as np

a_2d = np.arange(6).reshape(2, 3)
print(a_2d)
# [[0 1 2]
#  [3 4 5]]

a_2d_flipud = np.flipud(a_2d)
print(a_2d_flipud)
# [[3 4 5]
#  [0 1 2]]

print(np.shares_memory(a_2d, a_2d_flipud))
# True

a_2d_flipud_copy = np.flipud(a_2d).copy()
print(a_2d_flipud_copy)
# [[3 4 5]
#  [0 1 2]]

print(np.shares_memory(a_2d, a_2d_flipud_copy))
# False

print(a_2d[::-1])
# [[3 4 5]
#  [0 1 2]]

a_1d = np.arange(3)
print(a_1d)
# [0 1 2]

print(np.flipud(a_1d))
# [2 1 0]

print(a_1d[::-1])
# [2 1 0]

a_3d = np.arange(24).reshape(2, 3, 4)
print(a_3d)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
# 
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

print(np.flipud(a_3d))
# [[[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]
# 
#  [[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]]

print(a_3d[::-1])
# [[[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]
# 
#  [[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]]
