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

print(df.dtypes)
# name      object
# age      float64
# state     object
# point    float64
# other    float64
# dtype: object

print(df.at[1, 'name'])
print(type(df.at[1, 'name']))
# nan
# <class 'float'>

print(df.at[0, 'point'])
print(type(df.at[0, 'point']))
# nan
# <class 'numpy.float64'>

print(df.isnull())
#     name    age  state  point  other
# 0  False  False  False   True   True
# 1   True   True   True   True   True
# 2  False   True  False   True   True
# 3  False  False  False  False   True
# 4  False   True  False  False   True
# 5  False  False   True   True   True

import numpy as np
import math

s_nan = pd.Series([None, np.nan, math.nan, float('nan')])
print(s_nan)
# 0   NaN
# 1   NaN
# 2   NaN
# 3   NaN
# dtype: float64

print(s_nan[0])
print(type(s_nan[0]))
# nan
# <class 'numpy.float64'>

print(s_nan.isnull())
# 0    True
# 1    True
# 2    True
# 3    True
# dtype: bool

s_nan_str = pd.Series([None, float('nan'), 'NaN', 'nan'])
print(s_nan_str)
# 0    None
# 1     NaN
# 2     NaN
# 3     nan
# dtype: object

print(s_nan_str[0])
print(type(s_nan_str[0]))
# None
# <class 'NoneType'>

print(s_nan_str.isnull())
# 0     True
# 1     True
# 2    False
# 3    False
# dtype: bool

print(s_nan_str.dropna())
# 2    NaN
# 3    nan
# dtype: object

print(s_nan_str.fillna(100))
# 0    100
# 1    100
# 2    NaN
# 3    nan
# dtype: object

s_nan_str_replace = s_nan_str.replace({'NaN': float('nan'), 'nan': float('nan')})
print(s_nan_str_replace)
# 0   NaN
# 1   NaN
# 2   NaN
# 3   NaN
# dtype: float64

print(s_nan_str_replace.isnull())
# 0    True
# 1    True
# 2    True
# 3    True
# dtype: bool
