import numpy as np

print(np.__version__)
# 1.26.1

a = np.arange(24)
print(a)
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]

print(a.shape)
# (24,)

print(a.ndim)
# 1

a_4_6 = a.reshape([4, 6])
print(a_4_6)
# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]
#  [12 13 14 15 16 17]
#  [18 19 20 21 22 23]]

print(a_4_6.shape)
# (4, 6)

print(a_4_6.ndim)
# 2

a_2_3_4 = a.reshape((2, 3, 4))
print(a_2_3_4)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
# 
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

print(a_2_3_4.shape)
# (2, 3, 4)

print(a_2_3_4.ndim)
# 3

# a_5_6 = a.reshape([5, 6])
# ValueError: cannot reshape array of size 24 into shape (5,6)

print(a.reshape(4, 6))
# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]
#  [12 13 14 15 16 17]
#  [18 19 20 21 22 23]]

print(a.reshape(2, 3, 4))
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
# 
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

print(np.reshape(a, [4, 6]))
# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]
#  [12 13 14 15 16 17]
#  [18 19 20 21 22 23]]

print(np.reshape(a, (2, 3, 4)))
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
# 
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

# print(np.reshape(a, [5, 6]))
# ValueError: cannot reshape array of size 24 into shape (5,6)

# print(np.reshape(a, 4, 6))
# TypeError: order must be str, not int

# print(np.reshape(a, 2, 3, 4))
# TypeError: reshape() takes from 2 to 3 positional arguments but 4 were given

print(a.reshape([4, 6], order='C'))
# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]
#  [12 13 14 15 16 17]
#  [18 19 20 21 22 23]]

print(a.reshape([4, 6], order='F'))
# [[ 0  4  8 12 16 20]
#  [ 1  5  9 13 17 21]
#  [ 2  6 10 14 18 22]
#  [ 3  7 11 15 19 23]]

print(a.reshape([2, 3, 4], order='C'))
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
# 
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

print(a.reshape([2, 3, 4], order='F'))
# [[[ 0  6 12 18]
#   [ 2  8 14 20]
#   [ 4 10 16 22]]
# 
#  [[ 1  7 13 19]
#   [ 3  9 15 21]
#   [ 5 11 17 23]]]

print(np.reshape(a, [4, 6], order='F'))
# [[ 0  4  8 12 16 20]
#  [ 1  5  9 13 17 21]
#  [ 2  6 10 14 18 22]
#  [ 3  7 11 15 19 23]]

# print(a.reshape([4, 6], 'F'))
# TypeError: 'list' object cannot be interpreted as an integer

print(np.reshape(a, [4, 6], 'F'))
# [[ 0  4  8 12 16 20]
#  [ 1  5  9 13 17 21]
#  [ 2  6 10 14 18 22]
#  [ 3  7 11 15 19 23]]

print(a.reshape([4, -1]))
# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]
#  [12 13 14 15 16 17]
#  [18 19 20 21 22 23]]

print(a.reshape([2, -1, 4]))
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
# 
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

# print(a.reshape([2, -1, -1]))
# ValueError: can only specify one unknown dimension

# print(a.reshape([2, -1, 5]))
# ValueError: cannot reshape array of size 24 into shape (2,newaxis,5)

print(a.reshape([4, -100]))
# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]
#  [12 13 14 15 16 17]
#  [18 19 20 21 22 23]]

a = np.arange(8)
print(a)
# [0 1 2 3 4 5 6 7]

a_2_4 = a.reshape([2, 4])
print(a_2_4)
# [[0 1 2 3]
#  [4 5 6 7]]

print(np.shares_memory(a, a_2_4))
# True

a[0] = 100
print(a)
# [100   1   2   3   4   5   6   7]

print(a_2_4)
# [[100   1   2   3]
#  [  4   5   6   7]]

a_2_4[0, 0] = 0
print(a_2_4)
# [[0 1 2 3]
#  [4 5 6 7]]

print(a)
# [0 1 2 3 4 5 6 7]

a_2_4_copy = a.reshape([2, 4]).copy()
print(a_2_4_copy)
# [[0 1 2 3]
#  [4 5 6 7]]

print(np.shares_memory(a, a_2_4_copy))
# False

a[0] = 100
print(a)
# [100   1   2   3   4   5   6   7]

print(a_2_4_copy)
# [[0 1 2 3]
#  [4 5 6 7]]

a_2_4_copy[0, 0] = 200
print(a_2_4_copy)
# [[200   1   2   3]
#  [  4   5   6   7]]

print(a)
# [100   1   2   3   4   5   6   7]

a = np.arange(8).reshape(2, 4)
print(a)
# [[0 1 2 3]
#  [4 5 6 7]]

a_step3 = a[:, ::3]
print(a_step3)
# [[0 3]
#  [4 7]]

a_step3_reshape = a_step3.reshape(-1)
print(a_step3_reshape)
# [0 3 4 7]

print(np.shares_memory(a_step3, a_step3_reshape))
# False

a_step2 = a[:, ::2]
print(a_step2)
# [[0 2]
#  [4 6]]

a_step2_reshape = a_step2.reshape(-1)
print(a_step2_reshape)
# [0 2 4 6]

print(np.shares_memory(a_step2, a_step2_reshape))
# True
