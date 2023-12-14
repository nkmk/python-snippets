import pandas as pd

print(pd.__version__)
# 2.1.4

s = pd.Series(['X', 'X', 'X', 'Y'])
print(s)
# 0    X
# 1    X
# 2    X
# 3    Y
# dtype: object

print(s.mode())
# 0    X
# dtype: object

print(type(s.mode()))
# <class 'pandas.core.series.Series'>

print(s.mode()[0])
# X

print(type(s.mode()[0]))
# <class 'str'>

s_multi = pd.Series(['X', 'X', 'Y', 'Y'])
print(s_multi)
# 0    X
# 1    X
# 2    Y
# 3    Y
# dtype: object

print(s_multi.mode())
# 0    X
# 1    Y
# dtype: object

print(s_multi.mode()[0])
# X

print(s_multi.mode().tolist())
# ['X', 'Y']

print(type(s_multi.mode().tolist()))
# <class 'list'>

s_nan = pd.Series(['X', float('nan'), float('nan'), float('nan')])
print(s_nan)
# 0      X
# 1    NaN
# 2    NaN
# 3    NaN
# dtype: object

print(s_nan.mode())
# 0    X
# dtype: object

print(s_nan.mode(dropna=False))
# 0    NaN
# dtype: object

df = pd.DataFrame({'col1': ['X', 'X', 'X', 'Y'],
                   'col2': ['X', 'X', 'Y', 'Y']},
                  index=['row1', 'row2', 'row3', 'row4'])
print(df)
#      col1 col2
# row1    X    X
# row2    X    X
# row3    X    Y
# row4    Y    Y

print(df.mode())
#   col1 col2
# 0    X    X
# 1  NaN    Y

print(type(df.mode()))
# <class 'pandas.core.frame.DataFrame'>

print(df.mode().count())
# col1    1
# col2    2
# dtype: int64

print(df.mode().iloc[0])
# col1    X
# col2    X
# Name: 0, dtype: object

print(df.mode()['col1'])
# 0      X
# 1    NaN
# Name: col1, dtype: object

print(df['col1'].mode())
# 0    X
# Name: col1, dtype: object

s_list = df.apply(lambda x: x.mode().tolist())
print(s_list)
# col1       [X]
# col2    [X, Y]
# dtype: object

print(s_list.at['col2'])
# ['X', 'Y']

print(type(s_list.at['col2']))
# <class 'list'>

print(df.mode(axis=1))
#       0    1
# row1  X  NaN
# row2  X  NaN
# row3  X    Y
# row4  Y  NaN

print(df.mode(axis=1).count(axis=1))
# row1    1
# row2    1
# row3    2
# row4    1
# dtype: int64

print(df.T)
#      row1 row2 row3 row4
# col1    X    X    X    Y
# col2    X    X    Y    Y

print(df.T.mode())
#   row1 row2 row3 row4
# 0    X    X    X    Y
# 1  NaN  NaN    Y  NaN

df_nan = df.copy()
df_nan.iloc[1:, 1] = float('nan')
print(df_nan)
#      col1 col2
# row1    X    X
# row2    X  NaN
# row3    X  NaN
# row4    Y  NaN

print(df_nan.mode())
#   col1 col2
# 0    X    X

print(df_nan.mode(dropna=False))
#   col1 col2
# 0    X  NaN

df_num = df.copy()
df_num['col3'] = [1, 1, 1, 0]
print(df_num)
#      col1 col2  col3
# row1    X    X     1
# row2    X    X     1
# row3    X    Y     1
# row4    Y    Y     0

print(df_num.mode())
#   col1 col2  col3
# 0    X    X   1.0
# 1  NaN    Y   NaN

print(df_num.mode(numeric_only=True))
#    col3
# 0     1

print(df_num.select_dtypes(exclude='number').mode())
#   col1 col2
# 0    X    X
# 1  NaN    Y

print(df['col1'].value_counts())
# col1
# X    3
# Y    1
# Name: count, dtype: int64

print(df['col1'].value_counts().iat[0])
# 3

print(df.describe())
#        col1 col2
# count     4    4
# unique    2    2
# top       X    X
# freq      3    2

print(df.describe().loc['freq'])
# col1    3
# col2    2
# Name: freq, dtype: object

print(df.describe().at['freq', 'col2'])
# 2

print(df.T.describe())
#        row1 row2 row3 row4
# count     2    2    2    2
# unique    1    1    2    1
# top       X    X    X    Y
# freq      2    2    1    2
