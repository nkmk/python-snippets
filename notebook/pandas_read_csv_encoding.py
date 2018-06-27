import pandas as pd

# df_sjis = pd.read_csv('data/src/sample_header_shift_jis.csv')
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0x82 in position 0: invalid start byte

df_sjis = pd.read_csv('data/src/sample_header_shift_jis.csv',
                      encoding='shift_jis')
print(df_sjis)
#    a   b   c   d
# 0  あ  12  13  14
# 1  い  22  23  24
# 2  う  32  33  34
