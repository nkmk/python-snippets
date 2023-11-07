import numpy as np

print(np.__version__)
# 1.26.1

l_1d = [0, 1, 2]

a_1d = np.array(l_1d)
print(a_1d)
# [0 1 2]

print(type(a_1d))
# <class 'numpy.ndarray'>

print(a_1d.dtype)
# int64

a_1d_f = np.array(l_1d, dtype=float)
print(a_1d_f)
# [0. 1. 2.]

print(a_1d_f.dtype)
# float64

l_2d = [[0, 1, 2], [3, 4, 5]]

a_2d = np.array(l_2d)
print(a_2d)
# [[0 1 2]
#  [3 4 5]]

l_2d_jagged = [[0, 1, 2], [3, 4]]

# a_2d_jagged = np.array(l_2d_jagged)
# ValueError: setting an array element with a sequence.
# The requested array has an inhomogeneous shape after 1 dimensions.
# The detected shape was (2,) + inhomogeneous part.

a_2d_jagged = np.array(l_2d_jagged, dtype=object)
print(a_2d_jagged)
# [list([0, 1, 2]) list([3, 4])]

print(a_2d_jagged.shape)
# (2,)

print(a_2d_jagged.dtype)
# object

print(a_2d_jagged[0])
# [0, 1, 2]

print(type(a_2d_jagged[0]))
# <class 'list'>

a_1d = np.arange(3)
print(a_1d)
# [0 1 2]

l_1d = a_1d.tolist()
print(l_1d)
# [0, 1, 2]

a_2d = np.arange(6).reshape((2, 3))
print(a_2d)
# [[0 1 2]
#  [3 4 5]]

l_2d = a_2d.tolist()
print(l_2d)
# [[0, 1, 2], [3, 4, 5]]

a_3d = np.arange(24).reshape((2, 3, 4))
print(a_3d)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
# 
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

l_3d = a_3d.tolist()
print(l_3d)
# [[[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]], [[12, 13, 14, 15], [16, 17, 18, 19], [20, 21, 22, 23]]]

print(l_3d[0])
# [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]

print(l_3d[0][0])
# [0, 1, 2, 3]

print(l_3d[0][0][0])
# 0

a_0d = np.array(100)
print(a_0d)
# 100

print(type(a_0d))
# <class 'numpy.ndarray'>

i = a_0d.tolist()
print(i)
# 100

print(type(i))
# <class 'int'>
