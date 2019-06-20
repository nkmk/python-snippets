import numpy as np

a_2d = np.arange(6).reshape(2, 3)
print(a_2d)
# [[0 1 2]
#  [3 4 5]]

a_2d_fliplr = np.fliplr(a_2d)
print(a_2d_fliplr)
# [[2 1 0]
#  [5 4 3]]

print(np.shares_memory(a_2d, a_2d_fliplr))
# True

print(a_2d[:, ::-1])
# [[2 1 0]
#  [5 4 3]]

a_1d = np.arange(3)
print(a_1d)
# [0 1 2]

# print(np.fliplr(a_1d))
# ValueError: Input must be >= 2-d.

a_3d = np.arange(24).reshape(2, 3, 4)
print(a_3d)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
# 
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

print(np.fliplr(a_3d))
# [[[ 8  9 10 11]
#   [ 4  5  6  7]
#   [ 0  1  2  3]]
# 
#  [[20 21 22 23]
#   [16 17 18 19]
#   [12 13 14 15]]]

print(a_3d[:, ::-1])
# [[[ 8  9 10 11]
#   [ 4  5  6  7]
#   [ 0  1  2  3]]
# 
#  [[20 21 22 23]
#   [16 17 18 19]
#   [12 13 14 15]]]
