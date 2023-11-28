import numpy as np

print(np.__version__)
# 1.26.1

a = np.array([1, 2, 3])
print(a)
print(a.dtype)
# [1 2 3]
# int64

a_float = a.astype(np.float32)
print(a_float)
print(a_float.dtype)
# [1. 2. 3.]
# float32

print(a)
print(a.dtype)
# [1 2 3]
# int64

a_int = a.astype('int32')
print(a_int)
print(a_int.dtype)
# [1 2 3]
# int32

a_uint = a.astype('u8')
print(a_uint)
print(a_uint.dtype)
# [1 2 3]
# uint64

a_float = a.astype(float)
print(a_float)
print(a_float.dtype)
# [1. 2. 3.]
# float64

a = np.array([-2, -1.5, -1, -0.5, 0.5, 1, 1.5, 2])
print(a)
# [-2.  -1.5 -1.  -0.5  0.5  1.   1.5  2. ]

print(a.astype(int))
# [-2 -1 -1  0  0  1  1  2]
