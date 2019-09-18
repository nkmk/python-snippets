import numpy as np

a = np.array([-100, -10, 0, 10, 100])
print(a)
# [-100  -10    0   10  100]

print(np.signbit(a))
# [ True  True False False False]

print(type(np.signbit(a)))
# <class 'numpy.ndarray'>

print(np.signbit(a).dtype)
# bool

print(np.signbit(-100))
# True

print(a == 0)
# [False False  True False False]

print(a > 0)
# [False False False  True  True]

print(a >= 0)
# [False False  True  True  True]

print(a < 0)
# [ True  True False False False]

print(a <= 0)
# [ True  True  True False False]

print(np.count_nonzero(np.signbit(a)))
# 2

print(~np.signbit(a))
# [False False  True  True  True]

print(np.count_nonzero(~np.signbit(a)))
# 3

print(np.count_nonzero(a == 0))
# 1

print(np.count_nonzero(a < 0))
# 2

print(np.count_nonzero(a >= 0))
# 3

a_special = np.array([-np.inf, np.inf, np.nan])
print(a_special)
# [-inf  inf  nan]

print(np.signbit(a_special))
# [ True False False]

print(np.nan == 0)
# False

print(np.nan < 0)
# False

print(np.nan > 0)
# False

print(a_special < 0)
# [ True False False]
# 
# /usr/local/lib/python3.7/site-packages/ipykernel_launcher.py:1: RuntimeWarning: invalid value encountered in less
#   """Entry point for launching an IPython kernel.

print(a_special > 0)
# [False  True False]
# 
# /usr/local/lib/python3.7/site-packages/ipykernel_launcher.py:1: RuntimeWarning: invalid value encountered in greater
#   """Entry point for launching an IPython kernel.

a_complex = np.array([3 + 4j, -3 - 4j])
print(a_complex)
# [ 3.+4.j -3.-4.j]

# print(np.signbit(a_complex))
# TypeError: ufunc 'signbit' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''

print(np.abs(a_complex))
# [5. 5.]

print(a_complex.real)
# [ 3. -3.]

print(a_complex.imag)
# [ 4. -4.]

print(np.signbit(a_complex.real))
# [False  True]

print(a_complex.real < 0)
# [False  True]
