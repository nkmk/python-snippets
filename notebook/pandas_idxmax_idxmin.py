import pandas as pd

df = pd.DataFrame({'col1': [0, 3, 2, 3], 'col2': [4, 0, 2, 1]},
                   index=['a', 'b', 'c', 'd'])

print(df)
#    col1  col2
# a     0     4
# b     3     0
# c     2     2
# d     3     1

print(df['col1'])
# a    0
# b    3
# c    2
# d    3
# Name: col1, dtype: int64

print(type(df['col1']))
# <class 'pandas.core.series.Series'>

print(df['col1'].max())
# 3

print(df['col1'].min())
# 0

print(df.max())
# col1    3
# col2    4
# dtype: int64

print(df.min())
# col1    0
# col2    0
# dtype: int64

print(df.max(axis=1))
# a    4
# b    3
# c    2
# d    3
# dtype: int64

print(df.min(axis=1))
# a    0
# b    0
# c    2
# d    1
# dtype: int64

print(type(df.max()))
# <class 'pandas.core.series.Series'>

print(df['col1'].idxmax())
# b

print(df['col1'].idxmin())
# a

print(df['col1'] == df['col1'].max())
# a    False
# b     True
# c    False
# d     True
# Name: col1, dtype: bool

print(df['col1'][df['col1'] == df['col1'].max()])
# b    3
# d    3
# Name: col1, dtype: int64

print(df['col1'][df['col1'] == df['col1'].max()].index)
# Index(['b', 'd'], dtype='object')

print(df['col1'][df['col1'] == df['col1'].max()].index.values)
# ['b' 'd']

print(type(df['col1'][df['col1'] == df['col1'].max()].index.values))
# <class 'numpy.ndarray'>

print(list(df['col1'][df['col1'] == df['col1'].max()].index))
# ['b', 'd']

print(type(list(df['col1'][df['col1'] == df['col1'].max()].index)))
# <class 'list'>

print(df['col1'][df['col1'] == df['col1'].min()].index.values)
# ['a']

print(df.loc['a'])
# col1    0
# col2    4
# Name: a, dtype: int64

print(df.loc['a'].idxmax())
# col2

print(df.loc['a'].idxmin())
# col1

print(df.idxmax())
# col1    b
# col2    a
# dtype: object

print(df.idxmin())
# col1    a
# col2    b
# dtype: object

print(df.apply(lambda x: list(x[x == x.max()].index)))
# col1    [b, d]
# col2       [a]
# dtype: object

print(df.apply(lambda x: list(x[x == x.min()].index)))
# col1    [a]
# col2    [b]
# dtype: object

print(df.idxmax(axis=1))
# a    col2
# b    col1
# c    col1
# d    col1
# dtype: object

print(df.idxmin(axis=1))
# a    col1
# b    col2
# c    col1
# d    col2
# dtype: object

print(df.apply(lambda x: list(x[x == x.max()].index), axis=1))
# a          [col2]
# b          [col1]
# c    [col1, col2]
# d          [col1]
# dtype: object

print(df.apply(lambda x: list(x[x == x.min()].index), axis=1))
# a          [col1]
# b          [col2]
# c    [col1, col2]
# d          [col2]
# dtype: object

df_nan = df.copy()
df_nan.at['b'] = pd.np.nan

print(df_nan)
#    col1  col2
# a   0.0   4.0
# b   NaN   NaN
# c   2.0   2.0
# d   3.0   1.0

print(df_nan.idxmax())
# col1    d
# col2    a
# dtype: object

print(df_nan.idxmin())
# col1    a
# col2    d
# dtype: object

print(df_nan.idxmax(axis=1))
# a    col2
# b     NaN
# c    col1
# d    col1
# dtype: object

print(df_nan.idxmin(axis=1))
# a    col1
# b     NaN
# c    col1
# d    col2
# dtype: object

print(df_nan.idxmax(skipna=False))
# col1   NaN
# col2   NaN
# dtype: float64

print(df_nan.idxmin(skipna=False))
# col1   NaN
# col2   NaN
# dtype: float64

print(df_nan.idxmax(axis=1, skipna=False))
# a    col2
# b     NaN
# c    col1
# d    col1
# dtype: object

print(df_nan.idxmin(axis=1, skipna=False))
# a    col1
# b     NaN
# c    col1
# d    col2
# dtype: object

print(df_nan['col1'].idxmax())
# d

print(df_nan['col1'].idxmin())
# a

print(df_nan['col1'].idxmax(skipna=False))
# nan

print(df_nan['col1'].idxmin(skipna=False))
# nan
