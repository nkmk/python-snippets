s = {3, 1, 2, 2, 3, 1, 4}
print(s)
# {1, 2, 3, 4}

print(type(s))
# <class 'set'>

s = {1.23, 'abc', (0, 1, 2)}
print(s)
# {(0, 1, 2), 1.23, 'abc'}

# s = {[0, 1, 2]}
# TypeError: unhashable type: 'list'

s = {1, 1.0, True}
print(s)
# {1}

s = {}
print(s)
# {}

print(type(s))
# <class 'dict'>

s = set()
print(s)
# set()

print(type(s))
# <class 'set'>

s = {i**2 for i in range(5)}
print(s)
# {0, 1, 4, 9, 16}

l = [2, 2, 3, 1, 3, 4]
print(set(l))
# {1, 2, 3, 4}

t = (2, 2, 3, 1, 3, 4)
print(set(t))
# {1, 2, 3, 4}

s = {1, 2, 3}

print(list(s))
# [1, 2, 3]

print(tuple(s))
# (1, 2, 3)

s = {0, 1, 2}

s.add(3)
print(s)
# {0, 1, 2, 3}

s = {0, 1, 2}

s.discard(1)
print(s)
# {0, 2}

s.discard(10)
print(s)
# {0, 2}

s = {0, 1, 2}

s.remove(1)
print(s)
# {0, 2}

# s.remove(10)
# KeyError: 10

s = {0, 1, 2}

v = s.pop()
print(v)
# 0

print(s)
# {1, 2}

s = set()

# v = s.pop()
# KeyError: 'pop from an empty set'

s = {0, 1, 2}

s.clear()
print(s)
# set()

s1 = {0, 1, 2}
s2 = {1, 2, 3}
s3 = {2, 3, 4}

print(s1 | s2)
# {0, 1, 2, 3}

print(s1.union(s2))
# {0, 1, 2, 3}

print(s1.union(s2, s3))
# {0, 1, 2, 3, 4}

print(s1.union(s2, [5, 6, 5, 7, 5]))
# {0, 1, 2, 3, 5, 6, 7}

s1 |= s2
print(s1)
# {0, 1, 2, 3}

s2.update(s3)
print(s2)
# {1, 2, 3, 4}

s1 = {0, 1, 2}
s2 = {1, 2, 3}
s3 = {2, 3, 4}

print(s1 & s2)
# {1, 2}

print(s1.intersection(s2))
# {1, 2}

print(s1.intersection(s2, s3))
# {2}

s1 &= s2
print(s1)
# {1, 2}

s2.intersection_update(s3)
print(s2)
# {2, 3}

s1 = {0, 1, 2}
s2 = {1, 2, 3}
s3 = {2, 3, 4}

print(s1 - s2)
# {0}

print(s1.difference(s2))
# {0}

print(s1.difference(s2, s3))
# {0}

s1 -= s2
print(s1)
# {0}

s2.difference_update(s3)
print(s2)
# {1}

s1 = {0, 1, 2}
s2 = {1, 2, 3}
s3 = {2, 3, 4}

print(s1 ^ s2)
# {0, 3}

print(s1.symmetric_difference(s2))
# {0, 3}

s1 ^= s2
print(s1)
# {0, 3}

s2.symmetric_difference_update(s3)
print(s2)
# {1, 4}

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
