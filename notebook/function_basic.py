def hello():
    print('Hello')

hello()
# Hello

def add(a, b):
    x = a + b
    return x

x = add(3, 4)
print(x)
# 7

def func(a, b, c):
    print(f'a={a}, b={b}, c={c}')

func(1, 10, 100)
# a=1, b=10, c=100

# func(1)
# TypeError: func() missing 2 required positional arguments: 'b' and 'c'

# func(1, 10, 100, 1000)
# TypeError: func() takes 3 positional arguments but 4 were given

func(b=10, c=100, a=1)
# a=1, b=10, c=100

func(1, c=100, b=10)
# a=1, b=10, c=100

# func(a=1, 10, 100)
# SyntaxError: positional argument follows keyword argument

def func_pos_only(a, b, /, c):
    print(f'a={a}, b={b}, c={c}')

# func_pos_only(a=1, b=10, c=100)
# TypeError: func_pos_only() got some positional-only arguments passed as keyword arguments: 'a, b'

func_pos_only(1, 10, 100)
# a=1, b=10, c=100

func_pos_only(1, 10, c=100)
# a=1, b=10, c=100

def func_kw_only(a, b, *, c):
    print(f'a={a}, b={b}, c={c}')

# func_kw_only(1, 10, 100)
# TypeError: func_kw_only() takes 2 positional arguments but 3 were given

func_kw_only(1, 10, c=100)
# a=1, b=10, c=100

func_kw_only(1, c=100, b=10)
# a=1, b=10, c=100

def func_pos_kw_only(a, /, b, *, c):
    print(f'a={a}, b={b}, c={c}')

# func_pos_kw_only(1, 10, 100)
# TypeError: func_pos_kw_only() takes 2 positional arguments but 3 were given

# func_pos_kw_only(a=1, b=10, c=100)
# TypeError: func_pos_kw_only() got some positional-only arguments passed as keyword arguments: 'a'

func_pos_kw_only(1, 10, c=100)
# a=1, b=10, c=100

func_pos_kw_only(1, c=100, b=10)
# a=1, b=10, c=100

# def func_pos_kw_only(a, *, b, /, c):
#     print(f'a={a}, b={b}, c={c}')
# SyntaxError: invalid syntax

def func_default(a, b, c=100):
    print(f'a={a}, b={b}, c={c}')

func_default(1, 10)
# a=1, b=10, c=100

func_default(1, 10, 200)
# a=1, b=10, c=200

# def func_default(a=1, b, c=100):
#     print(f'a={a}, b={b}, c={c}')
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

def func(a, b, c):
    print(f'a={a}, b={b}, c={c}')

l = [1, 10, 100]
func(*l)
# a=1, b=10, c=100

l = [1, 10]
# func(*l)
# TypeError: func() missing 1 required positional argument: 'c'

d = {'a': 1, 'b': 10, 'c': 100}
func(**d)
# a=1, b=10, c=100

d = {'a': 1, 'b': 10, 'x': 100}
# func(**d)
# TypeError: func() got an unexpected keyword argument 'x'

def func_return(a, b):
    return a + b

x = func_return(3, 4)
print(x)
# 7

print(type(x))
# <class 'int'>

x = func_return(0.3, 0.4)
print(x)
# 0.7

print(type(x))
# <class 'float'>

def func_none():
    # do something
    pass

x = func_none()
print(x)
# None

def func_none2():
    return

x = func_none2()
print(x)
# None

def func_none3():
    return None

x = func_none3()
print(x)
# None

def func_return_multi(a, b):
    return a + b, a * b, a / b

x = func_return_multi(3, 4)
print(x)
# (7, 12, 0.75)

print(type(x))
# <class 'tuple'>

x, y, z = func_return_multi(3, 4)
print(x)
# 7

print(y)
# 12

print(z)
# 0.75
