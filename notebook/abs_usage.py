print(abs(100))
# 100

print(abs(-100))
# 100

print(type(abs(100)))
# <class 'int'>

print(abs(1.23))
# 1.23

print(abs(-1.23))
# 1.23

print(type(abs(1.23)))
# <class 'float'>

print(abs(1 + 1j))
# 1.4142135623730951

print(abs(3 + 4j))
# 5.0

print(type(abs(3 + 4j)))
# <class 'float'>

print((-100).__abs__())
# 100

print((-1.23).__abs__())
# 1.23

print((3 + 4j).__abs__())
# 5.0

l = [-2, -1, 0, 1, 2]

print(hasattr(l, '__abs__'))
# False

# print(abs(l))
# TypeError: bad operand type for abs(): 'list'

class MyClass:
    def __abs__(self):
        return 100

mc = MyClass()

print(abs(mc))
# 100

print([abs(i) for i in l])
# [2, 1, 0, 1, 2]
