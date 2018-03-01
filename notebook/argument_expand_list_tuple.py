def func(arg1, arg2, arg3):
    print(arg1)
    print(arg2)
    print(arg3)

l = ['one', 'two', 'three']

func(*l)
# one
# two
# three

func(*['one', 'two', 'three'])
# one
# two
# three

t = ('one', 'two', 'three')

func(*t)
# one
# two
# three

func(*('one', 'two', 'three'))
# one
# two
# three

# func(*['one', 'two'])
# TypeError: func() missing 1 required positional argument: 'arg3'

# func(*['one', 'two', 'three', 'four'])
# TypeError: func() takes 3 positional arguments but 4 were given

def func_default(arg1=1, arg2=2, arg3=3):
    print(arg1)
    print(arg2)
    print(arg3)

func_default(*['one', 'two'])
# one
# two
# 3

func_default(*['one'])
# one
# 2
# 3

# func_default(*['one', 'two', 'three', 'four'])
# TypeError: func_default() takes from 0 to 3 positional arguments but 4 were given

def func_args(arg1, *args):
    print(arg1)
    for arg in args:
        print(arg)

func_args(*['one', 'two'])
# one
# two

func_args(*['one', 'two', 'three'])
# one
# two
# three

func_args(*['one', 'two', 'three', 'four'])
# one
# two
# three
# four
