import pandas as pd
import numpy as np

print(pd.__version__)
# 2.0.3

df_simple = pd.DataFrame(np.arange(12).reshape(3, 4))
print(df_simple)
#    0  1   2   3
# 0  0  1   2   3
# 1  4  5   6   7
# 2  8  9  10  11

print(df_simple.values)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(type(df_simple.values))
# <class 'numpy.ndarray'>

print(df_simple.columns)
# RangeIndex(start=0, stop=4, step=1)

print(type(df_simple.columns))
# <class 'pandas.core.indexes.range.RangeIndex'>

print(df_simple.index)
# RangeIndex(start=0, stop=3, step=1)

print(type(df_simple.index))
# <class 'pandas.core.indexes.range.RangeIndex'>

print(df_simple.columns.tolist())
# [0, 1, 2, 3]

print(type(df_simple.columns.tolist()))
# <class 'list'>

df = pd.DataFrame(np.arange(12).reshape(3, 4),
                  columns=['col_0', 'col_1', 'col_2', 'col_3'],
                  index=['row_0', 'row_1', 'row_2'])
print(df)
#        col_0  col_1  col_2  col_3
# row_0      0      1      2      3
# row_1      4      5      6      7
# row_2      8      9     10     11

print(df.columns)
# Index(['col_0', 'col_1', 'col_2', 'col_3'], dtype='object')

print(type(df.columns))
# <class 'pandas.core.indexes.base.Index'>

print(df.index)
# Index(['row_0', 'row_1', 'row_2'], dtype='object')

print(type(df.index))
# <class 'pandas.core.indexes.base.Index'>

print(df.columns.tolist())
# ['col_0', 'col_1', 'col_2', 'col_3']

print(type(df.columns.tolist()))
# <class 'list'>

print(df.columns[0])
# col_0

# df.columns[0] = 'Col_0'
# TypeError: Index does not support mutable operations

print(df['col_1'])
# row_0    1
# row_1    5
# row_2    9
# Name: col_1, dtype: int64

print(type(df['col_1']))
# <class 'pandas.core.series.Series'>

print(df.col_1)
# row_0    1
# row_1    5
# row_2    9
# Name: col_1, dtype: int64

print(df.loc['row_1'])
# col_0    4
# col_1    5
# col_2    6
# col_3    7
# Name: row_1, dtype: int64

print(df.loc[['row_0', 'row_2'], ['col_1', 'col_3']])
#        col_1  col_3
# row_0      1      3
# row_2      9     11

print(type(df.loc[['row_0', 'row_2'], ['col_1', 'col_3']]))
# <class 'pandas.core.frame.DataFrame'>

print(df.at['row_0', 'col_1'])
# 1

print(type(df.at['row_0', 'col_1']))
# <class 'numpy.int64'>

print(df.iloc[[0, 2], [1, 3]])
#        col_1  col_3
# row_0      1      3
# row_2      9     11

print(df.iat[0, 1])
# 1

print(df.query('col_0 > 2'))
#        col_0  col_1  col_2  col_3
# row_1      4      5      6      7
# row_2      8      9     10     11

df.at['row_1', 'col_2'] = 600
print(df)
#        col_0  col_1  col_2  col_3
# row_0      0      1      2      3
# row_1      4      5    600      7
# row_2      8      9     10     11

df.iloc[:, 1] = [10, 50, 90]
print(df)
#        col_0  col_1  col_2  col_3
# row_0      0     10      2      3
# row_1      4     50    600      7
# row_2      8     90     10     11

# df.iloc[:, 1] = [10, 50, 90, 130]
# ValueError: Length of values (4) does not match length of index (3)

df_multi = pd.DataFrame({'col_0': [0, 1, 2],
                         'col_1': [0.0, 0.1, 0.2],
                         'col_2': ['A', 'B', 'C']})
print(df_multi)
#    col_0  col_1 col_2
# 0      0    0.0     A
# 1      1    0.1     B
# 2      2    0.2     C

print(df_multi.dtypes)
# col_0      int64
# col_1    float64
# col_2     object
# dtype: object
