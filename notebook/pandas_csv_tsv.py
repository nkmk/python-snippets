import pandas as pd

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

df_names = pd.read_csv('data/src/sample.csv', names=('A', 'B', 'C', 'D'))
print(df_names)
#     A   B   C   D
# 0  11  12  13  14
# 1  21  22  23  24
# 2  31  32  33  34

df_header = pd.read_csv('data/src/sample_header.csv')
print(df_header)
#     a   b   c   d
# 0  11  12  13  14
# 1  21  22  23  24
# 2  31  32  33  34

df_header_0 = pd.read_csv('data/src/sample_header.csv', header=0)
print(df_header_0)
#     a   b   c   d
# 0  11  12  13  14
# 1  21  22  23  24
# 2  31  32  33  34

df_header_index = pd.read_csv('data/src/sample_header_index.csv')
print(df_header_index)
#   Unnamed: 0   a   b   c   d
# 0        ONE  11  12  13  14
# 1        TWO  21  22  23  24
# 2      THREE  31  32  33  34

print(df_header_index.columns)
# Index(['Unnamed: 0', 'a', 'b', 'c', 'd'], dtype='object')

df_header_index_col = pd.read_csv('data/src/sample_header_index.csv', index_col=0)
print(df_header_index_col)
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

df_tsv_sep = pd.read_csv('data/src/sample_header_index.tsv', index_col=0, sep='\t')
print(df_tsv_sep)
#         a   b   c   d
# ONE    11  12  13  14
# TWO    21  22  23  24
# THREE  31  32  33  34
