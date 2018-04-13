d = {'k1': 1, 'k2': 2, 'k3': 3}
print(d)
# {'k1': 1, 'k2': 2, 'k3': 3}

d = {'k1': 1, 'k2': 2, 'k3': 3, 'k3': 300}
print(d)
# {'k1': 1, 'k2': 2, 'k3': 300}

d = dict(k1=1, k2=2, k3=3)
print(d)
# {'k1': 1, 'k2': 2, 'k3': 3}

d = dict([('k1', 1), ('k2', 2), ('k3', 4)])
print(d)
# {'k1': 1, 'k2': 2, 'k3': 4}

d = dict((['k1', 1], ['k2', 2], ['k3', 4]))
print(d)
# {'k1': 1, 'k2': 2, 'k3': 4}

d = dict([{'k1', 1}, {'k2', 2}, {'k3', 4}])
print(d)
# {1: 'k1', 2: 'k2', 'k3': 4}

keys = ['k1', 'k2', 'k3']
values = [1, 2, 3]

d = dict(zip(keys, values))
print(d)
# {'k1': 1, 'k2': 2, 'k3': 3}

d_other = {'k10': 10, 'k100': 100}

d = dict(d_other)
print(d)
# {'k10': 10, 'k100': 100}

print(d == d_other)
# True

print(d is d_other)
# False
