def add_def(a, b=1):
    return a + b

add_lambda = lambda a, b=1: a + b

print(add_def(3, 4))
# 7

print(add_def(3))
# 4

print(add_lambda(3, 4))
# 7

print(add_lambda(3))
# 4

get_odd_even = lambda x: 'even' if x % 2 == 0 else 'odd'

print(get_odd_even(3))
# odd

print(get_odd_even(4))
# even

l = ['Charle', 'Bob', 'Alice']

l_sorted = sorted(l)

print(l_sorted)
# ['Alice', 'Bob', 'Charle']

print(len('Alice'))
# 5

l_sorted = sorted(l, key=len)

print(l_sorted)
# ['Bob', 'Alice', 'Charle']

print((lambda x: x[1])('Alice'))
# l

l_sorted_second = sorted(l, key=lambda x: x[2])

print(l_sorted_second)
# ['Charle', 'Bob', 'Alice']

l = [0, 1, 2, 3]

map_square = map(lambda x: x**2, l)

print(map_square)
# <map object at 0x10cb5a048>

print(list(map_square))
# [0, 1, 4, 9]

l_square = [x**2 for x in l]

print(l_square)
# [0, 1, 4, 9]

g_square = (x**2 for x in l)

print(g_square)
# <generator object <genexpr> at 0x10cb10d58>

print(list(g_square))
# [0, 1, 4, 9]

filter_even = filter(lambda x: x % 2 == 0, l)

print(list(filter_even))
# [0, 2]

l_even = [x for x in l if x % 2 == 0]

print(l_even)
# [0, 2]
