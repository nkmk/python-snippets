import numpy as np

arr = np.array([0, 1, 2])
print(arr)
# [0 1 2]

arr_2d = np.array([[0, 1, 2], [3, 4, 5]])
print(arr_2d)
# [[0 1 2]
#  [3 4 5]]

arr_2d_sqrt = np.sqrt(arr_2d)
print(arr_2d_sqrt)
# [[0.         1.         1.41421356]
#  [1.73205081 2.         2.23606798]]

arr_1 = np.array([[1, 2], [3, 4]])
arr_2 = np.array([[1, 2, 3], [4, 5, 6]])

arr_product = np.dot(arr_1, arr_2)
print(arr_product)
# [[ 9 12 15]
#  [19 26 33]]
