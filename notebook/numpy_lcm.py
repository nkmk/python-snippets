import numpy as np

a = np.array([0, 2, 3, 6])
b = np.array([3, 4, 5, 15])

print(np.lcm(a, b))
# [ 0  4 15 30]

print(type(np.lcm(a, b)))
# <class 'numpy.ndarray'>

print(np.lcm(6, 15))
# 30

a_2d = np.array([[0, 2, 3, 6], [0, 2, 3, 6]])
print(a_2d)
# [[0 2 3 6]
#  [0 2 3 6]]

print(np.lcm(a_2d, b))
# [[ 0  4 15 30]
#  [ 0  4 15 30]]

print(np.lcm(a, 15))
# [ 0 30 15 30]
