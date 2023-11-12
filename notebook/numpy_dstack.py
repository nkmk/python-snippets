import numpy as np

print(np.__version__)
# 1.26.1

a1 = np.ones((3, 4), int)
print(a1)
# [[1 1 1 1]
#  [1 1 1 1]
#  [1 1 1 1]]

a2 = np.full((3, 4), 2)
print(a2)
# [[2 2 2 2]
#  [2 2 2 2]
#  [2 2 2 2]]

print(np.dstack([a1, a2]))
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

print(np.dstack([a1, a2]).shape)
# (3, 4, 2)

print(np.dstack([a1, a2])[:, :, 0])
# [[1 1 1 1]
#  [1 1 1 1]
#  [1 1 1 1]]

print(np.dstack([a1, a2])[:, :, 1])
# [[2 2 2 2]
#  [2 2 2 2]
#  [2 2 2 2]]

print(np.concatenate([a1.reshape(3, 4, 1), a2.reshape(3, 4, 1)], 2))
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

a1 = np.ones(3, int)
print(a1)
# [1 1 1]

a2 = np.full(3, 2)
print(a2)
# [2 2 2]

print(np.dstack([a1, a2]))
# [[[1 2]
#   [1 2]
#   [1 2]]]

print(np.dstack([a1, a2]).shape)
# (1, 3, 2)

print(np.dstack([a1, a2])[:, :, 0])
# [[1 1 1]]

print(np.dstack([a1, a2])[:, :, 1])
# [[2 2 2]]

print(np.concatenate([a1.reshape(1, -1, 1), a2.reshape(1, -1, 1)], 2))
# [[[1 2]
#   [1 2]
#   [1 2]]]
