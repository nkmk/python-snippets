import pandas as pd

print(pd.__version__)
# 1.4.1

df = pd.read_csv('data/src/sample_header.csv')
print(df)
#     a   b   c   d
# 0  11  12  13  14
# 1  21  22  23  24
# 2  31  32  33  34

s = df['c']
print(s)
# 0    13
# 1    23
# 2    33
# Name: c, dtype: int64

s_f = s.astype('float64')
print(s_f)
# 0    13.0
# 1    23.0
# 2    33.0
# Name: c, dtype: float64

print(s)
# 0    13
# 1    23
# 2    33
# Name: c, dtype: int64

s_f = s.astype('float')
print(s_f.dtype)
# float64

s_f = s.astype(float)
print(s_f.dtype)
# float64

s_f = s.astype('f8')
print(s_f.dtype)
# float64

print(df)
#     a   b   c   d
# 0  11  12  13  14
# 1  21  22  23  24
# 2  31  32  33  34

print(df.dtypes)
# a    int64
# b    int64
# c    int64
# d    int64
# dtype: object

df_f = df.astype('float64')
print(df_f)
#       a     b     c     d
# 0  11.0  12.0  13.0  14.0
# 1  21.0  22.0  23.0  24.0
# 2  31.0  32.0  33.0  34.0

print(df_f.dtypes)
# a    float64
# b    float64
# c    float64
# d    float64
# dtype: object

df_fcol = df.astype({'a': float})
print(df_fcol)
#       a   b   c   d
# 0  11.0  12  13  14
# 1  21.0  22  23  24
# 2  31.0  32  33  34

print(df_fcol.dtypes)
# a    float64
# b      int64
# c      int64
# d      int64
# dtype: object

df_fcol2 = df.astype({'a': 'float32', 'c': 'int8'})
print(df_fcol2)
#       a   b   c   d
# 0  11.0  12  13  14
# 1  21.0  22  23  24
# 2  31.0  32  33  34

print(df_fcol2.dtypes)
# a    float32
# b      int64
# c       int8
# d      int64
# dtype: object
