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

print(df.dropna(how='all'))
#       name   age state  point  other
# 0    Alice  24.0    NY    NaN    NaN
# 2  Charlie   NaN    CA    NaN    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen   NaN    CA   88.0    NaN
# 5    Frank  30.0   NaN    NaN    NaN

print(df.dropna(how='all', axis=1))
#       name   age state  point
# 0    Alice  24.0    NY    NaN
# 1      NaN   NaN   NaN    NaN
# 2  Charlie   NaN    CA    NaN
# 3     Dave  68.0    TX   70.0
# 4    Ellen   NaN    CA   88.0
# 5    Frank  30.0   NaN    NaN

# print(df.dropna(how='all', axis=[0, 1]))
# TypeError: supplying multiple axes to axis is no longer supported.

print(df.dropna(how='all').dropna(how='all', axis=1))
#       name   age state  point
# 0    Alice  24.0    NY    NaN
# 2  Charlie   NaN    CA    NaN
# 3     Dave  68.0    TX   70.0
# 4    Ellen   NaN    CA   88.0
# 5    Frank  30.0   NaN    NaN

df2 = df.dropna(how='all').dropna(how='all', axis=1)
print(df2)
#       name   age state  point
# 0    Alice  24.0    NY    NaN
# 2  Charlie   NaN    CA    NaN
# 3     Dave  68.0    TX   70.0
# 4    Ellen   NaN    CA   88.0
# 5    Frank  30.0   NaN    NaN

print(df2.dropna(how='any'))
#    name   age state  point
# 3  Dave  68.0    TX   70.0

print(df2.dropna())
#    name   age state  point
# 3  Dave  68.0    TX   70.0

print(df2.dropna(axis=1))
#       name
# 0    Alice
# 2  Charlie
# 3     Dave
# 4    Ellen
# 5    Frank

print(df.dropna(thresh=3))
#     name   age state  point  other
# 0  Alice  24.0    NY    NaN    NaN
# 3   Dave  68.0    TX   70.0    NaN
# 4  Ellen   NaN    CA   88.0    NaN

print(df.dropna(thresh=3, axis=1))
#       name   age state
# 0    Alice  24.0    NY
# 1      NaN   NaN   NaN
# 2  Charlie   NaN    CA
# 3     Dave  68.0    TX
# 4    Ellen   NaN    CA
# 5    Frank  30.0   NaN

print(df.dropna(subset=['age']))
#     name   age state  point  other
# 0  Alice  24.0    NY    NaN    NaN
# 3   Dave  68.0    TX   70.0    NaN
# 5  Frank  30.0   NaN    NaN    NaN

print(df.dropna(subset=['age', 'state']))
#     name   age state  point  other
# 0  Alice  24.0    NY    NaN    NaN
# 3   Dave  68.0    TX   70.0    NaN

print(df.dropna(subset=['age', 'state'], how='all'))
#       name   age state  point  other
# 0    Alice  24.0    NY    NaN    NaN
# 2  Charlie   NaN    CA    NaN    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen   NaN    CA   88.0    NaN
# 5    Frank  30.0   NaN    NaN    NaN

print(df.dropna(subset=[0, 4], axis=1))
#       name state
# 0    Alice    NY
# 1      NaN   NaN
# 2  Charlie    CA
# 3     Dave    TX
# 4    Ellen    CA
# 5    Frank   NaN

print(df.dropna(subset=[0, 4], axis=1, how='all'))
#       name   age state  point
# 0    Alice  24.0    NY    NaN
# 1      NaN   NaN   NaN    NaN
# 2  Charlie   NaN    CA    NaN
# 3     Dave  68.0    TX   70.0
# 4    Ellen   NaN    CA   88.0
# 5    Frank  30.0   NaN    NaN

# print(df.dropna(subset=['age', 'state', 'xxx']))
# KeyError: ['xxx']

# print(df.dropna(subset=['age', 'state'], axis=1))
# KeyError: ['age', 'state']

df.dropna(subset=['age'], inplace=True)
print(df)
#     name   age state  point  other
# 0  Alice  24.0    NY    NaN    NaN
# 3   Dave  68.0    TX   70.0    NaN
# 5  Frank  30.0   NaN    NaN    NaN

s = pd.read_csv('data/src/sample_pandas_normal_nan.csv')['age']
print(s)
# 0    24.0
# 1     NaN
# 2     NaN
# 3    68.0
# 4     NaN
# 5    30.0
# Name: age, dtype: float64

print(s.dropna())
# 0    24.0
# 3    68.0
# 5    30.0
# Name: age, dtype: float64

s.dropna(inplace=True)
print(s)
# 0    24.0
# 3    68.0
# 5    30.0
# Name: age, dtype: float64
