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

print(df2.dropna(how='any', axis=1))
#       name
# 0    Alice
# 2  Charlie
# 3     Dave
# 4    Ellen
# 5    Frank

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

# print(df.dropna(subset=[0, 4, 10], axis=1))
# KeyError: [10]

s = df['age']
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

print(df.fillna(0))
#       name   age state  point  other
# 0    Alice  24.0    NY    0.0    0.0
# 1        0   0.0     0    0.0    0.0
# 2  Charlie   0.0    CA    0.0    0.0
# 3     Dave  68.0    TX   70.0    0.0
# 4    Ellen   0.0    CA   88.0    0.0
# 5    Frank  30.0     0    0.0    0.0

print(df.fillna({'name': 'XXX', 'age': 20, 'ZZZ': 100}))
#       name   age state  point  other
# 0    Alice  24.0    NY    NaN    NaN
# 1      XXX  20.0   NaN    NaN    NaN
# 2  Charlie  20.0    CA    NaN    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen  20.0    CA   88.0    NaN
# 5    Frank  30.0   NaN    NaN    NaN

s_for_fill = pd.Series(['XXX', 20, 100], index=['name', 'age', 'ZZZ'])
print(s_for_fill)
# name    XXX
# age      20
# ZZZ     100
# dtype: object

print(df.fillna(s_for_fill))
#       name   age state  point  other
# 0    Alice  24.0    NY    NaN    NaN
# 1      XXX  20.0   NaN    NaN    NaN
# 2  Charlie  20.0    CA    NaN    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen  20.0    CA   88.0    NaN
# 5    Frank  30.0   NaN    NaN    NaN

print(df.mean())
# age      40.666667
# point    79.000000
# other          NaN
# dtype: float64

print(df.fillna(df.mean()))
#       name        age state  point  other
# 0    Alice  24.000000    NY   79.0    NaN
# 1      NaN  40.666667   NaN   79.0    NaN
# 2  Charlie  40.666667    CA   79.0    NaN
# 3     Dave  68.000000    TX   70.0    NaN
# 4    Ellen  40.666667    CA   88.0    NaN
# 5    Frank  30.000000   NaN   79.0    NaN

print(df.fillna(df.median()))
#       name   age state  point  other
# 0    Alice  24.0    NY   79.0    NaN
# 1      NaN  30.0   NaN   79.0    NaN
# 2  Charlie  30.0    CA   79.0    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen  30.0    CA   88.0    NaN
# 5    Frank  30.0   NaN   79.0    NaN
# 
# /usr/local/lib/python3.8/site-packages/numpy/lib/nanfunctions.py:1111: RuntimeWarning: Mean of empty slice
#   return np.nanmean(a, axis, out=out, keepdims=keepdims)

print(df.fillna(df.mode().iloc[0]))
#       name   age state  point  other
# 0    Alice  24.0    NY   70.0    NaN
# 1    Alice  24.0    CA   70.0    NaN
# 2  Charlie  24.0    CA   70.0    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen  24.0    CA   88.0    NaN
# 5    Frank  30.0    CA   70.0    NaN

print(df.fillna(method='ffill'))
#       name   age state  point  other
# 0    Alice  24.0    NY    NaN    NaN
# 1    Alice  24.0    NY    NaN    NaN
# 2  Charlie  24.0    CA    NaN    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen  68.0    CA   88.0    NaN
# 5    Frank  30.0    CA   88.0    NaN

print(df.fillna(method='bfill'))
#       name   age state  point  other
# 0    Alice  24.0    NY   70.0    NaN
# 1  Charlie  68.0    CA   70.0    NaN
# 2  Charlie  68.0    CA   70.0    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen  30.0    CA   88.0    NaN
# 5    Frank  30.0   NaN    NaN    NaN

print(df.fillna(method='bfill', limit=1))
#       name   age state  point  other
# 0    Alice  24.0    NY    NaN    NaN
# 1  Charlie   NaN    CA    NaN    NaN
# 2  Charlie  68.0    CA   70.0    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen  30.0    CA   88.0    NaN
# 5    Frank  30.0   NaN    NaN    NaN

s = df['age']
print(s)
# 0    24.0
# 1     NaN
# 2     NaN
# 3    68.0
# 4     NaN
# 5    30.0
# Name: age, dtype: float64

print(s.fillna(100))
# 0     24.0
# 1    100.0
# 2    100.0
# 3     68.0
# 4    100.0
# 5     30.0
# Name: age, dtype: float64

print(s.fillna({1: 100, 4: 0}))
# 0     24.0
# 1    100.0
# 2      NaN
# 3     68.0
# 4      0.0
# 5     30.0
# Name: age, dtype: float64

print(s.fillna(method='bfill', limit=1))
# 0    24.0
# 1     NaN
# 2    68.0
# 3    68.0
# 4    30.0
# 5    30.0
# Name: age, dtype: float64

print(df)
#       name   age state  point  other
# 0    Alice  24.0    NY    NaN    NaN
# 1      NaN   NaN   NaN    NaN    NaN
# 2  Charlie   NaN    CA    NaN    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen   NaN    CA   88.0    NaN
# 5    Frank  30.0   NaN    NaN    NaN

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
