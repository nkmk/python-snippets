import pandas as pd

s = pd.Series(['X', 'X', 'Y', 'X'])
print(s)
# 0    X
# 1    X
# 2    Y
# 3    X
# dtype: object

print(s.mode())
# 0    X
# dtype: object

print(type(s.mode()))
# <class 'pandas.core.series.Series'>

mode_value = s.mode()[0]
print(mode_value)
# X

print(type(mode_value))
# <class 'str'>

s_same = pd.Series(['X', 'Y', 'Y', 'X'])
print(s_same)
# 0    X
# 1    Y
# 2    Y
# 3    X
# dtype: object

print(s_same.mode())
# 0    X
# 1    Y
# dtype: object

print(s_same.mode()[0])
# X

l_modes = s_same.mode().tolist()
print(l_modes)
# ['X', 'Y']

print(type(l_modes))
# <class 'list'>

df = pd.DataFrame({'col1': ['X', 'X', 'Y', 'X'],
                   'col2': ['X', 'Y', 'Y', 'X']},
                  index=['row1', 'row2', 'row3', 'row4'])
print(df)
#      col1 col2
# row1    X    X
# row2    X    Y
# row3    Y    Y
# row4    X    X

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
# dtype: object

l_mode = df.apply(lambda x: x.mode().tolist())
print(l_mode)
# col1       [X]
# col2    [X, Y]
# dtype: object

print(l_mode.iat[1])
# ['X', 'Y']

print(type(l_mode.iat[1]))
# <class 'list'>

print(l_mode.iat[1][1])
# Y

print(type(l_mode.iat[1][1]))
# <class 'str'>

print(df.mode(axis=1))
#       0    1
# row1  X  NaN
# row2  X    Y
# row3  Y  NaN
# row4  X  NaN

print(df.mode(axis=1).count(axis=1))
# row1    1
# row2    2
# row3    1
# row4    1
# dtype: int64

df_t = df.T
print(df_t)
#      row1 row2 row3 row4
# col1    X    X    Y    X
# col2    X    Y    Y    X

print(df_t.mode())
#   row1 row2 row3 row4
# 0    X    X    Y    X
# 1  NaN    Y  NaN  NaN

print(df['col1'].value_counts())
# X    3
# Y    1
# Name: col1, dtype: int64

print(df['col1'].value_counts().iat[0])
# 3

print(df.apply(lambda x: x.value_counts().iat[0]))
# col1    3
# col2    2
# dtype: int64

print(df.describe())
#        col1 col2
# count     4    4
# unique    2    2
# top       X    Y
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
# unique    1    2    1    1
# top       X    Y    Y    X
# freq      2    1    2    2
