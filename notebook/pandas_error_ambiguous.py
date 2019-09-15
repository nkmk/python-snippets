import pandas as pd

df = pd.DataFrame(pd.np.arange(12).reshape(3, 4), columns=['a', 'b', 'c', 'd'], index=['x', 'y', 'z'])
print(df)
#    a  b   c   d
# x  0  1   2   3
# y  4  5   6   7
# z  8  9  10  11

print((df > 3) & (df % 2 == 0))
#        a      b      c      d
# x  False  False  False  False
# y   True  False   True  False
# z   True  False   True  False

# print((df > 3) and (df % 2 == 0))
# ValueError: The truth value of a DataFrame is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().

# print(df > 3 & df % 2 == 0)
# ValueError: The truth value of a DataFrame is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().

print(df & 7)
#    a  b  c  d
# x  0  1  2  3
# y  4  5  6  7
# z  0  1  2  3

print(df | 1)
#    a  b   c   d
# x  1  1   3   3
# y  5  5   7   7
# z  9  9  11  11

# print(df << 1)
# TypeError: unsupported operand type(s) for <<: 'DataFrame' and 'int'

# print(df << df)
# TypeError: unsupported operand type(s) for <<: 'DataFrame' and 'DataFrame'

print(df > 3)
#        a      b      c      d
# x  False  False  False  False
# y   True   True   True   True
# z   True   True   True   True

print((df > 3).all())
# a    False
# b    False
# c    False
# d    False
# dtype: bool

print((df > 3).all(axis=1))
# x    False
# y     True
# z     True
# dtype: bool

print((df > 3).all(axis=None))
# False

print(df.empty)
# False

df_empty = pd.DataFrame()
print(df_empty.empty)
# True

print(df.size)
# 12

print(df_empty.size)
# 0
