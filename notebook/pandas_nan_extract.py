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

print(df['point'].isnull())
# 0     True
# 1     True
# 2     True
# 3    False
# 4    False
# 5     True
# Name: point, dtype: bool

print(df[df['point'].isnull()])
#       name   age state  point  other
# 0    Alice  24.0    NY    NaN    NaN
# 1      NaN   NaN   NaN    NaN    NaN
# 2  Charlie   NaN    CA    NaN    NaN
# 5    Frank  30.0   NaN    NaN    NaN

print(df.iloc[2].isnull())
# name     False
# age       True
# state    False
# point     True
# other     True
# Name: 2, dtype: bool

print(df.loc[:, df.iloc[2].isnull()])
#     age  point  other
# 0  24.0    NaN    NaN
# 1   NaN    NaN    NaN
# 2   NaN    NaN    NaN
# 3  68.0   70.0    NaN
# 4   NaN   88.0    NaN
# 5  30.0    NaN    NaN

df2 = df.dropna(how='all').dropna(how='all', axis=1)
print(df2)
#       name   age state  point
# 0    Alice  24.0    NY    NaN
# 2  Charlie   NaN    CA    NaN
# 3     Dave  68.0    TX   70.0
# 4    Ellen   NaN    CA   88.0
# 5    Frank  30.0   NaN    NaN

print(df2.isnull())
#     name    age  state  point
# 0  False  False  False   True
# 2  False   True  False   True
# 3  False  False  False  False
# 4  False   True  False  False
# 5  False  False   True   True

print(df2.isnull().any(axis=1))
# 0     True
# 2     True
# 3    False
# 4     True
# 5     True
# dtype: bool

print(df2[df2.isnull().any(axis=1)])
#       name   age state  point
# 0    Alice  24.0    NY    NaN
# 2  Charlie   NaN    CA    NaN
# 4    Ellen   NaN    CA   88.0
# 5    Frank  30.0   NaN    NaN

print(df2.isnull().any())
# name     False
# age       True
# state     True
# point     True
# dtype: bool

print(df2.loc[:, df2.isnull().any()])
#     age state  point
# 0  24.0    NY    NaN
# 2   NaN    CA    NaN
# 3  68.0    TX   70.0
# 4   NaN    CA   88.0
# 5  30.0   NaN    NaN
