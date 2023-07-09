# print('hello'
# SyntaxError: incomplete input

print('hello')
# hello

# for i in range(3)
#     print(i)
# SyntaxError: expected ':'

for i in range(3):
    print(i)
# 0
# 1
# 2

n = 100

# if n == 100:
#     print('n is 100')
#   else:
#     print('n is not 100')
# IndentationError: unindent does not match any outer indentation level

n = 100

if n == 100:
    print('n is 100')
else:
    print('n is not 100')
# n is 100

# import mathematics
# ModuleNotFoundError: No module named 'mathematics'

import math

# import math.pi
# ModuleNotFoundError: No module named 'math.pi'; 'math' is not a package

from math import pi

# from math import COS
# ImportError: cannot import name 'COS' from 'math' (/opt/homebrew/Cellar/python@3.11/3.11.4_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/lib-dynload/math.cpython-311-darwin.so)

from math import cos

import math

# print(math.PI)
# AttributeError: module 'math' has no attribute 'PI'

print(math.pi)
# 3.141592653589793

l = 100
# l.append(200)
# AttributeError: 'int' object has no attribute 'append'

l = [100]
l.append(200)
print(l)
# [100, 200]

n = '100'
# print(n + 200)
# TypeError: can only concatenate str (not "int") to str

n = 100
print(100 + 200)
# 300

# print(float(['1.23E-3']))
# TypeError: float() argument must be a string or a number, not 'list'

print(float('1.23E-3'))
# 0.00123

# print(float('float number'))
# ValueError: could not convert string to float: 'float number'

print(float('1.23E-3'))
# 0.00123

n = 100
zero = 0

# print(n / zero)
# ZeroDivisionError: division by zero

# print(n // zero)
# ZeroDivisionError: integer division or modulo by zero

# print(n % zero)
# ZeroDivisionError: integer modulo by zero

my_number = 100
# print(myNumber)
# NameError: name 'myNumber' is not defined

print(my_number)
# 100

l = [0, 1, 2]
# print(l[100])
# IndexError: list index out of range

print(len(l))
# 3

print(l[1])
# 1

d = {'a': 1, 'b': 2, 'c': 3}
# print(d['x'])
# KeyError: 'x'

print(d['a'])
# 1

print(d)
# {'a': 1, 'b': 2, 'c': 3}

print(d.keys())
# dict_keys(['a', 'b', 'c'])

print(d.get('x'))
# None

# with open('not_exist_file.txt') as f:
#     print(f.read())
# FileNotFoundError: [Errno 2] No such file or directory: 'not_exist_file.txt'

import os

# os.mkdir('data')
# FileExistsError: [Errno 17] File exists: 'data'
