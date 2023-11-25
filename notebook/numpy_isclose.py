import numpy as np

print(np.__version__)
# 1.26.1

print(0.1 + 0.1 + 0.1)
# 0.30000000000000004

a = np.array([0.3, 0.1 + 0.1 + 0.1])
print(a)
# [0.3 0.3]

b = np.array([0.3, 0.3])
print(b)
# [0.3 0.3]

print(a == b)
# [ True False]

np.set_printoptions(precision=18)

print(a)
# [0.3                 0.30000000000000004]

print(np.isclose(a, b))
# [ True  True]

print(np.isclose(a, 0.3))
# [ True  True]

print(np.isclose(0.1 + 0.1 + 0.1, 0.3))
# True

print(np.isclose(100, 101))
# False

print(np.isclose(100, 101, rtol=0, atol=1))
# True

print(np.isclose(np.nan, np.nan))
# False

print(np.isclose(np.nan, np.nan, equal_nan=True))
# True

a_nan = np.array([np.nan, 1, 2])
b_nan = np.array([np.nan, 1, np.nan])

print(np.isclose(a_nan, b_nan))
# [False  True False]

print(np.isclose(a_nan, b_nan, equal_nan=True))
# [ True  True False]
