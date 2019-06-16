import numpy as np

a_2d = np.arange(12).reshape(3, 4)
print(a_2d)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

a_slice = a_2d[:2, :2]
print(a_slice)
# [[0 1]
#  [4 5]]

print(np.shares_memory(a_2d, a_slice))
# True

a_slice[0, 0] = 100
print(a_slice)
# [[100   1]
#  [  4   5]]

print(a_2d)
# [[100   1   2   3]
#  [  4   5   6   7]
#  [  8   9  10  11]]

a_2d[0, 0] = 0
print(a_2d)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a_slice)
# [[0 1]
#  [4 5]]

a_fancy_index = a_2d[[0, 1]]
print(a_fancy_index)
# [[0 1 2 3]
#  [4 5 6 7]]

print(np.shares_memory(a_2d, a_fancy_index))
# False

a_fancy_index[0, 0] = 100
print(a_fancy_index)
# [[100   1   2   3]
#  [  4   5   6   7]]

print(a_2d)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

a_slice_copy = a_2d[:2, :2].copy()
print(a_slice_copy)
# [[0 1]
#  [4 5]]

print(np.shares_memory(a_2d, a_slice_copy))
# False

a_slice_copy[0, 0] = 100
print(a_slice_copy)
# [[100   1]
#  [  4   5]]

print(a_2d)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

a_fancy_index_slice = a_2d[[0, 1], :3]
print(a_fancy_index_slice)
# [[0 1 2]
#  [4 5 6]]

print(np.shares_memory(a_2d, a_fancy_index_slice))
# False

a_scalar_slice = a_2d[1, :3]
print(a_scalar_slice)
# [4 5 6]

print(np.shares_memory(a_2d, a_scalar_slice))
# True
