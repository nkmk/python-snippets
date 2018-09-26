org_list = [1, 2, 3, 4, 5]

org_list.reverse()
print(org_list)
# [5, 4, 3, 2, 1]

print(org_list.reverse())
# None

org_list = [1, 2, 3, 4, 5]

reverse_iterator = reversed(org_list)
print(org_list)
# [1, 2, 3, 4, 5]

print(type(reverse_iterator))
# <class 'list_reverseiterator'>

for i in reversed(org_list):
    print(i)
# 5
# 4
# 3
# 2
# 1

new_list = list(reversed(org_list))
print(org_list)
print(new_list)
# [1, 2, 3, 4, 5]
# [5, 4, 3, 2, 1]

org_list = [1, 2, 3, 4, 5]

new_list = org_list[::-1]
print(org_list)
print(new_list)
# [1, 2, 3, 4, 5]
# [5, 4, 3, 2, 1]

org_str = 'abcde'

new_str_list = list(reversed(org_str))
print(new_str_list)
# ['e', 'd', 'c', 'b', 'a']

new_str = ''.join(list(reversed(org_str)))
print(new_str)
# edcba

new_str = org_str[::-1]
print(new_str)
# edcba

org_tuple = (1, 2, 3, 4, 5)

new_tuple = tuple(reversed(org_tuple))
print(new_tuple)
# (5, 4, 3, 2, 1)

new_tuple = org_tuple[::-1]
print(new_tuple)
# (5, 4, 3, 2, 1)
