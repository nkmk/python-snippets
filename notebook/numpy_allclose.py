import numpy as np

print(np.__version__)
# 1.26.1

a = np.array([0.3, 0.1 + 0.1 + 0.1])
b = np.array([0.3, 0.3])
c = np.array([0.1, 0.3])

print(np.allclose(a, b))
# True

print(np.allclose(a, c))
# False

a = np.array([99, 100, 101])

print(np.allclose(a, 100))
# False

print(np.allclose(a, 100, rtol=0, atol=1))
# True

a_nan = np.array([np.nan, 1, 2])
b_nan = np.array([np.nan, 1, 2])

print(np.allclose(a_nan, b_nan))
# False

print(np.allclose(a_nan, b_nan, equal_nan=True))
# True
