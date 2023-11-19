import numpy as np

print(np.__version__)
# 1.26.1

a = np.arange(12).reshape(3, 4)
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(np.sum(a))
# 66

print(np.sum(a, axis=0))
# [12 15 18 21]

print(np.sum(a, axis=1))
# [ 6 22 38]

print(np.sum(a, axis=-1))
# [ 6 22 38]

print(np.sum(a, axis=-2))
# [12 15 18 21]

# print(np.sum(a, axis=2))
# AxisError: axis 2 is out of bounds for array of dimension 2

# print(np.sum(a, axis=-3))
# AxisError: axis -3 is out of bounds for array of dimension 2

print(a.sum())
# 66

print(a.sum(axis=0))
# [12 15 18 21]

print(a.sum(axis=1))
# [ 6 22 38]

print(np.mean(a))
# 5.5

print(np.mean(a, axis=0))
# [4. 5. 6. 7.]

print(np.mean(a, axis=1))
# [1.5 5.5 9.5]

print(a.mean())
# 5.5

print(a.mean(axis=0))
# [4. 5. 6. 7.]

print(a.mean(axis=1))
# [1.5 5.5 9.5]

print(np.max(a))
# 11

print(np.max(a, axis=0))
# [ 8  9 10 11]

print(np.max(a, axis=1))
# [ 3  7 11]

print(np.min(a))
# 0

print(np.min(a, axis=0))
# [0 1 2 3]

print(np.min(a, axis=1))
# [0 4 8]

print(a.max())
# 11

print(a.max(axis=0))
# [ 8  9 10 11]

print(a.max(axis=1))
# [ 3  7 11]

print(a.min())
# 0

print(a.min(axis=0))
# [0 1 2 3]

print(a.min(axis=1))
# [0 4 8]
