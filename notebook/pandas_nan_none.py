import math

import numpy as np
import pandas as pd

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

s_none_object = pd.Series([None, 'NaN', ''])
print(s_none_object)
# 0    None
# 1     NaN
# 2        
# dtype: object

print(s_none_object.isnull())
# 0     True
# 1    False
# 2    False
# dtype: bool

s_replace = s_none_object.replace(['NaN', ''], float('nan'))
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

print(s_inf.isnull())
# 0    True
# 1    True
# dtype: bool
