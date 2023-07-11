import itertools

l = ['a', 'b', 'c', 'd']

p = itertools.permutations(l, 2)
print(type(p))
# <class 'itertools.permutations'>

for v in itertools.permutations(l, 2):
    print(v)
# ('a', 'b')
# ('a', 'c')
# ('a', 'd')
# ('b', 'a')
# ('b', 'c')
# ('b', 'd')
# ('c', 'a')
# ('c', 'b')
# ('c', 'd')
# ('d', 'a')
# ('d', 'b')
# ('d', 'c')

p_list = list(itertools.permutations(l, 2))
print(p_list)
# [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'a'), ('b', 'c'), ('b', 'd'), ('c', 'a'), ('c', 'b'), ('c', 'd'), ('d', 'a'), ('d', 'b'), ('d', 'c')]

print(len(p_list))
# 12

for v in itertools.permutations(l):
    print(v)
# ('a', 'b', 'c', 'd')
# ('a', 'b', 'd', 'c')
# ('a', 'c', 'b', 'd')
# ('a', 'c', 'd', 'b')
# ('a', 'd', 'b', 'c')
# ('a', 'd', 'c', 'b')
# ('b', 'a', 'c', 'd')
# ('b', 'a', 'd', 'c')
# ('b', 'c', 'a', 'd')
# ('b', 'c', 'd', 'a')
# ('b', 'd', 'a', 'c')
# ('b', 'd', 'c', 'a')
# ('c', 'a', 'b', 'd')
# ('c', 'a', 'd', 'b')
# ('c', 'b', 'a', 'd')
# ('c', 'b', 'd', 'a')
# ('c', 'd', 'a', 'b')
# ('c', 'd', 'b', 'a')
# ('d', 'a', 'b', 'c')
# ('d', 'a', 'c', 'b')
# ('d', 'b', 'a', 'c')
# ('d', 'b', 'c', 'a')
# ('d', 'c', 'a', 'b')
# ('d', 'c', 'b', 'a')

print(len(list(itertools.permutations(l))))
# 24

l = ['a', 'a']

for v in itertools.permutations(l, 2):
    print(v)
# ('a', 'a')
# ('a', 'a')

l = ['a', 'b', 'c', 'd']

c = itertools.combinations(l, 2)
print(type(c))
# <class 'itertools.combinations'>

for v in itertools.combinations(l, 2):
    print(v)
# ('a', 'b')
# ('a', 'c')
# ('a', 'd')
# ('b', 'c')
# ('b', 'd')
# ('c', 'd')

c_list = list(itertools.combinations(l, 2))
print(c_list)
# [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')]

print(len(c_list))
# 6

l = ['a', 'b', 'c', 'd']

h = itertools.combinations_with_replacement(l, 2)
print(type(h))
# <class 'itertools.combinations_with_replacement'>

for v in itertools.combinations_with_replacement(l, 2):
    print(v)
# ('a', 'a')
# ('a', 'b')
# ('a', 'c')
# ('a', 'd')
# ('b', 'b')
# ('b', 'c')
# ('b', 'd')
# ('c', 'c')
# ('c', 'd')
# ('d', 'd')

h_list = list(itertools.combinations_with_replacement(l, 2))
print(h_list)
# [('a', 'a'), ('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'b'), ('b', 'c'), ('b', 'd'), ('c', 'c'), ('c', 'd'), ('d', 'd')]

print(len(h_list))
# 10
