import numpy as np

print(np.__version__)
# 1.26.1

a = np.arange(3)
print(a)
# [0 1 2]

a_append = np.append(a, 3)
print(a_append)
# [0 1 2 3]

print(a)
# [0 1 2]

print(np.append(a, [3, 4, 5]))
# [0 1 2 3 4 5]

print(np.append(a, np.arange(3, 6)))
# [0 1 2 3 4 5]

print(np.append(-1, a))
# [-1  0  1  2]

print(np.append([-3, -2, -1], a))
# [-3 -2 -1  0  1  2]

print(np.append(np.arange(-3, 0), a))
# [-3 -2 -1  0  1  2]

a_2d = np.arange(6).reshape(2, 3)
print(a_2d)
# [[0 1 2]
#  [3 4 5]]

print(np.append(a_2d, 10))
# [ 0  1  2  3  4  5 10]

a_2d_ex = np.arange(6).reshape(2, 3) * 10
print(a_2d_ex)
# [[ 0 10 20]
#  [30 40 50]]

print(np.append(a_2d, a_2d_ex))
# [ 0  1  2  3  4  5  0 10 20 30 40 50]

print(np.append(a_2d, a_2d_ex, axis=0))
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 0 10 20]
#  [30 40 50]]

print(np.append(a_2d, a_2d_ex, axis=1))
# [[ 0  1  2  0 10 20]
#  [ 3  4  5 30 40 50]]

# print(np.append(a_2d, a_2d_ex, axis=2))
# AxisError: axis 2 is out of bounds for array of dimension 2

a_2d_ex2 = np.arange(2).reshape(1, 2) * 10
print(a_2d_ex2)
# [[ 0 10]]

# print(np.append(a_2d, a_2d_ex2, axis=0))
# ValueError: all the input array dimensions except for the concatenation axis must match exactly, but along dimension 1, the array at index 0 has size 3 and the array at index 1 has size 2

# print(np.append(a_2d, a_2d_ex2, axis=1))
# ValueError: all the input array dimensions except for the concatenation axis must match exactly, but along dimension 0, the array at index 0 has size 2 and the array at index 1 has size 1

print(np.append(a_2d_ex, a_2d, axis=0))
# [[ 0 10 20]
#  [30 40 50]
#  [ 0  1  2]
#  [ 3  4  5]]

print(np.append(a_2d_ex, a_2d, axis=1))
# [[ 0 10 20  0  1  2]
#  [30 40 50  3  4  5]]

print(np.append(a_2d, [[0, 10, 20], [30, 40, 50]], axis=0))
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 0 10 20]
#  [30 40 50]]

a_row_1d = np.arange(3) * 10
print(a_row_1d)
# [ 0 10 20]

# print(np.append(a_2d, a_row_1d, axis=0))
# ValueError: all the input arrays must have same number of dimensions, but the array at index 0 has 2 dimension(s) and the array at index 1 has 1 dimension(s)

print(a_row_1d.reshape(1, 3))
# [[ 0 10 20]]

print(np.append(a_2d, a_row_1d.reshape(1, 3), axis=0))
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 0 10 20]]

a_col_1d = np.arange(2) * 10
print(a_col_1d)
# [ 0 10]

# print(np.append(a_2d, a_col_1d, axis=1))
# ValueError: all the input arrays must have same number of dimensions, but the array at index 0 has 2 dimension(s) and the array at index 1 has 1 dimension(s)

print(a_col_1d.reshape(2, 1))
# [[ 0]
#  [10]]

print(np.append(a_2d, a_col_1d.reshape(2, 1), axis=1))
# [[ 0  1  2  0]
#  [ 3  4  5 10]]

print(np.vstack([a_2d, a_row_1d]))
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 0 10 20]]

print(np.vstack([a_2d, a_row_1d, [[0, -1, -2], [-3, -4, -5]]]))
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 0 10 20]
#  [ 0 -1 -2]
#  [-3 -4 -5]]

# print(np.hstack([a_2d, a_col_1d]))
# ValueError: all the input arrays must have same number of dimensions, but the array at index 0 has 2 dimension(s) and the array at index 1 has 1 dimension(s)

print(np.hstack([a_2d, a_col_1d.reshape(2, 1), [[0, -1], [-2, -3]]]))
# [[ 0  1  2  0  0 -1]
#  [ 3  4  5 10 -2 -3]]

a_3d = np.arange(12).reshape(2, 3, 2)
print(a_3d)
# [[[ 0  1]
#   [ 2  3]
#   [ 4  5]]
# 
#  [[ 6  7]
#   [ 8  9]
#   [10 11]]]

print(np.append(a_3d, 100))
# [  0   1   2   3   4   5   6   7   8   9  10  11 100]

a_3d_ex = np.arange(12).reshape(2, 3, 2) * 10
print(a_3d_ex)
# [[[  0  10]
#   [ 20  30]
#   [ 40  50]]
# 
#  [[ 60  70]
#   [ 80  90]
#   [100 110]]]

print(a_3d_ex.shape)
# (2, 3, 2)

print(np.append(a_3d, a_3d_ex, axis=0))
# [[[  0   1]
#   [  2   3]
#   [  4   5]]
# 
#  [[  6   7]
#   [  8   9]
#   [ 10  11]]
# 
#  [[  0  10]
#   [ 20  30]
#   [ 40  50]]
# 
#  [[ 60  70]
#   [ 80  90]
#   [100 110]]]

print(np.append(a_3d, a_3d_ex, axis=0).shape)
# (4, 3, 2)

print(np.append(a_3d, a_3d_ex, axis=1))
# [[[  0   1]
#   [  2   3]
#   [  4   5]
#   [  0  10]
#   [ 20  30]
#   [ 40  50]]
# 
#  [[  6   7]
#   [  8   9]
#   [ 10  11]
#   [ 60  70]
#   [ 80  90]
#   [100 110]]]

print(np.append(a_3d, a_3d_ex, axis=1).shape)
# (2, 6, 2)

print(np.append(a_3d, a_3d_ex, axis=2))
# [[[  0   1   0  10]
#   [  2   3  20  30]
#   [  4   5  40  50]]
# 
#  [[  6   7  60  70]
#   [  8   9  80  90]
#   [ 10  11 100 110]]]

print(np.append(a_3d, a_3d_ex, axis=2).shape)
# (2, 3, 4)

print(np.concatenate([a_3d_ex, a_3d, a_3d_ex], axis=2))
# [[[  0  10   0   1   0  10]
#   [ 20  30   2   3  20  30]
#   [ 40  50   4   5  40  50]]
# 
#  [[ 60  70   6   7  60  70]
#   [ 80  90   8   9  80  90]
#   [100 110  10  11 100 110]]]
