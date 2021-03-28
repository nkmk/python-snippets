l = [-2, -1, 0, 1, 2]
print(filter(lambda x: x % 2 == 0, l))
# <filter object at 0x10bb38580>

print(type(filter(lambda x: x % 2 == 0, l)))
# <class 'filter'>

for i in filter(lambda x: x % 2 == 0, l):
    print(i)
# -2
# 0
# 2

print(list(filter(lambda x: x % 2 == 0, l)))
# [-2, 0, 2]

print(list(filter(lambda x: x % 2 != 0, l)))
# [-1, 1]

l_s = ['apple', 'orange', 'strawberry']
print(list(filter(lambda x: x.endswith('e'), l_s)))
# ['apple', 'orange']

print(list(filter(lambda x: not x.endswith('e'), l_s)))
# ['strawberry']

def is_even(x):
    return x % 2 == 0

l = [-2, -1, 0, 1, 2]
print(list(filter(is_even, l)))
# [-2, 0, 2]

l = [-2, -1, 0, 1, 2]
print(list(filter(lambda x: x % 2 == 0 and x > 0, l)))
# [2]

print(list(filter(lambda x: x % 2 == 0 or x > 0, l)))
# [-2, 0, 1, 2]

l_b = [True, False]
print(list(filter(None, l_b)))
# [True]

l = [-2, -1, 0, 1, 2]
print(list(filter(None, l)))
# [-2, -1, 1, 2]

l_2d = [[0, 1, 2], [], [3, 4, 5]]
print(list(filter(None, l_2d)))
# [[0, 1, 2], [3, 4, 5]]

l_s = ['apple', '', 'orange', 'strawberry']
print(list(filter(None, l_s)))
# ['apple', 'orange', 'strawberry']

import itertools

l = [-2, -1, 0, 1, 2]
print(list(itertools.filterfalse(lambda x: x % 2 == 0, l)))
# [-1, 1]

print(list(itertools.filterfalse(lambda x: x % 2 != 0, l)))
# [-2, 0, 2]

l_s = ['apple', 'orange', 'strawberry']
print(list(itertools.filterfalse(lambda x: x.endswith('e'), l_s)))
# ['strawberry']

l = [-2, -1, 0, 1, 2]
print(list(itertools.filterfalse(None, l)))
# [0]

l = [-2, -1, 0, 1, 2]
print([x for x in l if x % 2 == 0])
# [-2, 0, 2]

print([x for x in l if x % 2 != 0])
# [-1, 1]

l_s = ['apple', 'orange', 'strawberry']
print([x for x in l_s if x.endswith('e')])
# ['apple', 'orange']

print([x for x in l_s if not x.endswith('e')])
# ['strawberry']

l = [-2, -1, 0, 1, 2]
print([x for x in l if x])
# [-2, -1, 1, 2]

l_2d = [[0, 1, 2], [], [3, 4, 5]]
print([x for x in l_2d if x])
# [[0, 1, 2], [3, 4, 5]]
