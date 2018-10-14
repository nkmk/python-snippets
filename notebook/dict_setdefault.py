d = {'k1': 1, 'k2': 2}

d.setdefault('k3', 3)
print(d)
# {'k1': 1, 'k2': 2, 'k3': 3}

d.setdefault('k4')
print(d)
# {'k1': 1, 'k2': 2, 'k3': 3, 'k4': None}

d.setdefault('k1', 100)
print(d)
# {'k1': 1, 'k2': 2, 'k3': 3, 'k4': None}

print(d.setdefault('k5', 5))
# 5

print(d)
# {'k1': 1, 'k2': 2, 'k3': 3, 'k4': None, 'k5': 5}

print(d.setdefault('k6'))
# None

print(d)
# {'k1': 1, 'k2': 2, 'k3': 3, 'k4': None, 'k5': 5, 'k6': None}

print(d.setdefault('k1', 100))
# 1

print(d.setdefault('k1', -100))
# 1

print(d.setdefault('k1'))
# 1

print(d)
# {'k1': 1, 'k2': 2, 'k3': 3, 'k4': None, 'k5': 5, 'k6': None}
