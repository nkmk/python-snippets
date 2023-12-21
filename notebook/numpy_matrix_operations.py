import numpy as np

print(np.__version__)
# 1.26.2

a = np.array([[0, 1, 2], [3, 4, 5]])
print(a)
# [[0 1 2]
#  [3 4 5]]

print(type(a))
# <class 'numpy.ndarray'>

print(np.arange(6).reshape(2, 3))
# [[0 1 2]
#  [3 4 5]]

a = np.array([[0, 1, 2], [3, 4, 5]])
print(a)
# [[0 1 2]
#  [3 4 5]]

print(a[0, 1])
# 1

a[0, 1] = 100
print(a)
# [[  0 100   2]
#  [  3   4   5]]

print(a[:, 1:])
# [[100   2]
#  [  4   5]]

a1 = np.arange(6).reshape(2, 3)
print(a1)
# [[0 1 2]
#  [3 4 5]]

a2 = np.arange(6, 18, 2).reshape(2, 3)
print(a2)
# [[ 6  8 10]
#  [12 14 16]]

print(a1 + a2)
# [[ 6  9 12]
#  [15 18 21]]

print(a1 - a2)
# [[ -6  -7  -8]
#  [ -9 -10 -11]]

print(a1 * a2)
# [[ 0  8 20]
#  [36 56 80]]

print(a1 / a2)
# [[0.         0.125      0.2       ]
#  [0.25       0.28571429 0.3125    ]]

print(a1**a2)
# [[           0            1         1024]
#  [      531441    268435456 152587890625]]

print(a1 * 100)
# [[  0 100 200]
#  [300 400 500]]

print(a1 * [10, 100, 1000])
# [[   0  100 2000]
#  [  30  400 5000]]

# print(a2 ** -1)
# ValueError: Integers to negative integer powers are not allowed.

print(a2.astype(float) ** -1)
# [[0.16666667 0.125      0.1       ]
#  [0.08333333 0.07142857 0.0625    ]]

print(np.multiply(a1, a2))
# [[ 0  8 20]
#  [36 56 80]]

a1 = np.arange(4).reshape((2, 2))
print(a1)
# [[0 1]
#  [2 3]]

a2 = np.arange(6).reshape((2, 3))
print(a2)
# [[0 1 2]
#  [3 4 5]]

print(a1 @ a2)
# [[ 3  4  5]
#  [ 9 14 19]]

print(np.matmul(a1, a2))
# [[ 3  4  5]
#  [ 9 14 19]]

print(np.dot(a1, a2))
# [[ 3  4  5]
#  [ 9 14 19]]

print(a1.dot(a2))
# [[ 3  4  5]
#  [ 9 14 19]]

a_row = np.arange(3).reshape(1, 3)
print(a_row)
# [[0 1 2]]

print(a_row.shape)
# (1, 3)

a_col = np.arange(3).reshape(3, 1)
print(a_col)
# [[0]
#  [1]
#  [2]]

print(a_col.shape)
# (3, 1)

a_2d = np.arange(9).reshape(3, 3)
print(a_2d)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

print(a_row @ a_2d)
# [[15 18 21]]

print(a_2d @ a_col)
# [[ 5]
#  [14]
#  [23]]

a_1d = np.array([0, 1, 2])

print(a_1d @ a_2d)
# [15 18 21]

print(np.dot(a_1d, a_2d))
# [15 18 21]

print(a_2d @ a_1d)
# [ 5 14 23]

print(np.dot(a_2d, a_1d))
# [ 5 14 23]

a1 = np.array([0, 1, 2])
a2 = np.array([3, 4, 5])

print(np.inner(a1, a2))
# 14

print(a1 @ a2)
# 14

print(np.dot(a1, a2))
# 14
