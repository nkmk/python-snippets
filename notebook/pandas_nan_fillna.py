import pandas as pd

print(pd.__version__)
# 2.1.4

df = pd.read_csv('data/src/sample_pandas_normal_nan.csv')
print(df)
#       name   age state  point  other
# 0    Alice  24.0    NY    NaN    NaN
# 1      NaN   NaN   NaN    NaN    NaN
# 2  Charlie   NaN    CA    NaN    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen   NaN    CA   88.0    NaN
# 5    Frank  30.0   NaN    NaN    NaN

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

print(df.mean(numeric_only=True))
# age      40.666667
# point    79.000000
# other          NaN
# dtype: float64

print(df.fillna(df.mean(numeric_only=True)))
#       name        age state  point  other
# 0    Alice  24.000000    NY   79.0    NaN
# 1      NaN  40.666667   NaN   79.0    NaN
# 2  Charlie  40.666667    CA   79.0    NaN
# 3     Dave  68.000000    TX   70.0    NaN
# 4    Ellen  40.666667    CA   88.0    NaN
# 5    Frank  30.000000   NaN   79.0    NaN

print(df.fillna(df.median(numeric_only=True)))
#       name   age state  point  other
# 0    Alice  24.0    NY   79.0    NaN
# 1      NaN  30.0   NaN   79.0    NaN
# 2  Charlie  30.0    CA   79.0    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen  30.0    CA   88.0    NaN
# 5    Frank  30.0   NaN   79.0    NaN

print(df.fillna(df.mode().iloc[0]))
#       name   age state  point  other
# 0    Alice  24.0    NY   70.0    NaN
# 1    Alice  24.0    CA   70.0    NaN
# 2  Charlie  24.0    CA   70.0    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen  24.0    CA   88.0    NaN
# 5    Frank  30.0    CA   70.0    NaN

print(df.ffill())
#       name   age state  point  other
# 0    Alice  24.0    NY    NaN    NaN
# 1    Alice  24.0    NY    NaN    NaN
# 2  Charlie  24.0    CA    NaN    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen  68.0    CA   88.0    NaN
# 5    Frank  30.0    CA   88.0    NaN

print(df.bfill())
#       name   age state  point  other
# 0    Alice  24.0    NY   70.0    NaN
# 1  Charlie  68.0    CA   70.0    NaN
# 2  Charlie  68.0    CA   70.0    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen  30.0    CA   88.0    NaN
# 5    Frank  30.0   NaN    NaN    NaN

print(df.ffill(limit=1))
#       name   age state  point  other
# 0    Alice  24.0    NY    NaN    NaN
# 1    Alice  24.0    NY    NaN    NaN
# 2  Charlie   NaN    CA    NaN    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen  68.0    CA   88.0    NaN
# 5    Frank  30.0    CA   88.0    NaN

print(df.bfill(limit=1))
#       name   age state  point  other
# 0    Alice  24.0    NY    NaN    NaN
# 1  Charlie   NaN    CA    NaN    NaN
# 2  Charlie  68.0    CA   70.0    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen  30.0    CA   88.0    NaN
# 5    Frank  30.0   NaN    NaN    NaN

print(df.ffill(axis=1))
#       name      age state point other
# 0    Alice     24.0    NY    NY    NY
# 1      NaN      NaN   NaN   NaN   NaN
# 2  Charlie  Charlie    CA    CA    CA
# 3     Dave     68.0    TX  70.0  70.0
# 4    Ellen    Ellen    CA  88.0  88.0
# 5    Frank     30.0  30.0  30.0  30.0

print(df.bfill(axis=1))
#       name   age state point other
# 0    Alice  24.0    NY   NaN   NaN
# 1      NaN   NaN   NaN   NaN   NaN
# 2  Charlie    CA    CA   NaN   NaN
# 3     Dave  68.0    TX  70.0   NaN
# 4    Ellen    CA    CA  88.0   NaN
# 5    Frank  30.0   NaN   NaN   NaN

print(df.fillna(method='ffill', limit=1))
#       name   age state  point  other
# 0    Alice  24.0    NY    NaN    NaN
# 1    Alice  24.0    NY    NaN    NaN
# 2  Charlie   NaN    CA    NaN    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen  68.0    CA   88.0    NaN
# 5    Frank  30.0    CA   88.0    NaN
# 
# /var/folders/rf/b7l8_vgj5mdgvghn_326rn_c0000gn/T/ipykernel_50534/2498159999.py:1: FutureWarning: DataFrame.fillna with 'method' is deprecated and will raise in a future version. Use obj.ffill() or obj.bfill() instead.
#   print(df.fillna(method='ffill', limit=1))

df.fillna(0, inplace=True)
print(df)
#       name   age state  point  other
# 0    Alice  24.0    NY    0.0    0.0
# 1        0   0.0     0    0.0    0.0
# 2  Charlie   0.0    CA    0.0    0.0
# 3     Dave  68.0    TX   70.0    0.0
# 4    Ellen   0.0    CA   88.0    0.0
# 5    Frank  30.0     0    0.0    0.0

s = pd.read_csv('data/src/sample_pandas_normal_nan.csv')['age']
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

print(s.fillna({1: 100, 4: -100}))
# 0     24.0
# 1    100.0
# 2      NaN
# 3     68.0
# 4   -100.0
# 5     30.0
# Name: age, dtype: float64

print(s.ffill(limit=1))
# 0    24.0
# 1    24.0
# 2     NaN
# 3    68.0
# 4    68.0
# 5    30.0
# Name: age, dtype: float64

print(s.bfill(limit=1))
# 0    24.0
# 1     NaN
# 2    68.0
# 3    68.0
# 4    30.0
# 5    30.0
# Name: age, dtype: float64

print(s.fillna(method='ffill', limit=1))
# 0    24.0
# 1    24.0
# 2     NaN
# 3    68.0
# 4    68.0
# 5    30.0
# Name: age, dtype: float64
# 
# /var/folders/rf/b7l8_vgj5mdgvghn_326rn_c0000gn/T/ipykernel_50534/2241812369.py:1: FutureWarning: Series.fillna with 'method' is deprecated and will raise in a future version. Use obj.ffill() or obj.bfill() instead.
#   print(s.fillna(method='ffill', limit=1))
