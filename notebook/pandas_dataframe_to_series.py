import pandas as pd

df = pd.DataFrame({'col0': [0, 1, 2], 'col1': [0.0, 0.1, 0.2], 'col2': ['a', 'b', 'c']},
                  index=['row0', 'row1', 'row2'])
print(df)
#       col0  col1 col2
# row0     0   0.0    a
# row1     1   0.1    b
# row2     2   0.2    c

print(df.dtypes)
# col0      int64
# col1    float64
# col2     object
# dtype: object

s = df['col1']
print(s)
# row0    0.0
# row1    0.1
# row2    0.2
# Name: col1, dtype: float64

print(type(s))
# <class 'pandas.core.series.Series'>

print(s.dtype)
# float64

print(s.index)
# Index(['row0', 'row1', 'row2'], dtype='object')

print(s.name)
# col1

print(df.loc[:, 'col1'])
# row0    0.0
# row1    0.1
# row2    0.2
# Name: col1, dtype: float64

print(df.iloc[:, 2])
# row0    a
# row1    b
# row2    c
# Name: col2, dtype: object

print(df.iloc[[0, 2], 2])
# row0    a
# row2    c
# Name: col2, dtype: object

print(df.iloc[:2, 2])
# row0    a
# row1    b
# Name: col2, dtype: object

df_only = df[['col1']]
print(df_only)
#       col1
# row0   0.0
# row1   0.1
# row2   0.2

print(type(df_only))
# <class 'pandas.core.frame.DataFrame'>

df_only2 = df.iloc[:, 1:2]
print(df_only2)
#       col1
# row0   0.0
# row1   0.1
# row2   0.2

print(type(df_only2))
# <class 'pandas.core.frame.DataFrame'>

s_r = df.loc['row1', :]
print(s_r)
# col0      1
# col1    0.1
# col2      b
# Name: row1, dtype: object

print(type(s_r))
# <class 'pandas.core.series.Series'>

print(s_r.dtype)
# object

print(s_r.index)
# Index(['col0', 'col1', 'col2'], dtype='object')

print(s_r.name)
# row1

print(df.loc['row1'])
# col0      1
# col1    0.1
# col2      b
# Name: row1, dtype: object

print(df.iloc[2, [0, 2]])
# col0    2
# col2    c
# Name: row2, dtype: object

df_only_r = df.iloc[[1]]
print(df_only_r)
#       col0  col1 col2
# row1     1   0.1    b

print(type(df_only_r))
# <class 'pandas.core.frame.DataFrame'>

df_only_r2 = df[1:2]
print(df_only_r2)
#       col0  col1 col2
# row1     1   0.1    b

print(type(df_only_r2))
# <class 'pandas.core.frame.DataFrame'>

print(s_r[0])
# 1

print(type(s_r[0]))
# <class 'numpy.int64'>

print(s_r[1])
# 0.1

print(type(s_r[1]))
# <class 'numpy.float64'>

print(s_r[2])
# b

print(type(s_r[2]))
# <class 'str'>

df_n = df[['col0', 'col1']]
print(df_n)
#       col0  col1
# row0     0   0.0
# row1     1   0.1
# row2     2   0.2

print(df_n.dtypes)
# col0      int64
# col1    float64
# dtype: object

s_n_r = df_n.iloc[1]
print(s_n_r)
# col0    1.0
# col1    0.1
# Name: row1, dtype: float64

print(s_n_r[0])
# 1.0

print(type(s_n_r[0]))
# <class 'numpy.float64'>

print(s_n_r[1])
# 0.1

print(type(s_n_r[1]))
# <class 'numpy.float64'>

print(df)
#       col0  col1 col2
# row0     0   0.0    a
# row1     1   0.1    b
# row2     2   0.2    c

s = df['col0']
print(s)
# row0    0
# row1    1
# row2    2
# Name: col0, dtype: int64

df.iat[0, 0] = 100
print(df)
#       col0  col1 col2
# row0   100   0.0    a
# row1     1   0.1    b
# row2     2   0.2    c

print(s)
# row0    100
# row1      1
# row2      2
# Name: col0, dtype: int64

s_copy = df['col1'].copy()
print(s_copy)
# row0    0.0
# row1    0.1
# row2    0.2
# Name: col1, dtype: float64

df.iat[0, 1] = 100
print(df)
#       col0   col1 col2
# row0   100  100.0    a
# row1     1    0.1    b
# row2     2    0.2    c

print(s_copy)
# row0    0.0
# row1    0.1
# row2    0.2
# Name: col1, dtype: float64

s_l = df.loc[['row0', 'row2'], 'col2']
print(s_l)
# row0    a
# row2    c
# Name: col2, dtype: object

df.iat[0, 2] = 'XXX'
print(df)
#       col0   col1 col2
# row0   100  100.0  XXX
# row1     1    0.1    b
# row2     2    0.2    c

print(s_l)
# row0    a
# row2    c
# Name: col2, dtype: object
