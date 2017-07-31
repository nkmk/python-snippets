import numpy as np

l = [[0, 0, 0], [0, 0, 0]]
arr = np.array(l)
arr
# array([[0, 0, 0],
#        [0, 0, 0]])

arr.dtype
# dtype('int64')

arr.shape
# (2, 3)

arr.ndim
# 2

l2 = [[0, 0, 0], [0, 0]]
arr2 = np.array(l2)
arr2
# array([[0, 0, 0], [0, 0]], dtype=object)

arr2.dtype
# dtype('O')

arr2.shape
# (2,)

arr2.ndim
# 1
