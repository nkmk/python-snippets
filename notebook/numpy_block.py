import numpy as np

a1 = np.ones((2, 3), int)
print(a1)
# [[1 1 1]
#  [1 1 1]]

a2 = np.full((2, 3), 2)
print(a2)
# [[2 2 2]
#  [2 2 2]]

print(np.block([a1, a2]))
# [[1 1 1 2 2 2]
#  [1 1 1 2 2 2]]

print(np.block([[a1], [a2]]))
# [[1 1 1]
#  [1 1 1]
#  [2 2 2]
#  [2 2 2]]

print(np.block([[a1, a2], [a2, a1]]))
# [[1 1 1 2 2 2]
#  [1 1 1 2 2 2]
#  [2 2 2 1 1 1]
#  [2 2 2 1 1 1]]

print(np.block([[[a1]], [[a2]]]))
# [[[1 1 1]
#   [1 1 1]]
# 
#  [[2 2 2]
#   [2 2 2]]]

print(np.block([[[a1]], [[a2]]]).shape)
# (2, 2, 3)

a3 = np.full(6, 3)
print(a3)
# [3 3 3 3 3 3]

print(np.block([[a1, a2], [a3]]))
# [[1 1 1 2 2 2]
#  [1 1 1 2 2 2]
#  [3 3 3 3 3 3]]

# print(np.block([[a1, a2], a3]))
# ValueError: List depths are mismatched. First element was at depth 2, but there is an element at depth 1 (arrays[1])

# print(np.block([[a1, a2, a3]]))
# ValueError: all the input array dimensions except for the concatenation axis must match exactly
