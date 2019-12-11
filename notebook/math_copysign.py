import math

print(math.copysign(123, -100))
# -123.0

print(math.copysign(123.0, -100.0))
# -123.0

def my_sign_with_copysign(x):
    return int(math.copysign(1, x))

print(my_sign_with_copysign(100))
# 1

print(my_sign_with_copysign(-100))
# -1

print(type(my_sign_with_copysign(100)))
# <class 'int'>

print(my_sign_with_copysign(1.23))
# 1

print(my_sign_with_copysign(-1.23))
# -1

print(type(my_sign_with_copysign(1.23)))
# <class 'int'>

print(my_sign_with_copysign(0))
# 1

print(my_sign_with_copysign(0.0))
# 1

print(my_sign_with_copysign(-0.0))
# -1

print(my_sign_with_copysign(float('nan')))
# 1

print(my_sign_with_copysign(float('-nan')))
# -1

# print(math.copysign(1, 3 + 4j))
# TypeError: can't convert complex to float

# print(my_sign_with_copysign(3 + 4j))
# TypeError: can't convert complex to float
