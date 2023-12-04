import pandas as pd
import numpy as np

print(pd.__version__)
# 2.1.2

print(np.__version__)
# 1.26.1

df = pd.DataFrame([[1, -2, 3], [-4, 5, -6]], index=['X', 'Y'], columns=['A', 'B', 'C'])
print(df)
#    A  B  C
# X  1 -2  3
# Y -4  5 -6

print(df.abs())
#    A  B  C
# X  1  2  3
# Y  4  5  6

print(df.sum())
# A   -3
# B    3
# C   -3
# dtype: int64

print(df.sum(axis=1))
# X    2
# Y   -5
# dtype: int64

print(df * 10)
#     A   B   C
# X  10 -20  30
# Y -40  50 -60

print(df['A'].abs() + df['B'] * 100)
# X   -199
# Y    504
# dtype: int64

df = pd.DataFrame([['a', 'ab', 'abc'], ['x', 'xy', 'xyz']], index=['X', 'Y'], columns=['A', 'B', 'C'])
print(df)
#    A   B    C
# X  a  ab  abc
# Y  x  xy  xyz

print(df['A'] + '-' + df['B'].str.upper() + '-' + df['C'].str.title())
# X    a-AB-Abc
# Y    x-XY-Xyz
# dtype: object

df = pd.DataFrame([[0.1, 0.5, 0.9], [-0.1, -0.5, -0.9]], index=['X', 'Y'], columns=['A', 'B', 'C'])
print(df)
#      A    B    C
# X  0.1  0.5  0.9
# Y -0.1 -0.5 -0.9

print(np.floor(df))
#      A    B    C
# X  0.0  0.0  0.0
# Y -1.0 -1.0 -1.0

print(type(np.floor(df)))
# <class 'pandas.core.frame.DataFrame'>

print(np.floor(df['A']))
# X    0.0
# Y   -1.0
# Name: A, dtype: float64

print(type(np.floor(df['A'])))
# <class 'pandas.core.series.Series'>

print(np.sum(df, axis=0))
# A    0.0
# B    0.0
# C    0.0
# dtype: float64

print(np.sum(df, axis=1))
# X    1.5
# Y   -1.5
# dtype: float64

print(type(np.sum(df, axis=0)))
# <class 'pandas.core.series.Series'>
