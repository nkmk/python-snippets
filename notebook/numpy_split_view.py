import numpy as np

print(np.__version__)
# 1.26.1

a = np.arange(16).reshape(4, 4)
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]

l = np.split(a, 2)

print(l[0])
# [[0 1 2 3]
#  [4 5 6 7]]

print(np.shares_memory(a, l[0]))
# True

a[0, 0] = 100
print(a)
# [[100   1   2   3]
#  [  4   5   6   7]
#  [  8   9  10  11]
#  [ 12  13  14  15]]

print(l[0])
# [[100   1   2   3]
#  [  4   5   6   7]]

print(np.shares_memory(a, np.vsplit(a, 2)[0]))
# True

print(np.shares_memory(a, np.hsplit(a, 2)[0]))
# True

print(np.shares_memory(a, np.array_split(a, 3)[0]))
# True

a_3d = np.arange(24).reshape(2, 3, 4)
print(np.shares_memory(a_3d, np.dsplit(a_3d, 2)[0]))
# True

a = np.arange(16).reshape(4, 4)

l_copy = np.split(a.copy(), 2)

print(np.shares_memory(a, l_copy[0]))
# False

a[0, 0] = 100
print(a)
# [[100   1   2   3]
#  [  4   5   6   7]
#  [  8   9  10  11]
#  [ 12  13  14  15]]

print(l_copy[0])
# [[0 1 2 3]
#  [4 5 6 7]]
