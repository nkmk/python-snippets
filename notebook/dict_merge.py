d1 = {'k1': 1, 'k2': 2}
d2 = {'k3': 3, 'k4': 4}

d = dict(**d1, **d2)
print(d)
# {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4}

d = {**d1, **d2}
print(d)
# {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4}

d1 = {'k1': 1, 'k2': 2}
d2 = {'k1': 100, 'k3': 3, 'k4': 4}

# d = dict(**d1, **d2)
# TypeError: dict() got multiple values for keyword argument 'k1'

d = {**d1, **d2}
print(d)
# {'k1': 100, 'k2': 2, 'k3': 3, 'k4': 4}

d1 = {'k1': 1, 'k2': 2}
d2 = {'k1': 100, 'k3': 3, 'k4': 4}

d = d1 | d2
print(d)
# {'k1': 100, 'k2': 2, 'k3': 3, 'k4': 4}

d = d2 | d1
print(d)
# {'k1': 1, 'k3': 3, 'k4': 4, 'k2': 2}

d1 = {'k1': 1, 'k2': 2}
d2 = {'k1': 100, 'k3': 3, 'k4': 4}
d3 = {'k5': 5, 'k6': 6}

d = d1 | d2 | d3
print(d)
# {'k1': 100, 'k2': 2, 'k3': 3, 'k4': 4, 'k5': 5, 'k6': 6}

d1 = {'k1': 1, 'k2': 2}
d2 = {'k1': 100, 'k3': 3, 'k4': 4}

d1 |= d2
print(d1)
# {'k1': 100, 'k2': 2, 'k3': 3, 'k4': 4}

d = {'k1': 1, 'k2': 2}

d |= [('k1', 100), ('k3', 3), ('k4', 4)]
print(d)
# {'k1': 100, 'k2': 2, 'k3': 3, 'k4': 4}

# d | [('k1', 100), ('k3', 3), ('k4', 4)]
# TypeError: unsupported operand type(s) for |: 'dict' and 'list'
