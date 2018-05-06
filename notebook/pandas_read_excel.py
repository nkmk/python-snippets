import pandas as pd

df = pd.read_excel('data/src/sample.xlsx')

print(df)
#         A   B   C
# one    11  12  13
# two    21  22  23
# three  31  32  33

df_sheet_index = pd.read_excel('data/src/sample.xlsx', sheet_name=1)

print(df_sheet_index)
#        AA  BB  CC
# ONE    11  12  13
# TWO    21  22  23
# THREE  31  32  33

df_sheet_name = pd.read_excel('data/src/sample.xlsx', sheet_name='sheet2')

print(df_sheet_name)
#        AA  BB  CC
# ONE    11  12  13
# TWO    21  22  23
# THREE  31  32  33

df_sheet_multi = pd.read_excel('data/src/sample.xlsx', sheet_name=[0, 'sheet2'])

print(df_sheet_multi)
# OrderedDict([(0,         A   B   C
# one    11  12  13
# two    21  22  23
# three  31  32  33), ('sheet2',        AA  BB  CC
# ONE    11  12  13
# TWO    21  22  23
# THREE  31  32  33)])

print(type(df_sheet_multi))
# <class 'collections.OrderedDict'>

print(df_sheet_multi['sheet2'])
#        AA  BB  CC
# ONE    11  12  13
# TWO    21  22  23
# THREE  31  32  33

print(type(df_sheet_multi['sheet2']))
# <class 'pandas.core.frame.DataFrame'>

df_sheet_all = pd.read_excel('data/src/sample.xlsx', sheet_name=None)

print(df_sheet_all)
# OrderedDict([('sheet1',         A   B   C
# one    11  12  13
# two    21  22  23
# three  31  32  33), ('sheet2',        AA  BB  CC
# ONE    11  12  13
# TWO    21  22  23
# THREE  31  32  33)])

print(type(df_sheet_all))
# <class 'collections.OrderedDict'>

print(df_sheet_all['sheet1'])
#         A   B   C
# one    11  12  13
# two    21  22  23
# three  31  32  33

print(type(df_sheet_all['sheet1']))
# <class 'pandas.core.frame.DataFrame'>

df_header_index = pd.read_excel('data/src/sample.xlsx', header=None, index_col=1)

print(df_header_index)
#         0   2   3
# 1                
# A     NaN   B   C
# 11    one  12  13
# 21    two  22  23
# 31  three  32  33

print(df_header_index.index)
# Index(['A', 11, 21, 31], dtype='object', name=1)

print(df_header_index.columns)
# Int64Index([0, 2, 3], dtype='int64')

df_use_skip = pd.read_excel('data/src/sample.xlsx', usecols=[0, 1, 3], skiprows=[1], skip_footer=1)

print(df_use_skip)
#       A   C
# two  21  23
