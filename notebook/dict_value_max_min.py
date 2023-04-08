d = {'a': 100, 'b': 20, 'c': 50, 'd': 100, 'e': 80}

print(max(d))
# e

print(min(d))
# a

d = {'a': 100, 'b': 20, 'c': 50, 'd': 100, 'e': 80}

print(max(d.values()))
# 100

print(min(d.values()))
# 20

d = {'a': 100, 'b': 20, 'c': 50, 'd': 100, 'e': 80}

print(max(d, key=d.get))
# a

print(min(d, key=d.get))
# b

d = {'a': 100, 'b': 20, 'c': 50, 'd': 100, 'e': 80}

print(max(d.items(), key=lambda x: x[1]))
# ('a', 100)

print(min(d.items(), key=lambda x: x[1]))
# ('b', 20)

max_k, max_v = max(d.items(), key=lambda x: x[1])
print(max_k)
# a

print(max_v)
# 100

d = {'a': 100, 'b': 20, 'c': 50, 'd': 100, 'e': 80}

print([kv for kv in d.items() if kv[1] == max(d.values())])
# [('a', 100), ('d', 100)]

print([kv[0] for kv in d.items() if kv[1] == max(d.values())])
# ['a', 'd']

print([kv for kv in d.items() if kv[1] == min(d.values())])
# [('b', 20)]
