import pandas as pd

print(pd.__version__)
# 1.5.3

df = pd.DataFrame({'a': [0, 1, 2], 'b': [3, 4, 5]}, index=['x', 'y', 'z'])
print(df)
#    a  b
# x  0  3
# y  1  4
# z  2  5

print(df.loc['x':'y']['a'])
# x    0
# y    1
# Name: a, dtype: int64

df.loc['x':'y']['a'] = 100
# /var/folders/rf/b7l8_vgj5mdgvghn_326rn_c0000gn/T/ipykernel_21852/3771299631.py:1: SettingWithCopyWarning: 
# A value is trying to be set on a copy of a slice from a DataFrame.
# Try using .loc[row_indexer,col_indexer] = value instead
# 
# See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
#   df.loc['x':'y']['a'] = 100

print(df)
#    a  b
# x  0  3
# y  1  4
# z  2  5

print(df.loc[['x', 'y']]['a'])
# x    0
# y    1
# Name: a, dtype: int64

df.loc[['x', 'y']]['a'] = 100
print(df)
#    a  b
# x  0  3
# y  1  4
# z  2  5

df.loc['x':'y', 'a'] = 100
print(df)
#      a  b
# x  100  3
# y  100  4
# z    2  5

df.loc[['x', 'y'], 'a'] = 0
print(df)
#    a  b
# x  0  3
# y  0  4
# z  2  5

df = pd.DataFrame({'a': [0, 1, 2], 'b': [3, 4, 5]}, index=['x', 'y', 'z'])
print(df)
#    a  b
# x  0  3
# y  1  4
# z  2  5

print(df.iloc[[0, 1]]['a'])
# x    0
# y    1
# Name: a, dtype: int64

# df.loc[[0, 1], 'a']
# KeyError: "None of [Int64Index([0, 1], dtype='int64')] are in the [index]"

# df.iloc[[0, 1], 'a']
# ValueError: Location based indexing can only have [integer, integer slice (START point is INCLUDED, END point is EXCLUDED), listlike of integers, boolean array] types

print(df.index[0])
# x

print(df.index[1])
# y

print(df.columns[0])
# a

print(df.columns[1])
# b

print(df.loc[[df.index[0], df.index[1]], 'a'])
# x    0
# y    1
# Name: a, dtype: int64

print(df.iloc[:2]['a'])
# x    0
# y    1
# Name: a, dtype: int64

print(df.loc[: df.index[2], 'a'])
# x    0
# y    1
# z    2
# Name: a, dtype: int64

print(df.loc[: df.index[2 - 1], 'a'])
# x    0
# y    1
# Name: a, dtype: int64

df = pd.DataFrame({'a': [0, 1, 2], 'b': [3, 4, 5]}, index=['x', 'y', 'z'])
print(df)
#    a  b
# x  0  3
# y  1  4
# z  2  5

df_slice = df.loc['x':'y']
print(df_slice)
#    a  b
# x  0  3
# y  1  4

print(df_slice['a'])
# x    0
# y    1
# Name: a, dtype: int64

df_slice['a'] = 100
# /var/folders/rf/b7l8_vgj5mdgvghn_326rn_c0000gn/T/ipykernel_21852/3718525832.py:1: SettingWithCopyWarning: 
# A value is trying to be set on a copy of a slice from a DataFrame.
# Try using .loc[row_indexer,col_indexer] = value instead
# 
# See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
#   df_slice['a'] = 100

print(df_slice)
#      a  b
# x  100  3
# y  100  4

print(df)
#    a  b
# x  0  3
# y  1  4
# z  2  5

df = pd.DataFrame({'a': [0, 1, 2], 'b': [3, 4, 5]}, index=['x', 'y', 'z'])
print(df)
#    a  b
# x  0  3
# y  1  4
# z  2  5

df_slice_copy = df.loc['x':'y'].copy()
print(df_slice_copy)
#    a  b
# x  0  3
# y  1  4

df_slice_copy['a'] = 100
print(df_slice_copy)
#      a  b
# x  100  3
# y  100  4

print(df)
#    a  b
# x  0  3
# y  1  4
# z  2  5
