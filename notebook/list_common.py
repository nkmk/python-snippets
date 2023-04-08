l1 = ['a', 'b', 'c']
l2 = ['b', 'c', 'd']
l3 = ['c', 'd', 'e']

l1_l2_and = set(l1) & set(l2)
print(l1_l2_and)
# {'c', 'b'}

print(type(l1_l2_and))
# <class 'set'>

l1_l2_and_list = list(l1_l2_and)
print(l1_l2_and_list)
# ['c', 'b']

print(type(l1_l2_and_list))
# <class 'list'>

print(len(l1_l2_and))
# 2

print(set(l1) & set(l2) & set(l3))
# {'c'}

l1 = ['a', 'b', 'c']
l2 = ['b', 'c', 'd']
l3 = ['c', 'd', 'e']

print(set(l1) - set(l2))
# {'a'}

print(set(l2) - set(l1))
# {'d'}

print(set(l2) - set(l1) - set(l3))
# set()

l1 = ['a', 'b', 'c']
l2 = ['b', 'c', 'd']
l3 = ['c', 'd', 'e']

print(set(l1) ^ set(l2))
# {'d', 'a'}

print(set(l1) ^ set(l2) ^ set(l3))
# {'c', 'a', 'e'}

l_all = l1 + l2 + l3
print(l_all)
# ['a', 'b', 'c', 'b', 'c', 'd', 'c', 'd', 'e']

print(set(l_all))
# {'c', 'd', 'a', 'b', 'e'}

print([x for x in set(l_all) if l_all.count(x) == 1])
# ['a', 'e']

l1_dup = ['a', 'a', 'b', 'c']
l_dup_all = l1_dup + l2 + l3
print([x for x in set(l_dup_all) if l_dup_all.count(x) == 1])
# ['e']

l_unique_all = list(set(l1_dup)) + list(set(l2)) + list(set(l3))
print(l_unique_all)
# ['c', 'b', 'a', 'c', 'd', 'b', 'c', 'd', 'e']

print([x for x in set(l_unique_all) if l_unique_all.count(x) == 1])
# ['a', 'e']

l1 = ['a', 'b', 'c']
l2 = ['b', 'c', 'd']
l3 = ['c', 'd', 'e']

print(set(l1 + l2))
# {'c', 'd', 'b', 'a'}

print(set(l1 + l2 + l3))
# {'c', 'd', 'a', 'b', 'e'}
