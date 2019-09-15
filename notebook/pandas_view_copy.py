import pandas as pd
import numpy as np

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

df_homo_slice = df_homo.iloc[:2]
print(df_homo_slice)
#    a  b
# 0  0  3
# 1  1  4

print(np.shares_memory(df_homo, df_homo_slice))
# True

print(df_homo_slice._is_view)
# True

df_homo_list = df_homo.iloc[[0, 1]]
print(df_homo_list)
#    a  b
# 0  0  3
# 1  1  4

print(np.shares_memory(df_homo, df_homo_list))
# False

print(df_homo_list._is_view)
# False

print(df_homo['a'] < 2)
# 0     True
# 1     True
# 2    False
# Name: a, dtype: bool

df_homo_bool = df_homo.loc[df_homo['a'] < 2]
print(df_homo_bool)
#    a  b
# 0  0  3
# 1  1  4

print(np.shares_memory(df_homo, df_homo_bool))
# False

print(df_homo_bool._is_view)
# False

s_homo_scalar = df_homo.iloc[0]
print(s_homo_scalar)
# a    0
# b    3
# Name: 0, dtype: int64

print(np.shares_memory(df_homo, s_homo_scalar))
# True

print(s_homo_scalar._is_view)
# True

s_homo_col = df_homo['a']
print(s_homo_col)
# 0    0
# 1    1
# 2    2
# Name: a, dtype: int64

print(np.shares_memory(df_homo, s_homo_col))
# True

print(s_homo_col._is_view)
# True

df_homo_col_multi = df_homo[['a', 'b']]
print(df_homo_col_multi)
#    a  b
# 0  0  3
# 1  1  4
# 2  2  5

print(np.shares_memory(df_homo, df_homo_col_multi))
# False

print(df_homo_col_multi._is_view)
# False

df_homo.iat[0, 0] = 100
print(df_homo)
#      a  b
# 0  100  3
# 1    1  4
# 2    2  5

print(df_homo_slice)
#      a  b
# 0  100  3
# 1    1  4

print(df_homo_list)
#    a  b
# 0  0  3
# 1  1  4

print(df_homo_bool)
#    a  b
# 0  0  3
# 1  1  4

print(s_homo_scalar)
# a    100
# b      3
# Name: 0, dtype: int64

print(s_homo_col)
# 0    100
# 1      1
# 2      2
# Name: a, dtype: int64

print(df_homo_col_multi)
#    a  b
# 0  0  3
# 1  1  4
# 2  2  5

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

df_hetero_slice = df_hetero.iloc[:2]
print(df_hetero_slice)
#    a  b
# 0  0  x
# 1  1  y

print(np.shares_memory(df_hetero, df_hetero_slice))
# False

print(df_hetero_slice._is_view)
# False

df_hetero_slice2 = df_hetero.iloc[:2, 0:]
print(df_hetero_slice2)
#    a  b
# 0  0  x
# 1  1  y

print(np.shares_memory(df_hetero, df_hetero_slice2))
# False

print(df_hetero_slice2._is_view)
# False

df_hetero_list = df_hetero.iloc[[0, 1]]
print(df_hetero_list)
#    a  b
# 0  0  x
# 1  1  y

print(np.shares_memory(df_hetero, df_hetero_list))
# False

print(df_hetero_list._is_view)
# False

df_hetero_bool = df_hetero.loc[df_hetero['a'] < 2]
print(df_hetero_bool)
#    a  b
# 0  0  x
# 1  1  y

print(df_hetero_bool._is_view)
# False

print(df_hetero_bool._is_view)
# False

s_hetero_scalar = df_hetero.iloc[0]
print(s_hetero_scalar)
# a    0
# b    x
# Name: 0, dtype: object

print(np.shares_memory(df_hetero, s_hetero_scalar))
# False

print(s_hetero_scalar._is_view)
# False

s_hetero_col = df_hetero['a']
print(s_hetero_col)
# 0    0
# 1    1
# 2    2
# Name: a, dtype: int64

print(np.shares_memory(df_hetero, s_hetero_col))
# False

print(s_hetero_col._is_view)
# True

df_hetero_col_multi = df_hetero[['a', 'b']]
print(df_hetero_col_multi)
#    a  b
# 0  0  x
# 1  1  y
# 2  2  z

print(np.shares_memory(df_hetero, df_hetero_col_multi))
# False

print(df_hetero_col_multi._is_view)
# False

df_hetero.iat[0, 0] = 100
print(df_hetero)
#      a  b
# 0  100  x
# 1    1  y
# 2    2  z

print(df_hetero_slice)
#      a  b
# 0  100  x
# 1    1  y

print(df_hetero_slice2)
#    a  b
# 0  0  x
# 1  1  y

print(df_hetero_list)
#    a  b
# 0  0  x
# 1  1  y

print(df_hetero_bool)
#    a  b
# 0  0  x
# 1  1  y

print(s_hetero_scalar)
# a    0
# b    x
# Name: 0, dtype: object

print(s_hetero_col)
# 0    100
# 1      1
# 2      2
# Name: a, dtype: int64

print(df_hetero_col_multi)
#    a  b
# 0  0  x
# 1  1  y
# 2  2  z
