import numpy as np

print(np.__version__)
# 1.26.1

a_1d = np.arange(4)
print(a_1d)
# [0 1 2 3]

print(a_1d[[True, False, True, False]])
# [0 2]

print(a_1d[np.array([True, False, True, False])])
# [0 2]

# print(a_1d[[True, False]])
# IndexError: boolean index did not match indexed array along dimension 0; dimension is 4 but corresponding boolean dimension is 2

a_2d = np.arange(12).reshape(3, 4)
print(a_2d)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a_2d[[True, False, True]])
# [[ 0  1  2  3]
#  [ 8  9 10 11]]

print(a_2d[:, [True, False, True, False]])
# [[ 0  2]
#  [ 4  6]
#  [ 8 10]]

print(a_2d[[True, False, True], [True, False, True, False]])
# [ 0 10]

print(a_2d[np.ix_([True, False, True], [True, False, True, False])])
# [[ 0  2]
#  [ 8 10]]

print(a_2d[:, [True, False, False, False]])
# [[0]
#  [4]
#  [8]]

print(a_2d > 5)
# [[False False False False]
#  [False False  True  True]
#  [ True  True  True  True]]

print(a_2d[a_2d > 5])
# [ 6  7  8  9 10 11]

print((a_2d > 5) & (a_2d < 10))
# [[False False False False]
#  [False False  True  True]
#  [ True  True False False]]

print(a_2d[(a_2d > 5) & (a_2d < 10)])
# [6 7 8 9]
