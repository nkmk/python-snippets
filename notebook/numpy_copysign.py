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

a_special = np.array([0.0, -0.0, np.inf, -np.inf, np.nan])
print(a_special)
# [  0.  -0.  inf -inf  nan]

print(np.copysign(a_special, 1))
# [ 0.  0. inf inf nan]

print(np.copysign(a_special, -1))
# [ -0.  -0. -inf -inf  nan]

print(np.copysign([10, 10, 10, 10, 10], a_special))
# [ 10. -10.  10. -10.  10.]

print(np.copysign([-10, -10, -10, -10, -10], a_special))
# [ 10. -10.  10. -10.  10.]

print(np.copysign(10, 0))
# 10.0

print(np.copysign(0, 10))
# 0.0

print(np.copysign(0, -10))
# -0.0

a_complex = np.array([10 + 10j, -10 + 10j])
print(a_complex)
# [ 10.+10.j -10.+10.j]

# print(np.copysign(a_complex, 1))
# TypeError: ufunc 'copysign' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''

# print(np.copysign([1, 1], a_complex))
# TypeError: ufunc 'copysign' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''
