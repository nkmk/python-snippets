import pandas as pd

df = pd.read_csv('data/src/sample_pandas_normal_nan.csv')[:3]
print(df)
#       name   age state  point  other
# 0    Alice  24.0    NY    NaN    NaN
# 1      NaN   NaN   NaN    NaN    NaN
# 2  Charlie   NaN    CA    NaN    NaN

print(df.isnull())
#     name    age  state  point  other
# 0  False  False  False   True   True
# 1   True   True   True   True   True
# 2  False   True  False   True   True

print(df.isna())
#     name    age  state  point  other
# 0  False  False  False   True   True
# 1   True   True   True   True   True
# 2  False   True  False   True   True

print(df.notnull())
#     name    age  state  point  other
# 0   True   True   True  False  False
# 1  False  False  False  False  False
# 2   True  False   True  False  False

print(df.notna())
#     name    age  state  point  other
# 0   True   True   True  False  False
# 1  False  False  False  False  False
# 2   True  False   True  False  False

print(df == float('nan'))
#     name    age  state  point  other
# 0  False  False  False  False  False
# 1  False  False  False  False  False
# 2  False  False  False  False  False

print(df != float('nan'))
#    name   age  state  point  other
# 0  True  True   True   True   True
# 1  True  True   True   True   True
# 2  True  True   True   True   True

print(df.isnull().all())
# name     False
# age      False
# state    False
# point     True
# other     True
# dtype: bool

print(df.isnull().all(axis=1))
# 0    False
# 1     True
# 2    False
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
# dtype: bool

print(df.isnull().sum())
# name     1
# age      2
# state    1
# point    3
# other    3
# dtype: int64

print(df.isnull().sum(axis=1))
# 0    2
# 1    5
# 2    3
# dtype: int64

print(df.count())
# name     2
# age      1
# state    2
# point    0
# other    0
# dtype: int64

print(df.count(axis=1))
# 0    3
# 1    0
# 2    2
# dtype: int64

print(df.isnull().values)
# [[False False False  True  True]
#  [ True  True  True  True  True]
#  [False  True False  True  True]]

print(type(df.isnull().values))
# <class 'numpy.ndarray'>

print(df.isnull().values.sum())
# 10

print(df.count().sum())
# 5

print(df.notnull().values.sum())
# 5

print(df.isnull().values.sum() != 0)
# True

print(df.size)
# 15

print(df.isnull().values.sum() == df.size)
# False

s = df['state']
print(s)
# 0     NY
# 1    NaN
# 2     CA
# Name: state, dtype: object

print(s.isnull())
# 0    False
# 1     True
# 2    False
# Name: state, dtype: bool

print(s.notnull())
# 0     True
# 1    False
# 2     True
# Name: state, dtype: bool

print(s.isnull().any())
# True

print(s.isnull().all())
# False

print(s.isnull().sum())
# 1

print(s.count())
# 2
