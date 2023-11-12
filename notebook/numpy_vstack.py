import numpy as np

print(np.__version__)
# 1.26.1

a1 = np.ones((2, 3), int)
print(a1)
# [[1 1 1]
#  [1 1 1]]

a2 = np.full((2, 3), 2)
print(a2)
# [[2 2 2]
#  [2 2 2]]

print(np.vstack([a1, a2]))
# [[1 1 1]
#  [1 1 1]
#  [2 2 2]
#  [2 2 2]]

print(np.concatenate([a1, a2], 0))
# [[1 1 1]
#  [1 1 1]
#  [2 2 2]
#  [2 2 2]]

a1 = np.ones(3, int)
print(a1)
# [1 1 1]

a2 = np.full(3, 2)
print(a2)
# [2 2 2]

print(np.vstack([a1, a2]))
# [[1 1 1]
#  [2 2 2]]

print(np.concatenate([a1.reshape(1, -1), a2.reshape(1, -1)], 0))
# [[1 1 1]
#  [2 2 2]]

a2_2d = np.full((2, 3), 2)
print(a2_2d)
# [[2 2 2]
#  [2 2 2]]

print(np.vstack([a1, a2_2d]))
# [[1 1 1]
#  [2 2 2]
#  [2 2 2]]

print(np.concatenate([a1.reshape(1, -1), a2_2d], 0))
# [[1 1 1]
#  [2 2 2]
#  [2 2 2]]
