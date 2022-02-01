import pandas as pd

df = pd.DataFrame({'a': [1, 2, 3],
                   'b': [0.1, 0.2, 0.3],
                   'c': ['X', 'Y', 'Z'],
                   'd': [[0, 0], [1, 1], [2, 2]],
                   'e': [True, True, False]})

df['f'] = pd.to_datetime(['2018-01-01', '2018-02-01', '2018-03-01'])

print(df)
#    a    b  c       d      e          f
# 0  1  0.1  X  [0, 0]   True 2018-01-01
# 1  2  0.2  Y  [1, 1]   True 2018-02-01
# 2  3  0.3  Z  [2, 2]  False 2018-03-01

print(df.dtypes)
# a             int64
# b           float64
# c            object
# d            object
# e              bool
# f    datetime64[ns]
# dtype: object

print(df.select_dtypes(include=int))
#    a
# 0  1
# 1  2
# 2  3

print(df.select_dtypes(include='int'))
#    a
# 0  1
# 1  2
# 2  3

print(df.select_dtypes(include='int64'))
#    a
# 0  1
# 1  2
# 2  3

print(df.select_dtypes(include='int32'))
# Empty DataFrame
# Columns: []
# Index: [0, 1, 2]

print(df.select_dtypes(include=[float, bool, 'datetime']))
#      b      e          f
# 0  0.1   True 2018-01-01
# 1  0.2   True 2018-02-01
# 2  0.3  False 2018-03-01

print(df.select_dtypes(include='number'))
#    a    b
# 0  1  0.1
# 1  2  0.2
# 2  3  0.3

# print(df.select_dtypes(include=str))
# TypeError: string dtypes are not allowed, use 'object' instead

print(df.select_dtypes(include=object))
#    c       d
# 0  X  [0, 0]
# 1  Y  [1, 1]
# 2  Z  [2, 2]

print(type(df.at[0, 'c']))
# <class 'str'>

print(type(df.at[0, 'd']))
# <class 'list'>

print(df.select_dtypes(exclude='number'))
#    c       d      e          f
# 0  X  [0, 0]   True 2018-01-01
# 1  Y  [1, 1]   True 2018-02-01
# 2  Z  [2, 2]  False 2018-03-01

print(df.select_dtypes(exclude=[bool, 'datetime']))
#    a    b  c       d
# 0  1  0.1  X  [0, 0]
# 1  2  0.2  Y  [1, 1]
# 2  3  0.3  Z  [2, 2]

print(df.select_dtypes(include='number', exclude=int))
#      b
# 0  0.1
# 1  0.2
# 2  0.3

# print(df.select_dtypes(include=[int, bool], exclude=int))
# ValueError: include and exclude overlap on frozenset({<class 'numpy.int64'>})
