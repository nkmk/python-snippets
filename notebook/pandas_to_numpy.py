import numpy as np
import pandas as pd

df = pd.DataFrame(data=[[1, 2, 3], [4, 5, 6]], columns=['a', 'b', 'c'])
print(df)
#    a  b  c
# 0  1  2  3
# 1  4  5  6

a_df = df.values
print(a_df)
# [[1 2 3]
#  [4 5 6]]

print(type(a_df))
# <class 'numpy.ndarray'>

print(a_df.dtype)
# int64

s = df['a']
print(s)
# 0    1
# 1    4
# Name: a, dtype: int64

a_s = s.values
print(a_s)
# [1 4]

print(type(a_s))
# <class 'numpy.ndarray'>

print(a_s.dtype)
# int64

df_f = pd.DataFrame([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]])
print(df_f)
#      0    1    2
# 0  0.1  0.2  0.3
# 1  0.4  0.5  0.6

a_df_f = df_f.values
print(a_df_f)
# [[0.1 0.2 0.3]
#  [0.4 0.5 0.6]]

print(type(a_df_f))
# <class 'numpy.ndarray'>

print(a_df_f.dtype)
# float64

df_multi = pd.read_csv('data/src/sample_pandas_normal.csv')
print(df_multi)
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

a_df_multi = df_multi.values
print(a_df_multi)
# [['Alice' 24 'NY' 64]
#  ['Bob' 42 'CA' 92]
#  ['Charlie' 18 'CA' 70]
#  ['Dave' 68 'TX' 70]
#  ['Ellen' 24 'CA' 88]
#  ['Frank' 30 'NY' 57]]

print(type(a_df_multi))
# <class 'numpy.ndarray'>

print(a_df_multi.dtype)
# object

a_df_int = df_multi[['age', 'point']].values
print(a_df_int)
# [[24 64]
#  [42 92]
#  [18 70]
#  [68 70]
#  [24 88]
#  [30 57]]

print(type(a_df_int))
# <class 'numpy.ndarray'>

print(a_df_int.dtype)
# int64

print(a_df_int.T)
# [[24 42 18 68 24 30]
#  [64 92 70 70 88 57]]

a_df_int = df_multi.select_dtypes(include=int).values
print(a_df_int)
# [[24 64]
#  [42 92]
#  [18 70]
#  [68 70]
#  [24 88]
#  [30 57]]

print(type(a_df_int))
# <class 'numpy.ndarray'>

print(a_df_int.dtype)
# int64
