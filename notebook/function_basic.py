def hello():
    print('Hello')

hello()
# Hello

def add(a, b):
    return a + b

x = add(3, 4)
print(x)
# 7

def print_add(a, b, c):
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)
    print('a + b + c = ', a + b + c)

print_add(1, 10, 100)
# a =  1
# b =  10
# c =  100
# a + b + c =  111

# print_add(1)
# TypeError: print_add() missing 2 required positional arguments: 'b' and 'c'

# print_add(1, 10, 100, 1000)
# TypeError: print_add() takes 3 positional arguments but 4 were given

print_add(b=10, c=100, a=1)
# a =  1
# b =  10
# c =  100
# a + b + c =  111

print_add(1, c=100, b=10)
# a =  1
# b =  10
# c =  100
# a + b + c =  111

# print_add(a=1, 10, 100)
# SyntaxError: positional argument follows keyword argument

def print_add_default(a, b, c=100):
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)
    print('a + b + c = ', a + b + c)

print_add_default(1, 10)
# a =  1
# b =  10
# c =  100
# a + b + c =  111

print_add_default(1, 10, 200)
# a =  1
# b =  10
# c =  200
# a + b + c =  211

# def print_add_default(a=1, b, c=100):
#     ...
# SyntaxError: non-default argument follows default argument

def func_args(*args):
    print(args)

func_args(1, 10)
# (1, 10)

func_args(1, 10, 100, 1000)
# (1, 10, 100, 1000)

def func_kwargs(**kwargs):
    print(kwargs)

func_kwargs(a=1, b=10)
# {'a': 1, 'b': 10}

func_kwargs(c=1, b=10, d=1000, a=100)
# {'c': 1, 'b': 10, 'd': 1000, 'a': 100}

def print_add(a, b, c):
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)
    print('a + b + c = ', a + b + c)

l = [1, 10, 100]

print_add(*l)
# a =  1
# b =  10
# c =  100
# a + b + c =  111

l = [1, 10]

# print_add(*l)
# TypeError: print_add() missing 1 required positional argument: 'c'

d = {'a': 1, 'b': 10, 'c': 100}

print_add(**d)
# a =  1
# b =  10
# c =  100
# a + b + c =  111

d = {'a': 1, 'b': 10, 'x': 100}

# print_add(**d)
# TypeError: print_add() got an unexpected keyword argument 'x'

def func_return(a, b):
    return a + b

x = func_return(3, 4)

print(x)
print(type(x))
# 7
# <class 'int'>

x = func_return(0.3, 0.4)

print(x)
print(type(x))
# 0.7
# <class 'float'>

def func_return_multi(a, b):
    return a + b, a * b, a / b

x = func_return_multi(3, 4)

print(x)
print(type(x))
# (7, 12, 0.75)
# <class 'tuple'>

x, y, z = func_return_multi(3, 4)

print(x)
print(y)
print(z)
# 7
# 12
# 0.75

def func_return_multi_list(a, b):
    return [a + b, a * b, a / b]

x = func_return_multi_list(3, 4)

print(x)
print(type(x))
# [7, 12, 0.75]
# <class 'list'>

x, y, z = func_return_multi_list(3, 4)

print(x)
print(y)
print(z)
# 7
# 12
# 0.75
