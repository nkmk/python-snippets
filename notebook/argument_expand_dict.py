def func(arg1, arg2, arg3):
    print(arg1)
    print(arg2)
    print(arg3)

d = {'arg1': 'one', 'arg2': 'two', 'arg3': 'three'}

func(**d)
# one
# two
# three

func(**{'arg1': 'one', 'arg2': 'two', 'arg3': 'three'})
# one
# two
# three

# func(**{'arg1': 'one', 'arg2': 'two'})
# TypeError: func() missing 1 required positional argument: 'arg3'

# func(**{'arg1': 'one', 'arg2': 'two', 'arg3': 'three', 'arg4': 'four'})
# TypeError: func() got an unexpected keyword argument 'arg4'

def func_default(arg1=1, arg2=2, arg3=3):
    print(arg1)
    print(arg2)
    print(arg3)

func_default(**{'arg1': 'one'})
# one
# 2
# 3

func_default(**{'arg2': 'two', 'arg3': 'three'})
# 1
# two
# three

# func_default(**{'arg1': 'one', 'arg4': 'four'})
# TypeError: func_default() got an unexpected keyword argument 'arg4'

def func_kwargs(arg1, **kwargs):
    print('arg1', arg1)
    for k, v in kwargs.items():
        print(k, v)

func_kwargs(**{'arg1': 'one', 'arg2': 'two', 'arg3': 'three'})
# arg1 one
# arg2 two
# arg3 three

func_kwargs(**{'arg1': 'one', 'arg2': 'two', 'arg3': 'three', 'arg4': 'four'})
# arg1 one
# arg2 two
# arg3 three
# arg4 four

func_kwargs(**{'arg1': 'one', 'arg3': 'three'})
# arg1 one
# arg3 three
