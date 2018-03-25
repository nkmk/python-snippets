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

print([i for i in l if i < 0])
# [-5, -4, -3, -2, -1]

print(len([i for i in l if i < 0]))
# 5

print([i for i in l if i % 2 == 1])
# [-5, -3, -1, 1, 3, 5]

print(len([i for i in l if i % 2 == 1]))
# 6

l = ['apple', 'orange', 'banana']

print([s for s in l if s.endswith('e')])
# ['apple', 'orange']

print(len([s for s in l if s.endswith('e')]))
# 2
