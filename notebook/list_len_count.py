l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']

print(len(l))
# 7

l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']

print(l.count('a'))
# 4

print(l.count('b'))
# 1

print(l.count('c'))
# 2

print(l.count('d'))
# 0

l = list(range(-5, 6))
print(l)
# [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

print([i < 0 for i in l])
# [True, True, True, True, True, False, False, False, False, False, False]

print(sum([i < 0 for i in l]))
# 5

print(sum((i < 0 for i in l)))
# 5

print(sum(i < 0 for i in l))
# 5

print([not (i < 0) for i in l])
# [False, False, False, False, False, True, True, True, True, True, True]

print(sum(not (i < 0) for i in l))
# 6

print(sum(i >= 0 for i in l))
# 6

print([i % 2 == 1 for i in l])
# [True, False, True, False, True, False, True, False, True, False, True]

print(sum(i % 2 == 1 for i in l))
# 6

l = ['apple', 'orange', 'banana']

print([s.endswith('e') for s in l])
# [True, True, False]

print(sum(s.endswith('e') for s in l))
# 2
