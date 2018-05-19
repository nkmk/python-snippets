import pandas as pd

df = pd.DataFrame({'a': [1, 2, 1, 3],
                   'b': [0.4, 1.1, 0.1, 0.8],
                   'c': ['X', 'Y', 'X', 'Z'],
                   'd': ['3', '5', '2', '1'],
                   'e': [True, True, False, True]})

print(df)
#    a    b  c  d      e
# 0  1  0.4  X  3   True
# 1  2  1.1  Y  5   True
# 2  1  0.1  X  2  False
# 3  3  0.8  Z  1   True

print(df.dtypes)
# a      int64
# b    float64
# c     object
# d     object
# e       bool
# dtype: object

print(df.describe())
#               a         b
# count  4.000000  4.000000
# mean   1.750000  0.600000
# std    0.957427  0.439697
# min    1.000000  0.100000
# 25%    1.000000  0.325000
# 50%    1.500000  0.600000
# 75%    2.250000  0.875000
# max    3.000000  1.100000

print(type(df.describe()))
# <class 'pandas.core.frame.DataFrame'>

print(df.describe().loc['std'])
# a    0.957427
# b    0.439697
# Name: std, dtype: float64

print(df.describe().at['std', 'b'])
# 0.439696865275764

print(df.describe(exclude='number'))
#         c  d     e
# count   4  4     4
# unique  3  4     2
# top     X  3  True
# freq    2  1     3

df_notnum = df[['c', 'd', 'e']]
print(df_notnum)
#    c  d      e
# 0  X  3   True
# 1  Y  5   True
# 2  X  2  False
# 3  Z  1   True

print(df_notnum.dtypes)
# c    object
# d    object
# e      bool
# dtype: object

print(df_notnum.describe())
#         c  d     e
# count   4  4     4
# unique  3  4     2
# top     X  3  True
# freq    2  1     3

print(df.describe(include='all'))
#                a         b    c    d     e
# count   4.000000  4.000000    4    4     4
# unique       NaN       NaN    3    4     2
# top          NaN       NaN    X    3  True
# freq         NaN       NaN    2    1     3
# mean    1.750000  0.600000  NaN  NaN   NaN
# std     0.957427  0.439697  NaN  NaN   NaN
# min     1.000000  0.100000  NaN  NaN   NaN
# 25%     1.000000  0.325000  NaN  NaN   NaN
# 50%     1.500000  0.600000  NaN  NaN   NaN
# 75%     2.250000  0.875000  NaN  NaN   NaN
# max     3.000000  1.100000  NaN  NaN   NaN

print(df.describe(include=int))
#               a
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
#         c  d     e
# count   4  4     4
# unique  3  4     2
# top     X  3  True
# freq    2  1     3

print(df.describe(exclude=[float, object]))
#                a     e
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

print(df.count())
# a    4
# b    4
# c    4
# d    4
# e    4
# dtype: int64

print(df.nunique())
# a    3
# b    4
# c    3
# d    4
# e    2
# dtype: int64

print(df.mode())
#      a    b    c  d     e
# 0  1.0  0.1    X  1  True
# 1  NaN  0.4  NaN  2   NaN
# 2  NaN  0.8  NaN  3   NaN
# 3  NaN  1.1  NaN  5   NaN

print(df.mode().count())
# a    1
# b    4
# c    1
# d    4
# e    1
# dtype: int64

print(df.mode().iloc[0])
# a       1
# b     0.1
# c       X
# d       1
# e    True
# Name: 0, dtype: object

print(df['c'].value_counts().iat[0])
# 2

print(df.apply(lambda x: x.value_counts().iat[0]))
# a    2
# b    1
# c    2
# d    1
# e    3
# dtype: int64

print(df.mean(numeric_only=True))
# a    1.75
# b    0.60
# e    0.75
# dtype: float64

print(df.std(numeric_only=True))
# a    0.957427
# b    0.439697
# e    0.500000
# dtype: float64

print(df.min(numeric_only=True))
# a    1.0
# b    0.1
# e    0.0
# dtype: float64

print(df.max(numeric_only=True))
# a    3.0
# b    1.1
# e    1.0
# dtype: float64

print(df.median(numeric_only=True))
# a    1.5
# b    0.6
# e    1.0
# dtype: float64

print(df.quantile(q=[0.25, 0.75], numeric_only=True))
#          a      b     e
# 0.25  1.00  0.325  0.75
# 0.75  2.25  0.875  1.00

print(df.quantile(q=[0, 0.25, 0.5, 0.75, 1], numeric_only=True))
#          a      b     e
# 0.00  1.00  0.100  0.00
# 0.25  1.00  0.325  0.75
# 0.50  1.50  0.600  1.00
# 0.75  2.25  0.875  1.00
# 1.00  3.00  1.100  1.00

print(df.describe(percentiles=[0.2, 0.4, 0.6, 0.8]))
#               a         b
# count  4.000000  4.000000
# mean   1.750000  0.600000
# std    0.957427  0.439697
# min    1.000000  0.100000
# 20%    1.000000  0.280000
# 40%    1.200000  0.480000
# 50%    1.500000  0.600000
# 60%    1.800000  0.720000
# 80%    2.400000  0.920000
# max    3.000000  1.100000

print(df.astype('str').describe())
#         a    b  c  d     e
# count   4    4  4  4     4
# unique  3    4  3  4     2
# top     1  1.1  X  3  True
# freq    2    1  2  1     3

print(df.astype({'a': str}).describe(exclude='number'))
#         a  c  d     e
# count   4  4  4     4
# unique  3  3  4     2
# top     1  X  3  True
# freq    2  2  1     3

print(df.astype({'d': int, 'e': int}).describe())
#               a         b         d     e
# count  4.000000  4.000000  4.000000  4.00
# mean   1.750000  0.600000  2.750000  0.75
# std    0.957427  0.439697  1.707825  0.50
# min    1.000000  0.100000  1.000000  0.00
# 25%    1.000000  0.325000  1.750000  0.75
# 50%    1.500000  0.600000  2.500000  1.00
# 75%    2.250000  0.875000  3.500000  1.00
# max    3.000000  1.100000  5.000000  1.00

s_int = df['a']
print(s_int)
# 0    1
# 1    2
# 2    1
# 3    3
# Name: a, dtype: int64

print(s_int.describe())
# count    4.000000
# mean     1.750000
# std      0.957427
# min      1.000000
# 25%      1.000000
# 50%      1.500000
# 75%      2.250000
# max      3.000000
# Name: a, dtype: float64

print(type(s_int.describe()))
# <class 'pandas.core.series.Series'>

s_str = df['d']
print(s_str.describe())
# count     4
# unique    4
# top       3
# freq      1
# Name: d, dtype: object

print(s_str.astype('int').describe())
# count    4.000000
# mean     2.750000
# std      1.707825
# min      1.000000
# 25%      1.750000
# 50%      2.500000
# 75%      3.500000
# max      5.000000
# Name: d, dtype: float64

df['dt'] = pd.to_datetime(['2018-01-01', '2018-03-15', '2018-02-20', '2018-03-15'])

print(df.dtypes)
# a              int64
# b            float64
# c             object
# d             object
# e               bool
# dt    datetime64[ns]
# dtype: object

print(df.describe(include='datetime'))
#                          dt
# count                     4
# unique                    3
# top     2018-03-15 00:00:00
# freq                      2
# first   2018-01-01 00:00:00
# last    2018-03-15 00:00:00

print(df['dt'].min())
# 2018-01-01 00:00:00

print(df['dt'].max())
# 2018-03-15 00:00:00

print(df.T.describe())
#         0                    1                    2                    3
# count   6                    6                    6                    6
# unique  5                    6                    6                    6
# top     1  2018-03-15 00:00:00  2018-02-20 00:00:00  2018-03-15 00:00:00
# freq    2                    1                    1                    1
