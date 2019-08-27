import numpy as np
import pandas as pd

df = pd.DataFrame(data=[[1, 2, 3], [4, 5, 6]], columns=['a', 'b', 'c'])
print(df)
#    a  b  c
# 0  1  2  3
# 1  4  5  6

a_values = df.values
print(a_values)
# [[1 2 3]
#  [4 5 6]]

print(np.shares_memory(a_values, df))
# True

a_values[0, 0] = 100
print(a_values)
# [[100   2   3]
#  [  4   5   6]]

print(df)
#      a  b  c
# 0  100  2  3
# 1    4  5  6

df_if = pd.DataFrame(data=[[1, 0.1], [2, 0.2]], columns=['int', 'float'])
print(df_if)
#    int  float
# 0    1    0.1
# 1    2    0.2

print(df_if.dtypes)
# int        int64
# float    float64
# dtype: object

a_values_if = df_if.values
print(a_values_if)
# [[1.  0.1]
#  [2.  0.2]]

print(np.shares_memory(a_values_if, df_if))
# False

a_values_if[0, 0] = 100
print(a_values_if)
# [[100.    0.1]
#  [  2.    0.2]]

print(df_if)
#    int  float
# 0    1    0.1
# 1    2    0.2

print(df[['a', 'c']].values)
# [[100   3]
#  [  4   6]]

print(np.shares_memory(df[['a', 'c']].values, df))
# False

print(df.iloc[:, ::2].values)
# [[100   3]
#  [  4   6]]

print(np.shares_memory(df.iloc[:, ::2].values, df))
# True

a_values_copy = df.values.copy()
print(a_values_copy)
# [[100   2   3]
#  [  4   5   6]]

print(np.shares_memory(a_values_copy, df))
# False

a_values_copy[0, 0] = 10
print(a_values_copy)
# [[10  2  3]
#  [ 4  5  6]]

print(df)
#      a  b  c
# 0  100  2  3
# 1    4  5  6

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
# [[1 2 3]
#  [4 5 6]]

df_a = pd.DataFrame(a, columns=['a', 'b', 'c'])
print(df_a)
#    a  b  c
# 0  1  2  3
# 1  4  5  6

print(np.shares_memory(a, df_a))
# True

a[0, 0] = 100
print(a)
# [[100   2   3]
#  [  4   5   6]]

print(df_a)
#      a  b  c
# 0  100  2  3
# 1    4  5  6

df_a.iat[1, 0] = 10
print(df_a)
#      a  b  c
# 0  100  2  3
# 1   10  5  6

print(a)
# [[100   2   3]
#  [ 10   5   6]]

df_a_copy = pd.DataFrame(a.copy(), columns=['a', 'b', 'c'])
print(df_a_copy)
#      a  b  c
# 0  100  2  3
# 1   10  5  6

a[0, 0] = 1
print(a)
# [[ 1  2  3]
#  [10  5  6]]

print(df_a_copy)
#      a  b  c
# 0  100  2  3
# 1   10  5  6
