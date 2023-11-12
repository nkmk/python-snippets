import numpy as np

print(np.__version__)
# 1.26.1

a = np.arange(16).reshape(4, 4)
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]

a0, a1 = np.vsplit(a, 2)

print(a0)
# [[0 1 2 3]
#  [4 5 6 7]]

print(a1)
# [[ 8  9 10 11]
#  [12 13 14 15]]

a0, a1 = np.split(a, [1])

print(a0)
# [[0 1 2 3]]

print(a1)
# [[ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]
