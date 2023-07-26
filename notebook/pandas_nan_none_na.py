import math

import numpy as np
import pandas as pd

print(pd.__version__)
# 2.0.3

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

print(df.dropna(how='all'))
#       name   age state  point  other
# 0    Alice  24.0    NY    NaN    NaN
# 2  Charlie   NaN    CA    NaN    NaN

print(df.fillna(0))
#       name   age state  point  other
# 0    Alice  24.0    NY    0.0    0.0
# 1        0   0.0     0    0.0    0.0
# 2  Charlie   0.0    CA    0.0    0.0

print(df.dtypes)
# name      object
# age      float64
# state     object
# point    float64
# other    float64
# dtype: object

print(df.at[1, 'name'])
# nan

print(type(df.at[1, 'name']))
# <class 'float'>

print(df.at[1, 'age'])
# nan

print(type(df.at[1, 'age']))
# <class 'numpy.float64'>

s_nan = pd.Series([float('nan'), math.nan, np.nan])
print(s_nan)
# 0   NaN
# 1   NaN
# 2   NaN
# dtype: float64

print(s_nan.isnull())
# 0    True
# 1    True
# 2    True
# dtype: bool

print(None)
# None

print(type(None))
# <class 'NoneType'>

s_none_float = pd.Series([None, 0.1, 0.2])
s_none_float[2] = None
print(s_none_float)
# 0    NaN
# 1    0.1
# 2    NaN
# dtype: float64

print(s_none_float.isnull())
# 0     True
# 1    False
# 2     True
# dtype: bool

s_none_int = pd.Series([None, 1, 2])
print(s_none_int)
# 0    NaN
# 1    1.0
# 2    2.0
# dtype: float64

s_none_object = pd.Series([None, 'abc', 'xyz'])
print(s_none_object)
# 0    None
# 1     abc
# 2     xyz
# dtype: object

print(s_none_object.isnull())
# 0     True
# 1    False
# 2    False
# dtype: bool

print(s_none_object.fillna(0))
# 0      0
# 1    abc
# 2    xyz
# dtype: object

s_str = pd.Series(['NaN', 'None', ''])
print(s_str)
# 0     NaN
# 1    None
# 2        
# dtype: object

print(s_str.isnull())
# 0    False
# 1    False
# 2    False
# dtype: bool

s_replace = s_str.replace(['NaN', 'None', ''], float('nan'))
print(s_replace)
# 0   NaN
# 1   NaN
# 2   NaN
# dtype: float64

print(s_replace.isnull())
# 0    True
# 1    True
# 2    True
# dtype: bool

s_inf = pd.Series([float('inf'), -float('inf')])
print(s_inf)
# 0    inf
# 1   -inf
# dtype: float64

print(s_inf.isnull())
# 0    False
# 1    False
# dtype: bool

pd.options.mode.use_inf_as_na = True

print(s_inf)
# 0   NaN
# 1   NaN
# dtype: float64

print(s_inf.isnull())
# 0    True
# 1    True
# dtype: bool

s_inf_object = pd.Series([float('inf'), -float('inf'), 'abc'])
print(s_inf_object)
# 0    NaN
# 1    NaN
# 2    abc
# dtype: object

print(s_inf_object.isnull())
# 0     True
# 1     True
# 2    False
# dtype: bool

print(pd.NA)
# <NA>

print(type(pd.NA))
# <class 'pandas._libs.missing.NAType'>

print(float('nan') == float('nan'))
# False

print(pd.NA == pd.NA)
# <NA>

s_na = pd.Series([None, 1, 2], dtype='Int64')
print(s_na)
# 0    <NA>
# 1       1
# 2       2
# dtype: Int64

print(s_na.isnull())
# 0     True
# 1    False
# 2    False
# dtype: bool

print(s_na.fillna(0))
# 0    0
# 1    1
# 2    2
# dtype: Int64
