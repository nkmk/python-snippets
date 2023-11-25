import numpy as np

print(np.__version__)
# 1.26.1

a_2d = np.arange(12).reshape(3, 4)
print(a_2d)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a_2d[1, 2])
# 6

print(a_2d[1])
# [4 5 6 7]

print(a_2d[:, 1])
# [1 5 9]

a_3d = np.arange(24).reshape(2, 3, 4)
print(a_3d)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
# 
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

print(a_3d[1, [True, False, True], ::2])
# [[12 14]
#  [20 22]]
