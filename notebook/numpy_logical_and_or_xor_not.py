import numpy as np

print(np.__version__)
# 1.17.3

a_bool = np.array([True, True, False, False])
b_bool = np.array([True, False, True, False])

print(a_bool.dtype)
# bool

print(b_bool.dtype)
# bool

print(a_bool & b_bool)
# [ True False False False]

print(a_bool | b_bool)
# [ True  True  True False]

print(a_bool ^ b_bool)
# [False  True  True False]

print(~a_bool)
# [False False  True  True]

print(type(a_bool & b_bool))
# <class 'numpy.ndarray'>

print((a_bool & b_bool).dtype)
# bool

# print(a_bool and b_bool)
# ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

print(np.logical_and(a_bool, b_bool))
# [ True False False False]

print(np.logical_or(a_bool, b_bool))
# [ True  True  True False]

print(np.logical_xor(a_bool, b_bool))
# [False  True  True False]

print(np.logical_not(a_bool))
# [False False  True  True]

c_int = np.arange(4)
print(c_int)
# [0 1 2 3]

print(np.logical_not(c_int))
# [ True False False False]

d_int = c_int + 4
print(d_int)
# [4 5 6 7]

print(np.logical_not(d_int))
# [False False False False]

print(np.logical_and(c_int, d_int))
# [False  True  True  True]

print(c_int & d_int)
# [0 1 2 3]

a_bool_2d = np.array([[True, True, False, False], [False, False, True, True]])
print(a_bool_2d)
# [[ True  True False False]
#  [False False  True  True]]

print(a_bool_2d & b_bool)
# [[ True False False False]
#  [False False  True False]]

print(np.logical_and(a_bool_2d, a_bool))
# [[ True  True False False]
#  [False False False False]]

print(a_bool & True)
# [ True  True False False]

print(np.logical_and(a_bool, True))
# [ True  True False False]

print(c_int)
# [0 1 2 3]

print(c_int < 2)
# [ True  True False False]

print(c_int % 2 == 0)
# [ True False  True False]

print((c_int < 2) & (c_int % 2 == 0))
# [ True False False False]

# print(c_int < 2 & c_int % 2 == 0)
# ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

# print(c_int < (2 & (c_int % 2)) == 0)
# ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

print(np.logical_and(c_int < 2, c_int % 2 == 0))
# [ True False False False]
