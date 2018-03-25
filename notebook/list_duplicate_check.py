def is_unique(seq):
    return len(seq) == len(set(seq))

l = [0, 'two', 1, 'two', 0]

print(is_unique(l))
# False

l = [0, 'one', 2]

print(is_unique(l))
# True

# l_2d = [[0, 1], [1, 1], [0, 1], [1, 0]]
# print(is_unique(l_2d))
# TypeError: unhashable type: 'list'

def is_unique2(seq):
    seen = []
    unique_list = [x for x in seq if x not in seen and not seen.append(x)]
    return len(seq) == len(unique_list)

l_2d = [[0, 1], [1, 1], [0, 1], [1, 0]]

print(is_unique2(l_2d))
# False

l_2d = [[0, 1], [1, 1], [1, 0]]

print(is_unique2(l_2d))
# True

l = [0, 'two', 1, 'two', 0]

print(is_unique2(l))
# False

l = [0, 'one', 2]

print(is_unique2(l))
# True

l = [[0, 1, 2], 'string', 100, [0, 1, 2]]

print(is_unique2(l))
# False

l = [[0, 1, 2], 'string', 100]

print(is_unique2(l))
# True
