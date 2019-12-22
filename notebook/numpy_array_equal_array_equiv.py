import numpy as np

a = np.arange(3)
print(a)
# [0 1 2]

b = np.arange(3)
print(b)
# [0 1 2]

c = np.arange(1, 4)
print(c)
# [1 2 3]

print(np.all(a == b))
# True

print(np.all(a == c))
# False

print(np.array_equal(a, b))
# True

print(np.array_equal(a, c))
# False

print(np.array_equiv(a, b))
# True

print(np.array_equiv(a, c))
# False

b_f = np.arange(3, dtype=float)
print(b_f)
# [0. 1. 2.]

print(np.array_equal(a, b_f))
# True

print(np.array_equiv(a, b_f))
# True

ones = np.ones(3)
print(ones)
# [1. 1. 1.]

print(np.array_equal(ones, 1))
# False

print(np.array_equiv(ones, 1))
# True

a_2d = np.array([[0, 1, 2], [0, 1, 2], [0, 1, 2]])
print(a_2d)
# [[0 1 2]
#  [0 1 2]
#  [0 1 2]]

print(np.array_equal(a_2d, b))
# False

print(np.array_equiv(a_2d, b))
# True

a_nan = np.array([np.nan, 1, 2])
print(a_nan)
# [nan  1.  2.]

b_nan = np.array([np.nan, 1, 2])
print(b_nan)
# [nan  1.  2.]

print(np.array_equal(a_nan, b_nan))
# False

print(np.array_equiv(a_nan, b_nan))
# False

print(np.all(a_nan == b_nan))
# False
