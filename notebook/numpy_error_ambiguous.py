import numpy as np

print(np.__version__)
# 1.17.3

a_bool = np.array([True, True, True])
b_bool = np.array([True, False, False])

# if a_bool:
#     pass
# ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

# a_bool and b_bool
# ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

# a_bool or b_bool
# ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

# not b_bool
# ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

print(bool([0, 1, 2]))
# True

print(bool([]))
# False

print(not [0, 1, 2])
# False

print(not [])
# True

# bool(a_bool)
# ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

print(a_bool.all())
# True

print(a_bool.any())
# True

print(b_bool.all())
# False

print(b_bool.any())
# True

a_bool_2d = np.array([[True, True, True], [True, False, False]])
print(a_bool_2d)
# [[ True  True  True]
#  [ True False False]]

print(a_bool_2d.all())
# False

print(a_bool_2d.all(axis=0))
# [ True False False]

print(a_bool_2d.all(axis=1))
# [ True False]

print(type(a_bool_2d.all(axis=0)))
# <class 'numpy.ndarray'>

print(a_bool.size)
# 3

print(a_bool.size == 0)
# False

print(a_bool & b_bool)
# [ True False False]

print(a_bool | b_bool)
# [ True  True  True]

print(~b_bool)
# [False  True  True]

print(a_bool ^ b_bool)
# [False  True  True]

a_int = np.array([0, 1, 3])  # [0b00 0b01 0b11]
b_int = np.array([1, 0, 2])  # [0b01 0b00 0b10]

print(a_int & b_int)
# [0 0 2]

print(a_int | b_int)
# [1 1 3]

print(a_int ^ b_int)
# [1 1 1]

print(~a_int)
# [-1 -2 -4]

a = np.arange(12).reshape(3, 4)
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a > 3)
# [[False False False False]
#  [ True  True  True  True]
#  [ True  True  True  True]]

print(a % 2 == 0)
# [[ True False  True False]
#  [ True False  True False]
#  [ True False  True False]]

# print(a > 3 & a % 2 == 0)
# ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

# print(a > (3 & (a % 2)) == 0)
# ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

print((a > 3) & (a % 2 == 0))
# [[False False False False]
#  [ True False  True False]
#  [ True False  True False]]

x = 10

print(x > 3)
# True

print(x % 2 == 1)
# False

print(x > 3 or x % 2 == 1)
# True

print((x > 3) or (x % 2 == 1))
# True

a_single = np.array([0])
b_single = np.array([1])
c_single = np.array([2])

print(bool(a_single))
# False

print(bool(b_single))
# True

print(bool(c_single))
# True

print(b_single and c_single)
# [2]

print(c_single and b_single)
# [1]

print(b_single or c_single)
# [1]

print(c_single or b_single)
# [2]

print(b_single & c_single)
# [0]

print(b_single | c_single)
# [3]

print(not a_single)
# True

print(not b_single)
# False

print(not c_single)
# False

print(~a_single)
# [-1]

print(~b_single)
# [-2]

print(~c_single)
# [-3]

a_empty = np.array([])
print(a_empty)
# []

print(bool(a_empty))
# False
# 
# /usr/local/lib/python3.7/site-packages/ipykernel_launcher.py:1: DeprecationWarning: The truth value of an empty array is ambiguous. Returning False, but in future this will result in an error. Use `array.size > 0` to check that an array is not empty.
#   """Entry point for launching an IPython kernel.
