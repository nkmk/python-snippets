import pandas as pd

print(pd.__version__)
# 2.1.2

s = pd.Series(['A', 'B', 'C', 'A', 'B'])
print(s)
# 0    A
# 1    B
# 2    C
# 3    A
# 4    B
# dtype: object

print(s.map({'A': 'XX', 'B': 'YY', 'C': 'ZZ'}))
# 0    XX
# 1    YY
# 2    ZZ
# 3    XX
# 4    YY
# dtype: object

print(s.replace({'A': 'XX', 'B': 'YY', 'C': 'ZZ'}))
# 0    XX
# 1    YY
# 2    ZZ
# 3    XX
# 4    YY
# dtype: object

print(s.map({'A': 'XX'}))
# 0     XX
# 1    NaN
# 2    NaN
# 3     XX
# 4    NaN
# dtype: object

print(s.replace({'A': 'XX'}))
# 0    XX
# 1     B
# 2     C
# 3    XX
# 4     B
# dtype: object

print(s.map({'A': 'XX'}).fillna(s))
# 0    XX
# 1     B
# 2     C
# 3    XX
# 4     B
# dtype: object
