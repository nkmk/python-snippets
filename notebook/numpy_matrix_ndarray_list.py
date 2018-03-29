import numpy as np

l_2d = [[0, 1, 2], [3, 4, 5]]

print(l_2d)
print(type(l_2d))
# [[0, 1, 2], [3, 4, 5]]
# <class 'list'>

arr = np.array([[0, 1, 2], [3, 4, 5]])

print(arr)
print(type(arr))
# [[0 1 2]
#  [3 4 5]]
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
print(type(mat))
# [[0 1 2]
#  [3 4 5]]
# <class 'numpy.matrixlib.defmatrix.matrix'>

mat = np.matrix(arr)

print(mat)
print(type(mat))
# [[0 1 2]
#  [3 4 5]]
# <class 'numpy.matrixlib.defmatrix.matrix'>

mat_1d = np.matrix([0, 1, 2])

print(mat_1d)
print(type(mat_1d))
print(mat_1d.shape)
# [[0 1 2]]
# <class 'numpy.matrixlib.defmatrix.matrix'>
# (1, 3)

# mat_3d = np.matrix([[[0, 1, 2]]])
# ValueError: matrix must be 2-dimensional

print(l_2d[0][1])
# 1

l_2d[0][1] = 100

print(l_2d)
# [[0, 100, 2], [3, 4, 5]]

print(arr[0][1])
# 1

print(arr[0, 1])
# 1

arr[0, 1] = 100

print(arr)
# [[  0 100   2]
#  [  3   4   5]]

l_2d = [[0, 1, 2], [3, 4, 5]]

print(l_2d)
# [[0, 1, 2], [3, 4, 5]]

l_2d_t = [list(x) for x in list(zip(*l_2d))]
print(l_2d_t)
# [[0, 3], [1, 4], [2, 5]]

arr = np.arange(6).reshape((2, 3))

print(arr)
# [[0 1 2]
#  [3 4 5]]

arr_t = arr.T

print(arr_t)
# [[0 3]
#  [1 4]
#  [2 5]]

l_2d_1 = [[0, 1, 2], [3, 4, 5]]
l_2d_2 = [[0, 2, 4], [6, 8, 10]]

l_2d_sum = l_2d_1 + l_2d_2

print(l_2d_sum)
# [[0, 1, 2], [3, 4, 5], [0, 2, 4], [6, 8, 10]]

# l_2d_sub = l_2d_1 - l_2d_2
# TypeError: unsupported operand type(s) for -: 'list' and 'list'

arr1 = np.arange(6).reshape((2, 3))

print(arr1)
# [[0 1 2]
#  [3 4 5]]

arr2 = np.arange(0, 12, 2).reshape((2, 3))

print(arr2)
# [[ 0  2  4]
#  [ 6  8 10]]

arr_sum = arr1 + arr2

print(arr_sum)
# [[ 0  3  6]
#  [ 9 12 15]]

arr_sub = arr1 - arr2

print(arr_sub)
# [[ 0 -1 -2]
#  [-3 -4 -5]]

mat1 = np.matrix(arr1)
mat2 = np.matrix(arr2)

mat_sum = mat1 + mat2

print(mat_sum)
# [[ 0  3  6]
#  [ 9 12 15]]

mat_sub = mat1 - mat2

print(mat_sub)
# [[ 0 -1 -2]
#  [-3 -4 -5]]

l_2d_mul = l_2d_1 * 2

print(l_2d_mul)
# [[0, 1, 2], [3, 4, 5], [0, 1, 2], [3, 4, 5]]

# l_2d_mul = l_2d_1 * l_2d_2
# TypeError: can't multiply sequence by non-int of type 'list'

arr_mul = arr1 * 2

print(arr_mul)
# [[ 0  2  4]
#  [ 6  8 10]]

mat_mul = mat1 * 2

print(mat_mul)
# [[ 0  2  4]
#  [ 6  8 10]]

arr_mul = np.multiply(arr1, arr2)

print(arr_mul)
# [[ 0  2  8]
#  [18 32 50]]

mat_mul = np.multiply(mat1, mat2)

print(mat_mul)
# [[ 0  2  8]
#  [18 32 50]]

arr_mul = arr1 * arr2

print(arr_mul)
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

arr_mul_matrix = np.dot(arr1, arr2)

print(arr_mul_matrix)
# [[ 3  4  5]
#  [ 9 14 19]]

arr_mul_matrix = arr1.dot(arr2)

print(arr_mul_matrix)
# [[ 3  4  5]
#  [ 9 14 19]]

arr_mul_matrix = np.matmul(arr1, arr2)

print(arr_mul_matrix)
# [[ 3  4  5]
#  [ 9 14 19]]

arr_mul_matrix = arr1 @ arr2

print(arr_mul_matrix)
# [[ 3  4  5]
#  [ 9 14 19]]

mat1 = np.matrix(arr1)
mat2 = np.matrix(arr2)

mat_mul_matrix = np.dot(mat1, mat2)

print(mat_mul_matrix)
# [[ 3  4  5]
#  [ 9 14 19]]

mat_mul_matrix = mat1.dot(mat2)

print(mat_mul_matrix)
# [[ 3  4  5]
#  [ 9 14 19]]

mat_mul_matrix = np.matmul(mat1, mat2)

print(mat_mul_matrix)
# [[ 3  4  5]
#  [ 9 14 19]]

mat_mul_matrix = mat1 @ mat2

print(mat_mul_matrix)
# [[ 3  4  5]
#  [ 9 14 19]]

mat_mul_matrix = mat1 * mat2

print(mat_mul_matrix)
# [[ 3  4  5]
#  [ 9 14 19]]

arr = np.arange(1, 5).reshape(2, 2)

print(arr)
# [[1 2]
#  [3 4]]

mat = np.matrix(arr)

print(mat)
# [[1 2]
#  [3 4]]

print(arr)
# [[1 2]
#  [3 4]]

arr_p = arr**2

print(arr_p)
# [[ 1  4]
#  [ 9 16]]

print(mat)
# [[1 2]
#  [3 4]]

mat_p = mat**2

print(mat_p)
# [[ 7 10]
#  [15 22]]

print(mat**2 == mat * mat)
# [[ True  True]
#  [ True  True]]

print(mat**3 == mat * mat * mat)
# [[ True  True]
#  [ True  True]]

# arr_n = arr**-1
# ValueError: Integers to negative integer powers are not allowed.

arr_f = np.array(arr, dtype=float)

arr_f_n = arr_f**-1

print(arr_f_n)
# [[1.         0.5       ]
#  [0.33333333 0.25      ]]

mat_inv = mat**-1

print(mat_inv)
# [[-2.   1. ]
#  [ 1.5 -0.5]]

mat_inv2 = mat**-2

print(mat_inv2)
# [[ 5.5  -2.5 ]
#  [-3.75  1.75]]

print(mat**-2 == mat**-1 * mat**-1)
# [[ True  True]
#  [ True  True]]

print(mat**-3 == mat**-1 * mat**-1 * mat**-1)
# [[ True  True]
#  [ True  True]]
