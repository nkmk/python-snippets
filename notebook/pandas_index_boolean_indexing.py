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

l_bool = [True, False, False, True, True]
print(df[l_bool])
print(type(df[l_bool]))
#       col_0 col_1 col_2 col_3
# row_0    00    01    02    03
# row_3    30    31    32    33
# row_4    40    41    42    43
# <class 'pandas.core.frame.DataFrame'>

l_bool = [True, False, False, False, False]
print(df[l_bool])
print(type(df[l_bool]))
#       col_0 col_1 col_2 col_3
# row_0    00    01    02    03
# <class 'pandas.core.frame.DataFrame'>

# print(df[[True, False, False]])
# ValueError: Item wrong length 3 instead of 5.

s_bool = pd.Series([True, False, False, True, True], index=reversed(df.index))
print(s_bool)
# row_4     True
# row_3    False
# row_2    False
# row_1     True
# row_0     True
# dtype: bool

print(df[s_bool])
#       col_0 col_1 col_2 col_3
# row_0    00    01    02    03
# row_1    10    11    12    13
# row_4    40    41    42    43
# 
# /var/folders/rf/b7l8_vgj5mdgvghn_326rn_c0000gn/T/ipykernel_39787/3866325019.py:1: UserWarning: Boolean Series key will be reindexed to match DataFrame index.
#   print(df[s_bool])

s_bool_wrong = pd.Series([True, False, False, True, True],
                         index=['A', 'B', 'C', 'D', 'E'])
# print(df[s_bool_wrong])
# IndexingError: Unalignable boolean Series provided as indexer (index of the boolean Series and of the indexed object do not match).

s = df['col_0']
print(s)
# row_0    00
# row_1    10
# row_2    20
# row_3    30
# row_4    40
# Name: col_0, dtype: object

l_bool = [True, False, False, True, True]
print(s[l_bool])
print(type(s[l_bool]))
# row_0    00
# row_3    30
# row_4    40
# Name: col_0, dtype: object
# <class 'pandas.core.series.Series'>

l_bool = [True, False, False, False, False]
print(s[l_bool])
print(type(s[l_bool]))
# row_0    00
# Name: col_0, dtype: object
# <class 'pandas.core.series.Series'>

# print(s[[True, False, False]])
# IndexError: Boolean index has wrong length: 3 instead of 5

s_bool = pd.Series(l_bool, index=reversed(df.index))
print(s_bool)
# row_4     True
# row_3    False
# row_2    False
# row_1    False
# row_0    False
# dtype: bool

print(s[s_bool])
# row_4    40
# Name: col_0, dtype: object

s_bool_wrong = pd.Series([True, False, False, True, True],
                         index=['A', 'B', 'C', 'D', 'E'])
# print(s[s_bool_wrong])
# IndexingError: Unalignable boolean Series provided as indexer (index of the boolean Series and of the indexed object do not match).
