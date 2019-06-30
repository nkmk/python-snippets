l = list(range(10))
print(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

l.clear()
print(l)
# []

l = list(range(10))
print(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(l.pop(0))
# 0

print(l)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(l.pop(3))
# 4

print(l)
# [1, 2, 3, 5, 6, 7, 8, 9]

print(l.pop(-2))
# 8

print(l)
# [1, 2, 3, 5, 6, 7, 9]

print(l.pop())
# 9

print(l)
# [1, 2, 3, 5, 6, 7]

# print(l.pop(100))
# IndexError: pop index out of range

l = ['Alice', 'Bob', 'Charlie', 'Bob', 'Dave']
print(l)
# ['Alice', 'Bob', 'Charlie', 'Bob', 'Dave']

l.remove('Alice')
print(l)
# ['Bob', 'Charlie', 'Bob', 'Dave']

l.remove('Bob')
print(l)
# ['Charlie', 'Bob', 'Dave']

# l.remove('xxx')
# ValueError: list.remove(x): x not in list

l = list(range(10))
print(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print([i for i in l if i % 2 == 0])
# [0, 2, 4, 6, 8]

print([i for i in l if i % 2 != 0])
# [1, 3, 5, 7, 9]

print(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

l = ['Alice', 'Bob', 'Charlie', 'Bob', 'David']
print(l)
# ['Alice', 'Bob', 'Charlie', 'Bob', 'David']

print([s for s in l if s != 'Bob'])
# ['Alice', 'Charlie', 'David']

print([s for s in l if s.endswith('e')])
# ['Alice', 'Charlie']

print(list(set(l)))
# ['David', 'Alice', 'Charlie', 'Bob']

l = list(range(10))
print(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

del l[0]
print(l)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

del l[-1]
print(l)
# [1, 2, 3, 4, 5, 6, 7, 8]

del l[6]
print(l)
# [1, 2, 3, 4, 5, 6, 8]

l = list(range(10))
print(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

del l[2:5]
print(l)
# [0, 1, 5, 6, 7, 8, 9]

l = list(range(10))
del l[:3]
print(l)
# [3, 4, 5, 6, 7, 8, 9]

l = list(range(10))
del l[4:]
print(l)
# [0, 1, 2, 3]

l = list(range(10))
del l[-3:]
print(l)
# [0, 1, 2, 3, 4, 5, 6]

l = list(range(10))
del l[:]
print(l)
# []

l = list(range(10))
del l[2:8:2]
print(l)
# [0, 1, 3, 5, 7, 8, 9]

l = list(range(10))
del l[::3]
print(l)
# [1, 2, 4, 5, 7, 8]
