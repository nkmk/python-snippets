import numpy as np

v = np.array([0, 1, 2])
print(v)
# [0 1 2]

print(v.shape)
# (3,)

print(np.inner(v, v))
# 5

print(type(np.inner(v, v)))
# <class 'numpy.int64'>

print(np.dot(v, v))
# 5

print(np.matmul(v, v))
# 5

print(v @ v)
# 5

arr_row = np.arange(3).reshape(1, 3)
print(arr_row)
# [[0 1 2]]

print(arr_row.shape)
# (1, 3)

arr_col = np.arange(3).reshape(3, 1)
print(arr_col)
# [[0]
#  [1]
#  [2]]

print(arr_col.shape)
# (3, 1)

arr = np.arange(9).reshape(3, 3)
print(arr)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

print(v @ arr)
# [15 18 21]

print(arr_row @ arr)
# [[15 18 21]]

print(arr @ v)
# [ 5 14 23]

print(arr @ arr_col)
# [[ 5]
#  [14]
#  [23]]
