d = {'key1': 1, 'key2': 2, 'key3': 3}

for k in d:
    print(k)
# key1
# key2
# key3

print(list(d))
# ['key1', 'key2', 'key3']

print(type(list(d)))
# <class 'list'>

for k in d.keys():
    print(k)
# key1
# key2
# key3

print(d.keys())
# dict_keys(['key1', 'key2', 'key3'])

print(type(d.keys()))
# <class 'dict_keys'>

print(list(d.keys()))
# ['key1', 'key2', 'key3']

print(type(list(d.keys())))
# <class 'list'>

for v in d.values():
    print(v)
# 1
# 2
# 3

print(d.values())
# dict_values([1, 2, 3])

print(type(d.values()))
# <class 'dict_values'>

print(list(d.values()))
# [1, 2, 3]

print(type(list(d.values())))
# <class 'list'>

for k, v in d.items():
    print(k, v)
# key1 1
# key2 2
# key3 3

for t in d.items():
    print(t)
    print(type(t))
    print(t[0])
    print(t[1])
    print('---')
# ('key1', 1)
# <class 'tuple'>
# key1
# 1
# ---
# ('key2', 2)
# <class 'tuple'>
# key2
# 2
# ---
# ('key3', 3)
# <class 'tuple'>
# key3
# 3
# ---

print(d.items())
# dict_items([('key1', 1), ('key2', 2), ('key3', 3)])

print(type(d.items()))
# <class 'dict_items'>

print(list(d.items()))
# [('key1', 1), ('key2', 2), ('key3', 3)]

print(type(list(d.items())))
# <class 'list'>

print(type(list(d.items())[0]))
# <class 'tuple'>
