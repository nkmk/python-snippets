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

s_object = pd.Series([0, 0.1, 'abc', pd.np.nan])
print(s_object)
# 0      0
# 1    0.1
# 2    abc
# 3    NaN
# dtype: object

print(s_object.map(type))
# 0      <class 'int'>
# 1    <class 'float'>
# 2      <class 'str'>
# 3    <class 'float'>
# dtype: object

s_str_constructor = pd.Series([0, 0.1, 'abc', pd.np.nan], dtype=str)
print(s_str_constructor)
# 0      0
# 1    0.1
# 2    abc
# 3    nan
# dtype: object

print(s_str_constructor.map(type))
# 0    <class 'str'>
# 1    <class 'str'>
# 2    <class 'str'>
# 3    <class 'str'>
# dtype: object

s_str_astype = s_object.astype(str)
print(s_str_astype)
# 0      0
# 1    0.1
# 2    abc
# 3    nan
# dtype: object

print(s_str_astype.map(type))
# 0    <class 'str'>
# 1    <class 'str'>
# 2    <class 'str'>
# 3    <class 'str'>
# dtype: object

print(s_str_astype.str.len())
# 0    1
# 1    3
# 2    3
# 3    3
# dtype: int64

print(s_object.str.len())
# 0    NaN
# 1    NaN
# 2    3.0
# 3    NaN
# dtype: float64

print(s_object.astype(str).str.len())
# 0    1
# 1    3
# 2    3
# 3    3
# dtype: int64

print(s_object)
# 0      0
# 1    0.1
# 2    abc
# 3    NaN
# dtype: object

print(s_object.map(type))
# 0      <class 'int'>
# 1    <class 'float'>
# 2      <class 'str'>
# 3    <class 'float'>
# dtype: object

print(s_object.isnull())
# 0    False
# 1    False
# 2    False
# 3     True
# dtype: bool

print(s_object.dropna())
# 0      0
# 1    0.1
# 2    abc
# dtype: object

print(s_str_astype)
# 0      0
# 1    0.1
# 2    abc
# 3    nan
# dtype: object

print(s_str_astype.map(type))
# 0    <class 'str'>
# 1    <class 'str'>
# 2    <class 'str'>
# 3    <class 'str'>
# dtype: object

print(s_str_astype.isnull())
# 0    False
# 1    False
# 2    False
# 3    False
# dtype: bool

print(s_str_astype.dropna())
# 0      0
# 1    0.1
# 2    abc
# 3    nan
# dtype: object

s_str_astype_nan = s_str_astype.replace('nan', pd.np.nan)
print(s_str_astype_nan)
# 0      0
# 1    0.1
# 2    abc
# 3    NaN
# dtype: object

print(s_str_astype_nan.map(type))
# 0      <class 'str'>
# 1      <class 'str'>
# 2      <class 'str'>
# 3    <class 'float'>
# dtype: object

print(s_str_astype_nan.isnull())
# 0    False
# 1    False
# 2    False
# 3     True
# dtype: bool
