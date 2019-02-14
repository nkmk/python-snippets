import numpy as np

a = np.arange(3)
print(a)
# [0 1 2]

print(a.shape)
# (3,)

b = np.arange(3).reshape(3, 1)
print(b)
# [[0]
#  [1]
#  [2]]

print(b.shape)
# (3, 1)

arrays = np.broadcast_arrays(a, b)

print(type(arrays))
# <class 'list'>

print(len(arrays))
# 2

print(arrays[0])
# [[0 1 2]
#  [0 1 2]
#  [0 1 2]]

print(arrays[1])
# [[0 0 0]
#  [1 1 1]
#  [2 2 2]]

print(type(arrays[0]))
# <class 'numpy.ndarray'>

c = np.zeros((2, 2))
print(c)
# [[0. 0.]
#  [0. 0.]]

print(c.shape)
# (2, 2)

# arrays = np.broadcast_arrays(a, c)
# ValueError: shape mismatch: objects cannot be broadcast to a single shape
