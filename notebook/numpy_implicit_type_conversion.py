import numpy as np

print(np.__version__)
# 1.26.1

a_int = np.array([1, 2, 3])
a_float = np.array([1.0, 2.0, 3.0])

print((a_int / a_int).dtype)
# float64

print((a_int / a_float).dtype)
# float64

print((a_int + a_int).dtype)
# int64

print((a_int + a_float).dtype)
# float64

print((a_int - a_int).dtype)
# int64

print((a_int - a_float).dtype)
# float64

print((a_int * a_int).dtype)
# int64

print((a_int * a_float).dtype)
# float64

print((a_int // a_int).dtype)
# int64

print((a_int // a_float).dtype)
# float64

print((a_int**a_int).dtype)
# int64

print((a_int**a_float).dtype)
# float64

a_int16 = np.array([1, 2, 3], np.int16)
a_int32 = np.array([1, 2, 3], np.int32)

print((a_int16 + a_int32).dtype)
# int32

a_float16 = np.array([1, 2, 3], np.float16)
a_float32 = np.array([1, 2, 3], np.float32)

print((a_float16 + a_float32).dtype)
# float32

print((a_int16 + a_float16).dtype)
# float32

print((a_int32 + a_float32).dtype)
# float64

a_int16[0] = 1.9
print(a_int16)
# [1 2 3]

print(a_int16.dtype)
# int16
