import numpy as np

print(np.sign(100))
# 1

print(np.sign(-100))
# -1

print(type(np.sign(100)))
# <class 'numpy.int64'>

print(np.sign(1.23))
# 1.0

print(np.sign(-1.23))
# -1.0

print(type(np.sign(1.23)))
# <class 'numpy.float64'>

print(np.sign(0))
# 0

print(np.sign(0.0))
# 0.0

print(np.sign(-0.0))
# 0.0

print(np.sign(float('nan')))
# nan

print(np.sign(float('-nan')))
# nan

print(100 > 0)
# True

print(True - False)
# 1

print(False - True)
# -1

print(False - False)
# 0

def my_sign(x):
    return (x > 0) - (x < 0)

print(my_sign(100))
# 1

print(my_sign(-100))
# -1

print(type(my_sign(100)))
# <class 'int'>

print(my_sign(1.23))
# 1

print(my_sign(-1.23))
# -1

print(type(my_sign(-1.23)))
# <class 'int'>

print(my_sign(0))
# 0

print(my_sign(0.0))
# 0

print(my_sign(-0.0))
# 0

print(my_sign(float('nan')))
# 0

print(my_sign(float('-nan')))
# 0

# print(my_sign(3 + 4j))
# TypeError: '>' not supported between instances of 'complex' and 'int'

def my_sign_with_abs(x):
    return 0.0 if abs(x) == 0 else x / abs(x)

print(my_sign_with_abs(100))
# 1.0

print(my_sign_with_abs(-100))
# -1.0

print(type(my_sign_with_abs(100)))
# <class 'float'>

print(my_sign_with_abs(1.23))
# 1.0

print(my_sign_with_abs(-1.23))
# -1.0

print(type(my_sign_with_abs(1.23)))
# <class 'float'>

print(my_sign_with_abs(0))
# 0.0

print(my_sign_with_abs(0.0))
# 0.0

print(my_sign_with_abs(-0.0))
# 0.0

print(my_sign_with_abs(float('nan')))
# nan

print(my_sign_with_abs(float('-nan')))
# nan

print(abs(3 + 4j))
# 5.0

print(my_sign_with_abs(3 + 4j))
# (0.6+0.8j)
