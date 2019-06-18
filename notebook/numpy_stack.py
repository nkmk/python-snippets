import numpy as np

a1 = np.ones(3, int)
print(a1)
# [1 1 1]

print(a1.shape)
# (3,)

a2 = np.full(3, 2)
print(a2)
# [2 2 2]

print(a2.shape)
# (3,)

print(np.stack([a1, a2]))
# [[1 1 1]
#  [2 2 2]]

print(np.stack([a1, a2], 0))
# [[1 1 1]
#  [2 2 2]]

print(np.stack([a1, a2], 0).shape)
# (2, 3)

print(np.stack([a1, a2], 1))
# [[1 2]
#  [1 2]
#  [1 2]]

print(np.stack([a1, a2], 1).shape)
# (3, 2)

# print(np.stack([a1, a2], 2))
# AxisError: axis 2 is out of bounds for array of dimension 2

print(np.stack([a1, a2], -1))
# [[1 2]
#  [1 2]
#  [1 2]]

print(np.stack([a1, a2], -1).shape)
# (3, 2)

a2_ = np.full(4, 2)
print(a2_)
# [2 2 2 2]

print(a2_.shape)
# (4,)

# print(np.stack([a1, a2]))
# ValueError: all input arrays must have the same shape

a1 = np.ones((3, 4), int)
print(a1)
# [[1 1 1 1]
#  [1 1 1 1]
#  [1 1 1 1]]

print(a1.shape)
# (3, 4)

a2 = np.full((3, 4), 2)
print(a2)
# [[2 2 2 2]
#  [2 2 2 2]
#  [2 2 2 2]]

print(a2.shape)
# (3, 4)

print(np.stack([a1, a2]))
# [[[1 1 1 1]
#   [1 1 1 1]
#   [1 1 1 1]]
# 
#  [[2 2 2 2]
#   [2 2 2 2]
#   [2 2 2 2]]]

print(np.stack([a1, a2], 0))
# [[[1 1 1 1]
#   [1 1 1 1]
#   [1 1 1 1]]
# 
#  [[2 2 2 2]
#   [2 2 2 2]
#   [2 2 2 2]]]

print(np.stack([a1, a2], 0).shape)
# (2, 3, 4)

print(np.stack([a1, a2], 1))
# [[[1 1 1 1]
#   [2 2 2 2]]
# 
#  [[1 1 1 1]
#   [2 2 2 2]]
# 
#  [[1 1 1 1]
#   [2 2 2 2]]]

print(np.stack([a1, a2], 1).shape)
# (3, 2, 4)

print(np.stack([a1, a2], 1)[:, 0, :])
# [[1 1 1 1]
#  [1 1 1 1]
#  [1 1 1 1]]

print(np.stack([a1, a2], 1)[:, 1, :])
# [[2 2 2 2]
#  [2 2 2 2]
#  [2 2 2 2]]

print(np.stack([a1, a2], 2))
# [[[1 2]
#   [1 2]
#   [1 2]
#   [1 2]]
# 
#  [[1 2]
#   [1 2]
#   [1 2]
#   [1 2]]
# 
#  [[1 2]
#   [1 2]
#   [1 2]
#   [1 2]]]

print(np.stack([a1, a2], 2).shape)
# (3, 4, 2)

print(np.stack([a1, a2], 2)[:, :, 0])
# [[1 1 1 1]
#  [1 1 1 1]
#  [1 1 1 1]]

print(np.stack([a1, a2], 2)[:, :, 1])
# [[2 2 2 2]
#  [2 2 2 2]
#  [2 2 2 2]]

# print(np.stack([a1, a2], 3))
# AxisError: axis 3 is out of bounds for array of dimension 3

print(np.stack([a1, a2], -1))
# [[[1 2]
#   [1 2]
#   [1 2]
#   [1 2]]
# 
#  [[1 2]
#   [1 2]
#   [1 2]
#   [1 2]]
# 
#  [[1 2]
#   [1 2]
#   [1 2]
#   [1 2]]]

print(np.stack([a1, a2], -1).shape)
# (3, 4, 2)

a2_ = np.full((2, 3), 2)
print(a2_)
# [[2 2 2]
#  [2 2 2]]

# print(np.stack([a1, a2_]))
# ValueError: all input arrays must have the same shape
