import numpy as np

print(np.__version__)
# 1.26.1

print(np.empty(3))
# [4.65836473e-310 0.00000000e+000 2.37151510e-322]

print(np.empty((2, 3)))
# [[1.13754784e-313 0.00000000e+000 1.39067149e-309]
#  [4.65939618e-310 5.56268846e-309 4.65939619e-310]]

print(np.empty(3).dtype)
# float64

print(np.empty(3, dtype=np.int64))
# [94286351876007              0             48]

print(np.empty(3, dtype=np.int64).dtype)
# int64

a_int64 = np.arange(3)
print(a_int64)
# [0 1 2]

print(a_int64.dtype)
# int64

print(np.empty_like(a_int64))
# [94286351876007              0             48]

print(np.empty_like(a_int64).dtype)
# int64

a_float64 = np.arange(6).reshape(2, 3) / 10
print(a_float64)
# [[0.  0.1 0.2]
#  [0.3 0.4 0.5]]

print(a_float64.dtype)
# float64

print(np.empty_like(a_float64))
# [[1.13754784e-313 0.00000000e+000 1.39067149e-309]
#  [4.65939618e-310 5.56268846e-309 4.65939619e-310]]

print(np.empty_like(a_float64).dtype)
# float64

print(np.empty_like(a_float64, dtype=np.int64))
# [[     23024224555                0  281475043902528]
#  [  94307228646232 1125900678677248   94307228749368]]

print(np.empty_like(a_float64, dtype=np.int64).dtype)
# int64

print(np.empty(0))
# []

print(type(np.empty(0)))
# <class 'numpy.ndarray'>

print(np.empty(0).size)
# 0

print(np.zeros(0))
# []

print(np.ones(0))
# []

print(np.array([]))
# []
