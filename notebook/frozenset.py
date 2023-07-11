fs = frozenset([2, 2, 3, 1, 3, 4])
print(fs)
# frozenset({1, 2, 3, 4})

print(type(fs))
# <class 'frozenset'>

# fs.add(5)
# AttributeError: 'frozenset' object has no attribute 'add'

# fs.discard(1)
# AttributeError: 'frozenset' object has no attribute 'discard'

fs1 = frozenset([0, 1, 2])
fs2 = frozenset([1, 2, 3])

print(fs1 | fs2)
# frozenset({0, 1, 2, 3})

print(fs1.difference(fs2))
# frozenset({0})

print(fs1.isdisjoint(fs2))
# False

s = {0, 1, 2}
fs = frozenset([0, 1, 2])

# d = {s: 100}
# TypeError: unhashable type: 'set'

d = {fs: 100}
print(d)
# {frozenset({0, 1, 2}): 100}

# ss = {s}
# TypeError: unhashable type: 'set'

ss = {fs}
print(ss)
# {frozenset({0, 1, 2})}
