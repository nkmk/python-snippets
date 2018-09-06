org_list = [3, 1, 4, 5, 2]

org_list.sort()
print(org_list)
# [1, 2, 3, 4, 5]

print(org_list.sort())
# None

org_list.sort(reverse=True)
print(org_list)
# [5, 4, 3, 2, 1]

org_list = [3, 1, 4, 5, 2]

new_list = sorted(org_list)
print(org_list)
print(new_list)
# [3, 1, 4, 5, 2]
# [1, 2, 3, 4, 5]

new_list_reverse = sorted(org_list, reverse=True)
print(org_list)
print(new_list_reverse)
# [3, 1, 4, 5, 2]
# [5, 4, 3, 2, 1]

org_str = 'cebad'

new_str_list = sorted(org_str)
print(org_str)
print(new_str_list)
# cebad
# ['a', 'b', 'c', 'd', 'e']

new_str = ''.join(new_str_list)
print(new_str)
# abcde

new_str = ''.join(sorted(org_str))
print(new_str)
# abcde

new_str_reverse = ''.join(sorted(org_str, reverse=True))
print(new_str_reverse)
# edcba

org_tuple = (3, 1, 4, 5, 2)

new_tuple_list = sorted(org_tuple)
print(org_tuple)
print(new_tuple_list)
# (3, 1, 4, 5, 2)
# [1, 2, 3, 4, 5]

new_tuple = tuple(new_tuple_list)
print(new_tuple)
# (1, 2, 3, 4, 5)

new_tuple = tuple(sorted(new_tuple_list))
print(new_tuple)
# (1, 2, 3, 4, 5)

new_tuple_reverse = tuple(sorted(new_tuple_list, reverse=True))
print(new_tuple_reverse)
# (5, 4, 3, 2, 1)
