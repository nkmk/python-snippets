import numpy as np

print(np.__version__)
# 1.26.1

a_2d = np.arange(12).reshape(3, 4)
print(a_2d)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

a_2d[0, 0] = 10
print(a_2d)
# [[10  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

a_2d[1] = 100
print(a_2d)
# [[ 10   1   2   3]
#  [100 100 100 100]
#  [  8   9  10  11]]

a_2d[np.ix_([False, True, True], [1, 3])] = 1000
print(a_2d)
# [[  10    1    2    3]
#  [ 100 1000  100 1000]
#  [   8 1000   10 1000]]

a_2d = np.arange(12).reshape(3, 4)
print(a_2d)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a_2d[::2, 1:])
# [[ 1  2  3]
#  [ 9 10 11]]

print(np.arange(6).reshape(2, 3) * 100)
# [[  0 100 200]
#  [300 400 500]]

a_2d[::2, 1:] = np.arange(6).reshape(2, 3) * 100
print(a_2d)
# [[  0   0 100 200]
#  [  4   5   6   7]
#  [  8 300 400 500]]

a_2d = np.arange(12).reshape(3, 4)
print(a_2d)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a_2d[::2, 1:])
# [[ 1  2  3]
#  [ 9 10 11]]

print(np.arange(3) * 100)
# [  0 100 200]

a_2d[::2, 1:] = np.arange(3) * 100
print(a_2d)
# [[  0   0 100 200]
#  [  4   5   6   7]
#  [  8   0 100 200]]

a_2d = np.arange(12).reshape(3, 4)
print(a_2d)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a_2d[::2, 1:])
# [[ 1  2  3]
#  [ 9 10 11]]

print(np.arange(2) * 100)
# [  0 100]

# a_2d[::2, 1:] = np.arange(2) * 100
# ValueError: could not broadcast input array from shape (2,) into shape (2,3)
