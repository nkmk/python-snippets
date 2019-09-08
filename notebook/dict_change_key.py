d = {'k1': 1, 'k2': 2, 'k3': 3}

d['k10'] = d['k1']
del d['k1']

print(d)
# {'k2': 2, 'k3': 3, 'k10': 1}

d = {'k1': 1, 'k2': 2, 'k3': 3}

print(d.pop('k1'))
# 1

print(d)
# {'k2': 2, 'k3': 3}

d = {'k1': 1, 'k2': 2, 'k3': 3}

d['k10'] = d.pop('k1')

print(d)
# {'k2': 2, 'k3': 3, 'k10': 1}

d = {'k1': 1, 'k2': 2, 'k3': 3}

# print(d.pop('k10'))
# KeyError: 'k10'

print(d.pop('k10', None))
# None

print(d)
# {'k1': 1, 'k2': 2, 'k3': 3}

def change_dict_key(d, old_key, new_key, default_value=None):
    d[new_key] = d.pop(old_key, default_value)

d = {'k1': 1, 'k2': 2, 'k3': 3}
change_dict_key(d, 'k1', 'k10')
print(d)
# {'k2': 2, 'k3': 3, 'k10': 1}

d = {'k1': 1, 'k2': 2, 'k3': 3}
change_dict_key(d, 'k10', 'k100')
print(d)
# {'k1': 1, 'k2': 2, 'k3': 3, 'k100': None}

d = {'k1': 1, 'k2': 2, 'k3': 3}
change_dict_key(d, 'k10', 'k100', 100)
print(d)
# {'k1': 1, 'k2': 2, 'k3': 3, 'k100': 100}

d = {'k1': 1, 'k2': 2, 'k3': 3}
change_dict_key(d, 'k1', 'k2')
print(d)
# {'k2': 1, 'k3': 3}

def change_dict_key_setdefault(d, old_key, new_key, default_value=None):
    d.setdefault(new_key, d.pop(old_key, default_value))

d = {'k1': 1, 'k2': 2, 'k3': 3}
change_dict_key_setdefault(d, 'k1', 'k2')
print(d)
# {'k2': 2, 'k3': 3}

d = {'k1': 1, 'k2': 2, 'k3': 3}
change_dict_key_setdefault(d, 'k1', 'k10')
print(d)
# {'k2': 2, 'k3': 3, 'k10': 1}

d = {'k1': 1, 'k2': 2, 'k3': 3}
change_dict_key_setdefault(d, 'k10', 'k100')
print(d)
# {'k1': 1, 'k2': 2, 'k3': 3, 'k100': None}

def change_dict_key_exist(d, old_key, new_key):
    if old_key in d:
        d[new_key] = d.pop(old_key)

d = {'k1': 1, 'k2': 2, 'k3': 3}
change_dict_key_exist(d, 'k1', 'k10')
print(d)
# {'k2': 2, 'k3': 3, 'k10': 1}

d = {'k1': 1, 'k2': 2, 'k3': 3}
change_dict_key_exist(d, 'k10', 'k100')
print(d)
# {'k1': 1, 'k2': 2, 'k3': 3}

d = {'k1': 1, 'k2': 2, 'k3': 3}
change_dict_key_exist(d, 'k1', 'k2')
print(d)
# {'k2': 1, 'k3': 3}

def change_dict_key_exist_setdefault(d, old_key, new_key):
    if old_key in d:
        d.setdefault(new_key, d.pop(old_key))

d = {'k1': 1, 'k2': 2, 'k3': 3}
change_dict_key_exist_setdefault(d, 'k1', 'k2')
print(d)
# {'k2': 2, 'k3': 3}
