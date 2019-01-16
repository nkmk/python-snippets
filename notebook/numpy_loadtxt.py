import numpy as np

with open('data/src/sample.txt') as f:
    print(f.read())
# 11 12 13 14
# 21 22 23 24
# 31 32 33 34

a = np.loadtxt('data/src/sample.txt')

print(type(a))
# <class 'numpy.ndarray'>

print(a)
# [[11. 12. 13. 14.]
#  [21. 22. 23. 24.]
#  [31. 32. 33. 34.]]

print(a.dtype)
# float64

with open('data/src/sample.csv') as f:
    print(f.read())
# 11,12,13,14
# 21,22,23,24
# 31,32,33,34

# print(np.loadtxt('data/src/sample.csv'))
# ValueError: could not convert string to float: '11,12,13,14'

print(np.loadtxt('data/src/sample.csv', delimiter=','))
# [[11. 12. 13. 14.]
#  [21. 22. 23. 24.]
#  [31. 32. 33. 34.]]

a = np.loadtxt('data/src/sample.csv', delimiter=',', dtype='int64')

print(a)
# [[11 12 13 14]
#  [21 22 23 24]
#  [31 32 33 34]]

print(a.dtype)
# int64

with open('data/src/sample_header_index.csv') as f:
    print(f.read())
# ,a,b,c,d
# ONE,11,12,13,14
# TWO,21,22,23,24
# THREE,31,32,33,34

a = np.loadtxt('data/src/sample_header_index.csv', delimiter=',', dtype='int64',
               skiprows=1, usecols=[1, 2, 3, 4])

print(a)
# [[11 12 13 14]
#  [21 22 23 24]
#  [31 32 33 34]]
