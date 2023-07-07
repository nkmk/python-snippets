import pandas as pd

print(pd.__version__)
# 2.0.3

df_empty = pd.DataFrame()
print(df_empty)
# Empty DataFrame
# Columns: []
# Index: []

print(df_empty.empty)
# True

df_full = pd.DataFrame({'A': [0, 1, 2]})
print(df_full)
#    A
# 0  0
# 1  1
# 2  2

print(df_full.empty)
# False

df_nan = pd.DataFrame({'A': [float('NaN'), float('NaN'), float('NaN')]})
print(df_nan)
#     A
# 0 NaN
# 1 NaN
# 2 NaN

print(df_nan.empty)
# False

print(df_nan.dropna())
# Empty DataFrame
# Columns: [A]
# Index: []

print(df_nan.dropna().empty)
# True

df_mix = pd.DataFrame({'A': [float('NaN'), float('NaN'), float('NaN')], 'B': [0, 1, 2]})
print(df_mix)
#     A  B
# 0 NaN  0
# 1 NaN  1
# 2 NaN  2

print(df_mix.dropna())
# Empty DataFrame
# Columns: [A, B]
# Index: []

print(df_mix.dropna(how='all'))
#     A  B
# 0 NaN  0
# 1 NaN  1
# 2 NaN  2

s_empty = pd.Series()
print(s_empty)
# Series([], dtype: object)

print(s_empty.empty)
# True

s_full = pd.Series([0, 1, 2])
print(s_full)
# 0    0
# 1    1
# 2    2
# dtype: int64

print(s_full.empty)
# False

s_nan = pd.Series([float('NaN'), float('NaN'), float('NaN')])
print(s_nan)
# 0   NaN
# 1   NaN
# 2   NaN
# dtype: float64

print(s_nan.empty)
# False

print(s_nan.dropna())
# Series([], dtype: float64)

print(s_nan.dropna().empty)
# True

l_empty = []

print(bool(l_empty))
# False

if not l_empty:
    print('Empty!')
# Empty!

df_empty = pd.DataFrame()
print(df_empty)
# Empty DataFrame
# Columns: []
# Index: []

# print(bool(df_empty))
# ValueError: The truth value of a DataFrame is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().

print(df_empty.empty)
# True

# if df_empty:
#     print('Empty!')
# ValueError: The truth value of a DataFrame is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().

if df_empty.empty:
    print('Empty!')
# Empty!

df = pd.DataFrame({'A': [0, 1, 2], 'B': ['aaa', 'bbb', 'ccc']})
print(df)
#    A    B
# 0  0  aaa
# 1  1  bbb
# 2  2  ccc

print(df[df['A'] < 0])
# Empty DataFrame
# Columns: [A, B]
# Index: []

print(df[df['A'] < 0].empty)
# True

print(df.query('A < 0'))
# Empty DataFrame
# Columns: [A, B]
# Index: []

print(df.query('A < 0').empty)
# True
