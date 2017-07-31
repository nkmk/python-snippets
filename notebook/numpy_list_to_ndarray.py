import numpy as np

l = [[0, 0, 0], [0, 0, 0]]
arr = np.array(l)
print(arr)
# [[0 0 0]
#  [0 0 0]]

print(arr.dtype, arr.shape, arr.ndim)
# int64 (2, 3) 2

l2 = [[0, 0, 0], [0, 0]]
arr2 = np.array(l2)
print(arr2)
# [[0, 0, 0] [0, 0]]

print(arr2.dtype, arr2.shape, arr2.ndim)
# object (2,) 1
