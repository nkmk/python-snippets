# https://docs.python.jp/3/library/stdtypes.html#mapping-types-dict

d = {'one': 1, 'two': 2, 'three': 3}

print(d)
print(d.keys())
print(d.values())
print(d.items())
# {'one': 1, 'two': 2, 'three': 3}
# dict_keys(['one', 'two', 'three'])
# dict_values([1, 2, 3])
# dict_items([('one', 1), ('two', 2), ('three', 3)])

print(d.get('one'))
# 1

print(d.get('four'))
# None

print(d.get('five', 'default_value'))
# default_value

print(d)
# {'one': 1, 'two': 2, 'three': 3}

print(d.setdefault('one'))
# 1

print(d.setdefault('four'))
print(d)
# None
# {'one': 1, 'two': 2, 'three': 3, 'four': None}

print(d.setdefault('five', 'default_value'))
print(d)
# default_value
# {'one': 1, 'two': 2, 'three': 3, 'four': None, 'five': 'default_value'}
