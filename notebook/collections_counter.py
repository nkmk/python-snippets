import collections

l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']
c = collections.Counter(l)

print(c)
# Counter({'a': 4, 'c': 2, 'b': 1})

print(type(c))
# <class 'collections.Counter'>

print(issubclass(type(c), dict))
# True

print(c['a'])
# 4

print(c['b'])
# 1

print(c['c'])
# 2

print(c['d'])
# 0

print(c.keys())
# dict_keys(['a', 'b', 'c'])

print(c.values())
# dict_values([4, 1, 2])

print(c.items())
# dict_items([('a', 4), ('b', 1), ('c', 2)])

print(c.most_common())
# [('a', 4), ('c', 2), ('b', 1)]

print(c.most_common()[0])
# ('a', 4)

print(c.most_common()[-1])
# ('b', 1)

print(c.most_common()[0][0])
# a

print(c.most_common()[0][1])
# 4

print(c.most_common()[::-1])
# [('b', 1), ('c', 2), ('a', 4)]

print(c.most_common(2))
# [('a', 4), ('c', 2)]

values, counts = zip(*c.most_common())

print(values)
# ('a', 'c', 'b')

print(counts)
# (4, 2, 1)

l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']
c = collections.Counter(l)

print(len(c))
# 3

print(set(l))
# {'b', 'a', 'c'}

print(len(set(l)))
# 3

l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']

print([i for i in l if l.count(i) >= 2])
# ['a', 'a', 'a', 'a', 'c', 'c']

print(len([i for i in l if l.count(i) >= 2]))
# 6

c = collections.Counter(l)

print([i[0] for i in c.items() if i[1] >= 2])
# ['a', 'c']

print(len([i[0] for i in c.items() if i[1] >= 2]))
# 2

s = 'government of the people, by the people, for the people.'

s_remove = s.replace(',', '').replace('.', '')

print(s_remove)
# government of the people by the people for the people

word_list = s_remove.split()

print(word_list)
# ['government', 'of', 'the', 'people', 'by', 'the', 'people', 'for', 'the', 'people']

print(word_list.count('people'))
# 3

print(len(set(word_list)))
# 6

c = collections.Counter(word_list)

print(c)
# Counter({'the': 3, 'people': 3, 'government': 1, 'of': 1, 'by': 1, 'for': 1})

print(c.most_common()[0][0])
# the

s = 'supercalifragilisticexpialidocious'

print(s.count('p'))
# 2

c = collections.Counter(s)

print(c)
# Counter({'i': 7, 's': 3, 'c': 3, 'a': 3, 'l': 3, 'u': 2, 'p': 2, 'e': 2, 'r': 2, 'o': 2, 'f': 1, 'g': 1, 't': 1, 'x': 1, 'd': 1})

print(c.most_common(5))
# [('i', 7), ('s', 3), ('c', 3), ('a', 3), ('l', 3)]

values, counts = zip(*c.most_common(5))

print(values)
# ('i', 's', 'c', 'a', 'l')
