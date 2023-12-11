import math

print(math.fabs(-100))
# 100.0

print(type(math.fabs(-100)))
# <class 'float'>

print(math.fabs(-1.23))
# 1.23

print(type(math.fabs(-1.23)))
# <class 'float'>

# print(math.fabs(3 + 4j))
# TypeError: must be real number, not complex

class MyClass:
    def __abs__(self):
        return 100

mc = MyClass()

# math.fabs(mc)
# TypeError: must be real number, not MyClass
