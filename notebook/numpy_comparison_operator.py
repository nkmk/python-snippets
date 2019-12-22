import numpy as np

a = np.arange(12).reshape(3, 4)
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

b = np.arange(12).reshape(4, 3).T
print(b)
# [[ 0  3  6  9]
#  [ 1  4  7 10]
#  [ 2  5  8 11]]

a_compare = a < b
print(a_compare)
# [[False  True  True  True]
#  [False False  True  True]
#  [False False False False]]

print(type(a_compare))
# <class 'numpy.ndarray'>

print(a_compare.dtype)
# bool

print(a > b)
# [[False False False False]
#  [ True  True False False]
#  [ True  True  True False]]

print(a <= b)
# [[ True  True  True  True]
#  [False False  True  True]
#  [False False False  True]]

print(a >= b)
# [[ True False False False]
#  [ True  True False False]
#  [ True  True  True  True]]

print(a == b)
# [[ True False False False]
#  [False False False False]
#  [False False False  True]]

print(a != b)
# [[False  True  True  True]
#  [ True  True  True  True]
#  [ True  True  True False]]

b_float = b.astype(float)
print(b_float)
# [[ 0.  3.  6.  9.]
#  [ 1.  4.  7. 10.]
#  [ 2.  5.  8. 11.]]

print(b_float.dtype)
# float64

print(a == b_float)
# [[ True False False False]
#  [False False False False]
#  [False False False  True]]

b_1d = np.arange(4, 8)
print(b_1d)
# [4 5 6 7]

print(a < b_1d)
# [[ True  True  True  True]
#  [False False False False]
#  [False False False False]]

print(a < 6)
# [[ True  True  True  True]
#  [ True  True False False]
#  [False False False False]]

print(a % 2)
# [[0 1 0 1]
#  [0 1 0 1]
#  [0 1 0 1]]

print(a % 2 == 0)
# [[ True False  True False]
#  [ True False  True False]
#  [ True False  True False]]

print(np.count_nonzero(a < 6))
# 6

print(np.all(a < 6))
# False

print(np.all(a < 6, axis=1))
# [ True False False]

print(np.any(a < 6))
# True

print(np.any(a < 6, axis=1))
# [ True  True False]

a_nan = np.array([0, 1, np.nan])
print(a_nan)
# [ 0.  1. nan]

print(a_nan == np.nan)
# [False False False]

print(np.isnan(a_nan))
# [False False  True]

print(a_nan > 0)
# [False  True False]
# 
# /usr/local/lib/python3.7/site-packages/ipykernel_launcher.py:1: RuntimeWarning: invalid value encountered in greater
#   """Entry point for launching an IPython kernel.

a_nan_only = np.array([np.nan])
print(a_nan_only)
# [nan]

print(a_nan_only > 0)
# [False]

print(np.nan > 0)
# False

x = 6

print(4 < x < 8)
# True

# print(4 < a < 8)
# ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

print((a > 4) & (a < 8))
# [[False False False False]
#  [False  True  True  True]
#  [False False False False]]

# print((a > 4) and (a < 8))
# ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

# print(a > 4 & a < 8)
# ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

x = 6
y = 6
z = 6

print(x == y == z)
# True

c = np.zeros((3, 4), int)
print(c)
# [[0 0 0 0]
#  [0 0 0 0]
#  [0 0 0 0]]

# print(a == b == c)
# ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

print((a == b) & (b == c))
# [[ True False False False]
#  [False False False False]
#  [False False False False]]
