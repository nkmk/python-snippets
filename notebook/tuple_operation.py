t = (0, 1, 2)

print(t)
# (0, 1, 2)

print(type(t))
# <class 'tuple'>

print(t[0])
# 0

print(t[:2])
# (0, 1)

# t[0] = 100
# TypeError: 'tuple' object does not support item assignment

# t.append(100)
# AttributeError: 'tuple' object has no attribute 'append'

t_add = t + (3, 4, 5)

print(t_add)
# (0, 1, 2, 3, 4, 5)

print(t)
# (0, 1, 2)

# print(t + [3, 4, 5])
# TypeError: can only concatenate tuple (not "list") to tuple

print(t + tuple([3, 4, 5]))
# (0, 1, 2, 3, 4, 5)

# print(t + tuple(3))
# TypeError: 'int' object is not iterable

print(t + (3,))
# (0, 1, 2, 3)

l = list(t)

print(l)
# [0, 1, 2]

print(type(l))
# <class 'list'>

l.insert(2, 100)

print(l)
# [0, 1, 100, 2]

t_insert = tuple(l)

print(t_insert)
# (0, 1, 100, 2)

print(type(t_insert))
# <class 'tuple'>

l = list(t)
l[1] = 100
t_change = tuple(l)

print(t_change)
# (0, 100, 2)

l = list(t)
l.remove(1)
t_remove = tuple(l)

print(t_remove)
# (0, 2)
