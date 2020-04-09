import pandas as pd

s = pd.Series([1, 2, 3], index=['ONE', 'TWO', 'THREE'])
print(s)
# ONE      1
# TWO      2
# THREE    3
# dtype: int64

print(s.rename({'ONE': 'a', 'THREE': 'c'}))
# a      1
# TWO    2
# c      3
# dtype: int64

print(s.rename(str.lower))
# one      1
# two      2
# three    3
# dtype: int64

print(s.add_prefix('X_'))
# X_ONE      1
# X_TWO      2
# X_THREE    3
# dtype: int64

print(s.add_suffix('_X'))
# ONE_X      1
# TWO_X      2
# THREE_X    3
# dtype: int64

s.index = ['a', 'b', 'c']
print(s)
# a    1
# b    2
# c    3
# dtype: int64
