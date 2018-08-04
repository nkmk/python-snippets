import pandas as pd

df = pd.DataFrame({'col1': [0, pd.np.nan, pd.np.nan, 3, 4],
                   'col2': [pd.np.nan, 1, 2, pd.np.nan, pd.np.nan],
                   'col3': [4, pd.np.nan, pd.np.nan, 7, 10]})

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

df_copy = df.copy()
df_copy.interpolate(inplace=True)
print(df_copy)
#    col1  col2  col3
# 0   0.0   NaN   4.0
# 1   1.0   1.0   5.0
# 2   2.0   2.0   6.0
# 3   3.0   2.0   7.0
# 4   4.0   2.0  10.0

s = pd.Series([0, pd.np.nan, pd.np.nan, pd.np.nan, 4, pd.np.nan, pd.np.nan],
              index=[0, 2, 5, 6, 8, 10, 14])
print(s)
# 0     0.0
# 2     NaN
# 5     NaN
# 6     NaN
# 8     4.0
# 10    NaN
# 14    NaN
# dtype: float64

print(s.interpolate())
# 0     0.0
# 2     1.0
# 5     2.0
# 6     3.0
# 8     4.0
# 10    4.0
# 14    4.0
# dtype: float64

print(s.interpolate('index'))
# 0     0.0
# 2     1.0
# 5     2.5
# 6     3.0
# 8     4.0
# 10    4.0
# 14    4.0
# dtype: float64

print(s.interpolate('values'))
# 0     0.0
# 2     1.0
# 5     2.5
# 6     3.0
# 8     4.0
# 10    4.0
# 14    4.0
# dtype: float64

s.index = list('abcdefg')
print(s)
# a    0.0
# b    NaN
# c    NaN
# d    NaN
# e    4.0
# f    NaN
# g    NaN
# dtype: float64

print(s.interpolate())
# a    0.0
# b    1.0
# c    2.0
# d    3.0
# e    4.0
# f    4.0
# g    4.0
# dtype: float64

# print(s.interpolate('values'))
# TypeError: Cannot cast array data from dtype('O') to dtype('float64') according to the rule 'safe'

s = pd.Series([0, 10, pd.np.nan, pd.np.nan, 4, pd.np.nan, pd.np.nan],
              index=[0, 2, 5, 6, 8, 10, 14])

print(s.interpolate('spline', order=2))
# 0      0.00
# 2     10.00
# 5     13.75
# 6     12.00
# 8      4.00
# 10   -10.00
# 14   -56.00
# dtype: float64

s.index = range(7)

print(s.interpolate('spline', order=2))
# 0     0.0
# 1    10.0
# 2    14.0
# 3    12.0
# 4     4.0
# 5   -10.0
# 6   -30.0
# dtype: float64

s.index = list('abcdefg')

# print(s.interpolate('spline', order=2))
# TypeError: unsupported operand type(s) for -: 'str' and 'str'
