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

print(df['col_2'])
print(type(df['col_2']))
# row_0    02
# row_1    12
# row_2    22
# row_3    32
# row_4    42
# Name: col_2, dtype: object
# <class 'pandas.core.series.Series'>

print(df.col_2)
# row_0    02
# row_1    12
# row_2    22
# row_3    32
# row_4    42
# Name: col_2, dtype: object

print(df[['col_2', 'col_0']])
print(type(df[['col_2', 'col_0']]))
#       col_2 col_0
# row_0    02    00
# row_1    12    10
# row_2    22    20
# row_3    32    30
# row_4    42    40
# <class 'pandas.core.frame.DataFrame'>

print(df[['col_2']])
print(type(df[['col_2']]))
#       col_2
# row_0    02
# row_1    12
# row_2    22
# row_3    32
# row_4    42
# <class 'pandas.core.frame.DataFrame'>

print(df.loc[:, 'col_1':'col_3'])
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

print(df[1:4])
print(type(df[1:4]))
#       col_0 col_1 col_2 col_3
# row_1    10    11    12    13
# row_2    20    21    22    23
# row_3    30    31    32    33
# <class 'pandas.core.frame.DataFrame'>

print(df[:-3])
#       col_0 col_1 col_2 col_3
# row_0    00    01    02    03
# row_1    10    11    12    13

print(df[::2])
#       col_0 col_1 col_2 col_3
# row_0    00    01    02    03
# row_2    20    21    22    23
# row_4    40    41    42    43

print(df[1::2])
#       col_0 col_1 col_2 col_3
# row_1    10    11    12    13
# row_3    30    31    32    33

# print(df[1])
# KeyError: 1

print(df[1:2])
print(type(df[1:2]))
#       col_0 col_1 col_2 col_3
# row_1    10    11    12    13
# <class 'pandas.core.frame.DataFrame'>

print(df['row_1':'row_3'])
#       col_0 col_1 col_2 col_3
# row_1    10    11    12    13
# row_2    20    21    22    23
# row_3    30    31    32    33

print(df.loc[['row_1', 'row_3']])
#       col_0 col_1 col_2 col_3
# row_1    10    11    12    13
# row_3    30    31    32    33

print(df.iloc[1])
# col_0    10
# col_1    11
# col_2    12
# col_3    13
# Name: row_1, dtype: object

print(df['col_1']['row_2'])
# 21

print(df['row_1':'row_3'][['col_1', 'col_3']])
#       col_1 col_3
# row_1    11    13
# row_2    21    23
# row_3    31    33

print(df.at['row_2', 'col_1'])
# 21

print(df.loc['row_1':'row_3', ['col_1', 'col_3']])
#       col_1 col_3
# row_1    11    13
# row_2    21    23
# row_3    31    33
