import pandas as pd

print(pd.__version__)
# 2.1.4

df = pd.DataFrame({'col_1': range(11), 'col_2': [i**2 for i in range(11)]})
print(df)
#     col_1  col_2
# 0       0      0
# 1       1      1
# 2       2      4
# 3       3      9
# 4       4     16
# 5       5     25
# 6       6     36
# 7       7     49
# 8       8     64
# 9       9     81
# 10     10    100

print(df.quantile())
# col_1     5.0
# col_2    25.0
# Name: 0.5, dtype: float64

print(type(df.quantile()))
# <class 'pandas.core.series.Series'>

print(df['col_1'].quantile())
# 5.0

print(type(df['col_1'].quantile()))
# <class 'numpy.float64'>

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

df_str = df.copy()
df_str['col_3'] = list('abcdefghijk')
print(df_str)
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

print(df_str.dtypes)
# col_1     int64
# col_2     int64
# col_3    object
# dtype: object

print(df_str.quantile(numeric_only=True))
# col_1     5.0
# col_2    25.0
# Name: 0.5, dtype: float64

# print(df_str.quantile())
# TypeError: unsupported operand type(s) for -: 'str' and 'str'

# print(df_str.quantile(interpolation='midpoint'))
# TypeError: unsupported operand type(s) for -: 'str' and 'str'

print(df_str.quantile([0.2, 0.21, 0.3], interpolation='lower'))
#       col_1  col_2 col_3
# 0.20      2      4     c
# 0.21      2      4     c
# 0.30      3      9     d

print(df_str.quantile([0.2, 0.21, 0.3], interpolation='higher'))
#       col_1  col_2 col_3
# 0.20      2      4     c
# 0.21      3      9     d
# 0.30      3      9     d

print(df_str.quantile([0.2, 0.21, 0.3], interpolation='nearest'))
#       col_1  col_2 col_3
# 0.20      2      4     c
# 0.21      2      4     c
# 0.30      3      9     d

df_dt = df.copy()
df_dt['col_3'] = pd.date_range('2023-01-01', '2023-01-11')
print(df_dt)
#     col_1  col_2      col_3
# 0       0      0 2023-01-01
# 1       1      1 2023-01-02
# 2       2      4 2023-01-03
# 3       3      9 2023-01-04
# 4       4     16 2023-01-05
# 5       5     25 2023-01-06
# 6       6     36 2023-01-07
# 7       7     49 2023-01-08
# 8       8     64 2023-01-09
# 9       9     81 2023-01-10
# 10     10    100 2023-01-11

print(df_dt.dtypes)
# col_1             int64
# col_2             int64
# col_3    datetime64[ns]
# dtype: object

print(df_dt.quantile(numeric_only=True))
# col_1     5.0
# col_2    25.0
# Name: 0.5, dtype: float64

print(df_dt.quantile([0.2, 0.21, 0.3]))
#       col_1  col_2               col_3
# 0.20    2.0    4.0 2023-01-03 00:00:00
# 0.21    2.1    4.5 2023-01-03 02:24:00
# 0.30    3.0    9.0 2023-01-04 00:00:00

print(df_dt.quantile([0.2, 0.21, 0.3], interpolation='midpoint'))
#       col_1  col_2               col_3
# 0.20    2.0    4.0 2023-01-03 00:00:00
# 0.21    2.5    6.5 2023-01-03 12:00:00
# 0.30    3.0    9.0 2023-01-04 00:00:00

print(df_dt.quantile([0.2, 0.21, 0.3], interpolation='lower'))
#       col_1  col_2      col_3
# 0.20      2      4 2023-01-03
# 0.21      2      4 2023-01-03
# 0.30      3      9 2023-01-04

print(df_dt.quantile([0.2, 0.21, 0.3], interpolation='higher'))
#       col_1  col_2      col_3
# 0.20      2      4 2023-01-03
# 0.21      3      9 2023-01-04
# 0.30      3      9 2023-01-04

print(df_dt.quantile([0.2, 0.21, 0.3], interpolation='nearest'))
#       col_1  col_2      col_3
# 0.20      2      4 2023-01-03
# 0.21      2      4 2023-01-03
# 0.30      3      9 2023-01-04

df_bool = df.copy()
df_bool['col_3'] = [True, False, True, False, True, False, True, False, True, False, True]
print(df_bool)
#     col_1  col_2  col_3
# 0       0      0   True
# 1       1      1  False
# 2       2      4   True
# 3       3      9  False
# 4       4     16   True
# 5       5     25  False
# 6       6     36   True
# 7       7     49  False
# 8       8     64   True
# 9       9     81  False
# 10     10    100   True

print(df_bool.dtypes)
# col_1    int64
# col_2    int64
# col_3     bool
# dtype: object

# print(df_bool.quantile())
# TypeError: numpy boolean subtract, the `-` operator, is not supported, use the bitwise_xor, the `^` operator, or the logical_xor function instead.

# print(df_bool.quantile(numeric_only=True))
# TypeError: numpy boolean subtract, the `-` operator, is not supported, use the bitwise_xor, the `^` operator, or the logical_xor function instead.

print(df_bool.select_dtypes(exclude=bool))
#     col_1  col_2
# 0       0      0
# 1       1      1
# 2       2      4
# 3       3      9
# 4       4     16
# 5       5     25
# 6       6     36
# 7       7     49
# 8       8     64
# 9       9     81
# 10     10    100

print(df_bool.select_dtypes(exclude=bool).quantile())
# col_1     5.0
# col_2    25.0
# Name: 0.5, dtype: float64

print(df_bool.astype({'col_3': int}))
#     col_1  col_2  col_3
# 0       0      0      1
# 1       1      1      0
# 2       2      4      1
# 3       3      9      0
# 4       4     16      1
# 5       5     25      0
# 6       6     36      1
# 7       7     49      0
# 8       8     64      1
# 9       9     81      0
# 10     10    100      1

print(df_bool.astype({'col_3': int}).quantile())
# col_1     5.0
# col_2    25.0
# col_3     1.0
# Name: 0.5, dtype: float64
