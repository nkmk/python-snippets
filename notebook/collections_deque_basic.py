from collections import deque

d = deque()
print(d)
# deque([])

print(type(d))
# <class 'collections.deque'>

d = deque(['m', 'n'])
print(d)
# deque(['m', 'n'])

d.append('o')
print(d)
# deque(['m', 'n', 'o'])

d.appendleft('l')
print(d)
# deque(['l', 'm', 'n', 'o'])

d.extend(['p', 'q'])
print(d)
# deque(['l', 'm', 'n', 'o', 'p', 'q'])

d.extendleft(['k', 'j'])
print(d)
# deque(['j', 'k', 'l', 'm', 'n', 'o', 'p', 'q'])

d.insert(3, 'XXX')
print(d)
# deque(['j', 'k', 'l', 'XXX', 'm', 'n', 'o', 'p', 'q'])

d.insert(-1, 'YYY')
print(d)
# deque(['j', 'k', 'l', 'XXX', 'm', 'n', 'o', 'p', 'YYY', 'q'])

d.insert(100, 'ZZZ')
print(d)
# deque(['j', 'k', 'l', 'XXX', 'm', 'n', 'o', 'p', 'YYY', 'q', 'ZZZ'])

d.insert(-100, 'XYZ')
print(d)
# deque(['XYZ', 'j', 'k', 'l', 'XXX', 'm', 'n', 'o', 'p', 'YYY', 'q', 'ZZZ'])

d = deque(['a', 'b', 'c', 'b', 'd'])
print(d)
# deque(['a', 'b', 'c', 'b', 'd'])

print(d.pop())
# d

print(d)
# deque(['a', 'b', 'c', 'b'])

print(d.popleft())
# a

print(d)
# deque(['b', 'c', 'b'])

d.remove('b')
print(d)
# deque(['c', 'b'])

# d.remove('X')
# ValueError: deque.remove(x): x not in deque

d.clear()
print(d)
# deque([])

# d.pop()
# IndexError: pop from an empty deque

# d.popleft()
# IndexError: pop from an empty deque

d.clear()
print(d)
# deque([])

d = deque(['a', 'b', 'c', 'd', 'e'])
print(d)
# deque(['a', 'b', 'c', 'd', 'e'])

d.rotate()
print(d)
# deque(['e', 'a', 'b', 'c', 'd'])

d = deque(['a', 'b', 'c', 'd', 'e'])
d.rotate(2)
print(d)
# deque(['d', 'e', 'a', 'b', 'c'])

d = deque(['a', 'b', 'c', 'd', 'e'])
d.rotate(-1)
print(d)
# deque(['b', 'c', 'd', 'e', 'a'])

d = deque(['a', 'b', 'c', 'd', 'e'])
d.rotate(6)
print(d)
# deque(['e', 'a', 'b', 'c', 'd'])

d = deque(['a', 'b', 'c', 'c', 'd'])
print(d[0])
# a

print(d[-1])
# d

d[2] = 'X'
print(d)
# deque(['a', 'b', 'X', 'c', 'd'])

# print(d[2:4])
# TypeError: sequence index must be integer, not 'slice'

print(d.index('c'))
# 3

# print(d.index('x'))
# ValueError: 'x' is not in deque

d = deque(['a', 'a', 'b', 'c'])

print(len(d))
# 4

print(d.count('a'))
# 2

print(d.count('x'))
# 0

print('b' in d)
# True

print('x' in d)
# False

d = deque(['a', 'b', 'c', 'd', 'e'])
d.reverse()
print(d)
# deque(['e', 'd', 'c', 'b', 'a'])

d = deque(['a', 'b', 'c', 'd', 'e'])
print(deque(reversed(d)))
# deque(['e', 'd', 'c', 'b', 'a'])

d = deque(['a', 'b', 'c'])

for v in d:
    print(v)
# a
# b
# c

d = deque(['a', 'b', 'c'])

l = list(d)
print(l)
# ['a', 'b', 'c']

print(type(l))
# <class 'list'>
