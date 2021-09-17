s = {1, 2, 2, 3, 1, 4}

print(s)
print(type(s))
# {1, 2, 3, 4}
# <class 'set'>

s = {1.23, 'abc', (0, 1, 2), 'abc'}

print(s)
# {(0, 1, 2), 1.23, 'abc'}

# s = {[0, 1, 2]}
# TypeError: unhashable type: 'list'

s = {100, 100.0}

print(s)
# {100}

s = {}

print(s)
print(type(s))
# {}
# <class 'dict'>

l = [1, 2, 2, 3, 1, 4]

print(l)
print(type(l))
# [1, 2, 2, 3, 1, 4]
# <class 'list'>

s_l = set(l)

print(s_l)
print(type(s_l))
# {1, 2, 3, 4}
# <class 'set'>

fs_l = frozenset(l)

print(fs_l)
print(type(fs_l))
# frozenset({1, 2, 3, 4})
# <class 'frozenset'>

s = set()

print(s)
print(type(s))
# set()
# <class 'set'>

l = [2, 2, 3, 1, 3, 4]

l_unique = list(set(l))
print(l_unique)
# [1, 2, 3, 4]

s = {i**2 for i in range(5)}

print(s)
# {0, 1, 4, 9, 16}

s = {1, 2, 2, 3, 1, 4}

print(s)
print(len(s))
# {1, 2, 3, 4}
# 4

s = {0, 1, 2}

s.add(3)
print(s)
# {0, 1, 2, 3}

s = {0, 1, 2}

s.discard(1)
print(s)
# {0, 2}

s = {0, 1, 2}

s.discard(10)
print(s)
# {0, 1, 2}

s = {0, 1, 2}

s.remove(1)
print(s)
# {0, 2}

# s = {0, 1, 2}

# s.remove(10)
# KeyError: 10

s = {2, 1, 0}

v = s.pop()

print(s)
print(v)
# {1, 2}
# 0

s = {2, 1, 0}

print(s.pop())
# 0

print(s.pop())
# 1

print(s.pop())
# 2

# print(s.pop())
# KeyError: 'pop from an empty set'

s = {0, 1, 2}

s.clear()
print(s)
# set()

s1 = {0, 1, 2}
s2 = {1, 2, 3}
s3 = {2, 3, 4}

s_union = s1 | s2
print(s_union)
# {0, 1, 2, 3}

s_union = s1.union(s2)
print(s_union)
# {0, 1, 2, 3}

s_union = s1.union(s2, s3)
print(s_union)
# {0, 1, 2, 3, 4}

s_union = s1.union(s2, [5, 6, 5, 7, 5])
print(s_union)
# {0, 1, 2, 3, 5, 6, 7}

s_intersection = s1 & s2
print(s_intersection)
# {1, 2}

s_intersection = s1.intersection(s2)
print(s_intersection)
# {1, 2}

s_intersection = s1.intersection(s2, s3)
print(s_intersection)
# {2}

s_difference = s1 - s2
print(s_difference)
# {0}

s_difference = s1.difference(s2)
print(s_difference)
# {0}

s_difference = s1.difference(s2, s3)
print(s_difference)
# {0}

s_symmetric_difference = s1 ^ s2
print(s_symmetric_difference)
# {0, 3}

s_symmetric_difference = s1.symmetric_difference(s2)
print(s_symmetric_difference)
# {0, 3}

s1 = {0, 1}
s2 = {0, 1, 2, 3}

print(s1 <= s2)
# True

print(s1.issubset(s2))
# True

print(s1 <= s1)
# True

print(s1.issubset(s1))
# True

print(s1 < s1)
# False

s1 = {0, 1}
s2 = {0, 1, 2, 3}

print(s2 >= s1)
# True

print(s2.issuperset(s1))
# True

print(s1 >= s1)
# True

print(s1.issuperset(s1))
# True

print(s1 > s1)
# False

s1 = {0, 1}
s2 = {1, 2}
s3 = {2, 3}

print(s1.isdisjoint(s2))
# False

print(s1.isdisjoint(s3))
# True
