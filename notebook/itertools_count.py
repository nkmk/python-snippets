import itertools

for i in itertools.count():
    print(i)
    if i > 3:
        break
# 0
# 1
# 2
# 3
# 4

for i in itertools.count(2):
    print(i)
    if i > 3:
        break
# 2
# 3
# 4

for i in itertools.count(step=3):
    print(i)
    if i > 8:
        break
# 0
# 3
# 6
# 9

for i in itertools.count(2, 3):
    print(i)
    if i > 8:
        break
# 2
# 5
# 8
# 11

for i in itertools.count(10, -1):
    print(i)
    if i < 8:
        break
# 10
# 9
# 8
# 7

for i in itertools.count(0.1, 1.5):
    print(i)
    if i > 3:
        break
# 0.1
# 1.6
# 3.1

for i in itertools.count():
    ii = 0.1 + 1.5 * i
    print(ii)
    if ii > 3:
        break
# 0.1
# 1.6
# 3.1

l1 = ['a', 'b', 'c']
l2 = ['x', 'y', 'z']

print(list(zip(itertools.count(), l1, l2)))
# [(0, 'a', 'x'), (1, 'b', 'y'), (2, 'c', 'z')]

print(list(enumerate(zip(l1, l2))))
# [(0, ('a', 'x')), (1, ('b', 'y')), (2, ('c', 'z'))]
