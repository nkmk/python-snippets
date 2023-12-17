import pandas as pd
import numpy as np

print(pd.__version__)
# 2.1.4

print(np.__version__)
# 1.26.2

df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=['X', 'Y'])
print(df)
#    A  B
# X  1  3
# Y  2  4

print(df.to_numpy())
# [[1 3]
#  [2 4]]

print(type(df.to_numpy()))
# <class 'numpy.ndarray'>

s = df['A']
print(s)
# X    1
# Y    2
# Name: A, dtype: int64

print(s.to_numpy())
# [1 2]

print(type(s.to_numpy()))
# <class 'numpy.ndarray'>

df_int = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=['X', 'Y'])
print(df_int)
#    A  B
# X  1  3
# Y  2  4

print(df_int.dtypes)
# A    int64
# B    int64
# dtype: object

print(df_int.to_numpy())
# [[1 3]
#  [2 4]]

print(df_int.to_numpy().dtype)
# int64

df_int_float = pd.DataFrame({'A': [1, 2], 'B': [0.1, 0.2]}, index=['X', 'Y'])
print(df_int_float)
#    A    B
# X  1  0.1
# Y  2  0.2

print(df_int_float.dtypes)
# A      int64
# B    float64
# dtype: object

print(df_int_float.to_numpy())
# [[1.  0.1]
#  [2.  0.2]]

print(df_int_float.to_numpy().dtype)
# float64

df_int_str = pd.DataFrame({'A': [1, 2], 'B': ['abc', 'xyz']}, index=['X', 'Y'])
print(df_int_str)
#    A    B
# X  1  abc
# Y  2  xyz

print(df_int_str.dtypes)
# A     int64
# B    object
# dtype: object

print(df_int_str.to_numpy())
# [[1 'abc']
#  [2 'xyz']]

print(df_int_str.to_numpy().dtype)
# object

print(df_int_str.to_numpy()[0, 0])
# 1

print(type(df_int_str.to_numpy()[0, 0]))
# <class 'int'>

print(df_int_str.to_numpy()[0, 1])
# abc

print(type(df_int_str.to_numpy()[0, 1]))
# <class 'str'>

print(df_int_float.to_numpy(dtype='float32'))
# [[1.  0.1]
#  [2.  0.2]]

print(df_int_float.to_numpy(dtype=int))
# [[1 0]
#  [2 0]]

# print(df_int_str.to_numpy(dtype=int))
# ValueError: invalid literal for int() with base 10: 'abc'

df_int_float_str = pd.DataFrame({'A': [1, 2], 'B': [0.1, 0.2], 'C': ['abc', 'xyz']}, index=['X', 'Y'])
print(df_int_float_str)
#    A    B    C
# X  1  0.1  abc
# Y  2  0.2  xyz

print(df_int_float_str.select_dtypes('number').to_numpy())
# [[1.  0.1]
#  [2.  0.2]]

df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=['X', 'Y'])
a = df.to_numpy()

print(np.shares_memory(df, a))
# True

a[0, 0] = 100
print(a)
# [[100   3]
#  [  2   4]]

print(df)
#      A  B
# X  100  3
# Y    2  4

df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=['X', 'Y'])
a_copy = df.to_numpy(copy=True)

print(np.shares_memory(df, a_copy))
# False

a_copy[0, 0] = 100
print(a_copy)
# [[100   3]
#  [  2   4]]

print(df)
#    A  B
# X  1  3
# Y  2  4

df_int_float = pd.DataFrame({'A': [1, 2], 'B': [0.1, 0.2]}, index=['X', 'Y'])
a_float = df_int_float.to_numpy()

print(np.shares_memory(df_int_float, a_float))
# False

df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=['X', 'Y'])
print(df)
#    A  B
# X  1  3
# Y  2  4

print(df.values)
# [[1 3]
#  [2 4]]

print(type(df.values))
# <class 'numpy.ndarray'>

s = df['A']
print(s)
# X    1
# Y    2
# Name: A, dtype: int64

print(s.values)
# [1 2]

print(type(s.values))
# <class 'numpy.ndarray'>

df_int_float = pd.DataFrame({'A': [1, 2], 'B': [0.1, 0.2]}, index=['X', 'Y'])
print(df_int_float.values)
# [[1.  0.1]
#  [2.  0.2]]

print(df_int_float.values.dtype)
# float64

df_int_str = pd.DataFrame({'A': [1, 2], 'B': ['abc', 'xyz']}, index=['X', 'Y'])
print(df_int_str.values)
# [[1 'abc']
#  [2 'xyz']]

print(df_int_str.values.dtype)
# object

df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=['X', 'Y'])
print(np.shares_memory(df, df.values))
# True

df_int_float = pd.DataFrame({'A': [1, 2], 'B': [0.1, 0.2]}, index=['X', 'Y'])
print(np.shares_memory(df_int_float, df_int_float.values))
# False

print(np.shares_memory(df, df.values.copy()))
# False
