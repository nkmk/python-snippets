import numpy as np

a = np.random.randint(0, 10, 10)
print(a)
# [8 0 5 0 1 5 5 5 3 0]

sort = np.sort(a)
print(sort)
# [0 0 0 1 3 5 5 5 5 8]

print(a)
# [8 0 5 0 1 5 5 5 3 0]

sort_inverse = np.sort(a)[::-1]
print(sort_inverse)
# [8 5 5 5 5 3 1 0 0 0]

a = np.random.randint(0, 100, 30).reshape((3, 10))
print(a)
# [[11 76 26  3 23 79 81 47 42 86]
#  [ 2 27 50 92 22 47 23 61 66 59]
#  [42  5 12  0 79 12  2  7 33 57]]

sort_col = np.sort(a, axis=0)
print(sort_col)
# [[ 2  5 12  0 22 12  2  7 33 57]
#  [11 27 26  3 23 47 23 47 42 59]
#  [42 76 50 92 79 79 81 61 66 86]]

sort_col_inverse = np.sort(a, axis=0)[::-1]
print(sort_col_inverse)
# [[42 76 50 92 79 79 81 61 66 86]
#  [11 27 26  3 23 47 23 47 42 59]
#  [ 2  5 12  0 22 12  2  7 33 57]]

sort_row = np.sort(a, axis=1)
print(sort_row)
# [[ 3 11 23 26 42 47 76 79 81 86]
#  [ 2 22 23 27 47 50 59 61 66 92]
#  [ 0  2  5  7 12 12 33 42 57 79]]

sort_row = np.sort(a)
print(sort_row)
# [[ 3 11 23 26 42 47 76 79 81 86]
#  [ 2 22 23 27 47 50 59 61 66 92]
#  [ 0  2  5  7 12 12 33 42 57 79]]

sort_row = np.sort(a, axis=-1)
print(sort_row)
# [[ 3 11 23 26 42 47 76 79 81 86]
#  [ 2 22 23 27 47 50 59 61 66 92]
#  [ 0  2  5  7 12 12 33 42 57 79]]

sort_row_inverse = np.sort(a, axis=1)[:, ::-1]
print(sort_row_inverse)
# [[86 81 79 76 47 42 26 23 11  3]
#  [92 66 61 59 50 47 27 23 22  2]
#  [79 57 42 33 12 12  7  5  2  0]]

sort_col_index = np.argsort(a, axis=0)
print(sort_col_index)
# [[1 2 2 2 1 2 2 2 2 2]
#  [0 1 0 0 0 1 1 0 0 1]
#  [2 0 1 1 2 0 0 1 1 0]]

sort_row_index = np.argsort(a)
print(sort_row_index)
# [[3 0 4 2 8 7 1 5 6 9]
#  [0 4 6 1 5 2 9 7 8 3]
#  [3 6 1 7 2 5 8 0 9 4]]

col_num = 2

print(np.argsort(a[:, col_num]))
# [2 0 1]

sort_col_num = a[np.argsort(a[:, col_num]), :]
print(sort_col_num)
# [[42  5 12  0 79 12  2  7 33 57]
#  [11 76 26  3 23 79 81 47 42 86]
#  [ 2 27 50 92 22 47 23 61 66 59]]

sort_col_num = a[np.argsort(a[:, col_num])]
print(sort_col_num)
# [[42  5 12  0 79 12  2  7 33 57]
#  [11 76 26  3 23 79 81 47 42 86]
#  [ 2 27 50 92 22 47 23 61 66 59]]

print(np.argsort(a[:, col_num])[::-1])
# [1 0 2]

sort_col_num_inverse = a[np.argsort(a[:, col_num])[::-1]]
print(sort_col_num_inverse)
# [[ 2 27 50 92 22 47 23 61 66 59]
#  [11 76 26  3 23 79 81 47 42 86]
#  [42  5 12  0 79 12  2  7 33 57]]

row_num = 1

print(np.argsort(a[row_num]))
# [0 4 6 1 5 2 9 7 8 3]

sort_row_num = a[:, np.argsort(a[row_num])]
print(sort_row_num)
# [[11 23 81 76 79 26 86 47 42  3]
#  [ 2 22 23 27 47 50 59 61 66 92]
#  [42 79  2  5 12 12 57  7 33  0]]

print(np.argsort(a[row_num])[::-1])
# [3 8 7 9 2 5 1 6 4 0]

sort_row_num_inverse = a[:, np.argsort(a[row_num])[::-1]]
print(sort_row_num_inverse)
# [[ 3 42 47 86 26 79 76 81 23 11]
#  [92 66 61 59 50 47 27 23 22  2]
#  [ 0 33  7 57 12 12  5  2 79 42]]
