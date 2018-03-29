import numpy as np

arr = np.array([[2, 5], [1, 3]])

arr_inv = np.linalg.inv(arr)

print(arr_inv)
# [[ 3. -5.]
#  [-1.  2.]]

mat = np.matrix([[2, 5], [1, 3]])

mat_inv = np.linalg.inv(mat)

print(mat_inv)
# [[ 3. -5.]
#  [-1.  2.]]

mat_inv = mat**-1

print(mat_inv)
# [[ 3. -5.]
#  [-1.  2.]]

mat_inv = mat.I

print(mat_inv)
# [[ 3. -5.]
#  [-1.  2.]]

result = mat * mat.I

print(result)
# [[1. 0.]
#  [0. 1.]]
