import numpy as np

a = np.arange(9).reshape((3, 3))

print(a)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

print(np.diag(a))
# [0 4 8]

print(np.diag(a, k=1))
# [1 5]

print(np.diag(a, k=2))
# [2]

print(np.diag(a, k=3))
# []

print(np.diag(a, k=-1))
# [3 7]

print(np.diag(a, k=-2))
# [6]

print(np.diag(a, k=-3))
# []

a = np.arange(12).reshape((3, 4))

print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(np.diag(a))
# [ 0  5 10]

print(np.diag(a, k=1))
# [ 1  6 11]

print(np.diag(a, k=-1))
# [4 9]

a = np.arange(27).reshape((3, 3, 3))

print(a)
# [[[ 0  1  2]
#   [ 3  4  5]
#   [ 6  7  8]]
# 
#  [[ 9 10 11]
#   [12 13 14]
#   [15 16 17]]
# 
#  [[18 19 20]
#   [21 22 23]
#   [24 25 26]]]

# print(np.diag(a))
# ValueError: Input must be 1- or 2-d.

a = np.arange(9).reshape((3, 3))

print(a)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

a_diag = np.diag(a)

print(a_diag)
# [0 4 8]

# a_diag[0] = 100
# ValueError: assignment destination is read-only

a_diag.flags.writeable = True

a_diag[0] = 100

print(a_diag)
# [100   4   8]

print(a)
# [[100   1   2]
#  [  3   4   5]
#  [  6   7   8]]

a_diag_copy = np.diag(a).copy()

print(a_diag_copy)
# [100   4   8]

a_diag_copy[1] = 100

print(a_diag_copy)
# [100 100   8]

print(a)
# [[100   1   2]
#  [  3   4   5]
#  [  6   7   8]]
