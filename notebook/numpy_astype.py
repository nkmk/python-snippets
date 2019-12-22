import numpy as np

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

a_float = a.astype(float)
print(a_float)
print(a_float.dtype)
# [1. 2. 3.]
# float64

a_str = a.astype('str')
print(a_str)
print(a_str.dtype)
# ['1' '2' '3']
# <U21

a_int = a.astype('int32')
print(a_int)
print(a_int.dtype)
# [1 2 3]
# int32

a = np.arange(50).reshape((5, 10)) / 10 - 2
print(a)
print(a.dtype)
# [[-2.  -1.9 -1.8 -1.7 -1.6 -1.5 -1.4 -1.3 -1.2 -1.1]
#  [-1.  -0.9 -0.8 -0.7 -0.6 -0.5 -0.4 -0.3 -0.2 -0.1]
#  [ 0.   0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9]
#  [ 1.   1.1  1.2  1.3  1.4  1.5  1.6  1.7  1.8  1.9]
#  [ 2.   2.1  2.2  2.3  2.4  2.5  2.6  2.7  2.8  2.9]]
# float64

a_int = a.astype('int64')
print(a_int)
print(a_int.dtype)
# [[-2 -1 -1 -1 -1 -1 -1 -1 -1 -1]
#  [-1  0  0  0  0  0  0  0  0  0]
#  [ 0  0  0  0  0  0  0  0  0  0]
#  [ 1  1  1  1  1  1  1  1  1  1]
#  [ 2  2  2  2  2  2  2  2  2  2]]
# int64

print(np.round(a).astype(int))
# [[-2 -2 -2 -2 -2 -2 -1 -1 -1 -1]
#  [-1 -1 -1 -1 -1  0  0  0  0  0]
#  [ 0  0  0  0  0  0  1  1  1  1]
#  [ 1  1  1  1  1  2  2  2  2  2]
#  [ 2  2  2  2  2  2  3  3  3  3]]

my_round_int = lambda x: np.round((x * 2 + 1) // 2)

print(my_round_int(a).astype(int))
# [[-2 -2 -2 -2 -2 -1 -1 -1 -1 -1]
#  [-1 -1 -1 -1 -1  0  0  0  0  0]
#  [ 0  0  0  0  0  1  1  1  1  1]
#  [ 1  1  1  1  1  2  2  2  2  2]
#  [ 2  2  2  2  2  3  3  3  3  3]]

def my_round(x, digit=0):
    p = 10 ** digit
    s = np.copysign(1, x)
    return (s * x * p * 2 + 1) // 2 / p * s

print(my_round(a).astype(int))
# [[-2 -2 -2 -2 -2 -2 -1 -1 -1 -1]
#  [-1 -1 -1 -1 -1 -1  0  0  0  0]
#  [ 0  0  0  0  0  1  1  1  1  1]
#  [ 1  1  1  1  1  2  2  2  2  2]
#  [ 2  2  2  2  2  3  3  3  3  3]]
