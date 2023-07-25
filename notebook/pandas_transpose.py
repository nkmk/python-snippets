import pandas as pd

print(pd.__version__)
# 2.0.3

df = pd.DataFrame({'X': [0, 1, 2], 'Y': [3, 4, 5]}, index=['A', 'B', 'C'])
print(df)
#    X  Y
# A  0  3
# B  1  4
# C  2  5

print(df.T)
#    A  B  C
# X  0  1  2
# Y  3  4  5

print(df.transpose())
#    A  B  C
# X  0  1  2
# Y  3  4  5

df = df.T
print(df)
#    A  B  C
# X  0  1  2
# Y  3  4  5

df = pd.DataFrame({'X': [0, 1, 2], 'Y': [3, 4, 5]}, index=['A', 'B', 'C'])
print(df)
#    X  Y
# A  0  3
# B  1  4
# C  2  5

print(df.dtypes)
# X    int64
# Y    int64
# dtype: object

print(df.T)
#    A  B  C
# X  0  1  2
# Y  3  4  5

print(df.T.dtypes)
# A    int64
# B    int64
# C    int64
# dtype: object

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

print(df_mix.T)
#              A    B    C
# col_int    0.0  1.0  2.0
# col_float  0.1  0.2  0.3

print(df_mix.T.dtypes)
# A    float64
# B    float64
# C    float64
# dtype: object

print(df_mix.T.T)
#    col_int  col_float
# A      0.0        0.1
# B      1.0        0.2
# C      2.0        0.3

print(df_mix.T.T.dtypes)
# col_int      float64
# col_float    float64
# dtype: object

df_mix2 = pd.DataFrame({'col_int': [0, 1, 2], 'col_float': [0.1, 0.2, 0.3], 'col_str': ['a', 'b', 'c']},
                       index=['A', 'B', 'C'])
print(df_mix2)
#    col_int  col_float col_str
# A        0        0.1       a
# B        1        0.2       b
# C        2        0.3       c

print(df_mix2.dtypes)
# col_int        int64
# col_float    float64
# col_str       object
# dtype: object

print(df_mix2.T)
#              A    B    C
# col_int      0    1    2
# col_float  0.1  0.2  0.3
# col_str      a    b    c

print(df_mix2.T.dtypes)
# A    object
# B    object
# C    object
# dtype: object

print(df_mix2.T.T)
#   col_int col_float col_str
# A       0       0.1       a
# B       1       0.2       b
# C       2       0.3       c

print(df_mix2.T.T.dtypes)
# col_int      object
# col_float    object
# col_str      object
# dtype: object

df = pd.DataFrame({'X': [0, 1, 2], 'Y': [3, 4, 5]}, index=['A', 'B', 'C'])
print(df)
#    X  Y
# A  0  3
# B  1  4
# C  2  5

df_T = df.T
print(df_T)
#    A  B  C
# X  0  1  2
# Y  3  4  5

df_transpose = df.transpose()
print(df_transpose)
#    A  B  C
# X  0  1  2
# Y  3  4  5

df.at['A', 'X'] = 100
print(df)
#      X  Y
# A  100  3
# B    1  4
# C    2  5

print(df_T)
#      A  B  C
# X  100  1  2
# Y    3  4  5

print(df_transpose)
#      A  B  C
# X  100  1  2
# Y    3  4  5

df_mix = pd.DataFrame({'col_int': [0, 1, 2], 'col_float': [0.1, 0.2, 0.3]}, index=['A', 'B', 'C'])
print(df_mix)
#    col_int  col_float
# A        0        0.1
# B        1        0.2
# C        2        0.3

df_mix_T = df_mix.T
print(df_mix_T)
#              A    B    C
# col_int    0.0  1.0  2.0
# col_float  0.1  0.2  0.3

df_mix_transpose = df_mix.transpose()
print(df_mix_transpose)
#              A    B    C
# col_int    0.0  1.0  2.0
# col_float  0.1  0.2  0.3

df_mix.at['A', 'col_int'] = 100
print(df_mix)
#    col_int  col_float
# A      100        0.1
# B        1        0.2
# C        2        0.3

print(df_mix_T)
#              A    B    C
# col_int    0.0  1.0  2.0
# col_float  0.1  0.2  0.3

print(df_mix_transpose)
#              A    B    C
# col_int    0.0  1.0  2.0
# col_float  0.1  0.2  0.3

df = pd.DataFrame({'X': [0, 1, 2], 'Y': [3, 4, 5]}, index=['A', 'B', 'C'])
print(df)
#    X  Y
# A  0  3
# B  1  4
# C  2  5

df_T_copy = df.T.copy()
print(df_T_copy)
#    A  B  C
# X  0  1  2
# Y  3  4  5

df_transpose_copy = df.transpose(copy=True)
print(df_transpose_copy)
#    A  B  C
# X  0  1  2
# Y  3  4  5

df.at['A', 'X'] = 100
print(df)
#      X  Y
# A  100  3
# B    1  4
# C    2  5

print(df_T_copy)
#    A  B  C
# X  0  1  2
# Y  3  4  5

print(df_transpose_copy)
#    A  B  C
# X  0  1  2
# Y  3  4  5
