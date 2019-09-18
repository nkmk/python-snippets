import numpy as np

a = np.array([0, 1, 2])
b = np.array([2, 0, 6])

print(np.maximum(a, b))
# [2 1 6]

print(np.fmax(a, b))
# [2 1 6]

l_a = [0, 1, 2]
l_b = [2, 0, 6]

print(np.maximum(l_a, l_b))
# [2 1 6]

print(np.fmax(l_a, l_b))
# [2 1 6]

print(np.maximum(0, 2))
# 2

print(np.fmax(0, 2))
# 2

print(max(0, 2))
# 2

a_2d = np.arange(6).reshape(2, 3)
print(a_2d)
# [[0 1 2]
#  [3 4 5]]

print(b)
# [2 0 6]

print(a_2d + b)
# [[ 2  1  8]
#  [ 5  4 11]]

print(np.maximum(a_2d, b))
# [[2 1 6]
#  [3 4 6]]

print(np.fmax(a_2d, b))
# [[2 1 6]
#  [3 4 6]]

a_mismatch = np.array([0, 1, 2, 3])

# print(np.maximum(a_mismatch, b))
# ValueError: operands could not be broadcast together with shapes (4,) (3,) 

# print(np.fmax(a_mismatch, b))
# ValueError: operands could not be broadcast together with shapes (4,) (3,) 

print(np.maximum(a_2d, 2))
# [[2 2 2]
#  [3 4 5]]

print(np.fmax(a_2d, 2))
# [[2 2 2]
#  [3 4 5]]

print(np.maximum(2, a_2d))
# [[2 2 2]
#  [3 4 5]]

print(np.fmax(2, a_2d))
# [[2 2 2]
#  [3 4 5]]

print(np.maximum([np.nan, np.nan], [np.inf, 0]))
# [nan nan]

print(np.fmax([np.nan, np.nan], [np.inf, 0]))
# [inf  0.]
