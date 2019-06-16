import numpy as np

a_1d = np.arange(10)
print(a_1d)
# [0 1 2 3 4 5 6 7 8 9]

print(a_1d[0])
# 0

print(a_1d[4])
# 4

print(a_1d[-1])
# 9

print(a_1d[-4])
# 6

# print(a_1d[100])
# IndexError: index 100 is out of bounds for axis 0 with size 10

# print(a_1d[-100])
# IndexError: index -100 is out of bounds for axis 0 with size 10

a_2d = np.arange(12).reshape(3, 4)
print(a_2d)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a_2d[0, -1])
# 3

print(a_2d[0])
# [0 1 2 3]

print(a_2d[0, :])
# [0 1 2 3]

print(a_2d[:, 0])
# [0 4 8]

print(type(a_2d[0, -1]))
# <class 'numpy.int64'>

print(type(a_2d[0]))
# <class 'numpy.ndarray'>
