import pandas as pd

df_mix = pd.DataFrame({'col_int': [0, 1, 2], 'col_float': [0.1, 0.2, 0.3]}, index=['A', 'B', 'C'])
print(df_mix)
#    col_int  col_float
# A        0        0.1
# B        1        0.2
# C        2        0.3

print(df_mix.dtypes)
# col_int        int64
# col_float    float64
# dtype: object

print(df_mix['col_int'] + df_mix['col_float'])
# A    0.1
# B    1.2
# C    2.3
# dtype: float64

print(df_mix / 1)
#    col_int  col_float
# A      0.0        0.1
# B      1.0        0.2
# C      2.0        0.3

print((df_mix / 1).dtypes)
# col_int      float64
# col_float    float64
# dtype: object

print(df_mix * 1)
#    col_int  col_float
# A        0        0.1
# B        1        0.2
# C        2        0.3

print((df_mix * 1).dtypes)
# col_int        int64
# col_float    float64
# dtype: object

print(df_mix * 1.0)
#    col_int  col_float
# A      0.0        0.1
# B      1.0        0.2
# C      2.0        0.3

print((df_mix * 1.0).dtypes)
# col_int      float64
# col_float    float64
# dtype: object

print(df_mix.loc['A'])
# col_int      0.0
# col_float    0.1
# Name: A, dtype: float64

print(df_mix.T)
#              A    B    C
# col_int    0.0  1.0  2.0
# col_float  0.1  0.2  0.3

print(df_mix.T.dtypes)
# A    float64
# B    float64
# C    float64
# dtype: object

df_mix.at['A', 'col_int'] = 10.9
df_mix.at['A', 'col_float'] = 10
print(df_mix)
#    col_int  col_float
# A       10       10.0
# B        1        0.2
# C        2        0.3

print(df_mix.dtypes)
# col_int        int64
# col_float    float64
# dtype: object

# df_mix.at['A', 'col_int'] = 'abc'
# ValueError: invalid literal for int() with base 10: 'abc'
