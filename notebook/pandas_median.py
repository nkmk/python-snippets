import pandas as pd

df = pd.DataFrame({'col_1': range(5),
                   'col_2': [i ** 2 for i in range(5)],
                   'col_3': list('abcde')})

print(df)
#    col_1  col_2 col_3
# 0      0      0     a
# 1      1      1     b
# 2      2      4     c
# 3      3      9     d
# 4      4     16     e

print(df.median())
# col_1    2.0
# col_2    4.0
# dtype: float64

print(type(df.median()))
# <class 'pandas.core.series.Series'>

print(df.mean())
# col_1    2.0
# col_2    6.0
# dtype: float64

print(df['col_1'].median())
# 2.0

print(type(df['col_1'].median()))
# <class 'numpy.float64'>

df_even = pd.DataFrame({'col_1': range(6),
                        'col_2': [i ** 2 for i in range(6)],
                        'col_3': list('abcdef')})

print(df_even)
#    col_1  col_2 col_3
# 0      0      0     a
# 1      1      1     b
# 2      2      4     c
# 3      3      9     d
# 4      4     16     e
# 5      5     25     f

print(df_even.median())
# col_1    2.5
# col_2    6.5
# dtype: float64

print(df.median(axis=1))
# 0     0.0
# 1     1.0
# 2     3.0
# 3     6.0
# 4    10.0
# dtype: float64
