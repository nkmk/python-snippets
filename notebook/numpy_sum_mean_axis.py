import numpy as np

a = np.arange(12).reshape(3, 4)
print(a.shape)
print(a)
# (3, 4)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(np.sum(a))
# 66

print(np.sum(a, axis=0))
print(np.sum(a, axis=1))
# [12 15 18 21]
# [ 6 22 38]

print(a.sum())
# 66

print(a.sum(axis=0))
print(a.sum(axis=1))
# [12 15 18 21]
# [ 6 22 38]

print(np.mean(a))
# 5.5

print(np.mean(a, axis=0))
print(np.mean(a, axis=1))
# [ 4.  5.  6.  7.]
# [ 1.5  5.5  9.5]

print(a.mean())
# 5.5

print(a.mean(axis=0))
print(a.mean(axis=1))
# [ 4.  5.  6.  7.]
# [ 1.5  5.5  9.5]

print(np.min(a))
print(np.min(a, axis=0))
# 0
# [0 1 2 3]

print(a.max())
print(a.max(axis=1))
# 11
# [ 3  7 11]

b = np.arange(24).reshape(2, 3, 4)
print(b.shape)
print(b)
# (2, 3, 4)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

print(b.sum(axis=0))
# [[12 14 16 18]
#  [20 22 24 26]
#  [28 30 32 34]]

print(b[0, :, :] + b[1, :, :])
# [[12 14 16 18]
#  [20 22 24 26]
#  [28 30 32 34]]

print(b.sum(axis=1))
# [[12 15 18 21]
#  [48 51 54 57]]

print(b[:, 0, :] + b[:, 1, :] + b[:, 2, :])
# [[12 15 18 21]
#  [48 51 54 57]]

print(b.sum(axis=2))
# [[ 6 22 38]
#  [54 70 86]]

print(b[:, :, 0] + b[:, :, 1] + b[:, :, 2] + b[:, :, 3])
# [[ 6 22 38]
#  [54 70 86]]

print(b.sum(axis=(0, 1)))
# [60 66 72 78]

print(b.sum(axis=(0, 2)))
# [ 60  92 124]

print(b.sum(axis=(1, 2)))
# [ 66 210]
