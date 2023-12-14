import pandas as pd
import numpy as np

print(pd.__version__)
# 2.1.4

print(np.__version__)
# 1.26.2

s = pd.Series([-2, -1, 0, 1, 2])
print(s)
# 0   -2
# 1   -1
# 2    0
# 3    1
# 4    2
# dtype: int64

print(s < 0)
# 0     True
# 1     True
# 2    False
# 3    False
# 4    False
# dtype: bool

print(s.where(s < 0))
# 0   -2.0
# 1   -1.0
# 2    NaN
# 3    NaN
# 4    NaN
# dtype: float64

print(s.where([False, True, False, True, False]))
# 0    NaN
# 1   -1.0
# 2    NaN
# 3    1.0
# 4    NaN
# dtype: float64

print(s.where(s < 0, 10))
# 0    -2
# 1    -1
# 2    10
# 3    10
# 4    10
# dtype: int64

print(s.where(s < 0, [0, 10, 20, 30, 40]))
# 0    -2
# 1    -1
# 2    20
# 3    30
# 4    40
# dtype: int64

s2 = pd.Series([0, 10, 20, 30, 40], index=[4, 3, 2, 1, 0])
print(s2)
# 4     0
# 3    10
# 2    20
# 1    30
# 0    40
# dtype: int64

print(s.where(s < 0, s2))
# 0    -2
# 1    -1
# 2    20
# 3    10
# 4     0
# dtype: int64

print(s * 100 + 10)
# 0   -190
# 1    -90
# 2     10
# 3    110
# 4    210
# dtype: int64

print(s.where(s < 0, s * 100 + 10))
# 0     -2
# 1     -1
# 2     10
# 3    110
# 4    210
# dtype: int64

s.where(s < 0, 10, inplace=True)
print(s)
# 0    -2
# 1    -1
# 2    10
# 3    10
# 4    10
# dtype: int64

df = pd.DataFrame({'A': [-2, -1, 0, 1, 2], 'B': [0, 10, 20, 30, 40]})
print(df)
#    A   B
# 0 -2   0
# 1 -1  10
# 2  0  20
# 3  1  30
# 4  2  40

print((df < 0) | (df > 20))
#        A      B
# 0   True  False
# 1   True  False
# 2  False  False
# 3  False   True
# 4  False   True

print(df.where((df < 0) | (df > 20)))
#      A     B
# 0 -2.0   NaN
# 1 -1.0   NaN
# 2  NaN   NaN
# 3  NaN  30.0
# 4  NaN  40.0

print(df.where((df < 0) | (df > 20), 100))
#      A    B
# 0   -2  100
# 1   -1  100
# 2  100  100
# 3  100   30
# 4  100   40

print(df * 100 + 10)
#      A     B
# 0 -190    10
# 1  -90  1010
# 2   10  2010
# 3  110  3010
# 4  210  4010

print(df.where((df < 0) | (df > 20), df * 100 + 10))
#      A     B
# 0   -2    10
# 1   -1  1010
# 2   10  2010
# 3  110    30
# 4  210    40

df['C'] = ['A', 'B', 'C', 'D', 'E']
print(df)
#    A   B  C
# 0 -2   0  A
# 1 -1  10  B
# 2  0  20  C
# 3  1  30  D
# 4  2  40  E

# print(df < 0)
# TypeError: '<' not supported between instances of 'str' and 'int'

print(df['C'].where(df['A'] < 0, 'X'))
# 0    A
# 1    B
# 2    X
# 3    X
# 4    X
# Name: C, dtype: object

df['D'] = df['C'].where(df['A'] < 0, 'X')
print(df)
#    A   B  C  D
# 0 -2   0  A  A
# 1 -1  10  B  B
# 2  0  20  C  X
# 3  1  30  D  X
# 4  2  40  E  X

df_num = df.select_dtypes('number')
print(df_num.where(df_num > 0, -10))
#     A   B
# 0 -10 -10
# 1 -10  10
# 2 -10  20
# 3   1  30
# 4   2  40

print(df.select_dtypes(exclude='number'))
#    C  D
# 0  A  A
# 1  B  B
# 2  C  X
# 3  D  X
# 4  E  X

print(pd.concat([df_num.where(df_num > 0, -10), df.select_dtypes(exclude='number')],
                axis=1))
#     A   B  C  D
# 0 -10 -10  A  A
# 1 -10  10  B  B
# 2 -10  20  C  X
# 3   1  30  D  X
# 4   2  40  E  X

s = pd.Series(['Alice', 'Bob', 'Charlie', 'Dave', 'Ellen'])
print(s)
# 0      Alice
# 1        Bob
# 2    Charlie
# 3       Dave
# 4      Ellen
# dtype: object

print(s.mask(s.str.endswith('e')))
# 0      NaN
# 1      Bob
# 2      NaN
# 3      NaN
# 4    Ellen
# dtype: object

print(s.mask(s.str.endswith('e'), 'X'))
# 0        X
# 1      Bob
# 2        X
# 3        X
# 4    Ellen
# dtype: object

print(s.mask(s.str.endswith('e'), s.str.upper()))
# 0      ALICE
# 1        Bob
# 2    CHARLIE
# 3       DAVE
# 4      Ellen
# dtype: object

df = pd.DataFrame({'A': [-2, -1, 0, 1, 2], 'B': [0, 10, 20, 30, 40]})
print(df)
#    A   B
# 0 -2   0
# 1 -1  10
# 2  0  20
# 3  1  30
# 4  2  40

print(df.mask((df < 0) | (df > 20)))
#      A     B
# 0  NaN   0.0
# 1  NaN  10.0
# 2  0.0  20.0
# 3  1.0   NaN
# 4  2.0   NaN

print(df.mask((df < 0) | (df > 20), 100))
#      A    B
# 0  100    0
# 1  100   10
# 2    0   20
# 3    1  100
# 4    2  100

print(df.mask((df < 0) | (df > 20), df * 100 + 10))
#      A     B
# 0 -190     0
# 1  -90    10
# 2    0    20
# 3    1  3010
# 4    2  4010

s = pd.Series([-2, -1, 0, 1, 2])
print(s)
# 0   -2
# 1   -1
# 2    0
# 3    1
# 4    2
# dtype: int64

print(np.where(s < 0, -100, 1))
# [-100 -100    1    1    1]

print(np.where(s < 0, s * 10, s * 100 + 10))
# [-20 -10  10 110 210]

print(type(np.where(s < 0, -100, 1)))
# <class 'numpy.ndarray'>

df = pd.DataFrame({'A': [-2, -1, 0, 1, 2], 'B': [0, 10, 20, 30, 40]})
print(df)
#    A   B
# 0 -2   0
# 1 -1  10
# 2  0  20
# 3  1  30
# 4  2  40

print(np.where((df < 0) | (df > 20), -100, 1))
# [[-100    1]
#  [-100    1]
#  [   1    1]
#  [   1 -100]
#  [   1 -100]]

print(np.where((df < 0) | (df > 20), df * 10, df * 100 + 10))
# [[ -20   10]
#  [ -10 1010]
#  [  10 2010]
#  [ 110  300]
#  [ 210  400]]

print(type(np.where((df < 0) | (df > 20), -100, 1)))
# <class 'numpy.ndarray'>

print(pd.Series(np.where(s < 0, -100, 1), index=s.index))
# 0   -100
# 1   -100
# 2      1
# 3      1
# 4      1
# dtype: int64

print(pd.DataFrame(np.where((df < 0) | (df > 20), -100, 1),
                   index=df.index, columns=df.columns))
#      A    B
# 0 -100    1
# 1 -100    1
# 2    1    1
# 3    1 -100
# 4    1 -100

df['C'] = np.where(df['A'] < 0, -100, 1)
print(df)
#    A   B    C
# 0 -2   0 -100
# 1 -1  10 -100
# 2  0  20    1
# 3  1  30    1
# 4  2  40    1

df = pd.DataFrame({'A': [-2, -1, 0, 1, 2], 'B': [0, 10, 20, 30, 40]})
print(df)
#    A   B
# 0 -2   0
# 1 -1  10
# 2  0  20
# 3  1  30
# 4  2  40

print(df.loc[df['A'] < 0, 'A'])
# 0   -2
# 1   -1
# Name: A, dtype: int64

df.loc[df['A'] < 0, 'A'] = -10
print(df)
#     A   B
# 0 -10   0
# 1 -10  10
# 2   0  20
# 3   1  30
# 4   2  40

df.loc[df['A'] >= 0, 'A'] = df['B'] * 10
print(df)
#      A   B
# 0  -10   0
# 1  -10  10
# 2  200  20
# 3  300  30
# 4  400  40

df.loc[df['A'] < 0, 'C'] = -100
print(df)
#      A   B      C
# 0  -10   0 -100.0
# 1  -10  10 -100.0
# 2  200  20    NaN
# 3  300  30    NaN
# 4  400  40    NaN
