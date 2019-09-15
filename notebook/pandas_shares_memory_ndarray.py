import pandas as pd
import numpy as np

a = np.array([[0, 1], [2, 3], [4, 5]])
print(a)
# [[0 1]
#  [2 3]
#  [4 5]]

df = pd.DataFrame(a)
print(df)
#    0  1
# 0  0  1
# 1  2  3
# 2  4  5

print(np.shares_memory(a, df))
# True

print(df._is_view)
# True

a[0, 0] = 100
print(a)
# [[100   1]
#  [  2   3]
#  [  4   5]]

print(df)
#      0  1
# 0  100  1
# 1    2  3
# 2    4  5

a_str = np.array([['a', 'x'], ['b', 'y'], ['c', 'z']])
print(a_str)
# [['a' 'x']
#  ['b' 'y']
#  ['c' 'z']]

df_str = pd.DataFrame(a_str)
print(df_str)
#    0  1
# 0  a  x
# 1  b  y
# 2  c  z

print(np.shares_memory(a_str, df_str))
# False

print(df_str._is_view)
# False

a_str[0, 0] = 'n'
print(a_str)
# [['n' 'x']
#  ['b' 'y']
#  ['c' 'z']]

print(df_str)
#    0  1
# 0  a  x
# 1  b  y
# 2  c  z

df_homo = pd.DataFrame({'a': [0, 1, 2], 'b': [3, 4, 5]})
print(df_homo)
#    a  b
# 0  0  3
# 1  1  4
# 2  2  5

print(df_homo.dtypes)
# a    int64
# b    int64
# dtype: object

a_homo = df_homo.values
print(a_homo)
# [[0 3]
#  [1 4]
#  [2 5]]

print(np.shares_memory(a_homo, df_homo))
# True

df_homo.iat[0, 0] = 100
print(df_homo)
#      a  b
# 0  100  3
# 1    1  4
# 2    2  5

print(a_homo)
# [[100   3]
#  [  1   4]
#  [  2   5]]

df_hetero = pd.DataFrame({'a': [0, 1, 2], 'b': ['x', 'y', 'z']})
print(df_hetero)
#    a  b
# 0  0  x
# 1  1  y
# 2  2  z

print(df_hetero.dtypes)
# a     int64
# b    object
# dtype: object

a_hetero = df_hetero.values
print(a_hetero)
# [[0 'x']
#  [1 'y']
#  [2 'z']]

print(np.shares_memory(a_hetero, df_hetero))
# False

df_hetero.iat[0, 0] = 100
print(df_hetero)
#      a  b
# 0  100  x
# 1    1  y
# 2    2  z

print(a_hetero)
# [[0 'x']
#  [1 'y']
#  [2 'z']]
