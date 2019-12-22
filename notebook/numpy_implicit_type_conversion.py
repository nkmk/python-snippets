import numpy as np

a = np.array([1, 2, 3])
print(a)
print(a.dtype)
# [1 2 3]
# int64

print((a / 1).dtype)
# float64

print((a / 1.0).dtype)
# float64

print((a + 1).dtype)
# int64

print((a + 1.0).dtype)
# float64

print((a - 1).dtype)
# int64

print((a - 1.0).dtype)
# float64

print((a * 1).dtype)
# int64

print((a * 1.0).dtype)
# float64

print((a // 1).dtype)
# int64

print((a // 1.0).dtype)
# float64

print((a ** 1).dtype)
# int64

print((a ** 1.0).dtype)
# float64

ones_int16 = np.ones(3, np.int16)
print(ones_int16)
# [1 1 1]

ones_int32 = np.ones(3, np.int32)
print(ones_int32)
# [1 1 1]

print((ones_int16 + ones_int32).dtype)
# int32

ones_float16 = np.ones(3, np.float16)
print(ones_float16)
# [1. 1. 1.]

print((ones_int16 + ones_float16).dtype)
# float32

ones_int16[0] = 10.9
print(ones_int16)
# [10  1  1]

print(ones_int16.dtype)
# int16
