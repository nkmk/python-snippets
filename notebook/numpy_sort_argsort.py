import numpy as np

a = np.array([3, 4, 2, 0, 1])
print(a)
# [3 4 2 0 1]

a_sort = np.sort(a)
print(a_sort)
# [0 1 2 3 4]

print(a)
# [3 4 2 0 1]

a_sort_reverse = np.sort(a)[::-1]
print(a_sort_reverse)
# [4 3 2 1 0]

a_2d = np.array([[20, 3, 100], [1, 200, 30], [300, 10, 2]])
print(a_2d)
# [[ 20   3 100]
#  [  1 200  30]
#  [300  10   2]]

a_2d_sort_col = np.sort(a_2d, axis=0)
print(a_2d_sort_col)
# [[  1   3   2]
#  [ 20  10  30]
#  [300 200 100]]

a_2d_sort_row = np.sort(a_2d, axis=1)
print(a_2d_sort_row)
# [[  3  20 100]
#  [  1  30 200]
#  [  2  10 300]]

a_2d_sort_row = np.sort(a_2d)
print(a_2d_sort_row)
# [[  3  20 100]
#  [  1  30 200]
#  [  2  10 300]]

a_2d_sort_row = np.sort(a_2d, axis=-1)
print(a_2d_sort_row)
# [[  3  20 100]
#  [  1  30 200]
#  [  2  10 300]]

a_2d_sort_col_reverse = np.sort(a_2d, axis=0)[::-1]
print(a_2d_sort_col_reverse)
# [[300 200 100]
#  [ 20  10  30]
#  [  1   3   2]]

a_2d_sort_row_reverse = np.sort(a_2d, axis=1)[:, ::-1]
print(a_2d_sort_row_reverse)
# [[100  20   3]
#  [200  30   1]
#  [300  10   2]]

print(a_2d)
# [[ 20   3 100]
#  [  1 200  30]
#  [300  10   2]]

a_2d.sort()

print(a_2d)
# [[  3  20 100]
#  [  1  30 200]
#  [  2  10 300]]

a_2d.sort(axis=0)

print(a_2d[::-1])
# [[  3  30 300]
#  [  2  20 200]
#  [  1  10 100]]

a_2d = np.array([[20, 3, 100], [1, 200, 30], [300, 10, 2]])
print(a_2d)
# [[ 20   3 100]
#  [  1 200  30]
#  [300  10   2]]

a_2d_sort_col_index = np.argsort(a_2d, axis=0)
print(a_2d_sort_col_index)
# [[1 0 2]
#  [0 2 1]
#  [2 1 0]]

a_2d_sort_row_index = np.argsort(a_2d)
print(a_2d_sort_row_index)
# [[1 0 2]
#  [0 2 1]
#  [2 1 0]]

print(a_2d)
# [[ 20   3 100]
#  [  1 200  30]
#  [300  10   2]]

col_num = 1

print(a_2d[:, col_num])
# [  3 200  10]

print(np.argsort(a_2d[:, col_num]))
# [0 2 1]

a_2d_sort_col_num = a_2d[np.argsort(a_2d[:, col_num])]
print(a_2d_sort_col_num)
# [[ 20   3 100]
#  [300  10   2]
#  [  1 200  30]]

print(np.argsort(a_2d[:, col_num])[::-1])
# [1 2 0]

a_2d_sort_col_num_reverse = a_2d[np.argsort(a_2d[:, col_num])[::-1]]
print(a_2d_sort_col_num_reverse)
# [[  1 200  30]
#  [300  10   2]
#  [ 20   3 100]]

print(a_2d)
# [[ 20   3 100]
#  [  1 200  30]
#  [300  10   2]]

row_num = 1

print(a_2d[row_num])
# [  1 200  30]

print(np.argsort(a_2d[row_num]))
# [0 2 1]

a_2d_sort_row_num = a_2d[:, np.argsort(a_2d[row_num])]
print(a_2d_sort_row_num)
# [[ 20 100   3]
#  [  1  30 200]
#  [300   2  10]]

print(np.argsort(a_2d[row_num])[::-1])
# [1 2 0]

a_2d_sort_row_num_inverse = a_2d[:, np.argsort(a_2d[row_num])[::-1]]
print(a_2d_sort_row_num_inverse)
# [[  3 100  20]
#  [200  30   1]
#  [ 10   2 300]]
