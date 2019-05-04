import pandas as pd

d = {'a': 100, 'b': 20, 'c': 50, 'd': 100, 'e': 80}

s = pd.Series(d)

print(s)
# a    100
# b     20
# c     50
# d    100
# e     80
# dtype: int64

print(s.index)
# Index(['a', 'b', 'c', 'd', 'e'], dtype='object')

print(s.values)
# [100  20  50 100  80]

print(s.max())
# 100

print(s.min())
# 20

print(max(s.index))
# e

print(min(s.index))
# a

print(s.idxmax())
# a

print(s.idxmin())
# b

print(s[s == s.max()])
# a    100
# d    100
# dtype: int64

print(s[s == s.max()].index)
# Index(['a', 'd'], dtype='object')

print(s[s == s.max()].index.tolist())
# ['a', 'd']

print(list(s[s == s.max()].index))
# ['a', 'd']

print(s[s == s.min()])
# b    20
# dtype: int64

print(s[s == s.min()].index)
# Index(['b'], dtype='object')

print(s[s == s.min()].index.tolist())
# ['b']

print(list(s[s == s.min()].index))
# ['b']

print(s.sort_values())
# b     20
# c     50
# e     80
# a    100
# d    100
# dtype: int64

print(s[s > 60])
# a    100
# d    100
# e     80
# dtype: int64
