d = {'k1': 1, 'k2': 2, 'k3': 3}

d.clear()
print(d)
# {}

d = {'k1': 1, 'k2': 2, 'k3': 3}

removed_value = d.pop('k1')
print(d)
# {'k2': 2, 'k3': 3}

print(removed_value)
# 1

d = {'k1': 1, 'k2': 2, 'k3': 3}

# removed_value = d.pop('k4')
# print(d)
# KeyError: 'k4'

d = {'k1': 1, 'k2': 2, 'k3': 3}

removed_value = d.pop('k4', None)
print(d)
# {'k1': 1, 'k2': 2, 'k3': 3}

print(removed_value)
# None

d = {'k1': 1, 'k2': 2}

k, v = d.popitem()
print(k)
print(v)
print(d)
# k2
# 2
# {'k1': 1}

k, v = d.popitem()
print(k)
print(v)
print(d)
# k1
# 1
# {}

# k, v = d.popitem()
# KeyError: 'popitem(): dictionary is empty'

d = {'k1': 1, 'k2': 2, 'k3': 3}

del d['k2']
print(d)
# {'k1': 1, 'k3': 3}

d = {'k1': 1, 'k2': 2, 'k3': 3}

del d['k1'], d['k3']
print(d)
# {'k2': 2}

d = {'k1': 1, 'k2': 2, 'k3': 3}

# del d['k4']
# print(d)
# KeyError: 'k4'
