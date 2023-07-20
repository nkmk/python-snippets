import pandas as pd

print(pd.__version__)
# 2.0.3

# df_sjis = pd.read_csv('data/src/sample_header_shift_jis.csv')
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0x82 in position 8: invalid start byte

df_sjis = pd.read_csv('data/src/sample_header_shift_jis.csv',
                      encoding='shift_jis')
print(df_sjis)
#    a   b   c   d
# 0  あ  12  13  14
# 1  い  22  23  24
# 2  う  32  33  34

df_ignore = pd.read_csv('data/src/sample_header_shift_jis.csv',
                        encoding_errors='ignore')
print(df_ignore)
#     a   b   c   d
# 0 NaN  12  13  14
# 1 NaN  22  23  24
# 2 NaN  32  33  34

df_replace = pd.read_csv('data/src/sample_header_shift_jis.csv',
                         encoding_errors='replace')
print(df_replace)
#     a   b   c   d
# 0  ��  12  13  14
# 1  ��  22  23  24
# 2  ��  32  33  34

df_backslash = pd.read_csv('data/src/sample_header_shift_jis.csv',
                           encoding_errors='backslashreplace')
print(df_backslash)
#           a   b   c   d
# 0  \x82\xa0  12  13  14
# 1  \x82\xa2  22  23  24
# 2  \x82\xa4  32  33  34
