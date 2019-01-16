import numpy as np

with open('data/src/sample_nan.csv') as f:
    print(f.read())
# 11,12,,14
# 21,,,24
# 31,32,33,34

# a = np.loadtxt('data/src/sample_nan.csv', delimiter=',')
# ValueError: could not convert string to float: 

a = np.genfromtxt('data/src/sample_nan.csv', delimiter=',')

print(a)
# [[11. 12. nan 14.]
#  [21. nan nan 24.]
#  [31. 32. 33. 34.]]

print(a[0, 2])
# nan

print(type(a[0, 2]))
# <class 'numpy.float64'>

with open('data/src/sample_pandas_normal.csv') as f:
    print(f.read())
# name,age,state,point
# Alice,24,NY,64
# Bob,42,CA,92
# Charlie,18,CA,70
# Dave,68,TX,70
# Ellen,24,CA,88
# Frank,30,NY,57

a = np.loadtxt('data/src/sample_pandas_normal.csv', delimiter=',', skiprows=1,
               dtype={'names': ('name', 'age', 'state', 'point'),
                      'formats': ('<U7', '<i8', '<U2', '<i8')})

print(type(a))
# <class 'numpy.ndarray'>

print(a)
# [('Alice', 24, 'NY', 64) ('Bob', 42, 'CA', 92) ('Charlie', 18, 'CA', 70)
#  ('Dave', 68, 'TX', 70) ('Ellen', 24, 'CA', 88) ('Frank', 30, 'NY', 57)]

print(a.dtype)
# [('name', '<U7'), ('age', '<i8'), ('state', '<U2'), ('point', '<i8')]

a = np.genfromtxt('data/src/sample_pandas_normal.csv', delimiter=',',
                  names=True, dtype=None, encoding='utf-8')

print(type(a))
# <class 'numpy.ndarray'>

print(a)
# [('Alice', 24, 'NY', 64) ('Bob', 42, 'CA', 92) ('Charlie', 18, 'CA', 70)
#  ('Dave', 68, 'TX', 70) ('Ellen', 24, 'CA', 88) ('Frank', 30, 'NY', 57)]

print(a.dtype)
# [('name', '<U7'), ('age', '<i8'), ('state', '<U2'), ('point', '<i8')]
