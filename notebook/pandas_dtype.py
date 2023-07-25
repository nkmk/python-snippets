import pandas as pd
import numpy as np

print(pd.__version__)
# 2.0.3

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

s_object = pd.Series([0, 'abcde', np.nan])
print(s_object)
# 0        0
# 1    abcde
# 2      NaN
# dtype: object

print(s_object.map(type))
# 0      <class 'int'>
# 1      <class 'str'>
# 2    <class 'float'>
# dtype: object

s_str_astype = s_object.astype(str)
print(s_str_astype)
# 0        0
# 1    abcde
# 2      nan
# dtype: object

print(s_str_astype.map(type))
# 0    <class 'str'>
# 1    <class 'str'>
# 2    <class 'str'>
# dtype: object

s_str_constructor = pd.Series([0, 'abcde', np.nan], dtype=str)
print(s_str_constructor)
# 0        0
# 1    abcde
# 2      NaN
# dtype: object

print(s_str_constructor.map(type))
# 0      <class 'str'>
# 1      <class 'str'>
# 2    <class 'float'>
# dtype: object

print(s_object.str.len())
# 0    NaN
# 1    5.0
# 2    NaN
# dtype: float64

print(s_str_astype.str.len())
# 0    1
# 1    5
# 2    3
# dtype: int64

print(s_object.isnull())
# 0    False
# 1    False
# 2     True
# dtype: bool

print(s_object.dropna())
# 0        0
# 1    abcde
# dtype: object

print(s_str_astype.isnull())
# 0    False
# 1    False
# 2    False
# dtype: bool

print(s_str_astype.dropna())
# 0        0
# 1    abcde
# 2      nan
# dtype: object

s_str_astype_nan = s_str_astype.replace('nan', np.nan)
print(s_str_astype_nan)
# 0        0
# 1    abcde
# 2      NaN
# dtype: object

print(s_str_astype_nan.map(type))
# 0      <class 'str'>
# 1      <class 'str'>
# 2    <class 'float'>
# dtype: object

print(s_str_astype_nan.isnull())
# 0    False
# 1    False
# 2     True
# dtype: bool
