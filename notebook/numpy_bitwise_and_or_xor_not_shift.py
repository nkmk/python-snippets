import numpy as np

print(np.__version__)
# 1.17.3

a_int = np.array([0, 1, 3])  # [0b00 0b01 0b11]
b_int = np.array([1, 0, 2])  # [0b01 0b00 0b10]

print(a_int.dtype)
# int64

print(b_int.dtype)
# int64

print(a_int & b_int)
# [0 0 2]

print(a_int | b_int)
# [1 1 3]

print(a_int ^ b_int)
# [1 1 1]

print(~a_int)
# [-1 -2 -4]

print(a_int << b_int)
# [ 0  1 12]

print(a_int >> b_int)
# [0 1 0]

print(np.bitwise_and(a_int, b_int))
# [0 0 2]

print(np.bitwise_or(a_int, b_int))
# [1 1 3]

print(np.bitwise_xor(a_int, b_int))
# [1 1 1]

print(np.bitwise_not(a_int))
# [-1 -2 -4]

print(np.invert(a_int))
# [-1 -2 -4]

print(~a_int)
# [-1 -2 -4]

print(-(a_int + 1))
# [-1 -2 -4]

a_uint8 = np.array([0, 1, 3], dtype=np.uint8)

print(~a_uint8)
# [255 254 252]

a_uint16 = np.array([0, 1, 3], dtype=np.uint16)

print(~a_uint16)
# [65535 65534 65532]

c_int_2d = np.arange(6).reshape(2, 3)
print(c_int_2d)
# [[0 1 2]
#  [3 4 5]]

print(c_int_2d & a_int)
# [[0 1 2]
#  [0 0 1]]

print(np.bitwise_and(c_int_2d, a_int))
# [[0 1 2]
#  [0 0 1]]

print(c_int_2d & 2)
# [[0 0 2]
#  [2 0 0]]

print(np.bitwise_and(c_int_2d, 2))
# [[0 0 2]
#  [2 0 0]]

d_float = np.array([0, 1, 3], dtype=float)

# print(a_int & d_float)
# TypeError: ufunc 'bitwise_and' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''

# print(~d_float)
# TypeError: ufunc 'invert' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''

# print(np.bitwise_and(a_int, d_float))
# TypeError: ufunc 'bitwise_and' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''

# print(np.bitwise_not(d_float))
# TypeError: ufunc 'invert' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''

e_bool = np.array([True, False, True])

print(a_int & e_bool)
# [0 0 1]

print((a_int & e_bool).dtype)
# int64

print(np.bitwise_and(a_int, e_bool))
# [0 0 1]

print(np.bitwise_and(a_int, e_bool).dtype)
# int64

print(~e_bool)
# [False  True False]

print(np.logical_not(e_bool))
# [False  True False]

print(np.bitwise_not(e_bool))
# [False  True False]

print(np.invert(e_bool))
# [False  True False]
