import numpy as np

a = np.arange(16).reshape(4, 4)
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]

a0, a1 = np.hsplit(a, 2)

print(a0)
# [[ 0  1]
#  [ 4  5]
#  [ 8  9]
#  [12 13]]

print(a1)
# [[ 2  3]
#  [ 6  7]
#  [10 11]
#  [14 15]]

a0, a1 = np.hsplit(a, [1])

print(a0)
# [[ 0]
#  [ 4]
#  [ 8]
#  [12]]

print(a1)
# [[ 1  2  3]
#  [ 5  6  7]
#  [ 9 10 11]
#  [13 14 15]]

a_1d = np.arange(6)
print(a_1d)
# [0 1 2 3 4 5]

# np.split(a_1d, 2, 1)
# IndexError: tuple index out of range

a0, a1 = np.hsplit(a_1d, 2)

print(a0)
# [0 1 2]

print(a1)
# [3 4 5]
