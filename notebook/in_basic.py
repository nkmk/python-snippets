print(1 in [0, 1, 2])
# True

print(100 in [0, 1, 2])
# False

print(1 in (0, 1, 2))
# True

print(1 in {0, 1, 2})
# True

print(1 in range(3))
# True

l = [0, 1, 2]
i = 0

if i in l:
    print('{} is a member of {}.'.format(i, l))
else:
    print('{} is not a member of {}.'.format(i, l))
# 0 is a member of [0, 1, 2].

l = [0, 1, 2]
i = 100

if i in l:
    print('{} is a member of {}.'.format(i, l))
else:
    print('{} is not a member of {}.'.format(i, l))
# 100 is not a member of [0, 1, 2].

l = [0, 1, 2]

if l:
    print('not empty')
else:
    print('empty')
# not empty

l = []

if l:
    print('not empty')
else:
    print('empty')
# empty

d = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

print('key1' in d)
# True

print('value1' in d)
# False

print('value1' in d.values())
# True

print(('key1', 'value1') in d.items())
# True

print(('key1', 'value2') in d.items())
# False

print('a' in 'abc')
# True

print('x' in 'abc')
# False

print('ab' in 'abc')
# True

print('ac' in 'abc')
# False

print(10 in [1, 2, 3])
# False

print(10 not in [1, 2, 3])
# True

print(not 10 in [1, 2, 3])
# True

print(not (10 in [1, 2, 3]))
# True

print((not 10) in [1, 2, 3])
# False

print(not 10)
# False

print(False in [1, 2, 3])
# False

print([0, 1] in [0, 1, 2])
# False

print([0, 1] in [[0, 1], [1, 0]])
# True

l = [0, 1, 2]
v1 = 0
v2 = 100

print(v1 in l and v2 in l)
# False

print(v1 in l or v2 in l)
# True

print((v1 in l) or (v2 in l))
# True

l1 = [0, 1, 2, 3, 4]
l2 = [0, 1, 2]
l3 = [0, 1, 5]
l4 = [5, 6, 7]

print(set(l2) <= set(l1))
# True

print(set(l3) <= set(l1))
# False

print(set(l1).isdisjoint(set(l4)))
# True

print(not set(l1).isdisjoint(set(l3)))
# True

l = [0, 1, 2]

for i in l:
    print(i)
# 0
# 1
# 2

print([i * 10 for i in l])
# [0, 10, 20]
