import pandas as pd

df = pd.read_csv('data/src/sample_pandas_normal_nan.csv')
print(df)
#       name   age state  point  other
# 0    Alice  24.0    NY    NaN    NaN
# 1      NaN   NaN   NaN    NaN    NaN
# 2  Charlie   NaN    CA    NaN    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen   NaN    CA   88.0    NaN
# 5    Frank  30.0   NaN    NaN    NaN

print(df.isnull())
#     name    age  state  point  other
# 0  False  False  False   True   True
# 1   True   True   True   True   True
# 2  False   True  False   True   True
# 3  False  False  False  False   True
# 4  False   True  False  False   True
# 5  False  False   True   True   True

print(df.isnull().all())
# name     False
# age      False
# state    False
# point    False
# other     True
# dtype: bool

print(df.isnull().all(axis=1))
# 0    False
# 1     True
# 2    False
# 3    False
# 4    False
# 5    False
# dtype: bool

print(df.isnull().any())
# name     True
# age      True
# state    True
# point    True
# other    True
# dtype: bool

print(df.isnull().any(axis=1))
# 0    True
# 1    True
# 2    True
# 3    True
# 4    True
# 5    True
# dtype: bool

print(df.isnull().sum())
# name     1
# age      3
# state    2
# point    4
# other    6
# dtype: int64

print(df.isnull().sum(axis=1))
# 0    2
# 1    5
# 2    3
# 3    1
# 4    2
# 5    3
# dtype: int64

print(df.count())
# name     5
# age      3
# state    4
# point    2
# other    0
# dtype: int64

print(df.count(axis=1))
# 0    3
# 1    0
# 2    2
# 3    4
# 4    3
# 5    2
# dtype: int64

print(df.isnull().values)
# [[False False False  True  True]
#  [ True  True  True  True  True]
#  [False  True False  True  True]
#  [False False False False  True]
#  [False  True False False  True]
#  [False False  True  True  True]]

print(type(df.isnull().values))
# <class 'numpy.ndarray'>

print(df.isnull().values.sum())
# 16

print(df.count().sum())
# 14

print(df.isnull().values.sum() != 0)
# True

print(df.size)
# 30

print(df.isnull().values.sum() == df.size)
# False

s = df['state']
print(s)
# 0     NY
# 1    NaN
# 2     CA
# 3     TX
# 4     CA
# 5    NaN
# Name: state, dtype: object

print(s.isnull())
# 0    False
# 1     True
# 2    False
# 3    False
# 4    False
# 5     True
# Name: state, dtype: bool

print(s.isnull().any())
# True

print(s.isnull().all())
# False

print(s.isnull().sum())
# 2

print(s.count())
# 4
