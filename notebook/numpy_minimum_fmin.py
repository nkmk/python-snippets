import numpy as np

a = np.array([0, 1, 2])
b = np.array([2, 0, 6])

print(np.minimum(a, b))
# [0 0 2]

print(np.fmin(a, b))
# [0 0 2]

a_2d = np.arange(6).reshape(2, 3)
print(a_2d)
# [[0 1 2]
#  [3 4 5]]

print(np.minimum(a_2d, b))
# [[0 0 2]
#  [2 0 5]]

print(np.fmin(a_2d, b))
# [[0 0 2]
#  [2 0 5]]

print(np.minimum(a_2d, 2))
# [[0 1 2]
#  [2 2 2]]

print(np.fmin(a_2d, 2))
# [[0 1 2]
#  [2 2 2]]

print(np.minimum([np.nan, np.nan], [np.inf, 0]))
# [nan nan]

print(np.fmin([np.nan, np.nan], [np.inf, 0]))
# [inf  0.]
