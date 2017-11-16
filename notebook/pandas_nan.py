import pandas as pd

df = pd.read_csv('data/src/sample_pandas_normal_nan.csv')
print(df)
#       name   age state  point   other
# 0    Alice  24.0    NY    NaN     NaN
# 1      NaN   NaN   NaN    NaN     NaN
# 2  Charlie   NaN    CA    NaN     NaN
# 3     Dave  68.0    TX   70.0     NaN
# 4    Ellen   NaN    CA   88.0     NaN
# 5    Frank  30.0   NaN    NaN     NaN

print(df.at[0, 'point'])
print(type(df.at[0, 'point']))
# nan
# <class 'numpy.float64'>

print(df.dropna(how='all'))
#       name   age state  point   other
# 0    Alice  24.0    NY    NaN     NaN
# 2  Charlie   NaN    CA    NaN     NaN
# 3     Dave  68.0    TX   70.0     NaN
# 4    Ellen   NaN    CA   88.0     NaN
# 5    Frank  30.0   NaN    NaN     NaN

print(df.dropna(how='all', axis=1))
#       name   age state  point
# 0    Alice  24.0    NY    NaN
# 1      NaN   NaN   NaN    NaN
# 2  Charlie   NaN    CA    NaN
# 3     Dave  68.0    TX   70.0
# 4    Ellen   NaN    CA   88.0
# 5    Frank  30.0   NaN    NaN

print(df.dropna(how='all', axis=[0, 1]))
#       name   age state  point
# 0    Alice  24.0    NY    NaN
# 2  Charlie   NaN    CA    NaN
# 3     Dave  68.0    TX   70.0
# 4    Ellen   NaN    CA   88.0
# 5    Frank  30.0   NaN    NaN

df2 = df.dropna(how='all', axis=[0, 1])
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

print(df2.dropna(how='any', axis=1))
#       name
# 0    Alice
# 2  Charlie
# 3     Dave
# 4    Ellen
# 5    Frank

print(df.dropna(thresh=3))
#     name   age state  point   other
# 0  Alice  24.0    NY    NaN     NaN
# 3   Dave  68.0    TX   70.0     NaN
# 4  Ellen   NaN    CA   88.0     NaN

print(df.dropna(thresh=3, axis=1))
#       name   age state
# 0    Alice  24.0    NY
# 1      NaN   NaN   NaN
# 2  Charlie   NaN    CA
# 3     Dave  68.0    TX
# 4    Ellen   NaN    CA
# 5    Frank  30.0   NaN

print(df.dropna(subset=['age']))
#     name   age state  point   other
# 0  Alice  24.0    NY    NaN     NaN
# 3   Dave  68.0    TX   70.0     NaN
# 5  Frank  30.0   NaN    NaN     NaN

print(df.dropna(subset=[0, 4], axis=1))
#       name state
# 0    Alice    NY
# 1      NaN   NaN
# 2  Charlie    CA
# 3     Dave    TX
# 4    Ellen    CA
# 5    Frank   NaN

series = df['age']
print(series)
# 0    24.0
# 1     NaN
# 2     NaN
# 3    68.0
# 4     NaN
# 5    30.0
# Name: age, dtype: float64

print(series.dropna())
# 0    24.0
# 3    68.0
# 5    30.0
# Name: age, dtype: float64

print(df.fillna(0))
#       name   age state  point   other
# 0    Alice  24.0    NY    0.0     0.0
# 1        0   0.0     0    0.0     0.0
# 2  Charlie   0.0    CA    0.0     0.0
# 3     Dave  68.0    TX   70.0     0.0
# 4    Ellen   0.0    CA   88.0     0.0
# 5    Frank  30.0     0    0.0     0.0

print(df.fillna({'name': 'XXX', 'age': 20, 'point': 0}))
#       name   age state  point   other
# 0    Alice  24.0    NY    0.0     NaN
# 1      XXX  20.0   NaN    0.0     NaN
# 2  Charlie  20.0    CA    0.0     NaN
# 3     Dave  68.0    TX   70.0     NaN
# 4    Ellen  20.0    CA   88.0     NaN
# 5    Frank  30.0   NaN    0.0     NaN

print(df.fillna(method='ffill'))
#       name   age state  point   other
# 0    Alice  24.0    NY    NaN     NaN
# 1    Alice  24.0    NY    NaN     NaN
# 2  Charlie  24.0    CA    NaN     NaN
# 3     Dave  68.0    TX   70.0     NaN
# 4    Ellen  68.0    CA   88.0     NaN
# 5    Frank  30.0    CA   88.0     NaN

print(df.fillna(method='bfill'))
#       name   age state  point   other
# 0    Alice  24.0    NY   70.0     NaN
# 1  Charlie  68.0    CA   70.0     NaN
# 2  Charlie  68.0    CA   70.0     NaN
# 3     Dave  68.0    TX   70.0     NaN
# 4    Ellen  30.0    CA   88.0     NaN
# 5    Frank  30.0   NaN    NaN     NaN

print(df.fillna(method='bfill', limit=1))
#       name   age state  point   other
# 0    Alice  24.0    NY    NaN     NaN
# 1  Charlie   NaN    CA    NaN     NaN
# 2  Charlie  68.0    CA   70.0     NaN
# 3     Dave  68.0    TX   70.0     NaN
# 4    Ellen  30.0    CA   88.0     NaN
# 5    Frank  30.0   NaN    NaN     NaN
