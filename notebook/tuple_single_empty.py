single_tuple_error = (0)

print(single_tuple_error)
print(type(single_tuple_error))
# 0
# <class 'int'>

single_tuple = (0, )

print(single_tuple)
print(type(single_tuple))
# (0,)
# <class 'tuple'>

# print((0, 1, 2) + (3))
# TypeError: can only concatenate tuple (not "int") to tuple

print((0, 1, 2) + (3, ))
# (0, 1, 2, 3)

t = 0, 1, 2

print(t)
print(type(t))
# (0, 1, 2)
# <class 'tuple'>

t_ = 0,

print(t_)
print(type(t_))
# (0,)
# <class 'tuple'>

empty_tuple = ()

print(empty_tuple)
print(type(empty_tuple))
# ()
# <class 'tuple'>

# empty_tuple_error = 
# SyntaxError: invalid syntax

# empty_tuple_error = ,
# SyntaxError: invalid syntax

# empty_tuple_error = (,)
# SyntaxError: invalid syntax

empty_tuple = tuple()

print(empty_tuple)
print(type(empty_tuple))
# ()
# <class 'tuple'>

def example(a, b):
    print(a, type(a))
    print(b, type(b))

example(0, 1)
# 0 <class 'int'>
# 1 <class 'int'>

# example((0, 1))
# TypeError: example() missing 1 required positional argument: 'b'

example((0, 1), 2)
# (0, 1) <class 'tuple'>
# 2 <class 'int'>

example(*(0, 1))
# 0 <class 'int'>
# 1 <class 'int'>
