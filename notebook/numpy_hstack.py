import numpy as np

a1 = np.ones((2, 3), int)
print(a1)
# [[1 1 1]
#  [1 1 1]]

a2 = np.full((2, 3), 2)
print(a2)
# [[2 2 2]
#  [2 2 2]]

print(np.hstack([a1, a2]))
# [[1 1 1 2 2 2]
#  [1 1 1 2 2 2]]

print(np.concatenate([a1, a2], 1))
# [[1 1 1 2 2 2]
#  [1 1 1 2 2 2]]

a1 = np.ones(3, int)
print(a1)
# [1 1 1]

a2 = np.full(3, 2)
print(a2)
# [2 2 2]

print(np.hstack([a1, a2]))
# [1 1 1 2 2 2]

print(np.concatenate([a1, a2], 0))
# [1 1 1 2 2 2]
