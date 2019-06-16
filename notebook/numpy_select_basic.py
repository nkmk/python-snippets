import numpy as np

a_1d = np.arange(10)
print(a_1d)
# [0 1 2 3 4 5 6 7 8 9]

print(a_1d[3])
# 3

a_2d = np.arange(12).reshape(3, 4)
print(a_2d)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a_2d[0, 2])
# 2

a_3d = np.arange(24).reshape(2, 3, 4)
print(a_3d)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
# 
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

print(a_3d[0, 1, 2])
# 6

print(a_3d[1, [True, False, True], ::2])
# [[12 14]
#  [20 22]]
