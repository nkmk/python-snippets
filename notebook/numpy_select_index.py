import numpy as np

print(np.__version__)
# 1.26.1

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

print(a_2d[1, -1])
# 7

print(a_2d[1])
# [4 5 6 7]

print(a_2d[1, :])
# [4 5 6 7]

print(a_2d[:, 1])
# [1 5 9]
