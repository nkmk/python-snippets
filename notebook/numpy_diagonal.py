import numpy as np

a = np.arange(9).reshape((3, 3))

print(a)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

print(a.diagonal())
# [0 4 8]

print(a.diagonal(offset=1))
# [1 5]

print(a.diagonal(offset=3))
# []

print(a.diagonal(offset=-2))
# [6]

a = np.arange(12).reshape((3, 4))

print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a.diagonal())
# [ 0  5 10]

print(a.diagonal(offset=1))
# [ 1  6 11]

a = np.arange(3)

print(a)
# [0 1 2]

# a.diagonal()
# ValueError: diag requires an array of at least two dimensions
