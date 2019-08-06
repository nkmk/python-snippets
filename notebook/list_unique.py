l = [3, 3, 2, 1, 5, 1, 4, 2, 3]

print(set(l))
# {1, 2, 3, 4, 5}

print(list(set(l)))
# [1, 2, 3, 4, 5]

print(dict.fromkeys(l))
# {3: None, 2: None, 1: None, 5: None, 4: None}

print(list(dict.fromkeys(l)))
# [3, 2, 1, 5, 4]

print(sorted(set(l), key=l.index))
# [3, 2, 1, 5, 4]

l_2d = [[1, 1], [0, 1], [0, 1], [0, 0], [1, 0], [1, 1], [1, 1]]

# l_2d_unique = list(set(l_2d))
# TypeError: unhashable type: 'list'

# l_2d_unique_order = dict.fromkeys(l_2d)
# TypeError: unhashable type: 'list'

def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]

print(get_unique_list(l_2d))
# [[1, 1], [0, 1], [0, 0], [1, 0]]

print(get_unique_list(l))
# [3, 2, 1, 5, 4]

print([x for x in set(l) if l.count(x) > 1])
# [1, 2, 3]

print([x for x in dict.fromkeys(l) if l.count(x) > 1])
# [3, 2, 1]

print(sorted([x for x in set(l) if l.count(x) > 1], key=l.index))
# [3, 2, 1]

print([x for x in l if l.count(x) > 1])
# [3, 3, 2, 1, 1, 2, 3]

def get_duplicate_list(seq):
    seen = []
    return [x for x in seq if not seen.append(x) and seen.count(x) == 2]

def get_duplicate_list_order(seq):
    seen = []
    return [x for x in seq if seq.count(x) > 1 and not seen.append(x) and seen.count(x) == 1]

print(get_duplicate_list(l_2d))
# [[0, 1], [1, 1]]

print(get_duplicate_list_order(l_2d))
# [[1, 1], [0, 1]]

print(get_duplicate_list(l))
# [3, 1, 2]

print(get_duplicate_list_order(l))
# [3, 2, 1]

print([x for x in l_2d if l_2d.count(x) > 1])
# [[1, 1], [0, 1], [0, 1], [1, 1], [1, 1]]
