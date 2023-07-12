l = [30, 50, 10, 40, 20]

print(l.index(30))
# 0

print(l.index(20))
# 4

# print(l.index(100))
# ValueError: 100 is not in list

def my_find(l, x):
    if x in l:
        return l.index(x)
    else:
        return -1

l = [30, 50, 10, 40, 20]

print(my_find(l, 30))
# 0

print(my_find(l, 100))
# -1

def my_find2(l, x):
    return l.index(x) if x in l else -1

print(my_find2(l, 30))
# 0

print(my_find2(l, 100))
# -1

l = [10, 30, 10, 10, 20, 20]

print(l.index(10))
# 0

print(l.index(20))
# 4

print([i for i, x in enumerate(l) if x == 10])
# [0, 2, 3]

print([i for i, x in enumerate(l) if x == 20])
# [4, 5]

print([i for i, x in enumerate(l) if x == 30])
# [1]

print([i for i, x in enumerate(l) if x == 100])
# []

def my_index_multi(l, x):
    return [i for i, _x in enumerate(l) if _x == x]

print(my_index_multi(l, 10))
# [0, 2, 3]

print(my_index_multi(l, 20))
# [4, 5]

print(my_index_multi(l, 30))
# [1]

print(my_index_multi(l, 100))
# []

l = [10, 30, 10, 10, 20, 20]

print(l.index(10))
# 0

print(l.index(10, 2))
# 2

# print(l.index(20, 2, 4))
# ValueError: 20 is not in list

print(l.index(20, 2, 5))
# 4

print(l[2:])
# [10, 10, 20, 20]

print(l[2:].index(10))
# 0

print(l[2:5])
# [10, 10, 20]

print(l[2:5].index(20))
# 2

t = ('c', 'a', 'a', 'b', 'c')

print(t.index('a'))
# 1

# print(t.index('x'))
# ValueError: tuple.index(x): x not in tuple

print(my_find(t, 'a'))
# 1

print(my_find(t, 'x'))
# -1

print(my_index_multi(t, 'a'))
# [1, 2]

print(my_index_multi(t, 'x'))
# []

l = [10, 30, 10, 10, 20, 20]

print(l.index(max(l)))
# 1

print(l.index(min(l)))
# 0

print(my_index_multi(l, max(l)))
# [1]

print(my_index_multi(l, min(l)))
# [0, 2, 3]
