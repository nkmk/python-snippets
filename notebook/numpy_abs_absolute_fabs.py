import numpy as np

print(np.__version__)
# 1.26.2

print(np.abs)
# <ufunc 'absolute'>

print(np.abs is np.absolute)
# True

a = np.array([-2, -1, 0, 1, 2])

print(np.abs(a))
# [2 1 0 1 2]

print(type(np.abs(a)))
# <class 'numpy.ndarray'>

l = [-2, -1, 0, 1, 2]

print(np.abs(l))
# [2 1 0 1 2]

print(type(np.abs(l)))
# <class 'numpy.ndarray'>

print(np.abs(-100))
# 100

print(type(np.abs(-100)))
# <class 'numpy.int64'>

a_int = np.array([-2, -1, 0, 1, 2])

print(a_int.dtype)
# int64

print(np.abs(a_int))
# [2 1 0 1 2]

print(np.abs(a_int).dtype)
# int64

a_float = np.array([-2.0, -1.0, 0, 1.0, 2.0])

print(a_float.dtype)
# float64

print(np.abs(a_float))
# [2. 1. 0. 1. 2.]

print(np.abs(a_float).dtype)
# float64

a_complex = np.array([3 + 4j, 5 + 12j])

print(a_complex.dtype)
# complex128

print(np.abs(a_complex))
# [ 5. 13.]

print(np.abs(a_complex).dtype)
# float64

a = np.array([-2, -1, 0, 1, 2])

print(a.__abs__())
# [2 1 0 1 2]

print(abs(a))
# [2 1 0 1 2]

print(type(abs(a)))
# <class 'numpy.ndarray'>

a_complex = np.array([3 + 4j, 5 + 12j])

print(abs(a_complex))
# [ 5. 13.]

a_int = np.array([-2, -1, 0, 1, 2])

print(a_int.dtype)
# int64

print(np.fabs(a_int))
# [2. 1. 0. 1. 2.]

print(np.fabs(a_int).dtype)
# float64

a_complex = np.array([3 + 4j, 5 + 12j])

# print(np.fabs(a_complex))
# TypeError: ufunc 'fabs' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''
