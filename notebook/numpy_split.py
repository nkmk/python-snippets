import numpy as np

a = np.arange(16).reshape(4, 4)
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]

a_split = np.split(a, 2)

print(type(a_split))
# <class 'list'>

print(len(a_split))
# 2

print(a_split[0])
# [[0 1 2 3]
#  [4 5 6 7]]

print(a_split[1])
# [[ 8  9 10 11]
#  [12 13 14 15]]

print(type(a_split[0]))
# <class 'numpy.ndarray'>

print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]

a0, a1 = np.split(a, 2)

print(a0)
# [[0 1 2 3]
#  [4 5 6 7]]

print(a1)
# [[ 8  9 10 11]
#  [12 13 14 15]]

# np.split(a, 3)
# ValueError: array split does not result in an equal division

a0, a1, a2 = np.split(a, [1, 3])

print(a0)
# [[0 1 2 3]]

print(a1)
# [[ 4  5  6  7]
#  [ 8  9 10 11]]

print(a2)
# [[12 13 14 15]]

a0, a1 = np.split(a, [1])

print(a0)
# [[0 1 2 3]]

print(a1)
# [[ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]

a0, a1 = np.split(a, 2, 0)

print(a0)
# [[0 1 2 3]
#  [4 5 6 7]]

print(a1)
# [[ 8  9 10 11]
#  [12 13 14 15]]

a0, a1 = np.split(a, 2, 1)

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

# np.split(a, 2, 2)
# IndexError: tuple index out of range

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

a0, a1 = np.split(a_3d, 2, 0)

print(a0)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]]

print(a1)
# [[[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

a0, a1 = np.split(a_3d, [1], 2)

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
