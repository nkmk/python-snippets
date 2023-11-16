import numpy as np

print(np.__version__)
# 1.26.1

a = np.arange(12).reshape(3, 4)
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(np.ravel(a))
# [ 0  1  2  3  4  5  6  7  8  9 10 11]

print(type(np.ravel(a)))
# <class 'numpy.ndarray'>

print(np.ravel([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]))
# [ 0  1  2  3  4  5  6  7  8  9 10 11]

print(type(np.ravel([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])))
# <class 'numpy.ndarray'>

# print(np.ravel([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9]]))
# ValueError: setting an array element with a sequence. The requested array has an inhomogeneous shape after 1 dimensions. The detected shape was (3,) + inhomogeneous part.

print(a.ravel())
# [ 0  1  2  3  4  5  6  7  8  9 10 11]

print(a.flatten())
# [ 0  1  2  3  4  5  6  7  8  9 10 11]

print(a.reshape(-1))
# [ 0  1  2  3  4  5  6  7  8  9 10 11]

print(np.reshape(a, -1))
# [ 0  1  2  3  4  5  6  7  8  9 10 11]

print(np.reshape([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]], -1))
# [ 0  1  2  3  4  5  6  7  8  9 10 11]

print(np.shares_memory(a, a.ravel()))
# True

print(np.shares_memory(a, np.ravel(a)))
# True

print(np.shares_memory(a, a.flatten()))
# False

print(np.shares_memory(a, a.reshape(-1)))
# True

print(np.shares_memory(a, np.reshape(a, -1)))
# True

a_ravel = a.ravel()
print(a_ravel)
# [ 0  1  2  3  4  5  6  7  8  9 10 11]

a_ravel[0] = 100
print(a_ravel)
# [100   1   2   3   4   5   6   7   8   9  10  11]

print(a)
# [[100   1   2   3]
#  [  4   5   6   7]
#  [  8   9  10  11]]

a = np.arange(12).reshape(3, 4)
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a[:, ::3])
# [[ 0  3]
#  [ 4  7]
#  [ 8 11]]

print(np.shares_memory(a[:, ::3], np.ravel(a[:, ::3])))
# False

print(np.shares_memory(a[:, ::3], np.reshape(a[:, ::3], -1)))
# False

print(a[:, ::2])
# [[ 0  2]
#  [ 4  6]
#  [ 8 10]]

print(np.shares_memory(a[:, ::2], np.ravel(a[:, ::2])))
# False

print(np.shares_memory(a[:, ::2], np.reshape(a[:, ::2], -1)))
# True

a_3d = np.arange(24).reshape(2, 3, 4)
print(a_3d)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
# 
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

print(a_3d.ravel())
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]

print(a_3d.ravel('F'))
# [ 0 12  4 16  8 20  1 13  5 17  9 21  2 14  6 18 10 22  3 15  7 19 11 23]
