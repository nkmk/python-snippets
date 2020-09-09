import pandas as pd

print(pd.__version__)
# 1.0.5

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['X', 'Y', 'Z'])
print(df)
#    A  B
# X  1  4
# Y  2  5
# Z  3  6

print(df.cumsum())
#    A   B
# X  1   4
# Y  3   9
# Z  6  15

print(df.cumsum(axis=1))
#    A  B
# X  1  5
# Y  2  7
# Z  3  9

print(df.cumprod())
#    A    B
# X  1    4
# Y  2   20
# Z  6  120

print(df.cumprod(axis=1))
#    A   B
# X  1   4
# Y  2  10
# Z  3  18

print(df['B'])
# X    4
# Y    5
# Z    6
# Name: B, dtype: int64

print(type(df['B']))
# <class 'pandas.core.series.Series'>

print(df['B'].cumsum())
# X     4
# Y     9
# Z    15
# Name: B, dtype: int64

print(df['B'].cumprod())
# X      4
# Y     20
# Z    120
# Name: B, dtype: int64

df_nan = pd.DataFrame({'A': [1, 2, 3], 'B': [4, float('nan'), 6]}, index=['X', 'Y', 'Z'])
print(df_nan)
#    A    B
# X  1  4.0
# Y  2  NaN
# Z  3  6.0

print(df_nan.cumsum())
#    A     B
# X  1   4.0
# Y  3   NaN
# Z  6  10.0

print(float('nan') + 4)
# nan

print(df_nan.cumsum(skipna=False))
#    A    B
# X  1  4.0
# Y  3  NaN
# Z  6  NaN

print(df_nan.cumprod())
#    A     B
# X  1   4.0
# Y  2   NaN
# Z  6  24.0

print(df_nan.cumprod(skipna=False))
#    A    B
# X  1  4.0
# Y  2  NaN
# Z  6  NaN

df2 = pd.DataFrame({'A': [1, 4, 2], 'B': [6, 3, 5]}, index=['X', 'Y', 'Z'])
print(df2)
#    A  B
# X  1  6
# Y  4  3
# Z  2  5

print(df2.cummax())
#    A  B
# X  1  6
# Y  4  6
# Z  4  6

print(df2.cummax(axis=1))
#    A  B
# X  1  6
# Y  4  4
# Z  2  5

print(df2.cummin())
#    A  B
# X  1  6
# Y  1  3
# Z  1  3

print(df2.cummin(axis=1))
#    A  B
# X  1  1
# Y  4  3
# Z  2  2
