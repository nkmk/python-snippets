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

l = list('abcdefg')
print(l)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']

l.remove('d')
print(l)
# ['a', 'b', 'c', 'e', 'f', 'g']

l = [0, 1, 2, 1, 3]
l.remove(1)
print(l)
# [0, 2, 1, 3]

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
