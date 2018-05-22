import pandas as pd

df = pd.DataFrame({'a': [1, 2, 1, 3],
                   'b': [0.4, 1.1, 0.1, 0.8],
                   'c': ['X', 'Y', 'X', 'Z'],
                   'd': [[0, 0], [0, 1], [1, 0], [1, 1]],
                   'e': [True, True, False, True]})

df['f'] = pd.to_datetime(['2018-01-01', '2018-03-15', '2018-02-20', '2018-03-15'])

print(df)
#    a    b  c       d      e          f
# 0  1  0.4  X  [0, 0]   True 2018-01-01
# 1  2  1.1  Y  [0, 1]   True 2018-03-15
# 2  1  0.1  X  [1, 0]  False 2018-02-20
# 3  3  0.8  Z  [1, 1]   True 2018-03-15

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
# 2  1
# 3  3

print(df.select_dtypes(include='int'))
#    a
# 0  1
# 1  2
# 2  1
# 3  3

print(df.select_dtypes(include='int64'))
#    a
# 0  1
# 1  2
# 2  1
# 3  3

print(df.select_dtypes(include='int32'))
# Empty DataFrame
# Columns: []
# Index: [0, 1, 2, 3]

print(df.select_dtypes(include=[int, float, 'datetime']))
#    a    b          f
# 0  1  0.4 2018-01-01
# 1  2  1.1 2018-03-15
# 2  1  0.1 2018-02-20
# 3  3  0.8 2018-03-15

print(df.select_dtypes(include='number'))
#    a    b
# 0  1  0.4
# 1  2  1.1
# 2  1  0.1
# 3  3  0.8

print(df.select_dtypes(include=object))
#    c       d
# 0  X  [0, 0]
# 1  Y  [0, 1]
# 2  X  [1, 0]
# 3  Z  [1, 1]

print(type(df.at[0, 'c']))
# <class 'str'>

print(type(df.at[0, 'd']))
# <class 'list'>

print(df.select_dtypes(exclude='number'))
#    c       d      e          f
# 0  X  [0, 0]   True 2018-01-01
# 1  Y  [0, 1]   True 2018-03-15
# 2  X  [1, 0]  False 2018-02-20
# 3  Z  [1, 1]   True 2018-03-15

print(df.select_dtypes(exclude=[bool, 'datetime']))
#    a    b  c       d
# 0  1  0.4  X  [0, 0]
# 1  2  1.1  Y  [0, 1]
# 2  1  0.1  X  [1, 0]
# 3  3  0.8  Z  [1, 1]

print(df.select_dtypes(include='number', exclude=int))
#      b
# 0  0.4
# 1  1.1
# 2  0.1
# 3  0.8

# print(df.select_dtypes(include=[int, bool], exclude=int))
# ValueError: include and exclude overlap on frozenset({<class 'numpy.int64'>})
