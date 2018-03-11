import pandas as pd
import numpy as np

s = pd.Series([0, 1, 2], dtype=np.float64)
print(s.dtype)
# float64

s = pd.Series([0, 1, 2], dtype='float64')
print(s.dtype)
# float64

s = pd.Series([0, 1, 2], dtype='f8')
print(s.dtype)
# float64

s = pd.Series([0, 1, 2], dtype='float')
print(s.dtype)
# float64

s = pd.Series([0, 1, 2], dtype=float)
print(s.dtype)
# float64

s = pd.Series([0, 1, 2], dtype='uint')
print(s.dtype)
# uint64

s_object = pd.Series([0, 0.1, 'abc'])
print(s_object.dtype)
print(type(s_object[0]))
print(type(s_object[1]))
print(type(s_object[2]))
# object
# <class 'int'>
# <class 'float'>
# <class 'str'>

s_str_constructor = pd.Series([0, 0.1, 'abc'], dtype=str)
print(s_str_constructor.dtype)
print(type(s_str_constructor[0]))
print(type(s_str_constructor[1]))
print(type(s_str_constructor[2]))
# object
# <class 'int'>
# <class 'float'>
# <class 'str'>

s_str_astype = s_str_constructor.astype(str)
print(s_str_astype.dtype)
print(type(s_str_astype[0]))
print(type(s_str_astype[1]))
print(type(s_str_astype[2]))
# object
# <class 'str'>
# <class 'str'>
# <class 'str'>

print(s_str_constructor.str.len())
# 0    NaN
# 1    NaN
# 2    3.0
# dtype: float64

print(s_str_astype.str.len())
# 0    1
# 1    3
# 2    3
# dtype: int64

print(s_str_constructor.astype(str).str.len())
# 0    1
# 1    3
# 2    3
# dtype: int64
