d = {'key1': 1, 'key2': 2, 'key3': 3}

for k in d:
    print(k)
# key1
# key2
# key3

for k in d.keys():
    print(k)
# key1
# key2
# key3

keys = d.keys()
print(keys)
print(type(keys))
# dict_keys(['key1', 'key2', 'key3'])
# <class 'dict_keys'>

k_list = list(d.keys())
print(k_list)
print(type(k_list))
# ['key1', 'key2', 'key3']
# <class 'list'>

for v in d.values():
    print(v)
# 1
# 2
# 3

values = d.values()
print(values)
print(type(values))
# dict_values([1, 2, 3])
# <class 'dict_values'>

v_list = list(d.values())
print(v_list)
print(type(v_list))
# [1, 2, 3]
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

items = d.items()
print(items)
print(type(items))
# dict_items([('key1', 1), ('key2', 2), ('key3', 3)])
# <class 'dict_items'>

i_list = list(d.items())
print(i_list)
print(type(i_list))
# [('key1', 1), ('key2', 2), ('key3', 3)]
# <class 'list'>

print(i_list[0])
print(type(i_list[0]))
# ('key1', 1)
# <class 'tuple'>
