import pandas as pd
import numpy as np
import math

s_nan = pd.Series([None, np.nan, math.nan, pd.np.nan])
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

s_nan_int = pd.Series([None, pd.np.nan, 0, 1])
print(s_nan_int)
# 0    NaN
# 1    NaN
# 2    0.0
# 3    1.0
# dtype: float64

print(s_nan_int.isnull())
# 0     True
# 1     True
# 2    False
# 3    False
# dtype: bool

s_nan_str = pd.Series([None, pd.np.nan, 'NaN', 'nan'])
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

s_nan_str_replace = s_nan_str.replace({'NaN': pd.np.nan, 'nan': pd.np.nan})
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
