import numpy as np

l_2d = [[0, 1, 2], [3, 4, 5]]
print(l_2d)
# [[0, 1, 2], [3, 4, 5]]

print(type(l_2d))
# <class 'list'>

arr = np.array([[0, 1, 2], [3, 4, 5]])
print(arr)
# [[0 1 2]
#  [3 4 5]]

print(type(arr))
# <class 'numpy.ndarray'>

arr = np.arange(6)
print(arr)
# [0 1 2 3 4 5]

arr = np.arange(6).reshape((2, 3))
print(arr)
# [[0 1 2]
#  [3 4 5]]

mat = np.matrix([[0, 1, 2], [3, 4, 5]])
print(mat)
# [[0 1 2]
#  [3 4 5]]

print(type(mat))
# <class 'numpy.matrix'>

mat = np.matrix(arr)
print(mat)
# [[0 1 2]
#  [3 4 5]]

print(type(mat))
# <class 'numpy.matrix'>

mat_1d = np.matrix([0, 1, 2])
print(mat_1d)
# [[0 1 2]]

print(type(mat_1d))
# <class 'numpy.matrix'>

print(mat_1d.shape)
# (1, 3)

# mat_3d = np.matrix([[[0, 1, 2]]])
# ValueError: matrix must be 2-dimensional

print(l_2d)
# [[0, 1, 2], [3, 4, 5]]

print(l_2d[0][1])
# 1

l_2d[0][1] = 100
print(l_2d)
# [[0, 100, 2], [3, 4, 5]]

print(arr)
# [[0 1 2]
#  [3 4 5]]

print(arr[0, 1])
# 1

arr[0, 1] = 100
print(arr)
# [[  0 100   2]
#  [  3   4   5]]

l_2d = [[0, 1, 2], [3, 4, 5]]
print(l_2d)
# [[0, 1, 2], [3, 4, 5]]

print([list(x) for x in list(zip(*l_2d))])
# [[0, 3], [1, 4], [2, 5]]

arr = np.arange(6).reshape((2, 3))
print(arr)
# [[0 1 2]
#  [3 4 5]]

print(arr.T)
# [[0 3]
#  [1 4]
#  [2 5]]

l_2d_1 = [[0, 1, 2], [3, 4, 5]]
l_2d_2 = [[0, 2, 4], [6, 8, 10]]

print(l_2d_1 + l_2d_2)
# [[0, 1, 2], [3, 4, 5], [0, 2, 4], [6, 8, 10]]

# print(l_2d_1 - l_2d_2)
# TypeError: unsupported operand type(s) for -: 'list' and 'list'

arr1 = np.arange(6).reshape((2, 3))
print(arr1)
# [[0 1 2]
#  [3 4 5]]

arr2 = np.arange(0, 12, 2).reshape((2, 3))
print(arr2)
# [[ 0  2  4]
#  [ 6  8 10]]

print(arr1 + arr2)
# [[ 0  3  6]
#  [ 9 12 15]]

print(arr1 - arr2)
# [[ 0 -1 -2]
#  [-3 -4 -5]]

mat1 = np.matrix(arr1)
mat2 = np.matrix(arr2)

print(mat1 + mat2)
# [[ 0  3  6]
#  [ 9 12 15]]

print(mat1 - mat2)
# [[ 0 -1 -2]
#  [-3 -4 -5]]

print(l_2d_1 * 2)
# [[0, 1, 2], [3, 4, 5], [0, 1, 2], [3, 4, 5]]

# print(l_2d_1 * l_2d_2)
# TypeError: can't multiply sequence by non-int of type 'list'

print(arr1 * 2)
# [[ 0  2  4]
#  [ 6  8 10]]

print(mat1 * 2)
# [[ 0  2  4]
#  [ 6  8 10]]

print(np.multiply(arr1, arr2))
# [[ 0  2  8]
#  [18 32 50]]

print(np.multiply(mat1, mat2))
# [[ 0  2  8]
#  [18 32 50]]

print(arr1 * arr2)
# [[ 0  2  8]
#  [18 32 50]]

arr1 = np.arange(4).reshape((2, 2))
print(arr1)
# [[0 1]
#  [2 3]]

arr2 = np.arange(6).reshape((2, 3))
print(arr2)
# [[0 1 2]
#  [3 4 5]]

print(np.dot(arr1, arr2))
# [[ 3  4  5]
#  [ 9 14 19]]

print(arr1.dot(arr2))
# [[ 3  4  5]
#  [ 9 14 19]]

print(np.matmul(arr1, arr2))
# [[ 3  4  5]
#  [ 9 14 19]]

print(arr1 @ arr2)
# [[ 3  4  5]
#  [ 9 14 19]]

mat1 = np.matrix(arr1)
mat2 = np.matrix(arr2)

print(np.dot(mat1, mat2))
# [[ 3  4  5]
#  [ 9 14 19]]

print(mat1.dot(mat2))
# [[ 3  4  5]
#  [ 9 14 19]]

print(np.matmul(mat1, mat2))
# [[ 3  4  5]
#  [ 9 14 19]]

print(mat1 @ mat2)
# [[ 3  4  5]
#  [ 9 14 19]]

print(mat1 * mat2)
# [[ 3  4  5]
#  [ 9 14 19]]

arr = np.arange(1, 5).reshape(2, 2)
print(arr)
# [[1 2]
#  [3 4]]

print(arr**2)
# [[ 1  4]
#  [ 9 16]]

mat = np.matrix(arr)
print(mat)
# [[1 2]
#  [3 4]]

print(mat**2)
# [[ 7 10]
#  [15 22]]

print(mat**2 == mat * mat)
# [[ True  True]
#  [ True  True]]

print(mat**3 == mat * mat * mat)
# [[ True  True]
#  [ True  True]]

# print(arr**-1)
# ValueError: Integers to negative integer powers are not allowed.

arr_f = np.array(arr, dtype=float)
print(arr_f**-1)
# [[1.         0.5       ]
#  [0.33333333 0.25      ]]

print(mat**-1)
# [[-2.   1. ]
#  [ 1.5 -0.5]]

print(mat**-2)
# [[ 5.5  -2.5 ]
#  [-3.75  1.75]]

print(mat**-2 == mat**-1 * mat**-1)
# [[ True  True]
#  [ True  True]]

print(mat**-3 == mat**-1 * mat**-1 * mat**-1)
# [[ True  True]
#  [ True  True]]
