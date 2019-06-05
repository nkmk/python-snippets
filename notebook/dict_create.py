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

l = ['Alice', 'Bob', 'Charlie']

d = {s: len(s) for s in l}
print(d)
# {'Alice': 5, 'Bob': 3, 'Charlie': 7}

keys = ['k1', 'k2', 'k3']
values = [1, 2, 3]

d = {k: v for k, v in zip(keys, values)}
print(d)
# {'k1': 1, 'k2': 2, 'k3': 3}

d = {k: v for k, v in zip(keys, values) if v % 2 == 1}
print(d)
# {'k1': 1, 'k3': 3}

d1 = {'k1': 1, 'k2': 2}
d2 = {'k3': 3, 'k4': 4}

d = {**d1, **d2}
print(d)
# {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4}

print(d1)
# {'k1': 1, 'k2': 2}

print(d2)
# {'k3': 3, 'k4': 4}

print({**d1, **d2, 'k5': 5})
# {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4, 'k5': 5}

d3 = {'k5': 5, 'k6': 6}

print({**d1, **d2, **d3})
# {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4, 'k5': 5, 'k6': 6}

d4 = {'k1': 100, 'k3': 300}

print({**d1, **d2, **d3, **d4, 'k5': 500})
# {'k1': 100, 'k2': 2, 'k3': 300, 'k4': 4, 'k5': 500, 'k6': 6}

d1 = {'k1': 1, 'k2': 2}
d2 = {'k3': 3, 'k4': 4}

# d = dict(d1, d2)
# TypeError: dict expected at most 1 arguments, got 2

d = dict(**d1, **d2)
print(d)
# {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4}
