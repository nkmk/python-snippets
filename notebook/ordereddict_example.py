import collections

od = collections.OrderedDict()

od['k1'] = 1
od['k2'] = 2
od['k3'] = 3

print(od)
# OrderedDict([('k1', 1), ('k2', 2), ('k3', 3)])

print(collections.OrderedDict(k1=1, k2=2, k3=3))
print(collections.OrderedDict([('k1', 1), ('k2', 2), ('k3', 3)]))
print(collections.OrderedDict((['k1', 1], ['k2', 2], ['k3', 3])))
# OrderedDict([('k1', 1), ('k2', 2), ('k3', 3)])
# OrderedDict([('k1', 1), ('k2', 2), ('k3', 3)])
# OrderedDict([('k1', 1), ('k2', 2), ('k3', 3)])

print(collections.OrderedDict({'k1': 1, 'k2': 2, 'k3': 3}))
# OrderedDict([('k1', 1), ('k2', 2), ('k3', 3)])

print(issubclass(collections.OrderedDict, dict))
# True

print(od['k1'])
# 1

od['k2'] = 200
print(od)
# OrderedDict([('k1', 1), ('k2', 200), ('k3', 3)])

od.update(k4=4, k5=5)
print(od)
# OrderedDict([('k1', 1), ('k2', 200), ('k3', 3), ('k4', 4), ('k5', 5)])

del od['k4'], od['k5']
print(od)
# OrderedDict([('k1', 1), ('k2', 200), ('k3', 3)])

od.move_to_end('k1')
print(od)
# OrderedDict([('k2', 200), ('k3', 3), ('k1', 1)])

od.move_to_end('k1', False)
print(od)
# OrderedDict([('k1', 1), ('k2', 200), ('k3', 3)])

l = list(od.items())
print(l)
# [('k1', 1), ('k2', 200), ('k3', 3)]

l.insert(1, ('kx', -1))
print(l)
# [('k1', 1), ('kx', -1), ('k2', 200), ('k3', 3)]

od = collections.OrderedDict(l)
print(od)
# OrderedDict([('k1', 1), ('kx', -1), ('k2', 200), ('k3', 3)])

l = list(od.items())
print(l)
# [('k1', 1), ('kx', -1), ('k2', 200), ('k3', 3)]

l[0], l[2] = l[2], l[0]
print(l)
# [('k2', 200), ('kx', -1), ('k1', 1), ('k3', 3)]

od = collections.OrderedDict(l)
print(od)
# OrderedDict([('k2', 200), ('kx', -1), ('k1', 1), ('k3', 3)])

l = list(od.items())
k = list(od.keys())
print(k)
# ['k2', 'kx', 'k1', 'k3']

print(k.index('kx'))
# 1

l[k.index('kx')], l[k.index('k3')] = l[k.index('k3')], l[k.index('kx')]
print(l)
# [('k2', 200), ('k3', 3), ('k1', 1), ('kx', -1)]

od = collections.OrderedDict(l)
print(od)
# OrderedDict([('k2', 200), ('k3', 3), ('k1', 1), ('kx', -1)])

od_sorted_key = collections.OrderedDict(
    sorted(od.items(), key=lambda x: x[0])
)
print(od_sorted_key)
# OrderedDict([('k1', 1), ('k2', 200), ('k3', 3), ('kx', -1)])

od_sorted_value = collections.OrderedDict(
    sorted(od.items(), key=lambda x: x[1], reverse=True)
)
print(od_sorted_value)
# OrderedDict([('k2', 200), ('k3', 3), ('k1', 1), ('kx', -1)])
