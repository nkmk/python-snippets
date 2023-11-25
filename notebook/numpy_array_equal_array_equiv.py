import numpy as np

print(np.__version__)
# 1.26.1

a = np.array([0, 1, 2])
b = np.array([0, 1, 2])
c = np.array([3, 4, 5])

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

b_float = b.astype(float)

print(np.array_equal(a, b_float))
# True

print(np.array_equiv(a, b_float))
# True

ones = np.array([1, 1, 1])

print(np.array_equal(ones, 1))
# False

print(np.array_equiv(ones, 1))
# True

a_1d = np.array([0, 1, 2])
a_2d = np.array([[0, 1, 2], [0, 1, 2], [0, 1, 2]])

print(np.array_equal(a_1d, a_2d))
# False

print(np.array_equiv(a_1d, a_2d))
# True

a_nan = np.array([np.nan, 1, 2])
b_nan = np.array([np.nan, 1, 2])

print(np.array_equal(a_nan, b_nan))
# False

print(np.array_equiv(a_nan, b_nan))
# False

print(np.all(a_nan == b_nan))
# False

print(np.array_equal(a_nan, b_nan, True))
# True
