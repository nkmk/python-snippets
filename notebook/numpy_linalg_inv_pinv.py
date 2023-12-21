import numpy as np

print(np.__version__)
# 1.26.2

a = np.array([[2, 5], [1, 3]])
print(a)
# [[2 5]
#  [1 3]]

print(np.linalg.inv(a))
# [[ 3. -5.]
#  [-1.  2.]]

print(a @ np.linalg.inv(a))
# [[1. 0.]
#  [0. 1.]]

a_singular = np.array([[0, 0], [1, 3]])
print(a_singular)
# [[0 0]
#  [1 3]]

# print(np.linalg.inv(a_singular))
# LinAlgError: Singular matrix

print(np.linalg.pinv(a_singular))
# [[0.  0.1]
#  [0.  0.3]]

print(a_singular @ np.linalg.pinv(a_singular))
# [[0. 0.]
#  [0. 1.]]

print(np.linalg.pinv(np.linalg.pinv(a_singular)))
# [[0. 0.]
#  [1. 3.]]

a = np.array([[2, 5], [1, 3]])
print(a)
# [[2 5]
#  [1 3]]

print(np.linalg.inv(a))
# [[ 3. -5.]
#  [-1.  2.]]

print(np.linalg.pinv(a))
# [[ 3. -5.]
#  [-1.  2.]]
