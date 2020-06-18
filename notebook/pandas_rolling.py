import pandas as pd

s = pd.Series(range(10))

print(s)
# 0    0
# 1    1
# 2    2
# 3    3
# 4    4
# 5    5
# 6    6
# 7    7
# 8    8
# 9    9
# dtype: int64

print(s.rolling(3))
# Rolling [window=3,center=False,axis=0]

print(type(s.rolling(3)))
# <class 'pandas.core.window.rolling.Rolling'>

print(s.rolling(3).sum())
# 0     NaN
# 1     NaN
# 2     3.0
# 3     6.0
# 4     9.0
# 5    12.0
# 6    15.0
# 7    18.0
# 8    21.0
# 9    24.0
# dtype: float64

print(s.rolling(2).sum())
# 0     NaN
# 1     1.0
# 2     3.0
# 3     5.0
# 4     7.0
# 5     9.0
# 6    11.0
# 7    13.0
# 8    15.0
# 9    17.0
# dtype: float64

print(s.rolling(4).sum())
# 0     NaN
# 1     NaN
# 2     NaN
# 3     6.0
# 4    10.0
# 5    14.0
# 6    18.0
# 7    22.0
# 8    26.0
# 9    30.0
# dtype: float64

print(s.rolling(3, center=True).sum())
# 0     NaN
# 1     3.0
# 2     6.0
# 3     9.0
# 4    12.0
# 5    15.0
# 6    18.0
# 7    21.0
# 8    24.0
# 9     NaN
# dtype: float64

print(s.rolling(4, center=True).sum())
# 0     NaN
# 1     NaN
# 2     6.0
# 3    10.0
# 4    14.0
# 5    18.0
# 6    22.0
# 7    26.0
# 8    30.0
# 9     NaN
# dtype: float64

print(s.rolling(3, min_periods=2).sum())
# 0     NaN
# 1     1.0
# 2     3.0
# 3     6.0
# 4     9.0
# 5    12.0
# 6    15.0
# 7    18.0
# 8    21.0
# 9    24.0
# dtype: float64

print(s.rolling(3, min_periods=1).sum())
# 0     0.0
# 1     1.0
# 2     3.0
# 3     6.0
# 4     9.0
# 5    12.0
# 6    15.0
# 7    18.0
# 8    21.0
# 9    24.0
# dtype: float64

df = pd.DataFrame({'a': range(10), 'b': range(10, 0, -1),
                   'c': range(10, 20), 'd': range(20, 10, -1)})

print(df.rolling(2).sum())
#       a     b     c     d
# 0   NaN   NaN   NaN   NaN
# 1   1.0  19.0  21.0  39.0
# 2   3.0  17.0  23.0  37.0
# 3   5.0  15.0  25.0  35.0
# 4   7.0  13.0  27.0  33.0
# 5   9.0  11.0  29.0  31.0
# 6  11.0   9.0  31.0  29.0
# 7  13.0   7.0  33.0  27.0
# 8  15.0   5.0  35.0  25.0
# 9  17.0   3.0  37.0  23.0

print(df.rolling(2, axis=1).sum())
#     a     b     c     d
# 0 NaN  10.0  20.0  30.0
# 1 NaN  10.0  20.0  30.0
# 2 NaN  10.0  20.0  30.0
# 3 NaN  10.0  20.0  30.0
# 4 NaN  10.0  20.0  30.0
# 5 NaN  10.0  20.0  30.0
# 6 NaN  10.0  20.0  30.0
# 7 NaN  10.0  20.0  30.0
# 8 NaN  10.0  20.0  30.0
# 9 NaN  10.0  20.0  30.0

print(s.rolling(3).mean())
# 0    NaN
# 1    NaN
# 2    1.0
# 3    2.0
# 4    3.0
# 5    4.0
# 6    5.0
# 7    6.0
# 8    7.0
# 9    8.0
# dtype: float64

print(s.rolling(3).agg(['sum', 'mean', 'skew', 'cov',
                        max, min,
                        lambda x: max(x) - min(x)]))
#     sum  mean          skew  cov  max  min  <lambda>
# 0   NaN   NaN           NaN  NaN  NaN  NaN       NaN
# 1   NaN   NaN           NaN  NaN  NaN  NaN       NaN
# 2   3.0   1.0  0.000000e+00  1.0  2.0  0.0       2.0
# 3   6.0   2.0 -7.993606e-15  1.0  3.0  1.0       2.0
# 4   9.0   3.0  2.398082e-14  1.0  4.0  2.0       2.0
# 5  12.0   4.0 -6.394885e-14  1.0  5.0  3.0       2.0
# 6  15.0   5.0 -7.993606e-14  1.0  6.0  4.0       2.0
# 7  18.0   6.0  1.918465e-13  1.0  7.0  5.0       2.0
# 8  21.0   7.0  2.238210e-13  1.0  8.0  6.0       2.0
# 9  24.0   8.0 -5.115908e-13  1.0  9.0  7.0       2.0
