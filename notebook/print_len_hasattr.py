import numpy as np

l = [0, 1, 2]
print(type(l))
# <class 'list'>

print(hasattr(l, 'append'))
# True

print(hasattr(l, 'xxx'))
# False

print(len(l))
# 3

print(l.__len__())
# 3

def print_len_hasattr(x):
    if hasattr(x, '__len__'):
        print(len(x))
    else:
        print('x has no __len__')

print_len_hasattr([0, 1, 2])
# 3

print_len_hasattr('abc')
# 3

print_len_hasattr(100)
# x has no __len__

a = np.arange(3)
print(a)
# [0 1 2]

print_len_hasattr(a)
# 3
