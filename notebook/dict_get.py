d = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}

print(d['key1'])
# val1

# print(d['key4'])
# KeyError: 'key4'

d['key4'] = 'val4'
print(d)
# {'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'key4': 'val4'}

d = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}

print(d.get('key1'))
# val1

print(d.get('key4'))
# None

print(d.get('key4', 'NO KEY'))
# NO KEY

print(d.get('key4', 100))
# 100

print(d)
# {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}
