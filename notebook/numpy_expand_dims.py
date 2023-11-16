import numpy as np

print(np.__version__)
# 1.26.1

a = np.arange(6).reshape(2, 3)
print(a)
# [[0 1 2]
#  [3 4 5]]

print(np.expand_dims(a, 0))
# [[[0 1 2]
#   [3 4 5]]]

print(np.expand_dims(a, 0).shape)
# (1, 2, 3)

print(np.expand_dims(a, 1).shape)
# (2, 1, 3)

print(np.expand_dims(a, 2).shape)
# (2, 3, 1)

print(np.expand_dims(a, -1).shape)
# (2, 3, 1)

print(np.expand_dims(a, -2).shape)
# (2, 1, 3)

print(np.expand_dims(a, -3).shape)
# (1, 2, 3)

# print(np.expand_dims(a, 3).shape)
# AxisError: axis 3 is out of bounds for array of dimension 3

# print(np.expand_dims(a, -4).shape)
# AxisError: axis -4 is out of bounds for array of dimension 3

print(np.expand_dims(a, (0, 1, -1)).shape)
# (1, 1, 2, 3, 1)

a_expand_dims = np.expand_dims(a, 0)

print(np.shares_memory(a, a_expand_dims))
# True
