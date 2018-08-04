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

print(df.shift())
#      a     b     c
# 0  NaN   NaN   NaN
# 1  1.0   1.0   1.0
# 2  2.0   4.0   8.0
# 3  3.0   9.0  27.0
# 4  4.0  16.0  64.0

print(df.shift(1))
#      a     b     c
# 0  NaN   NaN   NaN
# 1  1.0   1.0   1.0
# 2  2.0   4.0   8.0
# 3  3.0   9.0  27.0
# 4  4.0  16.0  64.0

print(df.shift(2))
#      a    b     c
# 0  NaN  NaN   NaN
# 1  NaN  NaN   NaN
# 2  1.0  1.0   1.0
# 3  2.0  4.0   8.0
# 4  3.0  9.0  27.0

print(df.shift(-1))
#      a     b      c
# 0  2.0   4.0    8.0
# 1  3.0   9.0   27.0
# 2  4.0  16.0   64.0
# 3  5.0  25.0  125.0
# 4  NaN   NaN    NaN

print(df.shift(axis=1))
#     a    b     c
# 0 NaN  1.0   1.0
# 1 NaN  2.0   4.0
# 2 NaN  3.0   9.0
# 3 NaN  4.0  16.0
# 4 NaN  5.0  25.0

print(df.shift(-1, axis=1))
#       a      b   c
# 0   1.0    1.0 NaN
# 1   4.0    8.0 NaN
# 2   9.0   27.0 NaN
# 3  16.0   64.0 NaN
# 4  25.0  125.0 NaN
