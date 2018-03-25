l = [3, 3, 2, 1, 5, 1, 4, 2, 3]

l_unique = list(set(l))

print(l_unique)
# [1, 2, 3, 4, 5]

print(dict.fromkeys(l))
# {3: None, 2: None, 1: None, 5: None, 4: None}

l_unique_order = list(dict.fromkeys(l))

print(l_unique_order)
# [3, 2, 1, 5, 4]

l_unique_order = sorted(set(l), key=l.index)

print(l_unique_order)
# [3, 2, 1, 5, 4]

l_2d = [[0], [2], [2], [1], [0], [0]]

print(l_2d)
# [[0], [2], [2], [1], [0], [0]]

# l_2d_unique = list(set(l_2d))
# TypeError: unhashable type: 'list'

# l_2d_unique_order = dict.fromkeys(l_2d)
# TypeError: unhashable type: 'list'

def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]

l_2d_unique = get_unique_list(l_2d)

print(l_2d_unique)
# [[0], [2], [1]]

l_unique = get_unique_list(l)

print(l_unique)
# [3, 2, 1, 5, 4]

l = [3, 3, 2, 1, 5, 1, 4, 2, 3]

l_duplicate = [x for x in set(l) if l.count(x) > 1]

print(l_duplicate)
# [1, 2, 3]

l_duplicate_order = [x for x in dict.fromkeys(l) if l.count(x) > 1]

print(l_duplicate_order)
# [3, 2, 1]

l_duplicate_order = sorted([x for x in set(l) if l.count(x) > 1], key=l.index)

print(l_duplicate_order)
# [3, 2, 1]

l_2d = [[0], [2], [2], [1], [0], [0]]

print(l_2d)
# [[0], [2], [2], [1], [0], [0]]

def get_duplicate_list(seq):
    seen = []
    return [x for x in seq if not seen.append(x) and seen.count(x) == 2]

def get_duplicate_list_order(seq):
    seen = []
    return [x for x in seq if seq.count(x) > 1 and not seen.append(x) and seen.count(x) == 1]

l_2d_duplicate = get_duplicate_list(l_2d)

print(l_2d_duplicate)
# [[2], [0]]

l_2d_duplicate_order = get_duplicate_list_order(l_2d)

print(l_2d_duplicate_order)
# [[0], [2]]

l_duplicate = get_duplicate_list(l)

print(l_duplicate)
# [3, 1, 2]

l_duplicate_order = get_duplicate_list_order(l)

print(l_duplicate_order)
# [3, 2, 1]
