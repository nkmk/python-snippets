import pandas as pd

df = pd.DataFrame({'a': range(1, 6),
                   'b': [x**2 for x in range(1, 6)],
                   'c': [x**3 for x in range(1, 6)]})

print(df)
#    a   b    c
# 0  1   1    1
# 1  2   4    8
# 2  3   9   27
# 3  4  16   64
# 4  5  25  125

print(df.diff())
#      a    b     c
# 0  NaN  NaN   NaN
# 1  1.0  3.0   7.0
# 2  1.0  5.0  19.0
# 3  1.0  7.0  37.0
# 4  1.0  9.0  61.0

print(df.diff(1))
#      a    b     c
# 0  NaN  NaN   NaN
# 1  1.0  3.0   7.0
# 2  1.0  5.0  19.0
# 3  1.0  7.0  37.0
# 4  1.0  9.0  61.0

print(df.diff(2))
#      a     b     c
# 0  NaN   NaN   NaN
# 1  NaN   NaN   NaN
# 2  2.0   8.0  26.0
# 3  2.0  12.0  56.0
# 4  2.0  16.0  98.0

print(df.diff(-1))
#      a    b     c
# 0 -1.0 -3.0  -7.0
# 1 -1.0 -5.0 -19.0
# 2 -1.0 -7.0 -37.0
# 3 -1.0 -9.0 -61.0
# 4  NaN  NaN   NaN

print(df.diff(axis=1))
#     a     b      c
# 0 NaN   0.0    0.0
# 1 NaN   2.0    4.0
# 2 NaN   6.0   18.0
# 3 NaN  12.0   48.0
# 4 NaN  20.0  100.0

print(df.diff(-1, axis=1))
#       a      b   c
# 0   0.0    0.0 NaN
# 1  -2.0   -4.0 NaN
# 2  -6.0  -18.0 NaN
# 3 -12.0  -48.0 NaN
# 4 -20.0 -100.0 NaN

print(df.diff(2).dropna())
#      a     b     c
# 2  2.0   8.0  26.0
# 3  2.0  12.0  56.0
# 4  2.0  16.0  98.0

print(df.diff(2).fillna(0))
#      a     b     c
# 0  0.0   0.0   0.0
# 1  0.0   0.0   0.0
# 2  2.0   8.0  26.0
# 3  2.0  12.0  56.0
# 4  2.0  16.0  98.0

print(df.diff(2).fillna(method='bfill'))
#      a     b     c
# 0  2.0   8.0  26.0
# 1  2.0   8.0  26.0
# 2  2.0   8.0  26.0
# 3  2.0  12.0  56.0
# 4  2.0  16.0  98.0

df['b_diff'] = df['b'].diff(-1)
print(df)
#    a   b    c  b_diff
# 0  1   1    1    -3.0
# 1  2   4    8    -5.0
# 2  3   9   27    -7.0
# 3  4  16   64    -9.0
# 4  5  25  125     NaN
