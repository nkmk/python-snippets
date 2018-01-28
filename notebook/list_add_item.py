l = list(range(3))
print(l)
# [0, 1, 2]

l.append(100)
print(l)
# [0, 1, 2, 100]

l.append('new')
print(l)
# [0, 1, 2, 100, 'new']

l.append([3, 4, 5])
print(l)
# [0, 1, 2, 100, 'new', [3, 4, 5]]

l = list(range(3))
print(l)
# [0, 1, 2]

l.extend([100, 101, 102])
print(l)
# [0, 1, 2, 100, 101, 102]

l.extend((-1, -2, -3))
print(l)
# [0, 1, 2, 100, 101, 102, -1, -2, -3]

l.extend('new')
print(l)
# [0, 1, 2, 100, 101, 102, -1, -2, -3, 'n', 'e', 'w']

l2 = l + [5, 6, 7]
print(l2)
# [0, 1, 2, 100, 101, 102, -1, -2, -3, 'n', 'e', 'w', 5, 6, 7]

l += [5, 6, 7]
print(l)
# [0, 1, 2, 100, 101, 102, -1, -2, -3, 'n', 'e', 'w', 5, 6, 7]

l = list(range(3))
print(l)
# [0, 1, 2]

l.insert(0, 100)
print(l)
# [100, 0, 1, 2]

l.insert(-1, 200)
print(l)
# [100, 0, 1, 200, 2]

l.insert(0, [-1, -2, -3])
print(l)
# [[-1, -2, -3], 100, 0, 1, 200, 2]

l = list(range(3))
print(l)
# [0, 1, 2]

l[1:1] = [100, 200, 300]
print(l)
# [0, 100, 200, 300, 1, 2]

l = list(range(3))
print(l)
# [0, 1, 2]

l[1:2] = [100, 200, 300]
print(l)
# [0, 100, 200, 300, 2]
