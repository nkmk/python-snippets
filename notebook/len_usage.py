l = [0, 1, 2]

print(len(l))
# 3

t = (0, 1, 2)

print(len(t))
# 3

s = {0, 1, 2}

print(len(s))
# 3

d = {'key0': 0, 'key1': 1, 'key2': 2}

print(len(d))
# 3

s = 'abcde'

print(len(s))
# 5

s = 'あいうえお'

print(len(s))
# 5

import numpy as np

a_1d = np.arange(3)

print(a_1d)
# [0 1 2]

print(len(a_1d))
# 3

a_2d = np.arange(12).reshape((3, 4))

print(a_2d)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(len(a_2d))
# 3

a_3d = np.arange(24).reshape((2, 3, 4))

print(a_3d)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

print(len(a_3d))
# 2

import pandas as pd

df = pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5]}, index=['a', 'b', 'c'])

print(df)
#    A  B
# a  0  3
# b  1  4
# c  2  5

print(len(df))
# 3

s = pd.Series([0, 1, 2], index=['a', 'b', 'c'])

print(s)
# a    0
# b    1
# c    2
# dtype: int64

print(len(s))
# 3

# print(len(100))
# TypeError: object of type 'int' has no len()

# print(len(0.1))
# TypeError: object of type 'float' has no len()

# print(len(True))
# TypeError: object of type 'bool' has no len()
