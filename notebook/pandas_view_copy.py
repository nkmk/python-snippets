import pandas as pd
import numpy as np

print(pd.__version__)
# 2.1.4

print(np.__version__)
# 1.26.2

df_homo = pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5]})
print(df_homo)
#    A  B
# 0  0  3
# 1  1  4
# 2  2  5

print(df_homo.dtypes)
# A    int64
# B    int64
# dtype: object

df_homo_slice = df_homo.iloc[:2]
print(df_homo_slice)
#    A  B
# 0  0  3
# 1  1  4

print(np.shares_memory(df_homo, df_homo_slice))
# True

print(df_homo_slice._is_view)
# True

df_homo_list = df_homo.iloc[[0, 1]]
print(df_homo_list)
#    A  B
# 0  0  3
# 1  1  4

print(np.shares_memory(df_homo, df_homo_list))
# False

print(df_homo_list._is_view)
# False

df_homo_bool = df_homo.loc[[True, False, True]]
print(df_homo_bool)
#    A  B
# 0  0  3
# 2  2  5

print(np.shares_memory(df_homo, df_homo_bool))
# False

print(df_homo_bool._is_view)
# False

s_homo_scalar = df_homo.iloc[0]
print(s_homo_scalar)
# A    0
# B    3
# Name: 0, dtype: int64

print(np.shares_memory(df_homo, s_homo_scalar))
# True

print(s_homo_scalar._is_view)
# True

s_homo_col = df_homo['A']
print(s_homo_col)
# 0    0
# 1    1
# 2    2
# Name: A, dtype: int64

print(np.shares_memory(df_homo, s_homo_col))
# True

print(s_homo_col._is_view)
# True

df_homo_col_list = df_homo[['A', 'B']]
print(df_homo_col_list)
#    A  B
# 0  0  3
# 1  1  4
# 2  2  5

print(np.shares_memory(df_homo, df_homo_col_list))
# False

print(df_homo_col_list._is_view)
# False

df_homo.iat[0, 0] = 100
print(df_homo)
#      A  B
# 0  100  3
# 1    1  4
# 2    2  5

print(df_homo_slice)
#      A  B
# 0  100  3
# 1    1  4

print(df_homo_list)
#    A  B
# 0  0  3
# 1  1  4

print(df_homo_bool)
#    A  B
# 0  0  3
# 2  2  5

print(s_homo_scalar)
# A    100
# B      3
# Name: 0, dtype: int64

print(s_homo_col)
# 0    100
# 1      1
# 2      2
# Name: A, dtype: int64

print(df_homo_col_list)
#    A  B
# 0  0  3
# 1  1  4
# 2  2  5

df_hetero = pd.DataFrame({'A': [0, 1, 2], 'B': ['x', 'y', 'z']})
print(df_hetero)
#    A  B
# 0  0  x
# 1  1  y
# 2  2  z

print(df_hetero.dtypes)
# A     int64
# B    object
# dtype: object

df_hetero_slice_row = df_hetero.iloc[:2]
print(df_hetero_slice_row)
#    A  B
# 0  0  x
# 1  1  y

print(np.shares_memory(df_hetero, df_hetero_slice_row))
# False

print(df_hetero_slice_row._is_view)
# False

df_hetero_slice_row_col = df_hetero.iloc[:2, 0:]
print(df_hetero_slice_row_col)
#    A  B
# 0  0  x
# 1  1  y

print(np.shares_memory(df_hetero, df_hetero_slice_row_col))
# False

print(df_hetero_slice_row_col._is_view)
# False

df_hetero_list = df_hetero.iloc[[0, 1]]
print(df_hetero_list)
#    A  B
# 0  0  x
# 1  1  y

print(np.shares_memory(df_hetero, df_hetero_list))
# False

print(df_hetero_list._is_view)
# False

df_hetero_bool = df_hetero.loc[[True, False, True]]
print(df_hetero_bool)
#    A  B
# 0  0  x
# 2  2  z

print(df_hetero_bool._is_view)
# False

print(df_hetero_bool._is_view)
# False

s_hetero_scalar = df_hetero.iloc[0]
print(s_hetero_scalar)
# A    0
# B    x
# Name: 0, dtype: object

print(np.shares_memory(df_hetero, s_hetero_scalar))
# False

print(s_hetero_scalar._is_view)
# False

s_hetero_col = df_hetero['A']
print(s_hetero_col)
# 0    0
# 1    1
# 2    2
# Name: A, dtype: int64

print(np.shares_memory(df_hetero, s_hetero_col))
# False

print(s_hetero_col._is_view)
# True

df_hetero_col_list = df_hetero[['A', 'B']]
print(df_hetero_col_list)
#    A  B
# 0  0  x
# 1  1  y
# 2  2  z

print(np.shares_memory(df_hetero, df_hetero_col_list))
# False

print(df_hetero_col_list._is_view)
# False

df_hetero.iat[0, 0] = 100
print(df_hetero)
#      A  B
# 0  100  x
# 1    1  y
# 2    2  z

print(df_hetero_slice_row)
#      A  B
# 0  100  x
# 1    1  y

print(df_hetero_slice_row_col)
#    A  B
# 0  0  x
# 1  1  y

print(df_hetero_list)
#    A  B
# 0  0  x
# 1  1  y

print(df_hetero_bool)
#    A  B
# 0  0  x
# 2  2  z

print(s_hetero_scalar)
# A    0
# B    x
# Name: 0, dtype: object

print(s_hetero_col)
# 0    100
# 1      1
# 2      2
# Name: A, dtype: int64

print(df_hetero_col_list)
#    A  B
# 0  0  x
# 1  1  y
# 2  2  z
