import numpy as np
import pandas as pd

df = pd.DataFrame(data=[[1, 2, 3], [4, 5, 6]], columns=['a', 'b', 'c'])
print(df)
#    a  b  c
# 0  1  2  3
# 1  4  5  6

a = df.to_numpy()
print(a)
# [[1 2 3]
#  [4 5 6]]

print(type(a))
# <class 'numpy.ndarray'>

print(np.shares_memory(df, a))
# True

a[0, 0] = 100
print(a)
# [[100   2   3]
#  [  4   5   6]]

print(df)
#      a  b  c
# 0  100  2  3
# 1    4  5  6

a_copy = df.to_numpy(copy=True)
print(a_copy)
# [[100   2   3]
#  [  4   5   6]]

print(np.shares_memory(df, a_copy))
# False

a_copy[0, 0] = 10
print(a_copy)
# [[10  2  3]
#  [ 4  5  6]]

print(df)
#      a  b  c
# 0  100  2  3
# 1    4  5  6

a_cols = df[['a', 'c']].to_numpy()
print(a_cols)
# [[100   3]
#  [  4   6]]

print(np.shares_memory(df, a_cols))
# False

a_f = df.to_numpy(dtype=float)
print(a_f)
# [[100.   2.   3.]
#  [  4.   5.   6.]]

print(np.shares_memory(df, a_f))
# False
