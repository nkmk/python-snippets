import numpy as np

a_2d = np.arange(12).reshape(3, 4)
print(a_2d)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

a_2d[0, 0] = 100
print(a_2d)
# [[100   1   2   3]
#  [  4   5   6   7]
#  [  8   9  10  11]]

a_2d[0] = 100
print(a_2d)
# [[100 100 100 100]
#  [  4   5   6   7]
#  [  8   9  10  11]]

a_2d[np.ix_([False, True, True], [1, 3])] = 200
print(a_2d)
# [[100 100 100 100]
#  [  4 200   6 200]
#  [  8 200  10 200]]

a_2d = np.arange(12).reshape(3, 4)
print(a_2d)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a_2d[::2, :3])
# [[ 0  1  2]
#  [ 8  9 10]]

print(np.arange(6).reshape(2, 3) * 100)
# [[  0 100 200]
#  [300 400 500]]

a_2d[::2, :3] = np.arange(6).reshape(2, 3) * 100
print(a_2d)
# [[  0 100 200   3]
#  [  4   5   6   7]
#  [300 400 500  11]]

a_2d = np.arange(12).reshape(3, 4)
print(a_2d)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a_2d[::2, :3])
# [[ 0  1  2]
#  [ 8  9 10]]

print(np.arange(3) * 100)
# [  0 100 200]

a_2d[::2, :3] = np.arange(3) * 100
print(a_2d)
# [[  0 100 200   3]
#  [  4   5   6   7]
#  [  0 100 200  11]]

a_2d = np.arange(12).reshape(3, 4)
print(a_2d)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a_2d[::2, :3])
# [[ 0  1  2]
#  [ 8  9 10]]

print(np.arange(2) * 100)
# [  0 100]

# a_2d[::2, :3] = np.arange(2) * 100
# ValueError: could not broadcast input array from shape (2) into shape (2,3)
