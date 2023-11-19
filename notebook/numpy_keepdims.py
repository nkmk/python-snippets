import numpy as np

print(np.__version__)
# 1.26.1

a = np.ones((3, 4), int)
print(a)
# [[1 1 1 1]
#  [1 1 1 1]
#  [1 1 1 1]]

print(a.shape)
# (3, 4)

print(np.sum(a, axis=1))
# [4 4 4]

print(np.sum(a, axis=1).shape)
# (3,)

print(np.sum(a, axis=1, keepdims=True))
# [[4]
#  [4]
#  [4]]

print(np.sum(a, axis=1, keepdims=True).shape)
# (3, 1)

# print(a + np.sum(a, axis=1))
# ValueError: operands could not be broadcast together with shapes (3,4) (3,)

print(a + np.sum(a, axis=1, keepdims=True))
# [[5 5 5 5]
#  [5 5 5 5]
#  [5 5 5 5]]

print(a + np.sum(a, axis=0))
# [[4 4 4 4]
#  [4 4 4 4]
#  [4 4 4 4]]

print(a + np.sum(a, axis=0, keepdims=True))
# [[4 4 4 4]
#  [4 4 4 4]
#  [4 4 4 4]]

a = np.ones((2, 3, 4), int)
print(a)
# [[[1 1 1 1]
#   [1 1 1 1]
#   [1 1 1 1]]
# 
#  [[1 1 1 1]
#   [1 1 1 1]
#   [1 1 1 1]]]

print(np.sum(a, axis=(0, 2)))
# [8 8 8]

print(np.sum(a, axis=(0, 2), keepdims=True))
# [[[8]
#   [8]
#   [8]]]

# print(a + np.sum(a, axis=(0, 2)))
# ValueError: operands could not be broadcast together with shapes (2,3,4) (3,)

print(a + np.sum(a, axis=(0, 2), keepdims=True))
# [[[9 9 9 9]
#   [9 9 9 9]
#   [9 9 9 9]]
# 
#  [[9 9 9 9]
#   [9 9 9 9]
#   [9 9 9 9]]]
