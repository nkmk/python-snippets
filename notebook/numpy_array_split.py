import numpy as np

a = np.arange(15).reshape(3, 5)
print(a)
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]]

# np.split(a, 2, 0)
# ValueError: array split does not result in an equal division

a0, a1 = np.array_split(a, 2, 0)

print(a0)
# [[0 1 2 3 4]
#  [5 6 7 8 9]]

print(a1)
# [[10 11 12 13 14]]

a0, a1, a2 = np.array_split(a, 3, 1)

print(a0)
# [[ 0  1]
#  [ 5  6]
#  [10 11]]

print(a1)
# [[ 2  3]
#  [ 7  8]
#  [12 13]]

print(a2)
# [[ 4]
#  [ 9]
#  [14]]
