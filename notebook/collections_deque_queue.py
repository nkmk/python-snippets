from collections import deque

d = deque(['a', 'b', 'c'])
print(d)
# deque(['a', 'b', 'c'])

d.append('d')
print(d)
# deque(['a', 'b', 'c', 'd'])

print(d.popleft())
# a

print(d)
# deque(['b', 'c', 'd'])
