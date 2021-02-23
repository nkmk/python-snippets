import pandas as pd

print(pd.__version__)
# 1.2.2

df = pd.read_excel('data/src/sample.xlsx', index_col=0)
print(df)
#         A   B   C
# one    11  12  13
# two    21  22  23
# three  31  32  33

print(type(df))
# <class 'pandas.core.frame.DataFrame'>

df_sheet_index = pd.read_excel('data/src/sample.xlsx', sheet_name=0, index_col=0)
print(df_sheet_index)
#         A   B   C
# one    11  12  13
# two    21  22  23
# three  31  32  33

df_sheet_name = pd.read_excel('data/src/sample.xlsx', sheet_name='sheet2', index_col=0)
print(df_sheet_name)
#        AA  BB  CC
# ONE    11  12  13
# TWO    21  22  23
# THREE  31  32  33

df_sheet_multi = pd.read_excel('data/src/sample.xlsx', sheet_name=[0, 'sheet2'], index_col=0)
print(type(df_sheet_multi))
# <class 'dict'>

print(len(df_sheet_multi))
# 2

print(df_sheet_multi.keys())
# dict_keys([0, 'sheet2'])

print(df_sheet_multi[0])
#         A   B   C
# one    11  12  13
# two    21  22  23
# three  31  32  33

print(type(df_sheet_multi[0]))
# <class 'pandas.core.frame.DataFrame'>

print(df_sheet_multi['sheet2'])
#        AA  BB  CC
# ONE    11  12  13
# TWO    21  22  23
# THREE  31  32  33

print(type(df_sheet_multi['sheet2']))
# <class 'pandas.core.frame.DataFrame'>

df_sheet_all = pd.read_excel('data/src/sample.xlsx', sheet_name=None, index_col=0)
print(type(df_sheet_all))
# <class 'dict'>

print(df_sheet_all.keys())
# dict_keys(['sheet1', 'sheet2'])

df_header_index = pd.read_excel('data/src/sample.xlsx', header=None, index_col=None)
print(df_header_index)
#        0   1   2   3
# 0    NaN   A   B   C
# 1    one  11  12  13
# 2    two  21  22  23
# 3  three  31  32  33

print(df_header_index.columns)
# Int64Index([0, 1, 2, 3], dtype='int64')

print(df_header_index.index)
# RangeIndex(start=0, stop=4, step=1)

df_default = pd.read_excel('data/src/sample.xlsx')
print(df_default)
#   Unnamed: 0   A   B   C
# 0        one  11  12  13
# 1        two  21  22  23
# 2      three  31  32  33

print(df_default.columns)
# Index(['Unnamed: 0', 'A', 'B', 'C'], dtype='object')

print(df_default.index)
# RangeIndex(start=0, stop=3, step=1)

print(pd.read_excel('data/src/sample.xlsx', index_col=0))
#         A   B   C
# one    11  12  13
# two    21  22  23
# three  31  32  33

df_use_skip = pd.read_excel('data/src/sample.xlsx', index_col=0,
                            usecols=[0, 1, 3], skiprows=[1], skipfooter=1)
print(df_use_skip)
#       A   C
# two  21  23
