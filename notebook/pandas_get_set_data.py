import pandas as pd

print(pd.__version__)
# 2.0.3

df = pd.DataFrame({'col_0': ['00', '10', '20', '30', '40'],
                   'col_1': ['01', '11', '21', '31', '41'],
                   'col_2': ['02', '12', '22', '32', '42'],
                   'col_3': ['03', '13', '23', '33', '43']},
                  index=['row_0', 'row_1', 'row_2', 'row_3', 'row_4'])
print(df)
#       col_0 col_1 col_2 col_3
# row_0    00    01    02    03
# row_1    10    11    12    13
# row_2    20    21    22    23
# row_3    30    31    32    33
# row_4    40    41    42    43

print(df.at['row_1', 'col_2'])
# 12

df.at['row_1', 'col_2'] = '0'
print(df.at['row_1', 'col_2'])
# 0

print(df.iat[1, 2])
# 0

df.iat[1, 2] = '12'
print(df.iat[1, 2])
# 12

print(df.loc['row_1', 'col_2'])
# 12

print(df.iloc[1, 2])
# 12

df.loc['row_1', 'col_2'] = '0'
print(df.loc['row_1', 'col_2'])
# 0

df.iloc[1, 2] = '12'
print(df.iloc[1, 2])
# 12

print(df.loc['row_1':'row_3', ['col_2', 'col_0']])
#       col_2 col_0
# row_1    12    10
# row_2    22    20
# row_3    32    30

print(df.iloc[1:3, [2, 0]])
#       col_2 col_0
# row_1    12    10
# row_2    22    20

print(df.iloc[::2, [0, 3]])
#       col_0 col_3
# row_0    00    03
# row_2    20    23
# row_4    40    43

print(df.iloc[1::2, [0, 3]])
#       col_0 col_3
# row_1    10    13
# row_3    30    33

df.iloc[1:3, [2, 0]] = '0'
print(df)
#       col_0 col_1 col_2 col_3
# row_0    00    01    02    03
# row_1     0    11     0    13
# row_2     0    21     0    23
# row_3    30    31    32    33
# row_4    40    41    42    43

df.iloc[1:3, [2, 0]] = [['12', '10'], ['22', '20']]
print(df)
#       col_0 col_1 col_2 col_3
# row_0    00    01    02    03
# row_1    10    11    12    13
# row_2    20    21    22    23
# row_3    30    31    32    33
# row_4    40    41    42    43

print(df.loc['row_1', ['col_0', 'col_2']])
print(type(df.loc['row_1', ['col_0', 'col_2']]))
# col_0    10
# col_2    12
# Name: row_1, dtype: object
# <class 'pandas.core.series.Series'>

print(df.loc['row_1':'row_1', ['col_0', 'col_2']])
print(type(df.loc['row_1':'row_1', ['col_0', 'col_2']]))
#       col_0 col_2
# row_1    10    12
# <class 'pandas.core.frame.DataFrame'>

print(df.loc[['row_1'], ['col_0', 'col_2']])
print(type(df.loc[['row_1'], ['col_0', 'col_2']]))
#       col_0 col_2
# row_1    10    12
# <class 'pandas.core.frame.DataFrame'>

print(df['row_1':'row_3'])
#       col_0 col_1 col_2 col_3
# row_1    10    11    12    13
# row_2    20    21    22    23
# row_3    30    31    32    33

print(df[1:3])
#       col_0 col_1 col_2 col_3
# row_1    10    11    12    13
# row_2    20    21    22    23

print(df['col_1'])
# row_0    01
# row_1    11
# row_2    21
# row_3    31
# row_4    41
# Name: col_1, dtype: object

print(df[['col_1', 'col_3']])
#       col_1 col_3
# row_0    01    03
# row_1    11    13
# row_2    21    23
# row_3    31    33
# row_4    41    43

print(df.loc['row_2'])
# col_0    20
# col_1    21
# col_2    22
# col_3    23
# Name: row_2, dtype: object

print(df.iloc[[1, 3]])
#       col_0 col_1 col_2 col_3
# row_1    10    11    12    13
# row_3    30    31    32    33

print(df.loc[:, 'col_1':])
#       col_1 col_2 col_3
# row_0    01    02    03
# row_1    11    12    13
# row_2    21    22    23
# row_3    31    32    33
# row_4    41    42    43

print(df.iloc[:, 2])
# row_0    02
# row_1    12
# row_2    22
# row_3    32
# row_4    42
# Name: col_2, dtype: object

print(df.loc['row_2'])
print(type(df.loc['row_2']))
# col_0    20
# col_1    21
# col_2    22
# col_3    23
# Name: row_2, dtype: object
# <class 'pandas.core.series.Series'>

print(df.loc['row_2':'row_2'])
print(type(df.loc['row_2':'row_2']))
#       col_0 col_1 col_2 col_3
# row_2    20    21    22    23
# <class 'pandas.core.frame.DataFrame'>

print(df.loc[['row_2']])
print(type(df.loc[['row_2']]))
#       col_0 col_1 col_2 col_3
# row_2    20    21    22    23
# <class 'pandas.core.frame.DataFrame'>

l_bool = [True, False, False, True, False]

print(df.loc[l_bool, ['col_0', 'col_2']])
#       col_0 col_2
# row_0    00    02
# row_3    30    32

print(df.iloc[l_bool, [0, 2]])
#       col_0 col_2
# row_0    00    02
# row_3    30    32

l_bool_wrong = [True, False, False]

# print(df.loc[l_bool_wrong, ['col_0', 'col_2']])
# IndexError: Boolean index has wrong length: 3 instead of 5

s_bool = pd.Series([True, False, False, True, False], index=reversed(df.index))
print(s_bool)
# row_4     True
# row_3    False
# row_2    False
# row_1     True
# row_0    False
# dtype: bool

print(df.loc[s_bool, ['col_0', 'col_2']])
#       col_0 col_2
# row_1    10    12
# row_4    40    42

# print(df.iloc[s_bool, ['col_0', 'col_2']])
# ValueError: Location based indexing can only have [integer, integer slice (START point is INCLUDED, END point is EXCLUDED), listlike of integers, boolean array] types

s_bool_wrong = pd.Series([True, False, False], index=['row_0', 'row_1', 'row_2'])

# print(df.loc[s_bool_wrong, ['col_0', 'col_2']])
# IndexingError: Unalignable boolean Series provided as indexer (index of the boolean Series and of the indexed object do not match).

s_bool_wrong = pd.Series([True, False, False, True, False],
                         index=['row_0', 'row_1', 'row_2', 'row_3', 'XXX'])

# print(df.loc[s_bool_wrong, ['col_0', 'col_2']])
# IndexingError: Unalignable boolean Series provided as indexer (index of the boolean Series and of the indexed object do not match).

df_duplicated = df.rename(columns={'col_2': 'col_1'}, index={'row_3': 'row_2'})
print(df_duplicated)
#       col_0 col_1 col_1 col_3
# row_0    00    01    02    03
# row_1    10    11    12    13
# row_2    20    21    22    23
# row_2    30    31    32    33
# row_4    40    41    42    43

print(df_duplicated.at['row_2', 'col_1'])
print(type(df_duplicated.at['row_2', 'col_1']))
#       col_1 col_1
# row_2    21    22
# row_2    31    32
# <class 'pandas.core.frame.DataFrame'>

print(df_duplicated.loc[:'row_2', ['col_1', 'col_3']])
print(type(df_duplicated.loc[:'row_2', ['col_1', 'col_3']]))
#       col_1 col_1 col_3
# row_0    01    02    03
# row_1    11    12    13
# row_2    21    22    23
# row_2    31    32    33
# <class 'pandas.core.frame.DataFrame'>

print(df_duplicated.iat[2, 1])
# 21

print(df_duplicated.iloc[:2, [1, 3]])
#       col_1 col_3
# row_0    01    03
# row_1    11    13

print(df_duplicated.index.is_unique)
# False

print(df_duplicated.columns.is_unique)
# False

print(df.index[2])
# row_2

print(df.columns[2])
# col_2

print(df.index[1:4])
# Index(['row_1', 'row_2', 'row_3'], dtype='object')

print(df.columns[[1, 3]])
# Index(['col_1', 'col_3'], dtype='object')

print(df.at[df.index[2], 'col_2'])
# 22

print(df.loc[['row_0', 'row_3'], df.columns[[1, 3]]])
#       col_1 col_3
# row_0    01    03
# row_3    31    33

print(df['col_2'][2])
# 22

print(df.loc[['row_0', 'row_3']].iloc[:, [1, 3]])
#       col_1 col_3
# row_0    01    03
# row_3    31    33
