import pandas as pd
import numpy as np

df = pd.DataFrame({'col1': [0, np.nan, np.nan, 3, 4],
                   'col2': [np.nan, 1, 2, np.nan, np.nan],
                   'col3': [4, np.nan, np.nan, 7, 10]})
print(df)
#    col1  col2  col3
# 0   0.0   NaN   4.0
# 1   NaN   1.0   NaN
# 2   NaN   2.0   NaN
# 3   3.0   NaN   7.0
# 4   4.0   NaN  10.0

print(df.interpolate())
#    col1  col2  col3
# 0   0.0   NaN   4.0
# 1   1.0   1.0   5.0
# 2   2.0   2.0   6.0
# 3   3.0   2.0   7.0
# 4   4.0   2.0  10.0

print(df.interpolate(axis=1))
#    col1  col2  col3
# 0   0.0   2.0   4.0
# 1   NaN   1.0   1.0
# 2   NaN   2.0   2.0
# 3   3.0   5.0   7.0
# 4   4.0   7.0  10.0

print(df.interpolate(limit=1))
#    col1  col2  col3
# 0   0.0   NaN   4.0
# 1   1.0   1.0   5.0
# 2   NaN   2.0   NaN
# 3   3.0   2.0   7.0
# 4   4.0   NaN  10.0

print(df.interpolate(limit=1, limit_direction='forward'))
#    col1  col2  col3
# 0   0.0   NaN   4.0
# 1   1.0   1.0   5.0
# 2   NaN   2.0   NaN
# 3   3.0   2.0   7.0
# 4   4.0   NaN  10.0

print(df.interpolate(limit=1, limit_direction='backward'))
#    col1  col2  col3
# 0   0.0   1.0   4.0
# 1   NaN   1.0   NaN
# 2   2.0   2.0   6.0
# 3   3.0   NaN   7.0
# 4   4.0   NaN  10.0

print(df.interpolate(limit=1, limit_direction='both'))
#    col1  col2  col3
# 0   0.0   1.0   4.0
# 1   1.0   1.0   5.0
# 2   2.0   2.0   6.0
# 3   3.0   2.0   7.0
# 4   4.0   NaN  10.0

print(df.interpolate(limit_direction='both'))
#    col1  col2  col3
# 0   0.0   1.0   4.0
# 1   1.0   1.0   5.0
# 2   2.0   2.0   6.0
# 3   3.0   2.0   7.0
# 4   4.0   2.0  10.0

print(df.interpolate(limit_area='inside'))
#    col1  col2  col3
# 0   0.0   NaN   4.0
# 1   1.0   1.0   5.0
# 2   2.0   2.0   6.0
# 3   3.0   NaN   7.0
# 4   4.0   NaN  10.0

print(df.interpolate(limit_area='outside'))
#    col1  col2  col3
# 0   0.0   NaN   4.0
# 1   NaN   1.0   NaN
# 2   NaN   2.0   NaN
# 3   3.0   2.0   7.0
# 4   4.0   2.0  10.0

print(df.interpolate(limit_area='outside', limit_direction='both'))
#    col1  col2  col3
# 0   0.0   1.0   4.0
# 1   NaN   1.0   NaN
# 2   NaN   2.0   NaN
# 3   3.0   2.0   7.0
# 4   4.0   2.0  10.0

df.interpolate(inplace=True)
print(df)
#    col1  col2  col3
# 0   0.0   NaN   4.0
# 1   1.0   1.0   5.0
# 2   2.0   2.0   6.0
# 3   3.0   2.0   7.0
# 4   4.0   2.0  10.0

s = pd.Series([0, np.nan, np.nan, 3],
              index=[0, 4, 6, 8])
print(s)
# 0    0.0
# 4    NaN
# 6    NaN
# 8    3.0
# dtype: float64

print(s.interpolate())
# 0    0.0
# 4    1.0
# 6    2.0
# 8    3.0
# dtype: float64

print(s.interpolate('index'))
# 0    0.00
# 4    1.50
# 6    2.25
# 8    3.00
# dtype: float64

s.index = list('abcd')
print(s)
# a    0.0
# b    NaN
# c    NaN
# d    3.0
# dtype: float64

print(s.interpolate())
# a    0.0
# b    1.0
# c    2.0
# d    3.0
# dtype: float64

# print(s.interpolate('index'))
# TypeError: Cannot cast array data from dtype('O') to dtype('float64') according to the rule 'safe'

s = pd.Series([np.nan, 1, np.nan, 2, np.nan])
print(s)
# 0    NaN
# 1    1.0
# 2    NaN
# 3    2.0
# 4    NaN
# dtype: float64

print(s.interpolate('ffill'))
# 0    NaN
# 1    1.0
# 2    1.0
# 3    2.0
# 4    2.0
# dtype: float64

print(s.interpolate('bfill'))
# 0    1.0
# 1    1.0
# 2    2.0
# 3    2.0
# 4    NaN
# dtype: float64

# s.interpolate('ffill', limit_direction='both')
# ValueError: `limit_direction` must be 'forward' for method `ffill`

# s.interpolate('bfill', limit_direction='both')
# ValueError: `limit_direction` must be 'backward' for method `bfill`

print(s.fillna(method='ffill'))
# 0    NaN
# 1    1.0
# 2    1.0
# 3    2.0
# 4    2.0
# dtype: float64

print(s.fillna(method='bfill'))
# 0    1.0
# 1    1.0
# 2    2.0
# 3    2.0
# 4    NaN
# dtype: float64

s = pd.Series([0, 10, np.nan, np.nan, 4, np.nan],
              index=[0, 2, 5, 6, 8, 12])
print(s)
# 0      0.0
# 2     10.0
# 5      NaN
# 6      NaN
# 8      4.0
# 12     NaN
# dtype: float64

print(s.interpolate('spline', order=2))
# 0      0.00
# 2     10.00
# 5     13.75
# 6     12.00
# 8      4.00
# 12   -30.00
# dtype: float64

s.index = range(6)
print(s)
# 0     0.0
# 1    10.0
# 2     NaN
# 3     NaN
# 4     4.0
# 5     NaN
# dtype: float64

print(s.interpolate('spline', order=2))
# 0     0.0
# 1    10.0
# 2    14.0
# 3    12.0
# 4     4.0
# 5   -10.0
# dtype: float64

s.index = list('abcdef')
print(s)
# a     0.0
# b    10.0
# c     NaN
# d     NaN
# e     4.0
# f     NaN
# dtype: float64

# print(s.interpolate('spline', order=2))
# ValueError: Index column must be numeric or datetime type when using spline method other than linear.
# Try setting a numeric or datetime index column before interpolating.

s_object = pd.Series(['A', np.nan, 'C'])
print(s_object)
# 0      A
# 1    NaN
# 2      C
# dtype: object

print(s_object.interpolate())
# 0      A
# 1    NaN
# 2      C
# dtype: object

print(s_object.interpolate('ffill'))
# 0    A
# 1    A
# 2    C
# dtype: object

s_object_num = pd.Series([0, np.nan, 2], dtype=object)
print(s_object_num)
# 0      0
# 1    NaN
# 2      2
# dtype: object

print(s_object_num.interpolate())
# 0      0
# 1    NaN
# 2      2
# dtype: object

print(s_object_num.interpolate('ffill'))
# 0    0
# 1    0
# 2    2
# dtype: int64

print(s_object_num.astype(float).interpolate())
# 0    0.0
# 1    1.0
# 2    2.0
# dtype: float64

# print(s_object_num.astype(int))
# ValueError: cannot convert float NaN to integer
