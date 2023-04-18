print([1, 2, 3] < [1, 2, 100])
# True

print([1, 2, 3] < [1, 2, 0])
# False

print([1, 2] < [1, 2, 3])
# True

print([100] < [1, 2, 3])
# False

print(['a', 'b', 'c'] < ['a', 'b', 'x'])
# True

# print([100] < ['a'])
# TypeError: '<' not supported between instances of 'int' and 'str'

print([1, 2, 3] == [1, 2, 3])
# True

print([1, 2, 3] == [3, 2, 1])
# False

print([1, 2, 3] == [1, 2])
# False

print([1, 2, 3] == [True, 2.0, 3 + 0j])
# True

print([1, 2, 3] != [1, 2, 3])
# False

print([1, 2, 3] != [3, 2, 1])
# True

print([1, 2, 3] != [1, 2])
# True

print([1, 2, 3] != [True, 2.0, 3 + 0j])
# False

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 is l2)
# False

l1_assign = l1
print(l1_assign)
# [1, 2, 3]

print(l1 is l1_assign)
# True

def lists_match(l1, l2):
    if len(l1) != len(l2):
        return False
    return all(x == y and type(x) == type(y) for x, y in zip(l1, l2))

print(lists_match([1, 2, 3], [1, 2, 3]))
# True

print(lists_match([1, 2, 3], [1, 2]))
# False

print(lists_match([1, 2, 3], [True, 2.0, 3 + 0j]))
# False

l1 = [1, 2, 3]
l2 = [3, 4, 5]
l3 = [5, 6, 7]
print(not set(l1).isdisjoint(l2))
# True

print(not set(l1).isdisjoint(l3))
# False

l1 = [1, 2]
l2 = [1, 2, 3]
print(set(l1).issubset(l2))
# True

print(set(l2).issuperset(l2))
# True

l1 = [1, 2, 3, 4, 5]
l2 = [2, 3, 4]
print(list(set(l1) - set(l2)))
# [1, 5]

print((1, 2, 3) < (1, 2, 100))
# True

print((1, 2, 3) == (1, 2, 3))
# True

print(set((1, 2)).issubset((1, 2, 3)))
# True

l = [1, 2, 3]
t = (1, 2, 3)

# print(l <= t)
# TypeError: '<=' not supported between instances of 'list' and 'tuple'

print(l <= list(t))
# True

print(l == t)
# False

print(l == list(t))
# True
