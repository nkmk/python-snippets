import pandas as pd

print(pd.__version__)
# 2.1.4

df = pd.DataFrame({'col0': [0, 1, 2], 'col1': [3, 4, 5], 'col2': [6, 7, 8]},
                  index=['row0', 'row1', 'row2'])
print(df)
#       col0  col1  col2
# row0     0     3     6
# row1     1     4     7
# row2     2     5     8

print(df['col0'])
# row0    0
# row1    1
# row2    2
# Name: col0, dtype: int64

print(df.loc[:, 'col0'])
# row0    0
# row1    1
# row2    2
# Name: col0, dtype: int64

print(df.iloc[:, 0])
# row0    0
# row1    1
# row2    2
# Name: col0, dtype: int64

print(df.iloc[[0, 2], 0])
# row0    0
# row2    2
# Name: col0, dtype: int64

print(df.iloc[:2, 0])
# row0    0
# row1    1
# Name: col0, dtype: int64

print(df.loc[:, ['col0']])
#       col0
# row0     0
# row1     1
# row2     2

print(df.iloc[:, :1])
#       col0
# row0     0
# row1     1
# row2     2

print(df.loc['row0', :])
# col0    0
# col1    3
# col2    6
# Name: row0, dtype: int64

print(df.iloc[0, :])
# col0    0
# col1    3
# col2    6
# Name: row0, dtype: int64

print(df.loc['row0'])
# col0    0
# col1    3
# col2    6
# Name: row0, dtype: int64

print(df.iloc[0])
# col0    0
# col1    3
# col2    6
# Name: row0, dtype: int64

print(df.iloc[0, [0, 2]])
# col0    0
# col2    6
# Name: row0, dtype: int64

print(df.iloc[0, :2])
# col0    0
# col1    3
# Name: row0, dtype: int64

print(df.loc[['row0']])
#       col0  col1  col2
# row0     0     3     6

print(df.iloc[:1])
#       col0  col1  col2
# row0     0     3     6

df_multi = pd.DataFrame({'col0': [0, 1, 2], 'col1': [0.0, 0.1, 0.2]},
                        index=['row0', 'row1', 'row2'])
print(df_multi)
#       col0  col1
# row0     0   0.0
# row1     1   0.1
# row2     2   0.2

s_row = df_multi.loc['row2']
print(s_row)
# col0    2.0
# col1    0.2
# Name: row2, dtype: float64

df_multi['col2'] = ['a', 'b', 'c']
print(df_multi)
#       col0  col1 col2
# row0     0   0.0    a
# row1     1   0.1    b
# row2     2   0.2    c

print(df_multi.dtypes)
# col0      int64
# col1    float64
# col2     object
# dtype: object

s_row = df_multi.loc['row2']
print(s_row)
# col0      2
# col1    0.2
# col2      c
# Name: row2, dtype: object

print(type(s_row['col0']))
# <class 'numpy.int64'>

print(type(s_row['col1']))
# <class 'numpy.float64'>

print(type(s_row['col2']))
# <class 'str'>

df = pd.DataFrame({'col0': [0, 1, 2], 'col1': [3, 4, 5], 'col2': [6, 7, 8]},
                  index=['row0', 'row1', 'row2'])
print(df)
#       col0  col1  col2
# row0     0     3     6
# row1     1     4     7
# row2     2     5     8

s = df['col0']
s['row0'] = 10
print(s)
# row0    10
# row1     1
# row2     2
# Name: col0, dtype: int64

print(df)
#       col0  col1  col2
# row0    10     3     6
# row1     1     4     7
# row2     2     5     8

s_copy = df['col1'].copy()
s_copy['row0'] = 100
print(s_copy)
# row0    100
# row1      4
# row2      5
# Name: col1, dtype: int64

print(df)
#       col0  col1  col2
# row0    10     3     6
# row1     1     4     7
# row2     2     5     8

s_list = df.loc[['row0', 'row2'], 'col2']
s_list['row0'] = 1000
print(s_list)
# row0    1000
# row2       8
# Name: col2, dtype: int64

print(df)
#       col0  col1  col2
# row0    10     3     6
# row1     1     4     7
# row2     2     5     8
