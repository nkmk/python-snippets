import itertools

l_2d = [[0, 1], [2, 3]]

print(list(itertools.chain.from_iterable(l_2d)))
# [0, 1, 2, 3]

t_2d = ((0, 1), (2, 3))

print(tuple(itertools.chain.from_iterable(t_2d)))
# (0, 1, 2, 3)

l_3d = [[[0, 1], [2, 3]], [[4, 5], [6, 7]]]

print(list(itertools.chain.from_iterable(l_3d)))
# [[0, 1], [2, 3], [4, 5], [6, 7]]

l_mix = [[0, 1], [2, 3], 4]

# print(list(itertools.chain.from_iterable(l_mix)))
# TypeError: 'int' object is not iterable

print(sum(l_2d, []))
# [0, 1, 2, 3]

# print(sum(l_2d))
# TypeError: unsupported operand type(s) for +: 'int' and 'list'

print(sum(t_2d, ()))
# (0, 1, 2, 3)

print(sum(l_3d, []))
# [[0, 1], [2, 3], [4, 5], [6, 7]]

# print(sum(l_mix, []))
# TypeError: can only concatenate list (not "int") to list

import collections

def flatten(l):
    for el in l:
        if isinstance(el, collections.abc.Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el

print(list(flatten(l_2d)))
# [0, 1, 2, 3]

print(list(flatten(l_3d)))
# [0, 1, 2, 3, 4, 5, 6, 7]

print(list(flatten(l_mix)))
# [0, 1, 2, 3, 4]

l_t_r_mix = [[0, 1], (2, 3), 4, range(5, 8)]

print(list(flatten(l_t_r_mix)))
# [0, 1, 2, 3, 4, 5, 6, 7]

def flatten_list(l):
    for el in l:
        if isinstance(el, list):
            yield from flatten_list(el)
        else:
            yield el

print(list(flatten_list(l_2d)))
# [0, 1, 2, 3]

print(list(flatten_list(l_3d)))
# [0, 1, 2, 3, 4, 5, 6, 7]

print(list(flatten_list(l_mix)))
# [0, 1, 2, 3, 4]

print(list(flatten_list(l_t_r_mix)))
# [0, 1, (2, 3), 4, range(5, 8)]

def flatten_list_tuple_range(l):
    for el in l:
        if isinstance(el, (list, tuple, range)):
            yield from flatten_list_tuple_range(el)
        else:
            yield el

print(list(flatten_list_tuple_range(l_t_r_mix)))
# [0, 1, 2, 3, 4, 5, 6, 7]
