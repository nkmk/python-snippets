import numpy as np

a = b = np.arange(3)
print(a)
# [0 1 2]

print(a.shape)
# (3,)

print(a * b)
# [0 1 4]

print(np.multiply(a, b))
# [0 1 4]

a_1_3 = a.reshape(1, 3)
print(a_1_3)
# [[0 1 2]]

print(a_1_3.shape)
# (1, 3)

b_3_1 = b.reshape(3, 1)
print(b_3_1)
# [[0]
#  [1]
#  [2]]

print(b_3_1.shape)
# (3, 1)

print(a_1_3 * b_3_1)
# [[0 0 0]
#  [0 1 2]
#  [0 2 4]]

print(np.multiply(a_1_3, b_3_1))
# [[0 0 0]
#  [0 1 2]
#  [0 2 4]]

print(a * b_3_1)
# [[0 0 0]
#  [0 1 2]
#  [0 2 4]]

print(np.multiply(a, b_3_1))
# [[0 0 0]
#  [0 1 2]
#  [0 2 4]]

print(a_1_3 @ b_3_1)
# [[5]]

print(np.matmul(a_1_3, b_3_1))
# [[5]]

print(np.dot(a_1_3, b_3_1))
# [[5]]

print(type(a_1_3 @ b_3_1))
# <class 'numpy.ndarray'>

print((a_1_3 @ b_3_1).shape)
# (1, 1)

print(a_1_3 @ b)
# [5]

print(np.matmul(a_1_3, b))
# [5]

print(np.dot(a_1_3, b))
# [5]

print(type(a_1_3 @ b))
# <class 'numpy.ndarray'>

print((a_1_3 @ b).shape)
# (1,)

print(a @ b)
# 5

print(np.matmul(a, b))
# 5

print(np.dot(a, b))
# 5

print(type(a @ b))
# <class 'numpy.int64'>

a = np.arange(6).reshape(2, 3)
print(a)
# [[0 1 2]
#  [3 4 5]]

b = np.arange(2).reshape(1, 2)
print(b)
# [[0 1]]

# print(a @ b)
# ValueError: shapes (2,3) and (1,2) not aligned: 3 (dim 1) != 1 (dim 0)

print(np.tile(b, (3, 1)))
# [[0 1]
#  [0 1]
#  [0 1]]

print(a @ np.tile(b, (3, 1)))
# [[ 0  3]
#  [ 0 12]]
