import itertools
import pprint

l1 = ['a', 'b', 'c']
l2 = ['X', 'Y', 'Z']

p = itertools.product(l1, l2)

print(p)
# <itertools.product object at 0x1026edd80>

print(type(p))
# <class 'itertools.product'>

for v in p:
    print(v)
# ('a', 'X')
# ('a', 'Y')
# ('a', 'Z')
# ('b', 'X')
# ('b', 'Y')
# ('b', 'Z')
# ('c', 'X')
# ('c', 'Y')
# ('c', 'Z')

for v in p:
    print(v)

for v1, v2 in itertools.product(l1, l2):
    print(v1, v2)
# a X
# a Y
# a Z
# b X
# b Y
# b Z
# c X
# c Y
# c Z

for v1 in l1:
    for v2 in l2:
        print(v1, v2)
# a X
# a Y
# a Z
# b X
# b Y
# b Z
# c X
# c Y
# c Z

l_p = list(itertools.product(l1, l2))

pprint.pprint(l_p)
# [('a', 'X'),
#  ('a', 'Y'),
#  ('a', 'Z'),
#  ('b', 'X'),
#  ('b', 'Y'),
#  ('b', 'Z'),
#  ('c', 'X'),
#  ('c', 'Y'),
#  ('c', 'Z')]

print(type(l_p))
# <class 'list'>

print(type(l_p[0]))
# <class 'tuple'>

t = ('one', 'two')
d = {'key1': 'value1', 'key2': 'value2'}
r = range(2)

l_p = list(itertools.product(t, d, r))

pprint.pprint(l_p)
# [('one', 'key1', 0),
#  ('one', 'key1', 1),
#  ('one', 'key2', 0),
#  ('one', 'key2', 1),
#  ('two', 'key1', 0),
#  ('two', 'key1', 1),
#  ('two', 'key2', 0),
#  ('two', 'key2', 1)]

l1 = ['a', 'b']

pprint.pprint(list(itertools.product(l1, repeat=3)))
# [('a', 'a', 'a'),
#  ('a', 'a', 'b'),
#  ('a', 'b', 'a'),
#  ('a', 'b', 'b'),
#  ('b', 'a', 'a'),
#  ('b', 'a', 'b'),
#  ('b', 'b', 'a'),
#  ('b', 'b', 'b')]

pprint.pprint(list(itertools.product(l1, l1, l1)))
# [('a', 'a', 'a'),
#  ('a', 'a', 'b'),
#  ('a', 'b', 'a'),
#  ('a', 'b', 'b'),
#  ('b', 'a', 'a'),
#  ('b', 'a', 'b'),
#  ('b', 'b', 'a'),
#  ('b', 'b', 'b')]

l1 = ['a', 'b']
l2 = ['X', 'Y']

pprint.pprint(list(itertools.product(l1, l2, repeat=2)))
# [('a', 'X', 'a', 'X'),
#  ('a', 'X', 'a', 'Y'),
#  ('a', 'X', 'b', 'X'),
#  ('a', 'X', 'b', 'Y'),
#  ('a', 'Y', 'a', 'X'),
#  ('a', 'Y', 'a', 'Y'),
#  ('a', 'Y', 'b', 'X'),
#  ('a', 'Y', 'b', 'Y'),
#  ('b', 'X', 'a', 'X'),
#  ('b', 'X', 'a', 'Y'),
#  ('b', 'X', 'b', 'X'),
#  ('b', 'X', 'b', 'Y'),
#  ('b', 'Y', 'a', 'X'),
#  ('b', 'Y', 'a', 'Y'),
#  ('b', 'Y', 'b', 'X'),
#  ('b', 'Y', 'b', 'Y')]

pprint.pprint(list(itertools.product(l1, l2, l1, l2)))
# [('a', 'X', 'a', 'X'),
#  ('a', 'X', 'a', 'Y'),
#  ('a', 'X', 'b', 'X'),
#  ('a', 'X', 'b', 'Y'),
#  ('a', 'Y', 'a', 'X'),
#  ('a', 'Y', 'a', 'Y'),
#  ('a', 'Y', 'b', 'X'),
#  ('a', 'Y', 'b', 'Y'),
#  ('b', 'X', 'a', 'X'),
#  ('b', 'X', 'a', 'Y'),
#  ('b', 'X', 'b', 'X'),
#  ('b', 'X', 'b', 'Y'),
#  ('b', 'Y', 'a', 'X'),
#  ('b', 'Y', 'a', 'Y'),
#  ('b', 'Y', 'b', 'X'),
#  ('b', 'Y', 'b', 'Y')]
