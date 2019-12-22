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

print(df_mix.loc['B'])
# col_int      1.0
# col_float    0.2
# Name: B, dtype: float64

print(type(df_mix.loc['B']))
# <class 'pandas.core.series.Series'>

print(df_mix.loc['B']['col_int'])
# 1.0

print(type(df_mix.loc['B']['col_int']))
# <class 'numpy.float64'>

print(df_mix.at['B', 'col_int'])
# 1

print(type(df_mix.at['B', 'col_int']))
# <class 'numpy.int64'>

print(df_mix.loc[['B']])
#    col_int  col_float
# B        1        0.2

print(type(df_mix.loc[['B']]))
# <class 'pandas.core.frame.DataFrame'>

print(df_mix.loc[['B']].dtypes)
# col_int        int64
# col_float    float64
# dtype: object
