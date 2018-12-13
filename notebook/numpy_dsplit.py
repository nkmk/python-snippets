import numpy as np

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

a0, a1 = np.dsplit(a_3d, 2)

print(a0)
# [[[ 0  1]
#   [ 4  5]
#   [ 8  9]]
# 
#  [[12 13]
#   [16 17]
#   [20 21]]]

print(a0.shape)
# (2, 3, 2)

print(a1)
# [[[ 2  3]
#   [ 6  7]
#   [10 11]]
# 
#  [[14 15]
#   [18 19]
#   [22 23]]]

print(a1.shape)
# (2, 3, 2)

a0, a1 = np.dsplit(a_3d, [1])

print(a0)
# [[[ 0]
#   [ 4]
#   [ 8]]
# 
#  [[12]
#   [16]
#   [20]]]

print(a1)
# [[[ 1  2  3]
#   [ 5  6  7]
#   [ 9 10 11]]
# 
#  [[13 14 15]
#   [17 18 19]
#   [21 22 23]]]

a = np.arange(16).reshape(4, 4)
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]

# np.dsplit(a, 2)
# ValueError: dsplit only works on arrays of 3 or more dimensions
