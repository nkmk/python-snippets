def func(arg1, arg2, arg3):
    print('arg1 =', arg1)
    print('arg2 =', arg2)
    print('arg3 =', arg3)

l = ['one', 'two', 'three']

func(*l)
# arg1 = one
# arg2 = two
# arg3 = three

func(*['one', 'two', 'three'])
# arg1 = one
# arg2 = two
# arg3 = three

t = ('one', 'two', 'three')

func(*t)
# arg1 = one
# arg2 = two
# arg3 = three

func(*('one', 'two', 'three'))
# arg1 = one
# arg2 = two
# arg3 = three

# func(*['one', 'two'])
# TypeError: func() missing 1 required positional argument: 'arg3'

# func(*['one', 'two', 'three', 'four'])
# TypeError: func() takes 3 positional arguments but 4 were given

def func_default(arg1=1, arg2=2, arg3=3):
    print('arg1 =', arg1)
    print('arg2 =', arg2)
    print('arg3 =', arg3)

func_default(*['one', 'two'])
# arg1 = one
# arg2 = two
# arg3 = 3

func_default(*['one'])
# arg1 = one
# arg2 = 2
# arg3 = 3

# func_default(*['one', 'two', 'three', 'four'])
# TypeError: func_default() takes from 0 to 3 positional arguments but 4 were given

def func_args(arg1, *args):
    print('arg1 =', arg1)
    print('args =', args)

func_args(*['one', 'two'])
# arg1 = one
# args = ('two',)

func_args(*['one', 'two', 'three'])
# arg1 = one
# args = ('two', 'three')

func_args(*['one', 'two', 'three', 'four'])
# arg1 = one
# args = ('two', 'three', 'four')
