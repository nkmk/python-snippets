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

# print(arr.I)
# AttributeError: 'numpy.ndarray' object has no attribute 'I'

arr_s = np.array([[0, 0], [1, 3]])

# print(np.linalg.inv(arr_s))
# LinAlgError: Singular matrix

arr_pinv = np.linalg.pinv(arr_s)
print(arr_pinv)
# [[0.  0.1]
#  [0.  0.3]]

print(arr_s @ arr_inv)
# [[0. 0.]
#  [0. 1.]]

print(np.linalg.pinv(arr_pinv))
# [[0. 0.]
#  [1. 3.]]

print(np.linalg.inv(arr))
# [[ 3. -5.]
#  [-1.  2.]]

print(np.linalg.pinv(arr))
# [[ 3. -5.]
#  [-1.  2.]]

mat_s = np.mat([[0, 0], [1, 3]])

# print(np.linalg.inv(mat_s))
# LinAlgError: Singular matrix

# print(mat_s**-1)
# LinAlgError: Singular matrix

# print(mat_s.I)
# LinAlgError: Singular matrix

print(np.linalg.pinv(mat_s))
# [[0.  0.1]
#  [0.  0.3]]
