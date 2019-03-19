import numpy as np

a = np.arange(3)
print(a)
# [0 1 2]

a_tile = np.tile(a, 3)
print(a_tile)
# [0 1 2 0 1 2 0 1 2]

print(a)
# [0 1 2]

print(np.tile(a, (2, 3)))
# [[0 1 2 0 1 2 0 1 2]
#  [0 1 2 0 1 2 0 1 2]]

print(np.tile(a, (2, 3)).shape)
# (2, 9)

print(np.tile(a, (2, 3, 4)))
# [[[0 1 2 0 1 2 0 1 2 0 1 2]
#   [0 1 2 0 1 2 0 1 2 0 1 2]
#   [0 1 2 0 1 2 0 1 2 0 1 2]]
# 
#  [[0 1 2 0 1 2 0 1 2 0 1 2]
#   [0 1 2 0 1 2 0 1 2 0 1 2]
#   [0 1 2 0 1 2 0 1 2 0 1 2]]]

print(np.tile(a, (2, 3, 4)).shape)
# (2, 3, 12)

a_2d = np.arange(6).reshape(2, 3)
print(a_2d)
# [[0 1 2]
#  [3 4 5]]

print(np.tile(a_2d, 2))
# [[0 1 2 0 1 2]
#  [3 4 5 3 4 5]]

print(np.tile(a_2d, (2, )))
# [[0 1 2 0 1 2]
#  [3 4 5 3 4 5]]

print(np.tile(a_2d, (1, 2)))
# [[0 1 2 0 1 2]
#  [3 4 5 3 4 5]]

print(np.tile(a_2d, (2, 1)))
# [[0 1 2]
#  [3 4 5]
#  [0 1 2]
#  [3 4 5]]

print(np.tile(a_2d, (2, 2, 2)))
# [[[0 1 2 0 1 2]
#   [3 4 5 3 4 5]
#   [0 1 2 0 1 2]
#   [3 4 5 3 4 5]]
# 
#  [[0 1 2 0 1 2]
#   [3 4 5 3 4 5]
#   [0 1 2 0 1 2]
#   [3 4 5 3 4 5]]]

print(np.tile(a_2d, (2, 2, 2)).shape)
# (2, 4, 6)
