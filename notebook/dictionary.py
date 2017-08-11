d = {'one': 1, 'two': 2, 'three': 3}

print(d.keys())
print(d.values())
print(d.items())
# dict_keys(['one', 'two', 'three'])
# dict_values([1, 2, 3])
# dict_items([('one', 1), ('two', 2), ('three', 3)])

print(d.get('one'))
print(d.get('four'))
print(d.get('five', 'nothing'))
# 1
# None
# nothing

print(d.setdefault('one'))
print(d.setdefault('four'))
print(d)
print(d.setdefault('five', 'nothing'))
print(d)
# 1
# None
# {'one': 1, 'two': 2, 'three': 3, 'four': None}
# nothing
# {'one': 1, 'two': 2, 'three': 3, 'four': None, 'five': 'nothing'}
