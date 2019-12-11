import math

print(math.floor(10.123))
# 10

print(math.floor(10.987))
# 10

print(type(math.floor(10.123)))
# <class 'int'>

print(math.floor(10))
# 10

# print(math.floor('10'))
# TypeError: must be real number, not str

print(hasattr(10, '__floor__'))
# True

print(hasattr('10', '__floor__'))
# False

print(math.floor(-10.123))
# -11

print(math.floor(-10.987))
# -11
