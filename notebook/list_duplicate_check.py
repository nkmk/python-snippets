def has_duplicates(seq):
    return len(seq) != len(set(seq))

l = [0, 1, 2]
print(has_duplicates(l))
# False

l = [0, 1, 1, 2]
print(has_duplicates(l))
# True

l_2d = [[0, 1], [1, 1], [0, 1], [1, 0]]
# print(has_duplicates(l_2d))
# TypeError: unhashable type: 'list'

def has_duplicates2(seq):
    seen = []
    unique_list = [x for x in seq if x not in seen and not seen.append(x)]
    return len(seq) != len(unique_list)

l_2d = [[0, 0], [0, 1], [1, 1], [1, 0]]
print(has_duplicates2(l_2d))
# False

l_2d = [[0, 0], [0, 1], [1, 1], [1, 1]]
print(has_duplicates2(l_2d))
# True

l = [0, 1, 2]
print(has_duplicates2(l))
# False

l = [0, 1, 1, 2]
print(has_duplicates2(l))
# True

l_2d = [[0, 1], [2, 3]]
print(sum(l_2d, []))
# [0, 1, 2, 3]

print(has_duplicates(sum(l_2d, [])))
# False

l_2d = [[0, 1], [2, 0]]
print(has_duplicates(sum(l_2d, [])))
# True
