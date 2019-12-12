import numpy as np

print(np.newaxis is None)
# True

a = np.arange(6).reshape(2, 3)
print(a)
# [[0 1 2]
#  [3 4 5]]

print(a.shape)
# (2, 3)

print(a[:, :, np.newaxis])
# [[[0]
#   [1]
#   [2]]
# 
#  [[3]
#   [4]
#   [5]]]

print(a[:, :, np.newaxis].shape)
# (2, 3, 1)

print(a[:, np.newaxis, :])
# [[[0 1 2]]
# 
#  [[3 4 5]]]

print(a[:, np.newaxis, :].shape)
# (2, 1, 3)

print(a[np.newaxis, :, :])
# [[[0 1 2]
#   [3 4 5]]]

print(a[np.newaxis, :, :].shape)
# (1, 2, 3)

print(a[:, np.newaxis])
# [[[0 1 2]]
# 
#  [[3 4 5]]]

print(a[:, np.newaxis].shape)
# (2, 1, 3)

print(a[np.newaxis])
# [[[0 1 2]
#   [3 4 5]]]

print(a[np.newaxis].shape)
# (1, 2, 3)

print(a[..., np.newaxis])
# [[[0]
#   [1]
#   [2]]
# 
#  [[3]
#   [4]
#   [5]]]

print(a[..., np.newaxis].shape)
# (2, 3, 1)

print(a[np.newaxis, :, np.newaxis, :, np.newaxis])
# [[[[[0]
#     [1]
#     [2]]]
# 
# 
#   [[[3]
#     [4]
#     [5]]]]]

print(a[np.newaxis, :, np.newaxis, :, np.newaxis].shape)
# (1, 2, 1, 3, 1)

a_newaxis = a[:, :, np.newaxis]

print(np.shares_memory(a, a_newaxis))
# True

a = np.zeros(27, dtype=np.int).reshape(3, 3, 3)
print(a)
# [[[0 0 0]
#   [0 0 0]
#   [0 0 0]]
# 
#  [[0 0 0]
#   [0 0 0]
#   [0 0 0]]
# 
#  [[0 0 0]
#   [0 0 0]
#   [0 0 0]]]

print(a.shape)
# (3, 3, 3)

b = np.arange(9).reshape(3, 3)
print(b)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

print(b.shape)
# (3, 3)

print(a + b)
# [[[0 1 2]
#   [3 4 5]
#   [6 7 8]]
# 
#  [[0 1 2]
#   [3 4 5]
#   [6 7 8]]
# 
#  [[0 1 2]
#   [3 4 5]
#   [6 7 8]]]

print(b[np.newaxis, :, :].shape)
# (1, 3, 3)

print(a + b[np.newaxis, :, :])
# [[[0 1 2]
#   [3 4 5]
#   [6 7 8]]
# 
#  [[0 1 2]
#   [3 4 5]
#   [6 7 8]]
# 
#  [[0 1 2]
#   [3 4 5]
#   [6 7 8]]]

print(b[:, np.newaxis, :].shape)
# (3, 1, 3)

print(a + b[:, np.newaxis, :])
# [[[0 1 2]
#   [0 1 2]
#   [0 1 2]]
# 
#  [[3 4 5]
#   [3 4 5]
#   [3 4 5]]
# 
#  [[6 7 8]
#   [6 7 8]
#   [6 7 8]]]

print(b[:, :, np.newaxis].shape)
# (3, 3, 1)

print(a + b[:, :, np.newaxis])
# [[[0 0 0]
#   [1 1 1]
#   [2 2 2]]
# 
#  [[3 3 3]
#   [4 4 4]
#   [5 5 5]]
# 
#  [[6 6 6]
#   [7 7 7]
#   [8 8 8]]]

a = np.arange(6).reshape(2, 3)
print(a)
# [[0 1 2]
#  [3 4 5]]

print(a.shape)
# (2, 3)

print(a[np.newaxis])
# [[[0 1 2]
#   [3 4 5]]]

print(a[np.newaxis].shape)
# (1, 2, 3)

print(np.expand_dims(a, 0))
# [[[0 1 2]
#   [3 4 5]]]

print(np.expand_dims(a, 0).shape)
# (1, 2, 3)

print(a.reshape(1, 2, 3))
# [[[0 1 2]
#   [3 4 5]]]

print(a.reshape(1, 2, 3).shape)
# (1, 2, 3)

print(a.reshape(1, *a.shape))
# [[[0 1 2]
#   [3 4 5]]]

print(a.reshape(1, *a.shape).shape)
# (1, 2, 3)
