l1 = ['a', 'b', 'c']
l2 = ['b', 'c', 'd']
l3 = ['c', 'd', 'e']

l1_l2_and = set(l1) & set(l2)
print(l1_l2_and)
# {'b', 'c'}

print(type(l1_l2_and))
# <class 'set'>

l1_l2_and_list = list(l1_l2_and)
print(l1_l2_and_list)
# ['b', 'c']

print(type(l1_l2_and_list))
# <class 'list'>

print(len(l1_l2_and))
# 2

l1_l2_l3_and = set(l1) & set(l2) & set(l3)
print(l1_l2_l3_and)
# {'c'}

l1_l2_sym_diff = set(l1) ^ set(l2)
print(l1_l2_sym_diff)
# {'d', 'a'}

print(list(l1_l2_sym_diff))
# ['d', 'a']

print(len(l1_l2_sym_diff))
# 2

l1_l2_l3_sym_diff = set(l1) ^ set(l2) ^ set(l3)
print(l1_l2_l3_sym_diff)
# {'e', 'c', 'a'}

l_all = l1 + l2 + l3
print(l_all)
# ['a', 'b', 'c', 'b', 'c', 'd', 'c', 'd', 'e']

l_all_only = [x for x in l_all if l_all.count(x) == 1]
print(l_all_only)
# ['a', 'e']

l1_duplicate = ['a', 'a', 'b', 'c'] 

l_duplicate_all = l1_duplicate + l2 + l3
l_duplicate_all_only = [x for x in l_duplicate_all if l_duplicate_all.count(x) == 1]
print(l_duplicate_all_only)
# ['e']

l_unique_all = list(set(l1_duplicate)) + list(set(l2)) + list(set(l3))
print(l_unique_all)
# ['b', 'c', 'a', 'd', 'b', 'c', 'd', 'e', 'c']

l_uniaues_all_only = [x for x in l_unique_all if l_unique_all.count(x) == 1]
print(l_uniaues_all_only)
# ['a', 'e']

l1_l2_or = set(l1 + l2)
print(l1_l2_or)
# {'d', 'b', 'c', 'a'}

print(list(l1_l2_or))
# ['d', 'b', 'c', 'a']

print(len(l1_l2_or))
# 4

l1_l2_l3_or = set(l1 + l2 + l3)
print(l1_l2_l3_or)
# {'a', 'c', 'b', 'd', 'e'}
