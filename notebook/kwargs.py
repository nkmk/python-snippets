def func_kwargs(**kwargs):
    print('kwargs: ', kwargs)
    print('type: ', type(kwargs))

func_kwargs(key1=1, key2=2, key3=3)
# kwargs:  {'key1': 1, 'key2': 2, 'key3': 3}
# type:  <class 'dict'>

def func_kwargs_positional(arg1, arg2, **kwargs):
    print('arg1: ', arg1)
    print('arg2: ', arg2)
    print('kwargs: ', kwargs)

func_kwargs_positional(0, 1, key1=1)
# arg1:  0
# arg2:  1
# kwargs:  {'key1': 1}

d = {'key1': 1, 'key2': 2, 'arg1': 100, 'arg2': 200}

func_kwargs_positional(**d)
# arg1:  100
# arg2:  200
# kwargs:  {'key1': 1, 'key2': 2}

# def func_kwargs_error(**kwargs, arg):
#     print(kwargs)

# SyntaxError: invalid syntax
