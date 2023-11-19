import numpy as np

print(np.__version__)
# 1.26.1

a = np.arange(12).reshape(3, 4)
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(np.sum(a, axis=0))
# [12 15 18 21]

print(np.sum(a, axis=1))
# [ 6 22 38]

print(np.sum(a))
# 66

print(np.sum(a, axis=None))
# 66

# print(np.sum(a, axis=2))
# AxisError: axis 2 is out of bounds for array of dimension 2

print(np.sum(a, axis=-1))
# [ 6 22 38]

print(np.sum(a, axis=-2))
# [12 15 18 21]

# print(np.sum(a, axis=-3))
# AxisError: axis -3 is out of bounds for array of dimension 2

a = np.arange(6).reshape(2, 3)
print(a)
# [[0 1 2]
#  [3 4 5]]

print(np.sum(a, axis=0))
# [3 5 7]

print(np.sum(a, axis=1))
# [ 3 12]

print(a[0, :] + a[1, :])
# [3 5 7]

print(a[:, 0] + a[:, 1] + a[:, 2])
# [ 3 12]

a = np.stack([np.ones((3, 4), int), np.full((3, 4), 10)])
print(a)
# [[[ 1  1  1  1]
#   [ 1  1  1  1]
#   [ 1  1  1  1]]
# 
#  [[10 10 10 10]
#   [10 10 10 10]
#   [10 10 10 10]]]

print(a.shape)
# (2, 3, 4)

print(np.sum(a, axis=0))
# [[11 11 11 11]
#  [11 11 11 11]
#  [11 11 11 11]]

print(np.sum(a, axis=1))
# [[ 3  3  3  3]
#  [30 30 30 30]]

print(np.sum(a, axis=2))
# [[ 4  4  4]
#  [40 40 40]]

print(a[0, :, :] + a[1, :, :])
# [[11 11 11 11]
#  [11 11 11 11]
#  [11 11 11 11]]

print(a[:, 0, :] + a[:, 1, :] + a[:, 2, :])
# [[ 3  3  3  3]
#  [30 30 30 30]]

print(a[:, :, 0] + a[:, :, 1] + a[:, :, 2] + a[:, :, 3])
# [[ 4  4  4]
#  [40 40 40]]

print(np.sum(a, axis=(0, 1)))
# [33 33 33 33]

print(np.sum(a, axis=(0, 2)))
# [44 44 44]

print(np.sum(a, axis=(1, 2)))
# [ 12 120]

print(
    a[0, 0, :] + a[0, 1, :] + a[0, 2, :] +
    a[1, 0, :] + a[1, 1, :] + a[1, 2, :]
)
# [33 33 33 33]

print(
    a[0, :, 0] + a[0, :, 1] + a[0, :, 2] + a[0, :, 3] +
    a[1, :, 0] + a[1, :, 1] + a[1, :, 2] + a[1, :, 3]
)
# [44 44 44]

print(
    a[:, 0, 0] + a[:, 0, 1] + a[:, 0, 2] + a[:, 0, 3] + 
    a[:, 1, 0] + a[:, 1, 1] + a[:, 1, 2] + a[:, 1, 3] + 
    a[:, 2, 0] + a[:, 2, 1] + a[:, 2, 2] + a[:, 2, 3]
)
# [ 12 120]
