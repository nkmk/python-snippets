import pandas as pd

print(pd.__version__)
# 2.0.3

df_mix = pd.DataFrame({'col_int': [0, 1, 2], 'col_float': [0.0, 0.1, 0.2]}, index=['A', 'B', 'C'])
print(df_mix)
#    col_int  col_float
# A        0        0.0
# B        1        0.1
# C        2        0.2

print(df_mix.dtypes)
# col_int        int64
# col_float    float64
# dtype: object

print(df_mix['col_int'] + df_mix['col_float'])
# A    0.0
# B    1.1
# C    2.2
# dtype: float64

print(df_mix / 1)
#    col_int  col_float
# A      0.0        0.0
# B      1.0        0.1
# C      2.0        0.2

print((df_mix / 1).dtypes)
# col_int      float64
# col_float    float64
# dtype: object

print(df_mix * 1)
#    col_int  col_float
# A        0        0.0
# B        1        0.1
# C        2        0.2

print((df_mix * 1).dtypes)
# col_int        int64
# col_float    float64
# dtype: object

print(df_mix * 1.0)
#    col_int  col_float
# A      0.0        0.0
# B      1.0        0.1
# C      2.0        0.2

print((df_mix * 1.0).dtypes)
# col_int      float64
# col_float    float64
# dtype: object

print(df_mix.loc['A'])
# col_int      0.0
# col_float    0.0
# Name: A, dtype: float64

print(df_mix.T)
#              A    B    C
# col_int    0.0  1.0  2.0
# col_float  0.0  0.1  0.2

print(df_mix.T.dtypes)
# A    float64
# B    float64
# C    float64
# dtype: object

df_mix.at['A', 'col_int'] = 10.1
df_mix.at['A', 'col_float'] = 10
print(df_mix)
#    col_int  col_float
# A     10.1       10.0
# B      1.0        0.1
# C      2.0        0.2

print(df_mix.dtypes)
# col_int      float64
# col_float    float64
# dtype: object

df_mix.at['A', 'col_float'] = 'abc'
print(df_mix)
#    col_int col_float
# A     10.1       abc
# B      1.0       0.1
# C      2.0       0.2

print(df_mix.dtypes)
# col_int      float64
# col_float     object
# dtype: object

print(df_mix.applymap(type))
#            col_int        col_float
# A  <class 'float'>    <class 'str'>
# B  <class 'float'>  <class 'float'>
# C  <class 'float'>  <class 'float'>
