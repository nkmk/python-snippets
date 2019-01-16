import numpy as np

with open('data/src/sample.csv') as f:
    print(f.read())
# 11,12,13,14
# 21,22,23,24
# 31,32,33,34

a = np.loadtxt('data/src/sample.csv', delimiter=',')

print(type(a))
# <class 'numpy.ndarray'>

print(a)
# [[11. 12. 13. 14.]
#  [21. 22. 23. 24.]
#  [31. 32. 33. 34.]]

print(a[1:, :2])
# [[21. 22.]
#  [31. 32.]]

print(a.mean())
# 22.5

print(a.sum(axis=0))
# [63. 66. 69. 72.]
