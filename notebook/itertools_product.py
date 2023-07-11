import itertools
import pprint

l1 = [1, 2, 3]
l2 = ['A', 'B']

p = itertools.product(l1, l2)
print(p)
# <itertools.product object at 0x105e6e2c0>

print(type(p))
# <class 'itertools.product'>

for v in p:
    print(v)
# (1, 'A')
# (1, 'B')
# (2, 'A')
# (2, 'B')
# (3, 'A')
# (3, 'B')

for v in p:
    print(v)

for v1, v2 in itertools.product(l1, l2):
    print(v1, v2)
# 1 A
# 1 B
# 2 A
# 2 B
# 3 A
# 3 B

for v1 in l1:
    for v2 in l2:
        print(v1, v2)
# 1 A
# 1 B
# 2 A
# 2 B
# 3 A
# 3 B

l1 = [1, 2, 3]
l2 = ['A', 'B']

l_p = list(itertools.product(l1, l2))
print(l_p)
# [(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B'), (3, 'A'), (3, 'B')]

print(type(l_p))
# <class 'list'>

print(type(l_p[0]))
# <class 'tuple'>

t = ('A', 'B')
d = {'key1': 'value1', 'key2': 'value2'}
r = range(2)

pprint.pprint(list(itertools.product(t, d, r)))
# [('A', 'key1', 0),
#  ('A', 'key1', 1),
#  ('A', 'key2', 0),
#  ('A', 'key2', 1),
#  ('B', 'key1', 0),
#  ('B', 'key1', 1),
#  ('B', 'key2', 0),
#  ('B', 'key2', 1)]

l1 = ['A', 'B']

pprint.pprint(list(itertools.product(l1, repeat=3)))
# [('A', 'A', 'A'),
#  ('A', 'A', 'B'),
#  ('A', 'B', 'A'),
#  ('A', 'B', 'B'),
#  ('B', 'A', 'A'),
#  ('B', 'A', 'B'),
#  ('B', 'B', 'A'),
#  ('B', 'B', 'B')]

pprint.pprint(list(itertools.product(l1, l1, l1)))
# [('A', 'A', 'A'),
#  ('A', 'A', 'B'),
#  ('A', 'B', 'A'),
#  ('A', 'B', 'B'),
#  ('B', 'A', 'A'),
#  ('B', 'A', 'B'),
#  ('B', 'B', 'A'),
#  ('B', 'B', 'B')]

l1 = [1, 2]
l2 = ['A', 'B']

pprint.pprint(list(itertools.product(l1, l2, repeat=2)))
# [(1, 'A', 1, 'A'),
#  (1, 'A', 1, 'B'),
#  (1, 'A', 2, 'A'),
#  (1, 'A', 2, 'B'),
#  (1, 'B', 1, 'A'),
#  (1, 'B', 1, 'B'),
#  (1, 'B', 2, 'A'),
#  (1, 'B', 2, 'B'),
#  (2, 'A', 1, 'A'),
#  (2, 'A', 1, 'B'),
#  (2, 'A', 2, 'A'),
#  (2, 'A', 2, 'B'),
#  (2, 'B', 1, 'A'),
#  (2, 'B', 1, 'B'),
#  (2, 'B', 2, 'A'),
#  (2, 'B', 2, 'B')]

pprint.pprint(list(itertools.product(l1, l2, l1, l2)))
# [(1, 'A', 1, 'A'),
#  (1, 'A', 1, 'B'),
#  (1, 'A', 2, 'A'),
#  (1, 'A', 2, 'B'),
#  (1, 'B', 1, 'A'),
#  (1, 'B', 1, 'B'),
#  (1, 'B', 2, 'A'),
#  (1, 'B', 2, 'B'),
#  (2, 'A', 1, 'A'),
#  (2, 'A', 1, 'B'),
#  (2, 'A', 2, 'A'),
#  (2, 'A', 2, 'B'),
#  (2, 'B', 1, 'A'),
#  (2, 'B', 1, 'B'),
#  (2, 'B', 2, 'A'),
#  (2, 'B', 2, 'B')]
