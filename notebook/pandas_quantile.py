import pandas as pd

df = pd.DataFrame({'col_1': range(11),
                   'col_2': [i ** 2 for i in range(11)],
                   'col_3': list('abcdefghijk')})

print(df)
#     col_1  col_2 col_3
# 0       0      0     a
# 1       1      1     b
# 2       2      4     c
# 3       3      9     d
# 4       4     16     e
# 5       5     25     f
# 6       6     36     g
# 7       7     49     h
# 8       8     64     i
# 9       9     81     j
# 10     10    100     k

print(df.quantile())
# col_1     5.0
# col_2    25.0
# Name: 0.5, dtype: float64

print(type(df.quantile()))
# <class 'pandas.core.series.Series'>

print(df['col_1'].quantile())
# 5.0

print(type(df['col_1'].quantile()))
# <class 'float'>

print(df.quantile(0.2))
# col_1    2.0
# col_2    4.0
# Name: 0.2, dtype: float64

print(df.quantile([0, 0.25, 0.5, 0.75, 1.0]))
#       col_1  col_2
# 0.00    0.0    0.0
# 0.25    2.5    6.5
# 0.50    5.0   25.0
# 0.75    7.5   56.5
# 1.00   10.0  100.0

print(type(df.quantile([0, 0.25, 0.5, 0.75, 1.0])))
# <class 'pandas.core.frame.DataFrame'>

print(df['col_1'].quantile([0, 0.25, 0.5, 0.75, 1.0]))
# 0.00     0.0
# 0.25     2.5
# 0.50     5.0
# 0.75     7.5
# 1.00    10.0
# Name: col_1, dtype: float64

print(type(df['col_1'].quantile([0, 0.25, 0.5, 0.75, 1.0])))
# <class 'pandas.core.series.Series'>

print(df.quantile(0.21))
# col_1    2.1
# col_2    4.5
# Name: 0.21, dtype: float64

print(df.quantile(0.21, interpolation='linear'))
# col_1    2.1
# col_2    4.5
# Name: 0.21, dtype: float64

print(df.quantile(0.21, interpolation='lower'))
# col_1    2
# col_2    4
# Name: 0.21, dtype: int64

print(df.quantile(0.21, interpolation='higher'))
# col_1    3
# col_2    9
# Name: 0.21, dtype: int64

print(df.quantile(0.21, interpolation='nearest'))
# col_1    2
# col_2    4
# Name: 0.21, dtype: int64

print(df.quantile(0.21, interpolation='midpoint'))
# col_1    2.5
# col_2    6.5
# Name: 0.21, dtype: float64

print(df.quantile(0.2))
# col_1    2.0
# col_2    4.0
# Name: 0.2, dtype: float64

print(df.quantile(0.2, interpolation='lower'))
# col_1    2
# col_2    4
# Name: 0.2, dtype: int64

print(df.quantile(axis=1))
# 0      0.0
# 1      1.0
# 2      3.0
# 3      6.0
# 4     10.0
# 5     15.0
# 6     21.0
# 7     28.0
# 8     36.0
# 9     45.0
# 10    55.0
# Name: 0.5, dtype: float64

# print(df.quantile(numeric_only=False))
# TypeError: can't multiply sequence by non-int of type 'float'

print(df.quantile(numeric_only=False, interpolation='lower'))
# col_1     5
# col_2    25
# col_3     f
# Name: 0.5, dtype: object

print(df.quantile(0.25, numeric_only=False, interpolation='lower'))
# col_1    2
# col_2    4
# col_3    c
# Name: 0.25, dtype: object

print(df.quantile(0.25, numeric_only=False, interpolation='higher'))
# col_1    3
# col_2    9
# col_3    d
# Name: 0.25, dtype: object

df['col_3'] = pd.date_range('2019-01-01', '2019-01-11')

print(df)
#     col_1  col_2      col_3
# 0       0      0 2019-01-01
# 1       1      1 2019-01-02
# 2       2      4 2019-01-03
# 3       3      9 2019-01-04
# 4       4     16 2019-01-05
# 5       5     25 2019-01-06
# 6       6     36 2019-01-07
# 7       7     49 2019-01-08
# 8       8     64 2019-01-09
# 9       9     81 2019-01-10
# 10     10    100 2019-01-11

print(df.dtypes)
# col_1             int64
# col_2             int64
# col_3    datetime64[ns]
# dtype: object

print(df.quantile())
# col_1     5.0
# col_2    25.0
# Name: 0.5, dtype: float64

print(df.quantile(numeric_only=False))
# col_1                      5
# col_2                     25
# col_3    2019-01-06 00:00:00
# Name: 0.5, dtype: object

print(df.quantile(0.25, numeric_only=False))
# col_1                    2.5
# col_2                    6.5
# col_3    2019-01-03 12:00:00
# Name: 0.25, dtype: object

print(df.quantile(0.25, numeric_only=False, interpolation='lower'))
# col_1                      2
# col_2                      4
# col_3    2019-01-03 00:00:00
# Name: 0.25, dtype: object
