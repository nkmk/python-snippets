import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [-20, -10, 0, 10, 20],
                   'B': [1, 2, 3, 4, 5],
                   'C': ['a', 'b', 'b', 'b', 'a']})

print(df)
#     A  B  C
# 0 -20  1  a
# 1 -10  2  b
# 2   0  3  b
# 3  10  4  b
# 4  20  5  a

df.loc[df['A'] < 0, 'A'] = -100
df.loc[~(df['A'] < 0), 'A'] = 100
print(df)
#      A  B  C
# 0 -100  1  a
# 1 -100  2  b
# 2  100  3  b
# 3  100  4  b
# 4  100  5  a

print(df['A'] < 0)
# 0     True
# 1     True
# 2    False
# 3    False
# 4    False
# Name: A, dtype: bool

print(~(df['A'] < 0))
# 0    False
# 1    False
# 2     True
# 3     True
# 4     True
# Name: A, dtype: bool

print(df.loc[df['A'] < 0, 'A'])
# 0   -100
# 1   -100
# Name: A, dtype: int64

df.loc[df['A'] < 0, 'A'] = -10
print(df)
#      A  B  C
# 0  -10  1  a
# 1  -10  2  b
# 2  100  3  b
# 3  100  4  b
# 4  100  5  a

df.loc[~(df['A'] < 0), 'A'] = df['B']
print(df)
#     A  B  C
# 0 -10  1  a
# 1 -10  2  b
# 2   3  3  b
# 3   4  4  b
# 4   5  5  a

df.loc[df['B'] % 2 == 0, 'D'] = 'even'
df.loc[df['B'] % 2 != 0, 'D'] = 'odd'
print(df)
#     A  B  C     D
# 0 -10  1  a   odd
# 1 -10  2  b  even
# 2   3  3  b   odd
# 3   4  4  b  even
# 4   5  5  a   odd

df.loc[~(df['A'] < 0) & (df['C'] == 'b'), 'E'] = df['B'] * 2
print(df)
#     A  B  C     D    E
# 0 -10  1  a   odd  NaN
# 1 -10  2  b  even  NaN
# 2   3  3  b   odd  6.0
# 3   4  4  b  even  8.0
# 4   5  5  a   odd  NaN

df.loc[~(df['A'] < 0), 'A'] = 10
print(df)
#     A  B  C     D    E
# 0 -10  1  a   odd  NaN
# 1 -10  2  b  even  NaN
# 2  10  3  b   odd  6.0
# 3  10  4  b  even  8.0
# 4  10  5  a   odd  NaN

df.loc[df['C'] == 'a', 'F'] = df['A']
df.loc[df['C'] == 'b', 'F'] = df['B']
print(df)
#     A  B  C     D    E     F
# 0 -10  1  a   odd  NaN -10.0
# 1 -10  2  b  even  NaN   2.0
# 2  10  3  b   odd  6.0   3.0
# 3  10  4  b  even  8.0   4.0
# 4  10  5  a   odd  NaN  10.0

df['F'] = df['F'].astype(int)
print(df)
#     A  B  C     D    E   F
# 0 -10  1  a   odd  NaN -10
# 1 -10  2  b  even  NaN   2
# 2  10  3  b   odd  6.0   3
# 3  10  4  b  even  8.0   4
# 4  10  5  a   odd  NaN  10

df.loc[df['C'] == 'a', ['E', 'F']] = 100
print(df)
#     A  B  C     D      E    F
# 0 -10  1  a   odd  100.0  100
# 1 -10  2  b  even    NaN    2
# 2  10  3  b   odd    6.0    3
# 3  10  4  b  even    8.0    4
# 4  10  5  a   odd  100.0  100

print(df < 0)
#        A      B     C     D      E      F
# 0   True  False  True  True  False  False
# 1   True  False  True  True  False  False
# 2  False  False  True  True  False  False
# 3  False  False  True  True  False  False
# 4  False  False  True  True  False  False

print(df[df < 0])
#       A   B  C     D   E   F
# 0 -10.0 NaN  a   odd NaN NaN
# 1 -10.0 NaN  b  even NaN NaN
# 2   NaN NaN  b   odd NaN NaN
# 3   NaN NaN  b  even NaN NaN
# 4   NaN NaN  a   odd NaN NaN

# df[df < 0] = 0
# TypeError: Cannot do inplace boolean setting on mixed-types with a non np.nan value

df = pd.DataFrame({'A': [-20, -10, 0, 10, 20],
                   'B': [1, 2, 3, 4, 5],
                   'C': ['a', 'b', 'b', 'b', 'a']})
print(df)
#     A  B  C
# 0 -20  1  a
# 1 -10  2  b
# 2   0  3  b
# 3  10  4  b
# 4  20  5  a

print(df['A'].where(df['C'] == 'a'))
# 0   -20.0
# 1     NaN
# 2     NaN
# 3     NaN
# 4    20.0
# Name: A, dtype: float64

print(df['A'].where(df['C'] == 'a', 100))
# 0    -20
# 1    100
# 2    100
# 3    100
# 4     20
# Name: A, dtype: int64

print(df['A'].where(df['C'] == 'a', df['B']))
# 0   -20
# 1     2
# 2     3
# 3     4
# 4    20
# Name: A, dtype: int64

df['D'] = df['A'].where(df['C'] == 'a', df['B'])
print(df)
#     A  B  C   D
# 0 -20  1  a -20
# 1 -10  2  b   2
# 2   0  3  b   3
# 3  10  4  b   4
# 4  20  5  a  20

df['D'].where((df['D'] % 2 == 0) & (df['A'] < 0), df['D'] * 100, inplace=True)
print(df)
#     A  B  C     D
# 0 -20  1  a   -20
# 1 -10  2  b     2
# 2   0  3  b   300
# 3  10  4  b   400
# 4  20  5  a  2000

print(df < 0)
#        A      B     C      D
# 0   True  False  True   True
# 1   True  False  True  False
# 2  False  False  True  False
# 3  False  False  True  False
# 4  False  False  True  False

print(df.where(df < 0))
#       A   B  C     D
# 0 -20.0 NaN  a -20.0
# 1 -10.0 NaN  b   NaN
# 2   NaN NaN  b   NaN
# 3   NaN NaN  b   NaN
# 4   NaN NaN  a   NaN

print(df.where(df < 0, df * 2))
#     A   B  C     D
# 0 -20   2  a   -20
# 1 -10   4  b     4
# 2   0   6  b   600
# 3  20   8  b   800
# 4  40  10  a  4000

print(df.where(df < 0, 100))
#      A    B  C    D
# 0  -20  100  a  -20
# 1  -10  100  b  100
# 2  100  100  b  100
# 3  100  100  b  100
# 4  100  100  a  100

df = pd.DataFrame({'A': [-20, -10, 0, 10, 20],
                   'B': [1, 2, 3, 4, 5],
                   'C': ['a', 'b', 'b', 'b', 'a']})
print(df)
#     A  B  C
# 0 -20  1  a
# 1 -10  2  b
# 2   0  3  b
# 3  10  4  b
# 4  20  5  a

print(df['C'].mask(df['C'] == 'a'))
# 0    NaN
# 1      b
# 2      b
# 3      b
# 4    NaN
# Name: C, dtype: object

print(df['C'].mask(df['C'] == 'a', 100))
# 0    100
# 1      b
# 2      b
# 3      b
# 4    100
# Name: C, dtype: object

df['D'] = df['A'].mask(df['C'] == 'a', df['B'])
print(df)
#     A  B  C   D
# 0 -20  1  a   1
# 1 -10  2  b -10
# 2   0  3  b   0
# 3  10  4  b  10
# 4  20  5  a   5

df['D'].mask(df['D'] % 2 != 0, df['D'] * 10, inplace=True)
print(df)
#     A  B  C   D
# 0 -20  1  a  10
# 1 -10  2  b -10
# 2   0  3  b   0
# 3  10  4  b  10
# 4  20  5  a  50

print(df.mask(df < 0, -100))
#      A  B     C    D
# 0 -100  1  -100   10
# 1 -100  2  -100 -100
# 2    0  3  -100    0
# 3   10  4  -100   10
# 4   20  5  -100   50

print(df.select_dtypes(include='number').mask(df < 0, -100))
#      A  B    D
# 0 -100  1   10
# 1 -100  2 -100
# 2    0  3    0
# 3   10  4   10
# 4   20  5   50

df_mask = df.select_dtypes(include='number').mask(df < 0, -100)
df_mask = pd.concat([df_mask, df.select_dtypes(exclude='number')], axis=1)
print(df_mask.sort_index(axis=1))
#      A  B  C    D
# 0 -100  1  a   10
# 1 -100  2  b -100
# 2    0  3  b    0
# 3   10  4  b   10
# 4   20  5  a   50

df = pd.DataFrame({'A': [-20, -10, 0, 10, 20],
                   'B': [1, 2, 3, 4, 5],
                   'C': ['a', 'b', 'b', 'b', 'a']})
print(df)
#     A  B  C
# 0 -20  1  a
# 1 -10  2  b
# 2   0  3  b
# 3  10  4  b
# 4  20  5  a

print(np.where(df['B'] % 2 == 0, 'even', 'odd'))
# ['odd' 'even' 'odd' 'even' 'odd']

print(np.where(df['C'] == 'a', df['A'], df['B']))
# [-20   2   3   4  20]

df['D'] = np.where(df['B'] % 2 == 0, 'even', 'odd')
print(df)
#     A  B  C     D
# 0 -20  1  a   odd
# 1 -10  2  b  even
# 2   0  3  b   odd
# 3  10  4  b  even
# 4  20  5  a   odd

df['E'] = np.where(df['C'] == 'a', df['A'], df['B'])
print(df)
#     A  B  C     D   E
# 0 -20  1  a   odd -20
# 1 -10  2  b  even   2
# 2   0  3  b   odd   3
# 3  10  4  b  even   4
# 4  20  5  a   odd  20

print(np.where(df < 0, df, 100))
# [[-20 100 'a' 'odd' -20]
#  [-10 100 'b' 'even' 100]
#  [100 100 'b' 'odd' 100]
#  [100 100 'b' 'even' 100]
#  [100 100 'a' 'odd' 100]]

df_np_where = pd.DataFrame(np.where(df < 0, df, 100),
                           index=df.index, columns=df.columns)

print(df_np_where)
#      A    B  C     D    E
# 0  -20  100  a   odd  -20
# 1  -10  100  b  even  100
# 2  100  100  b   odd  100
# 3  100  100  b  even  100
# 4  100  100  a   odd  100
