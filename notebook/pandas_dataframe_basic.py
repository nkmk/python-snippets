import pandas as pd
import numpy as np

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

print(list(df_simple.columns))
# [0, 1, 2, 3]

print(type(list(df_simple.columns)))
# <class 'list'>

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

df.columns = ['Col_0', 'Col_1', 'Col_2', 'Col_3']

df.index = ['Row_0', 'Row_1', 'Row_2']

print(df)
#        Col_0  Col_1  Col_2  Col_3
# Row_0      0      1      2      3
# Row_1      4      5      6      7
# Row_2      8      9     10     11

# df.values = np.arange(12).reshape(3, 4) * 10
# AttributeError: can't set attribute

print(df['Col_1'])
# Row_0    1
# Row_1    5
# Row_2    9
# Name: Col_1, dtype: int64

print(type(df['Col_1']))
# <class 'pandas.core.series.Series'>

print(df.Col_1)
# Row_0    1
# Row_1    5
# Row_2    9
# Name: Col_1, dtype: int64

print(df.loc[:, 'Col_1'])
# Row_0    1
# Row_1    5
# Row_2    9
# Name: Col_1, dtype: int64

print(df.loc['Row_1', :])
# Col_0    4
# Col_1    5
# Col_2    6
# Col_3    7
# Name: Row_1, dtype: int64

print(type(df.loc['Row_1', :]))
# <class 'pandas.core.series.Series'>

print(df.loc['Row_1'])
# Col_0    4
# Col_1    5
# Col_2    6
# Col_3    7
# Name: Row_1, dtype: int64

print(df.loc[['Row_0', 'Row_2'], ['Col_1', 'Col_3']])
#        Col_1  Col_3
# Row_0      1      3
# Row_2      9     11

print(type(df.loc[['Row_0', 'Row_2'], ['Col_1', 'Col_3']]))
# <class 'pandas.core.frame.DataFrame'>

print(df.loc['Row_0', 'Col_1'])
# 1

print(type(df.loc['Row_0', 'Col_1']))
# <class 'numpy.int64'>

print(df.at['Row_0', 'Col_1'])
# 1

# print(df.at[:, 'Col_1'])
# TypeError: 'slice(None, None, None)' is an invalid key

print(df.iloc[[0, 2], [1, 3]])
#        Col_1  Col_3
# Row_0      1      3
# Row_2      9     11

print(df.iat[0, 1])
# 1

print(df.query('Col_0 > 2'))
#        Col_0  Col_1  Col_2  Col_3
# Row_1      4      5      6      7
# Row_2      8      9     10     11

df.loc[:, 'Col_1'] = [10, 50, 90]

print(df)
#        Col_0  Col_1  Col_2  Col_3
# Row_0      0     10      2      3
# Row_1      4     50      6      7
# Row_2      8     90     10     11

df.loc[:] = np.arange(12).reshape(3, 4) * 100

print(df)
#        Col_0  Col_1  Col_2  Col_3
# Row_0      0    100    200    300
# Row_1    400    500    600    700
# Row_2    800    900   1000   1100

# df.loc[:, 'Col_1'] = [10, 50, 90, 130]
# ValueError: Length of values does not match length of index

# df.loc[:] = np.arange(16).reshape(4, 4) * 100
# ValueError: cannot set using a slice indexer with a different length than the value

df_multi = pd.read_csv('data/src/sample_pandas_normal.csv', index_col=0)

print(df_multi)
#          age state  point
# name                     
# Alice     24    NY     64
# Bob       42    CA     92
# Charlie   18    CA     70
# Dave      68    TX     70
# Ellen     24    CA     88
# Frank     30    NY     57

print(df_multi.dtypes)
# age       int64
# state    object
# point     int64
# dtype: object
