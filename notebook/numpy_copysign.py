import numpy as np

a = np.arange(12).reshape(3, 4)
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

b = np.arange(-5, 7).reshape(3, 4)
print(b)
# [[-5 -4 -3 -2]
#  [-1  0  1  2]
#  [ 3  4  5  6]]

a_copysign = np.copysign(a, b)
print(a_copysign)
# [[-0. -1. -2. -3.]
#  [-4.  5.  6.  7.]
#  [ 8.  9. 10. 11.]]

print(a_copysign.dtype)
# float64

print(np.copysign(10, -5))
# -10.0

print(type(np.copysign(10, -5)))
# <class 'numpy.float64'>

print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

b_small = np.array([-100, -100, 100, 100])
print(b_small)
# [-100 -100  100  100]

print(a + b_small)
# [[-100  -99  102  103]
#  [ -96  -95  106  107]
#  [ -92  -91  110  111]]

print(np.copysign(a, b_small))
# [[-0. -1.  2.  3.]
#  [-4. -5.  6.  7.]
#  [-8. -9. 10. 11.]]

b_mismatch = np.array([-100, -100, 100])
print(b_mismatch)
# [-100 -100  100]

# print(np.copysign(a, b_mismatch))
# ValueError: operands could not be broadcast together with shapes (3,4) (3,) 

print(np.copysign(b, -10))
# [[-5. -4. -3. -2.]
#  [-1. -0. -1. -2.]
#  [-3. -4. -5. -6.]]

print(np.abs(b) * -1)
# [[-5 -4 -3 -2]
#  [-1  0 -1 -2]
#  [-3 -4 -5 -6]]

print(np.abs(b) * -1.0)
# [[-5. -4. -3. -2.]
#  [-1. -0. -1. -2.]
#  [-3. -4. -5. -6.]]

zero_pos = np.copysign(0, 1)
print(zero_pos)
# 0.0

zero_nega = np.copysign(0, -1)
print(zero_nega)
# -0.0

print(zero_pos == zero_nega == 0)
# True

print(np.sign([zero_pos, zero_nega]))
# [0. 0.]

print(1 / zero_pos)
# inf
# 
# /usr/local/lib/python3.7/site-packages/ipykernel_launcher.py:1: RuntimeWarning: divide by zero encountered in double_scalars
#   """Entry point for launching an IPython kernel.

print(1 / zero_nega)
# -inf
# 
# /usr/local/lib/python3.7/site-packages/ipykernel_launcher.py:1: RuntimeWarning: divide by zero encountered in double_scalars
#   """Entry point for launching an IPython kernel.

a_special = np.array([-np.inf, np.inf, np.nan])
print(a_special)
# [-inf  inf  nan]

print(np.copysign(a_special, 1))
# [inf inf nan]

print(np.copysign(a_special, -1))
# [-inf -inf  nan]

print(np.copysign([10, 10, 10], a_special))
# [-10.  10.  10.]

print(np.copysign([-10, -10, -10], a_special))
# [-10.  10.  10.]

a_complex = np.array([10 + 10j, -10 + 10j])
print(a_complex)
# [ 10.+10.j -10.+10.j]

# print(np.copysign(a_complex, 1))
# TypeError: ufunc 'copysign' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''

# print(np.copysign([1, 1], a_complex))
# TypeError: ufunc 'copysign' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''
