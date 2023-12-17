import pandas as pd
import numpy as np

print(pd.__version__)
# 2.1.4

print(np.__version__)
# 1.26.2

a = np.array([[0, 1, 2], [3, 4, 5]])
print(a)
# [[0 1 2]
#  [3 4 5]]

df = pd.DataFrame(a)
print(df)
#    0  1  2
# 0  0  1  2
# 1  3  4  5

print(np.shares_memory(a, df))
# True

print(df._is_view)
# True

a[0, 0] = 100
print(a)
# [[100   1   2]
#  [  3   4   5]]

print(df)
#      0  1  2
# 0  100  1  2
# 1    3  4  5

a_str = np.array([['a', 'b', 'c'], ['x', 'y', 'z']])
print(a_str)
# [['a' 'b' 'c']
#  ['x' 'y' 'z']]

df_str = pd.DataFrame(a_str)
print(df_str)
#    0  1  2
# 0  a  b  c
# 1  x  y  z

print(np.shares_memory(a_str, df_str))
# False

print(df_str._is_view)
# False

a_str[0, 0] = 'A'
print(a_str)
# [['A' 'b' 'c']
#  ['x' 'y' 'z']]

print(df_str)
#    0  1  2
# 0  a  b  c
# 1  x  y  z

df_homo = pd.DataFrame([[0, 1, 2], [3, 4, 5]])
print(df_homo)
#    0  1  2
# 0  0  1  2
# 1  3  4  5

print(df_homo.dtypes)
# 0    int64
# 1    int64
# 2    int64
# dtype: object

a_homo = df_homo.values
print(a_homo)
# [[0 1 2]
#  [3 4 5]]

print(np.shares_memory(a_homo, df_homo))
# True

df_homo.iat[0, 0] = 100
print(df_homo)
#      0  1  2
# 0  100  1  2
# 1    3  4  5

print(a_homo)
# [[100   1   2]
#  [  3   4   5]]

df_hetero = pd.DataFrame([[0, 'x'], [1, 'y']])
print(df_hetero)
#    0  1
# 0  0  x
# 1  1  y

print(df_hetero.dtypes)
# 0     int64
# 1    object
# dtype: object

a_hetero = df_hetero.values
print(a_hetero)
# [[0 'x']
#  [1 'y']]

print(np.shares_memory(a_hetero, df_hetero))
# False

df_hetero.iat[0, 0] = 100
print(df_hetero)
#      0  1
# 0  100  x
# 1    1  y

print(a_hetero)
# [[0 'x']
#  [1 'y']]
