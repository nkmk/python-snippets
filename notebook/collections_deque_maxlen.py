from collections import deque

d = deque(['l', 'm', 'n'], 3)
print(d)
# deque(['l', 'm', 'n'], maxlen=3)

d.append('o')
print(d)
# deque(['m', 'n', 'o'], maxlen=3)

d.appendleft('l')
print(d)
# deque(['l', 'm', 'n'], maxlen=3)

d.extend(['o', 'p'])
print(d)
# deque(['n', 'o', 'p'], maxlen=3)

d.extendleft(['m', 'l'])
print(d)
# deque(['l', 'm', 'n'], maxlen=3)

# d.insert(0, 'XXX')
# IndexError: deque already at its maximum size

print(d.pop())
# n

print(d)
# deque(['l', 'm'], maxlen=3)

d.insert(1, 'XXX')
print(d)
# deque(['l', 'XXX', 'm'], maxlen=3)

print(d.maxlen)
# 3

# d.maxlen = 5
# AttributeError: attribute 'maxlen' of 'collections.deque' objects is not writable
