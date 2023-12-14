import pandas as pd

print(pd.__version__)
# 2.1.4

df = pd.DataFrame({'int': [1, 2, 3, 1],
                   'float': [0.1, 0.2, 0.3, float('nan')],
                   'str': ['X', 'Y', 'X', 'Z'],
                   'str_num': ['1', '2', '3', '1'],
                   'bool': [True, True, False, True]})

print(df)
#    int  float str str_num   bool
# 0    1    0.1   X       1   True
# 1    2    0.2   Y       2   True
# 2    3    0.3   X       3  False
# 3    1    NaN   Z       1   True

print(df.dtypes)
# int          int64
# float      float64
# str         object
# str_num     object
# bool          bool
# dtype: object

print(df['float'].describe())
# count    3.00
# mean     0.20
# std      0.10
# min      0.10
# 25%      0.15
# 50%      0.20
# 75%      0.25
# max      0.30
# Name: float, dtype: float64

print(df['str'].describe())
# count     4
# unique    3
# top       X
# freq      2
# Name: str, dtype: object

print(type(df['float'].describe()))
# <class 'pandas.core.series.Series'>

print(df.describe())
#             int  float
# count  4.000000   3.00
# mean   1.750000   0.20
# std    0.957427   0.10
# min    1.000000   0.10
# 25%    1.000000   0.15
# 50%    1.500000   0.20
# 75%    2.250000   0.25
# max    3.000000   0.30

print(type(df.describe()))
# <class 'pandas.core.frame.DataFrame'>

print(df.describe().loc['std'])
# int      0.957427
# float    0.100000
# Name: std, dtype: float64

print(df.describe().at['std', 'int'])
# 0.9574271077563381

print(df.describe(exclude='number'))
#        str str_num  bool
# count    4       4     4
# unique   3       3     2
# top      X       1  True
# freq     2       2     3

print(df[['str', 'str_num', 'bool']])
#   str str_num   bool
# 0   X       1   True
# 1   Y       2   True
# 2   X       3  False
# 3   Z       1   True

print(df[['str', 'str_num', 'bool']].describe())
#        str str_num  bool
# count    4       4     4
# unique   3       3     2
# top      X       1  True
# freq     2       2     3

print(df.describe(include='all'))
#              int  float  str str_num  bool
# count   4.000000   3.00    4       4     4
# unique       NaN    NaN    3       3     2
# top          NaN    NaN    X       1  True
# freq         NaN    NaN    2       2     3
# mean    1.750000   0.20  NaN     NaN   NaN
# std     0.957427   0.10  NaN     NaN   NaN
# min     1.000000   0.10  NaN     NaN   NaN
# 25%     1.000000   0.15  NaN     NaN   NaN
# 50%     1.500000   0.20  NaN     NaN   NaN
# 75%     2.250000   0.25  NaN     NaN   NaN
# max     3.000000   0.30  NaN     NaN   NaN

print(df.describe(include=int))
#             int
# count  4.000000
# mean   1.750000
# std    0.957427
# min    1.000000
# 25%    1.000000
# 50%    1.500000
# 75%    2.250000
# max    3.000000

print(type(df.describe(include=int)))
# <class 'pandas.core.frame.DataFrame'>

print(df.describe(include=[object, bool]))
#        str str_num  bool
# count    4       4     4
# unique   3       3     2
# top      X       1  True
# freq     2       2     3

print(df.describe(exclude=['f8', 'object']))
#              int  bool
# count   4.000000     4
# unique       NaN     2
# top          NaN  True
# freq         NaN     3
# mean    1.750000   NaN
# std     0.957427   NaN
# min     1.000000   NaN
# 25%     1.000000   NaN
# 50%     1.500000   NaN
# 75%     2.250000   NaN
# max     3.000000   NaN

print(df.astype(object).describe())
#         int  float str str_num  bool
# count     4    3.0   4       4     4
# unique    3    3.0   3       3     2
# top       1    0.1   X       1  True
# freq      2    1.0   2       2     3

print(df.astype({'int': object}).describe(exclude='number'))
#         int str str_num  bool
# count     4   4       4     4
# unique    3   3       3     2
# top       1   X       1  True
# freq      2   2       2     3

print(df.astype({'str_num': int, 'bool': int}).describe())
#             int  float   str_num  bool
# count  4.000000   3.00  4.000000  4.00
# mean   1.750000   0.20  1.750000  0.75
# std    0.957427   0.10  0.957427  0.50
# min    1.000000   0.10  1.000000  0.00
# 25%    1.000000   0.15  1.000000  0.75
# 50%    1.500000   0.20  1.500000  1.00
# 75%    2.250000   0.25  2.250000  1.00
# max    3.000000   0.30  3.000000  1.00

print(df.count())
# int        4
# float      3
# str        4
# str_num    4
# bool       4
# dtype: int64

print(df.nunique())
# int        3
# float      3
# str        3
# str_num    3
# bool       2
# dtype: int64

print(df.mode())
#    int  float  str str_num  bool
# 0  1.0    0.1    X       1  True
# 1  NaN    0.2  NaN     NaN   NaN
# 2  NaN    0.3  NaN     NaN   NaN

print(df.mode().iloc[0])
# int         1.0
# float       0.1
# str           X
# str_num       1
# bool       True
# Name: 0, dtype: object

print(df['str'].value_counts())
# str
# X    2
# Y    1
# Z    1
# Name: count, dtype: int64

print(df['str'].value_counts().iat[0])
# 2

print(df.mean(numeric_only=True))
# int      1.75
# float    0.20
# bool     0.75
# dtype: float64

print(df.std(numeric_only=True))
# int      0.957427
# float    0.100000
# bool     0.500000
# dtype: float64

print(df.min(numeric_only=True))
# int          1
# float      0.1
# bool     False
# dtype: object

print(df.max(numeric_only=True))
# int         3
# float     0.3
# bool     True
# dtype: object

print(df.median(numeric_only=True))
# int      1.5
# float    0.2
# bool     1.0
# dtype: float64

# print(df.quantile(q=[0.25, 0.75], numeric_only=True))
# TypeError: numpy boolean subtract, the `-` operator, is not supported, use the bitwise_xor, the `^` operator, or the logical_xor function instead.

print(df.iloc[:, :-1])
#    int  float str str_num
# 0    1    0.1   X       1
# 1    2    0.2   Y       2
# 2    3    0.3   X       3
# 3    1    NaN   Z       1

print(df.iloc[:, :-1].quantile(q=[0, 0.25, 0.5, 0.75, 1], numeric_only=True))
#        int  float
# 0.00  1.00   0.10
# 0.25  1.00   0.15
# 0.50  1.50   0.20
# 0.75  2.25   0.25
# 1.00  3.00   0.30

print(df.describe(percentiles=[0.2, 0.4, 0.6, 0.8]))
#             int  float
# count  4.000000   3.00
# mean   1.750000   0.20
# std    0.957427   0.10
# min    1.000000   0.10
# 20%    1.000000   0.14
# 40%    1.200000   0.18
# 50%    1.500000   0.20
# 60%    1.800000   0.22
# 80%    2.400000   0.26
# max    3.000000   0.30

df['dt'] = pd.to_datetime(['2023-12-01', '2023-12-08', '2023-12-15', '2023-12-22'])
print(df)
#    int  float str str_num   bool         dt
# 0    1    0.1   X       1   True 2023-12-01
# 1    2    0.2   Y       2   True 2023-12-08
# 2    3    0.3   X       3  False 2023-12-15
# 3    1    NaN   Z       1   True 2023-12-22

print(df.dtypes)
# int                 int64
# float             float64
# str                object
# str_num            object
# bool                 bool
# dt         datetime64[ns]
# dtype: object

print(df.describe())
#             int  float                   dt
# count  4.000000   3.00                    4
# mean   1.750000   0.20  2023-12-11 12:00:00
# min    1.000000   0.10  2023-12-01 00:00:00
# 25%    1.000000   0.15  2023-12-06 06:00:00
# 50%    1.500000   0.20  2023-12-11 12:00:00
# 75%    2.250000   0.25  2023-12-16 18:00:00
# max    3.000000   0.30  2023-12-22 00:00:00
# std    0.957427   0.10                  NaN

print(df.astype(object).describe())
#         int  float str str_num  bool                   dt
# count     4    3.0   4       4     4                    4
# unique    3    3.0   3       3     2                    4
# top       1    0.1   X       1  True  2023-12-01 00:00:00
# freq      2    1.0   2       2     3                    1
