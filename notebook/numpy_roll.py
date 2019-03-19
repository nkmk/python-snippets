import numpy as np

a = np.arange(10)
print(a)
# [0 1 2 3 4 5 6 7 8 9]

a_roll = np.roll(a, 3)
print(a_roll)
# [7 8 9 0 1 2 3 4 5 6]

print(a)
# [0 1 2 3 4 5 6 7 8 9]

a_roll[0] = 100
print(a_roll)
# [100   8   9   0   1   2   3   4   5   6]

print(a)
# [0 1 2 3 4 5 6 7 8 9]

print(np.roll(a, -3))
# [3 4 5 6 7 8 9 0 1 2]

print(np.roll(a, 12))
# [8 9 0 1 2 3 4 5 6 7]

# print(np.roll(a, 0.5))
# TypeError: slice indices must be integers or None or have an __index__ method

a_2d = np.arange(12).reshape(3, 4)
print(a_2d)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(np.roll(a_2d, 2))
# [[10 11  0  1]
#  [ 2  3  4  5]
#  [ 6  7  8  9]]

print(np.roll(a_2d, 5))
# [[ 7  8  9 10]
#  [11  0  1  2]
#  [ 3  4  5  6]]

print(np.roll(a_2d, 1, axis=0))
# [[ 8  9 10 11]
#  [ 0  1  2  3]
#  [ 4  5  6  7]]

print(np.roll(a_2d, 2, axis=1))
# [[ 2  3  0  1]
#  [ 6  7  4  5]
#  [10 11  8  9]]

print(np.roll(a_2d, (1, 2), axis=(0, 1)))
# [[10 11  8  9]
#  [ 2  3  0  1]
#  [ 6  7  4  5]]

a_3d = np.arange(24).reshape(2, 3, 4)
print(a_3d)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
# 
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

print(np.roll(a_3d, 3))
# [[[21 22 23  0]
#   [ 1  2  3  4]
#   [ 5  6  7  8]]
# 
#  [[ 9 10 11 12]
#   [13 14 15 16]
#   [17 18 19 20]]]

print(np.roll(a_3d, 2, axis=2))
# [[[ 2  3  0  1]
#   [ 6  7  4  5]
#   [10 11  8  9]]
# 
#  [[14 15 12 13]
#   [18 19 16 17]
#   [22 23 20 21]]]
