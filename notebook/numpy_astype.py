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

a = np.linspace(-3.0, 2.9, 60).reshape(6, 10)
print(a)
# [[-3.  -2.9 -2.8 -2.7 -2.6 -2.5 -2.4 -2.3 -2.2 -2.1]
#  [-2.  -1.9 -1.8 -1.7 -1.6 -1.5 -1.4 -1.3 -1.2 -1.1]
#  [-1.  -0.9 -0.8 -0.7 -0.6 -0.5 -0.4 -0.3 -0.2 -0.1]
#  [ 0.   0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9]
#  [ 1.   1.1  1.2  1.3  1.4  1.5  1.6  1.7  1.8  1.9]
#  [ 2.   2.1  2.2  2.3  2.4  2.5  2.6  2.7  2.8  2.9]]

print(a.astype(int))
# [[-3 -2 -2 -2 -2 -2 -2 -2 -2 -2]
#  [-2 -1 -1 -1 -1 -1 -1 -1 -1 -1]
#  [-1  0  0  0  0  0  0  0  0  0]
#  [ 0  0  0  0  0  0  0  0  0  0]
#  [ 1  1  1  1  1  1  1  1  1  1]
#  [ 2  2  2  2  2  2  2  2  2  2]]

print(np.round(a).astype(int))
# [[-3 -3 -3 -3 -3 -2 -2 -2 -2 -2]
#  [-2 -2 -2 -2 -2 -2 -1 -1 -1 -1]
#  [-1 -1 -1 -1 -1  0  0  0  0  0]
#  [ 0  0  0  0  0  0  1  1  1  1]
#  [ 1  1  1  1  1  2  2  2  2  2]
#  [ 2  2  2  2  2  2  3  3  3  3]]

def my_round(x, decimals=0):
    p = 10**decimals
    return (x * p * 2 + 1) // 2 / p

print(my_round(a).astype(int))
# [[-3 -3 -3 -3 -3 -2 -2 -2 -2 -2]
#  [-2 -2 -2 -2 -2 -1 -1 -1 -1 -1]
#  [-1 -1 -1 -1 -1  0  0  0  0  0]
#  [ 0  0  0  0  0  1  1  1  1  1]
#  [ 1  1  1  1  1  2  2  2  2  2]
#  [ 2  2  2  2  2  3  3  3  3  3]]

def my_round2(x, decimals=0):
    p = 10**decimals
    return (np.abs(x) * p * 2 + 1) // 2 / p * np.sign(x)

print(my_round2(a).astype(int))
# [[-3 -3 -3 -3 -3 -3 -2 -2 -2 -2]
#  [-2 -2 -2 -2 -2 -2 -1 -1 -1 -1]
#  [-1 -1 -1 -1 -1 -1  0  0  0  0]
#  [ 0  0  0  0  0  1  1  1  1  1]
#  [ 1  1  1  1  1  2  2  2  2  2]
#  [ 2  2  2  2  2  3  3  3  3  3]]
