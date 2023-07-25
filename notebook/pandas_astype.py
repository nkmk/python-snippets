import pandas as pd

print(pd.__version__)
# 2.0.3

s = pd.Series([1, 2, 3])
print(s)
# 0    1
# 1    2
# 2    3
# dtype: int64

s_f = s.astype('float64')
print(s_f)
# 0    1.0
# 1    2.0
# 2    3.0
# dtype: float64

s_f = s.astype('float')
print(s_f.dtype)
# float64

s_f = s.astype(float)
print(s_f.dtype)
# float64

s_f = s.astype('f8')
print(s_f.dtype)
# float64

df = pd.DataFrame({'a': [11, 21, 31], 'b': [12, 22, 32], 'c': [13, 23, 33]})
print(df)
#     a   b   c
# 0  11  12  13
# 1  21  22  23
# 2  31  32  33

print(df.dtypes)
# a    int64
# b    int64
# c    int64
# dtype: object

df_f = df.astype('float64')
print(df_f)
#       a     b     c
# 0  11.0  12.0  13.0
# 1  21.0  22.0  23.0
# 2  31.0  32.0  33.0

print(df_f.dtypes)
# a    float64
# b    float64
# c    float64
# dtype: object

df_fcol = df.astype({'a': float})
print(df_fcol)
#       a   b   c
# 0  11.0  12  13
# 1  21.0  22  23
# 2  31.0  32  33

print(df_fcol.dtypes)
# a    float64
# b      int64
# c      int64
# dtype: object

df_fcol2 = df.astype({'a': 'float32', 'c': 'int8'})
print(df_fcol2)
#       a   b   c
# 0  11.0  12  13
# 1  21.0  22  23
# 2  31.0  32  33

print(df_fcol2.dtypes)
# a    float32
# b      int64
# c       int8
# dtype: object
