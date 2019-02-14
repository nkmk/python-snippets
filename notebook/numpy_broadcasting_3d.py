import numpy as np

a = np.zeros((2, 3, 4), dtype=np.int)
print(a)
# [[[0 0 0 0]
#   [0 0 0 0]
#   [0 0 0 0]]
# 
#  [[0 0 0 0]
#   [0 0 0 0]
#   [0 0 0 0]]]

print(a.shape)
# (2, 3, 4)

b = np.arange(4)
print(b)
# [0 1 2 3]

print(b.shape)
# (4,)

print(a + b)
# [[[0 1 2 3]
#   [0 1 2 3]
#   [0 1 2 3]]
# 
#  [[0 1 2 3]
#   [0 1 2 3]
#   [0 1 2 3]]]

b_1_1_4 = b.reshape(1, 1, 4)
print(b_1_1_4)
# [[[0 1 2 3]]]

print(np.tile(b_1_1_4, (2, 3, 1)))
# [[[0 1 2 3]
#   [0 1 2 3]
#   [0 1 2 3]]
# 
#  [[0 1 2 3]
#   [0 1 2 3]
#   [0 1 2 3]]]
