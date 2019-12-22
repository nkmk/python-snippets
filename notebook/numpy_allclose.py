import numpy as np

a = np.array([0.3, 0.1 + 0.1 + 0.1])
print(a)
# [0.3 0.3]

b = np.array([0.3, 0.3])
print(b)
# [0.3 0.3]

c = np.array([0.2, 0.3])
print(c)
# [0.2 0.3]

print(np.allclose(a, b))
# True

print(np.allclose(a, c))
# False

a_100 = np.array([99, 100, 101])
print(a_100)
# [ 99 100 101]

print(np.allclose(a_100, 100))
# False

print(np.allclose(a_100, 100, rtol=0, atol=1))
# True

a_nan = np.array([np.nan, 1, 2])
print(a_nan)
# [nan  1.  2.]

b_nan = np.array([np.nan, 1, 2])
print(b_nan)
# [nan  1.  2.]

print(np.allclose(a_nan, b_nan))
# False

print(np.allclose(a_nan, b_nan, equal_nan=True))
# True
