d = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}

print('key1' in d)
# True

print('val1' in d)
# False

print('key4' not in d)
# True

print(d['key1'])
# val1

# print(d['key4'])
# KeyError: 'key4'

print(d.get('key4'))
# None

d = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}

print('val1' in d.values())
# True

print('val4' in d.values())
# False

print('val4' not in d.values())
# True

d = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}

print(('key1', 'val1') in d.items())
# True

print(('key1', 'val2') in d.items())
# False

print(('key1', 'val2') not in d.items())
# True
