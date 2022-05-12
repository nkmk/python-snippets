import itertools

l = [0, 0, 0, 1, 1, 2, 0, 0]
print([(k, list(g)) for k, g in itertools.groupby(l)])
# [(0, [0, 0, 0]), (1, [1, 1]), (2, [2]), (0, [0, 0])]

l = [0, 0, 0, 1, 1, 2, 0, 0]
print(itertools.groupby(l))
# <itertools.groupby object at 0x111813270>

for k, g in itertools.groupby(l):
    print(k, g)
# 0 <itertools._grouper object at 0x1117bccd0>
# 1 <itertools._grouper object at 0x111775e80>
# 2 <itertools._grouper object at 0x1117cdac0>
# 0 <itertools._grouper object at 0x1117cd430>

for k, g in itertools.groupby(l):
    print(k, list(g))
# 0 [0, 0, 0]
# 1 [1, 1]
# 2 [2]
# 0 [0, 0]

print([k for k, g in itertools.groupby(l)])
# [0, 1, 2, 0]

print([list(g) for k, g in itertools.groupby(l)])
# [[0, 0, 0], [1, 1], [2], [0, 0]]

print([(k, list(g)) for k, g in itertools.groupby(l)])
# [(0, [0, 0, 0]), (1, [1, 1]), (2, [2]), (0, [0, 0])]

l = ['aaa', 'bbb', 'ccc', 'a', 'b', 'aa', 'bb']
print([(k, list(g)) for k, g
       in itertools.groupby(l, len)])
# [(3, ['aaa', 'bbb', 'ccc']), (1, ['a', 'b']), (2, ['aa', 'bb'])]

l = [0, 2, 0, 3, 1, 4, 4, 0]
print([(k, list(g)) for k, g
       in itertools.groupby(l, lambda x: x % 2)])
# [(0, [0, 2, 0]), (1, [3, 1]), (0, [4, 4, 0])]

l = [[0, 'Alice', 0],
     [1, 'Alice', 10],
     [2, 'Bob', 20],
     [3, 'Bob', 30],
     [4, 'Alice', 40]]

for k, g in itertools.groupby(l, lambda x: x[1]):
    print(k, list(g))
# Alice [[0, 'Alice', 0], [1, 'Alice', 10]]
# Bob [[2, 'Bob', 20], [3, 'Bob', 30]]
# Alice [[4, 'Alice', 40]]

for k, g in itertools.groupby(sorted(l, key=lambda x: x[1]), lambda x: x[1]):
    print(k, list(g))
# Alice [[0, 'Alice', 0], [1, 'Alice', 10], [4, 'Alice', 40]]
# Bob [[2, 'Bob', 20], [3, 'Bob', 30]]

for k, g in itertools.groupby(sorted(l, key=lambda x: x[1]), lambda x: x[1]):
    print(k, sum(x[2] for x in g))
# Alice 50
# Bob 50

t = (0, 0, 0, 1, 1, 2, 0, 0)
print([(k, list(g)) for k, g in itertools.groupby(t)])
# [(0, [0, 0, 0]), (1, [1, 1]), (2, [2]), (0, [0, 0])]

print(tuple((k, tuple(g)) for k, g in itertools.groupby(t)))
# ((0, (0, 0, 0)), (1, (1, 1)), (2, (2,)), (0, (0, 0)))

s = 'aaabbcaa'
print([(k, list(g)) for k, g in itertools.groupby(s)])
# [('a', ['a', 'a', 'a']), ('b', ['b', 'b']), ('c', ['c']), ('a', ['a', 'a'])]

print([(k, ''.join(g)) for k, g in itertools.groupby(s)])
# [('a', 'aaa'), ('b', 'bb'), ('c', 'c'), ('a', 'aa')]
