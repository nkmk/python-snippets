import pandas as pd

print(pd.__version__)
# 2.1.2

df = pd.DataFrame([[10, 20, 30], [40, 50, 60]], index=['X', 'Y'], columns=['A', 'B', 'C'])
print(df)
#     A   B   C
# X  10  20  30
# Y  40  50  60

print(df.apply(sum))
# A    50
# B    70
# C    90
# dtype: int64

print(df.apply(lambda x: type(x)))
# A    <class 'pandas.core.series.Series'>
# B    <class 'pandas.core.series.Series'>
# C    <class 'pandas.core.series.Series'>
# dtype: object

# print(hex(df['A']))
# TypeError: 'Series' object cannot be interpreted as an integer

# print(df.apply(hex))
# TypeError: 'Series' object cannot be interpreted as an integer

print(df.apply(sum, axis=1))
# X     60
# Y    150
# dtype: int64

def my_func(x, y, z):
    return sum(x) + y + z * 2

print(df.apply(my_func, y=100, z=1000))
# A    2150
# B    2170
# C    2190
# dtype: int64

print(df.apply(my_func, args=(100, 1000)))
# A    2150
# B    2170
# C    2190
# dtype: int64

print(df.apply(lambda x: type(x), raw=True))
# A    <class 'numpy.ndarray'>
# B    <class 'numpy.ndarray'>
# C    <class 'numpy.ndarray'>
# dtype: object

print(df.apply(lambda x: x.name * 3))
# A    AAA
# B    BBB
# C    CCC
# dtype: object

# print(df.apply(lambda x: x.name * 3, raw=True))
# AttributeError: 'numpy.ndarray' object has no attribute 'name'

print(df['A'].map(lambda x: x**2))
# X     100
# Y    1600
# Name: A, dtype: int64

print(df.loc['Y'].map(hex))
# A    0x28
# B    0x32
# C    0x3c
# Name: Y, dtype: object

df['A'] = df['A'].map(lambda x: x**2)
df.loc['Y_hex'] = df.loc['Y'].map(hex)
print(df)
#            A     B     C
# X        100    20    30
# Y       1600    50    60
# Y_hex  0x640  0x32  0x3c
