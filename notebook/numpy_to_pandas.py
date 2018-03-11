import numpy as np
import pandas as pd

a = np.arange(4)
print(a)
# [0 1 2 3]

s = pd.Series(a)
print(s)
# 0    0
# 1    1
# 2    2
# 3    3
# dtype: int64

index = ['A', 'B', 'C', 'D']
name = 'sample'
s = pd.Series(data=a, index=index, name=name, dtype='float')
print(s)
# A    0.0
# B    1.0
# C    2.0
# D    3.0
# Name: sample, dtype: float64

a = np.arange(12).reshape((4, 3))
print(a)
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]

# s = pd.Series(a)
# print(s)
# Exception: Data must be 1-dimensional

s = pd.Series(a[2])
print(s)
# 0    6
# 1    7
# 2    8
# dtype: int64

s = pd.Series(a.T[2])
print(s)
# 0     2
# 1     5
# 2     8
# 3    11
# dtype: int64

a = np.arange(12).reshape((4, 3))
print(a)
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]

df = pd.DataFrame(a)
print(df)
#    0   1   2
# 0  0   1   2
# 1  3   4   5
# 2  6   7   8
# 3  9  10  11

index = ['A', 'B', 'C', 'D']
columns = ['a', 'b', 'c']
df = pd.DataFrame(data=a, index=index, columns=columns, dtype='float')
print(df)
#      a     b     c
# A  0.0   1.0   2.0
# B  3.0   4.0   5.0
# C  6.0   7.0   8.0
# D  9.0  10.0  11.0
