import pandas as pd

s = pd.Series([0, 1, 2], index=['a', 'b', 'c'])
print(s)
# a    0
# b    1
# c    2
# dtype: int64

df = pd.DataFrame(s)
print(df)
#    0
# a  0
# b  1
# c  2

print(type(df))
# <class 'pandas.core.frame.DataFrame'>

df_ = pd.DataFrame([s])
print(df_)
#    a  b  c
# 0  0  1  2

print(type(df_))
# <class 'pandas.core.frame.DataFrame'>

s_name = pd.Series([0, 1, 2], index=['a', 'b', 'c'], name='X')
print(s_name)
# a    0
# b    1
# c    2
# Name: X, dtype: int64

print(pd.DataFrame(s_name))
#    X
# a  0
# b  1
# c  2

print(pd.DataFrame([s_name]))
#    a  b  c
# X  0  1  2

s1 = pd.Series([0, 1, 2], index=['a', 'b', 'c'])
print(s1)
# a    0
# b    1
# c    2
# dtype: int64

s2 = pd.Series([0.0, 0.1, 0.2], index=['a', 'b', 'c'])
print(s2)
# a    0.0
# b    0.1
# c    0.2
# dtype: float64

print(pd.DataFrame({'col0': s1, 'col1': s2}))
#    col0  col1
# a     0   0.0
# b     1   0.1
# c     2   0.2

print(pd.DataFrame([s1, s2]))
#      a    b    c
# 0  0.0  1.0  2.0
# 1  0.0  0.1  0.2

print(pd.concat([s1, s2], axis=1))
#    0    1
# a  0  0.0
# b  1  0.1
# c  2  0.2

s1_name = pd.Series([0, 1, 2], index=['a', 'b', 'c'], name='X')
print(s1_name)
# a    0
# b    1
# c    2
# Name: X, dtype: int64

s2_name = pd.Series([0.0, 0.1, 0.2], index=['a', 'b', 'c'], name='Y')
print(s2_name)
# a    0.0
# b    0.1
# c    0.2
# Name: Y, dtype: float64

print(pd.DataFrame({s1_name.name: s1_name, s2_name.name: s2_name}))
#    X    Y
# a  0  0.0
# b  1  0.1
# c  2  0.2

print(pd.DataFrame([s1_name, s2_name]))
#      a    b    c
# X  0.0  1.0  2.0
# Y  0.0  0.1  0.2

print(pd.concat([s1_name, s2_name], axis=1))
#    X    Y
# a  0  0.0
# b  1  0.1
# c  2  0.2

s3 = pd.Series([0.1, 0.2, 0.3], index=['b', 'c', 'd'])
print(s3)
# b    0.1
# c    0.2
# d    0.3
# dtype: float64

print(pd.DataFrame({'col0': s1, 'col1': s3}))
#    col0  col1
# a   0.0   NaN
# b   1.0   0.1
# c   2.0   0.2
# d   NaN   0.3

print(pd.DataFrame([s1, s3]))
#      a    b    c    d
# 0  0.0  1.0  2.0  NaN
# 1  NaN  0.1  0.2  0.3

print(pd.concat([s1, s3], axis=1))
#      0    1
# a  0.0  NaN
# b  1.0  0.1
# c  2.0  0.2
# d  NaN  0.3
# 
# /usr/local/lib/python3.7/site-packages/ipykernel_launcher.py:1: FutureWarning: Sorting because non-concatenation axis is not aligned. A future version
# of pandas will change to not sort by default.
# 
# To accept the future behavior, pass 'sort=False'.
# 
# To retain the current behavior and silence the warning, pass 'sort=True'.
# 
#   """Entry point for launching an IPython kernel.

print(pd.concat([s1, s3], axis=1, join='inner'))
#    0    1
# b  1  0.1
# c  2  0.2

print(s1.values)
# [0 1 2]

print(type(s1.values))
# <class 'numpy.ndarray'>

print(pd.DataFrame({'col0': s1.values, 'col1': s3.values}))
#    col0  col1
# 0     0   0.1
# 1     1   0.2
# 2     2   0.3

print(pd.DataFrame([s1.values, s3.values]))
#      0    1    2
# 0  0.0  1.0  2.0
# 1  0.1  0.2  0.3

# print(pd.concat([s1.values, s3.values], axis=1))
# TypeError: cannot concatenate object of type '<class 'numpy.ndarray'>'; only Series and DataFrame objs are valid

print(pd.DataFrame({'col0': s1, 'col1': s3.values}))
#    col0  col1
# a     0   0.1
# b     1   0.2
# c     2   0.3

print(pd.DataFrame([s1, s3.values]))
#      a    b    c
# 0  0.0  1.0  2.0
# 1  NaN  NaN  NaN

print(pd.DataFrame({'col0': s1.values, 'col1': s3.values}, index=s1.index))
#    col0  col1
# a     0   0.1
# b     1   0.2
# c     2   0.3

print(pd.DataFrame([s1.values, s3.values], columns=s1.index))
#      a    b    c
# 0  0.0  1.0  2.0
# 1  0.1  0.2  0.3

s4 = pd.Series([0.1, 0.2], index=['b', 'd'])
print(s4)
# b    0.1
# d    0.2
# dtype: float64

print(pd.DataFrame({'col0': s1, 'col1': s4}))
#    col0  col1
# a   0.0   NaN
# b   1.0   0.1
# c   2.0   NaN
# d   NaN   0.2

print(pd.DataFrame([s1, s4]))
#      a    b    c    d
# 0  0.0  1.0  2.0  NaN
# 1  NaN  0.1  NaN  0.2

print(pd.concat([s1, s4], axis=1, join='inner'))
#    0    1
# b  1  0.1

# print(pd.DataFrame({'col0': s1.values, 'col1': s4.values}))
# ValueError: arrays must all be same length

print(pd.DataFrame([s1.values, s4.values]))
#      0    1    2
# 0  0.0  1.0  2.0
# 1  0.1  0.2  NaN

s4.index = ['a', 'b']
print(s4)
# a    0.1
# b    0.2
# dtype: float64

print(pd.DataFrame({'col0': s1, 'col1': s4}))
#    col0  col1
# a     0   0.1
# b     1   0.2
# c     2   NaN

print(pd.DataFrame({'col0': s1, 'col1': s4}).fillna(100))
#    col0   col1
# a     0    0.1
# b     1    0.2
# c     2  100.0

print(s)
# a    0
# b    1
# c    2
# dtype: int64

df = pd.DataFrame(s)
print(df)
#    0
# a  0
# b  1
# c  2

s[0] = 100
print(s)
# a    100
# b      1
# c      2
# dtype: int64

print(df)
#      0
# a  100
# b    1
# c    2

df_copy = pd.DataFrame(s, copy=True)
print(df_copy)
#      0
# a  100
# b    1
# c    2

s[1] = 100
print(s)
# a    100
# b    100
# c      2
# dtype: int64

print(df_copy)
#      0
# a  100
# b    1
# c    2

df_c = pd.concat([s1, s2], axis=1)
print(df_c)
#    0    1
# a  0  0.0
# b  1  0.1
# c  2  0.2

s1[0] = 100
print(s1)
# a    100
# b      1
# c      2
# dtype: int64

print(df_c)
#    0    1
# a  0  0.0
# b  1  0.1
# c  2  0.2

df_c_view = pd.concat([s1, s2], axis=1, copy=False)
print(df_c_view)
#      0    1
# a  100  0.0
# b    1  0.1
# c    2  0.2

s1[1] = 100
print(s1)
# a    100
# b    100
# c      2
# dtype: int64

print(df_c_view)
#      0    1
# a  100  0.0
# b    1  0.1
# c    2  0.2
