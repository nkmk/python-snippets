import math

print(math.ceil(10.123))
# 11

print(math.ceil(10.987))
# 11

print(type(math.ceil(10.123)))
# <class 'int'>

print(math.ceil(10))
# 10

# print(math.ceil('10'))
# TypeError: must be real number, not str

print(hasattr(10, '__ceil__'))
# True

print(hasattr('10', '__ceil__'))
# False

print(math.ceil(-10.123))
# -10

print(math.ceil(-10.987))
# -10
