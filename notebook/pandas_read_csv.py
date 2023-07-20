import pandas as pd

print(pd.__version__)
# 2.0.3

df = pd.read_csv('data/src/sample.csv')
print(df)
#    11  12  13  14
# 0  21  22  23  24
# 1  31  32  33  34

print(df.columns)
# Index(['11', '12', '13', '14'], dtype='object')

df_none = pd.read_csv('data/src/sample.csv', header=None)
print(df_none)
#     0   1   2   3
# 0  11  12  13  14
# 1  21  22  23  24
# 2  31  32  33  34

df_names = pd.read_csv('data/src/sample.csv', names=['A', 'B', 'C', 'D'])
print(df_names)
#     A   B   C   D
# 0  11  12  13  14
# 1  21  22  23  24
# 2  31  32  33  34

df = pd.read_csv('data/src/sample_header.csv')
print(df)
#     a   b   c   d
# 0  11  12  13  14
# 1  21  22  23  24
# 2  31  32  33  34

df_names = pd.read_csv('data/src/sample_header.csv', names=['A', 'B', 'C', 'D'])
print(df_names)
#     A   B   C   D
# 0   a   b   c   d
# 1  11  12  13  14
# 2  21  22  23  24
# 3  31  32  33  34

df_names_0 = pd.read_csv('data/src/sample_header.csv',
                         header=0, names=['A', 'B', 'C', 'D'])
print(df_names_0)
#     A   B   C   D
# 0  11  12  13  14
# 1  21  22  23  24
# 2  31  32  33  34

df_header_2 = pd.read_csv('data/src/sample_header.csv', header=2)
print(df_header_2)
#    21  22  23  24
# 0  31  32  33  34

df = pd.read_csv('data/src/sample_header_index.csv')
print(df)
#   Unnamed: 0   a   b   c   d
# 0        ONE  11  12  13  14
# 1        TWO  21  22  23  24
# 2      THREE  31  32  33  34

print(df.index)
# RangeIndex(start=0, stop=3, step=1)

df_index_col = pd.read_csv('data/src/sample_header_index.csv', index_col=0)
print(df_index_col)
#         a   b   c   d
# ONE    11  12  13  14
# TWO    21  22  23  24
# THREE  31  32  33  34

print(df_index_col.index)
# Index(['ONE', 'TWO', 'THREE'], dtype='object')

df_usecols = pd.read_csv('data/src/sample_header.csv', usecols=[1, 3])
print(df_usecols)
#     b   d
# 0  12  14
# 1  22  24
# 2  32  34

df_usecols = pd.read_csv('data/src/sample_header.csv', usecols=['a', 'c'])
print(df_usecols)
#     a   c
# 0  11  13
# 1  21  23
# 2  31  33

df_usecols = pd.read_csv('data/src/sample_header.csv',
                         usecols=lambda x: x != 'b')
print(df_usecols)
#     a   c   d
# 0  11  13  14
# 1  21  23  24
# 2  31  33  34

df_usecols = pd.read_csv('data/src/sample_header.csv',
                         usecols=lambda x: x not in ['a', 'c'])
print(df_usecols)
#     b   d
# 0  12  14
# 1  22  24
# 2  32  34

df = pd.read_csv('data/src/sample.csv', header=None)
print(df)
#     0   1   2   3
# 0  11  12  13  14
# 1  21  22  23  24
# 2  31  32  33  34

df_skiprows = pd.read_csv('data/src/sample.csv', header=None, skiprows=2)
print(df_skiprows)
#     0   1   2   3
# 0  31  32  33  34

df_skiprows = pd.read_csv('data/src/sample.csv', header=None, skiprows=[0, 2])
print(df_skiprows)
#     0   1   2   3
# 0  21  22  23  24

df_skiprows = pd.read_csv('data/src/sample.csv', header=None,
                          skiprows=lambda x: x not in [0, 2])
print(df_skiprows)
#     0   1   2   3
# 0  11  12  13  14
# 1  31  32  33  34

df_skiprows = pd.read_csv('data/src/sample_header.csv', skiprows=2)
print(df_skiprows)
#    21  22  23  24
# 0  31  32  33  34

df_skiprows = pd.read_csv('data/src/sample_header.csv', skiprows=[1, 3])
print(df_skiprows)
#     a   b   c   d
# 0  21  22  23  24

df_skipfooter = pd.read_csv('data/src/sample.csv', header=None,
                            skipfooter=1, engine='python')
print(df_skipfooter)
#     0   1   2   3
# 0  11  12  13  14
# 1  21  22  23  24

df_nrows = pd.read_csv('data/src/sample.csv', header=None, nrows=2)
print(df_nrows)
#     0   1   2   3
# 0  11  12  13  14
# 1  21  22  23  24

df_nrows = pd.read_csv('data/src/sample_header.csv', nrows=2)
print(df_nrows)
#     a   b   c   d
# 0  11  12  13  14
# 1  21  22  23  24

df_zip = pd.read_csv('data/src/sample_header.csv.zip')
print(df_zip)
#     a   b   c   d
# 0  11  12  13  14
# 1  21  22  23  24
# 2  31  32  33  34

df_web = pd.read_csv(
    'https://raw.githubusercontent.com/nkmk/python-snippets/master/notebook/data/src/sample_header.csv'
)
print(df_web)
#     a   b   c   d
# 0  11  12  13  14
# 1  21  22  23  24
# 2  31  32  33  34

df_tsv_sep = pd.read_csv('data/src/sample_header_index.tsv', index_col=0, sep='\t')
print(df_tsv_sep)
#         a   b   c   d
# ONE    11  12  13  14
# TWO    21  22  23  24
# THREE  31  32  33  34

df_tsv = pd.read_table('data/src/sample_header_index.tsv', index_col=0)
print(df_tsv)
#         a   b   c   d
# ONE    11  12  13  14
# TWO    21  22  23  24
# THREE  31  32  33  34
