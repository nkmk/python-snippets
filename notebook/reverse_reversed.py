org_list = [3, 1, 4, 5, 2]

org_list.reverse()
print(org_list)
# [2, 5, 4, 1, 3]

print(org_list.reverse())
# None

org_list = [3, 1, 4, 5, 2]

reverse_iterator = reversed(org_list)
print(org_list)
# [3, 1, 4, 5, 2]

print(type(reverse_iterator))
# <class 'list_reverseiterator'>

for i in reversed(org_list):
    print(i)
# 2
# 5
# 4
# 1
# 3

new_list = list(reversed(org_list))
print(org_list)
print(new_list)
# [3, 1, 4, 5, 2]
# [2, 5, 4, 1, 3]

org_list = [3, 1, 4, 5, 2]

new_list = org_list[::-1]
print(org_list)
print(new_list)
# [3, 1, 4, 5, 2]
# [2, 5, 4, 1, 3]

org_str = 'cebad'

new_str_list = list(reversed(org_str))
print(new_str_list)
# ['d', 'a', 'b', 'e', 'c']

new_str = ''.join(list(reversed(org_str)))
print(new_str)
# dabec

new_str = org_str[::-1]
print(new_str)
# dabec

org_tuple = (3, 1, 4, 5, 2)

new_tuple = tuple(reversed(org_tuple))
print(new_tuple)
# (2, 5, 4, 1, 3)

new_tuple = org_tuple[::-1]
print(new_tuple)
# (2, 5, 4, 1, 3)
