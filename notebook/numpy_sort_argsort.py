import numpy as np

a = np.random.randint(0, 10, 10)
print(a)
# [1 5 4 3 0 0 6 2 1 5]

sort = np.sort(a)
print(sort)
# [0 0 1 1 2 3 4 5 5 6]

print(a)
# [1 5 4 3 0 0 6 2 1 5]

sort_inverse = np.sort(a)[::-1]
print(sort_inverse)
# [6 5 5 4 3 2 1 1 0 0]

a = np.random.randint(0, 100, 30).reshape((3, 10))
print(a)
# [[19 62 24 59  1 33 28 39 16 52]
#  [52 82 13 81 95 28 36 14 85 25]
#  [96 16 25 28 93 63 30  6 76 78]]

sort_col = np.sort(a, axis=0)
print(sort_col)
# [[19 16 13 28  1 28 28  6 16 25]
#  [52 62 24 59 93 33 30 14 76 52]
#  [96 82 25 81 95 63 36 39 85 78]]

sort_col_inverse = np.sort(a, axis=0)[::-1]
print(sort_col_inverse)
# [[96 82 25 81 95 63 36 39 85 78]
#  [52 62 24 59 93 33 30 14 76 52]
#  [19 16 13 28  1 28 28  6 16 25]]

sort_row = np.sort(a, axis=1)
print(sort_row)
# [[ 1 16 19 24 28 33 39 52 59 62]
#  [13 14 25 28 36 52 81 82 85 95]
#  [ 6 16 25 28 30 63 76 78 93 96]]

sort_row = np.sort(a)
print(sort_row)
# [[ 1 16 19 24 28 33 39 52 59 62]
#  [13 14 25 28 36 52 81 82 85 95]
#  [ 6 16 25 28 30 63 76 78 93 96]]

sort_row = np.sort(a, axis=-1)
print(sort_row)
# [[ 1 16 19 24 28 33 39 52 59 62]
#  [13 14 25 28 36 52 81 82 85 95]
#  [ 6 16 25 28 30 63 76 78 93 96]]

sort_row_inverse = np.sort(a, axis=1)[:, ::-1]
print(sort_row_inverse)
# [[62 59 52 39 33 28 24 19 16  1]
#  [95 85 82 81 52 36 28 25 14 13]
#  [96 93 78 76 63 30 28 25 16  6]]

sort_col_index = np.argsort(a, axis=0)
print(sort_col_index)
# [[0 2 1 2 0 1 0 2 0 1]
#  [1 0 0 0 2 0 2 1 2 0]
#  [2 1 2 1 1 2 1 0 1 2]]

sort_row_index = np.argsort(a)
print(sort_row_index)
# [[4 8 0 2 6 5 7 9 3 1]
#  [2 7 9 5 6 0 3 1 8 4]
#  [7 1 2 3 6 5 8 9 4 0]]

col_num = 2

print(a[:, col_num])
# [24 13 25]

print(np.argsort(a[:, col_num]))
# [1 0 2]

sort_col_num = a[np.argsort(a[:, col_num]), :]
print(sort_col_num)
# [[52 82 13 81 95 28 36 14 85 25]
#  [19 62 24 59  1 33 28 39 16 52]
#  [96 16 25 28 93 63 30  6 76 78]]

sort_col_num = a[np.argsort(a[:, col_num])]
print(sort_col_num)
# [[52 82 13 81 95 28 36 14 85 25]
#  [19 62 24 59  1 33 28 39 16 52]
#  [96 16 25 28 93 63 30  6 76 78]]

print(np.argsort(a[:, col_num])[::-1])
# [2 0 1]

sort_col_num_inverse = a[np.argsort(a[:, col_num])[::-1]]
print(sort_col_num_inverse)
# [[96 16 25 28 93 63 30  6 76 78]
#  [19 62 24 59  1 33 28 39 16 52]
#  [52 82 13 81 95 28 36 14 85 25]]

row_num = 1

print(a[row_num])
# [52 82 13 81 95 28 36 14 85 25]

print(np.argsort(a[row_num]))
# [2 7 9 5 6 0 3 1 8 4]

sort_row_num = a[:, np.argsort(a[row_num])]
print(sort_row_num)
# [[24 39 52 33 28 19 59 62 16  1]
#  [13 14 25 28 36 52 81 82 85 95]
#  [25  6 78 63 30 96 28 16 76 93]]

print(np.argsort(a[row_num])[::-1])
# [4 8 1 3 0 6 5 9 7 2]

sort_row_num_inverse = a[:, np.argsort(a[row_num])[::-1]]
print(sort_row_num_inverse)
# [[ 1 16 62 59 19 28 33 52 39 24]
#  [95 85 82 81 52 36 28 25 14 13]
#  [93 76 16 28 96 30 63 78  6 25]]
