d = {'key1': 'aaa', 'key2': 'aaa', 'key3': 'bbb'}

value = d['key1']
print(value)
# aaa

keys = [k for k, v in d.items() if v == 'aaa']
print(keys)
# ['key1', 'key2']

keys = [k for k, v in d.items() if v == 'bbb']
print(keys)
# ['key3']

keys = [k for k, v in d.items() if v == 'xxx']
print(keys)
# []

key = [k for k, v in d.items() if v == 'aaa'][0]
print(key)
# key1

key = [k for k, v in d.items() if v == 'bbb'][0]
print(key)
# key3

# key = [k for k, v in d.items() if v == 'xxx'][0]
# print(key)
# IndexError: list index out of range

def get_keys_from_value(d, val):
    return [k for k, v in d.items() if v == val]

keys = get_keys_from_value(d, 'aaa')
print(keys)
# ['key1', 'key2']

def get_key_from_value(d, val):
    keys = [k for k, v in d.items() if v == val]
    if keys:
        return keys[0]
    return None

key = get_key_from_value(d, 'aaa')
print(key)
# key1

key = get_key_from_value(d, 'bbb')
print(key)
# key3

key = get_key_from_value(d, 'xxx')
print(key)
# None

d_num = {'key1': 1, 'key2': 2, 'key3': 3}

keys = [k for k, v in d_num.items() if v >= 2]
print(keys)
# ['key2', 'key3']

keys = [k for k, v in d_num.items() if v % 2 == 1]
print(keys)
# ['key1', 'key3']

d_str = {'key1': 'aaa@xxx.com', 'key2': 'bbb@yyy.net', 'key3': 'ccc@zzz.com'}

keys = [k for k, v in d_str.items() if v.endswith('com')]
print(keys)
# ['key1', 'key3']
