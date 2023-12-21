import pandas as pd
import numpy as np

print(pd.__version__)
# 2.1.4

print(np.__version__)
# 1.26.2

df = pd.DataFrame({'a': [1, 2, 3],
                   'b': np.array([10, 20, 30], dtype=np.int32),
                   'c': [0.1, 0.2, 0.3],
                   'd': ['X', 'Y', 'Z'],
                   'e': [[0, 0], [1, 1], [2, 2]],
                   'f': [True, True, False],
                   'g': pd.to_datetime(['2023-12-01', '2023-12-02', '2023-12-03'])})
print(df)
#    a   b    c  d       e      f          g
# 0  1  10  0.1  X  [0, 0]   True 2023-12-01
# 1  2  20  0.2  Y  [1, 1]   True 2023-12-02
# 2  3  30  0.3  Z  [2, 2]  False 2023-12-03

print(df.dtypes)
# a             int64
# b             int32
# c           float64
# d            object
# e            object
# f              bool
# g    datetime64[ns]
# dtype: object

print(df.select_dtypes(include=int))
#    a   b
# 0  1  10
# 1  2  20
# 2  3  30

print(df.select_dtypes(include=['int32', bool]))
#     b      f
# 0  10   True
# 1  20   True
# 2  30  False

print(df.select_dtypes(include='float32'))
# Empty DataFrame
# Columns: []
# Index: [0, 1, 2]

print(df.select_dtypes(include='number'))
#    a   b    c
# 0  1  10  0.1
# 1  2  20  0.2
# 2  3  30  0.3

print(df.select_dtypes(exclude=int))
#      c  d       e      f          g
# 0  0.1  X  [0, 0]   True 2023-12-01
# 1  0.2  Y  [1, 1]   True 2023-12-02
# 2  0.3  Z  [2, 2]  False 2023-12-03

print(df.select_dtypes(exclude=['int32', bool]))
#    a    c  d       e          g
# 0  1  0.1  X  [0, 0] 2023-12-01
# 1  2  0.2  Y  [1, 1] 2023-12-02
# 2  3  0.3  Z  [2, 2] 2023-12-03

print(df.select_dtypes(include='number', exclude='int32'))
#    a    c
# 0  1  0.1
# 1  2  0.2
# 2  3  0.3

# print(df.select_dtypes(include=['int32', bool], exclude='int32'))
# ValueError: include and exclude overlap on frozenset({<class 'numpy.int32'>})

print(df.select_dtypes(include=['i8', 'int32', np.float64]))
#    a   b    c
# 0  1  10  0.1
# 1  2  20  0.2
# 2  3  30  0.3

print(df.select_dtypes(include=['number', 'datetime']))
#    a   b    c          g
# 0  1  10  0.1 2023-12-01
# 1  2  20  0.2 2023-12-02
# 2  3  30  0.3 2023-12-03

# print(df.select_dtypes(include=str))
# TypeError: string dtypes are not allowed, use 'object' instead

print(df.select_dtypes(include=object))
#    d       e
# 0  X  [0, 0]
# 1  Y  [1, 1]
# 2  Z  [2, 2]

print(type(df.at[0, 'd']))
# <class 'str'>

print(type(df.at[0, 'e']))
# <class 'list'>

print(df.iloc[0].map(type) == str)
# a    False
# b    False
# c    False
# d     True
# e    False
# f    False
# g    False
# Name: 0, dtype: bool

print(df.loc[:, df.iloc[0].map(type) == str])
#    d
# 0  X
# 1  Y
# 2  Z
