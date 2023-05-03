l = [0, 1, 2]

l.clear()
print(l)
# []

l = [0, 10, 20, 30, 40, 50]

popped_item = l.pop(0)
print(popped_item)
# 0

print(l)
# [10, 20, 30, 40, 50]

popped_item = l.pop(3)
print(popped_item)
# 40

print(l)
# [10, 20, 30, 50]

popped_item = l.pop(-2)
print(popped_item)
# 30

print(l)
# [10, 20, 50]

popped_item = l.pop()
print(popped_item)
# 50

print(l)
# [10, 20]

# popped_item = l.pop(100)
# IndexError: pop index out of range

l = ['Alice', 'Bob', 'Charlie', 'Bob', 'Dave']

l.remove('Alice')
print(l)
# ['Bob', 'Charlie', 'Bob', 'Dave']

l.remove('Bob')
print(l)
# ['Charlie', 'Bob', 'Dave']

# l.remove('xxx')
# ValueError: list.remove(x): x not in list

l = [0, 10, 20, 30, 40, 50]

del l[0]
print(l)
# [10, 20, 30, 40, 50]

del l[3]
print(l)
# [10, 20, 30, 50]

del l[-1]
print(l)
# [10, 20, 30]

del l[-2]
print(l)
# [10, 30]

l = [0, 10, 20, 30, 40, 50]
del l[2:5]
print(l)
# [0, 10, 50]

l = [0, 10, 20, 30, 40, 50]
del l[:3]
print(l)
# [30, 40, 50]

l = [0, 10, 20, 30, 40, 50]
del l[-2:]
print(l)
# [0, 10, 20, 30]

l = [0, 10, 20, 30, 40, 50]
del l[:]
print(l)
# []

l = [0, 10, 20, 30, 40, 50]
del l[::2]
print(l)
# [10, 30, 50]

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = [i for i in l if i % 2 == 0]
print(evens)
# [0, 2, 4, 6, 8]

odds = [i for i in l if i % 2 != 0]
print(odds)
# [1, 3, 5, 7, 9]

print(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

l = ['Alice', 'Bob', 'Charlie', 'Bob', 'David']
print(l)
# ['Alice', 'Bob', 'Charlie', 'Bob', 'David']

print([s for s in l if s != 'Bob'])
# ['Alice', 'Charlie', 'David']

print([s for s in l if s.endswith('e')])
# ['Alice', 'Charlie']

print(list(set(l)))
# ['Alice', 'Charlie', 'David', 'Bob']
