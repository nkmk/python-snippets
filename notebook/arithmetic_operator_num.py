print(10 + 3)
# 13

print(10 - 3)
# 7

print(10 * 3)
# 30

print(10 / 3)
# 3.3333333333333335

print(10 // 3)
# 3

print(10 % 3)
# 1

print(10 ** 3)
# 1000

print(2 ** 0.5)
# 1.4142135623730951

print(10 ** -2)
# 0.01

print(0 ** 0)
# 1

# print(10 / 0)
# ZeroDivisionError: integer division or modulo by zero

# print(10 // 0)
# ZeroDivisionError: integer division or modulo by zero

# print(10 % 0)
# ZeroDivisionError: integer division or modulo by zero

# print(0 ** -1)
# ZeroDivisionError: 0.0 cannot be raised to a negative power

a = 10
b = 3
c = a + b

print('a:', a)
print('b:', b)
print('c:', c)
# a: 10
# b: 3
# c: 13

a = 10
b = 3
a += b

print('a:', a)
print('b:', b)
# a: 13
# b: 3

a = 10
b = 3
a %= b

print('a:', a)
print('b:', b)
# a: 1
# b: 3

a = 10
b = 3
a **= b

print('a:', a)
print('b:', b)
# a: 1000
# b: 3

print(2 + 3.0)
print(type(2 + 3.0))
# 5.0
# <class 'float'>

print(10 / 2)
print(type(10 / 2))
# 5.0
# <class 'float'>

print(2 ** 3)
print(type(2 ** 3))
# 8
# <class 'int'>

print(2.0 ** 3)
print(type(2.0 ** 3))
# 8.0
# <class 'float'>

print(25 ** 0.5)
print(type(25 ** 0.5))
# 5.0
# <class 'float'>

print(0.01 ** -2)
print(type(0.01 ** -2))
# 10000.0
# <class 'float'>

print(100 / 10 ** 2 + 2 * 3 - 5)
# 2.0

print(100 / (10 ** 2) + (2 * 3) - 5)
# 2.0

print((100 / 10) ** 2 + 2 * (3 - 5))
# 96.0
