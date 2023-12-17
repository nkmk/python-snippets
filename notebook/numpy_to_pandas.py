import numpy as np
import pandas as pd

print(np.__version__)
# 1.26.2

print(pd.__version__)
# 2.1.4

a_2d = np.array([[1, 2], [3, 4]])
print(a_2d)
# [[1 2]
#  [3 4]]

print(pd.DataFrame(a_2d))
#    0  1
# 0  1  2
# 1  3  4

a_1d = np.array([1, 2])
print(a_1d)
# [1 2]

print(pd.DataFrame(a_1d))
#    0
# 0  1
# 1  2

a_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(a_3d)
# [[[1 2]
#   [3 4]]
# 
#  [[5 6]
#   [7 8]]]

# print(pd.DataFrame(a_3d))
# ValueError: Must pass 2-d input. shape=(2, 2, 2)

print(pd.DataFrame(data=a_2d, index=['X', 'Y'], columns=['A', 'B'], dtype=float))
#      A    B
# X  1.0  2.0
# Y  3.0  4.0

a = np.array([[1, 2], [3, 4]])
df = pd.DataFrame(a)

print(np.shares_memory(a, df))
# True

a[0, 0] = 100
print(a)
# [[100   2]
#  [  3   4]]

print(df)
#      0  1
# 0  100  2
# 1    3  4

a = np.array([[1, 2], [3, 4]])
df_copy = pd.DataFrame(a, copy=True)

print(np.shares_memory(a, df_copy))
# False

a[0, 0] = 100
print(a)
# [[100   2]
#  [  3   4]]

print(df_copy)
#    0  1
# 0  1  2
# 1  3  4

a = np.array([[1, 2], [3, 4]])
df_float = pd.DataFrame(a, dtype=float)

print(np.shares_memory(a, df_float))
# False

a_1d = np.array([1, 2])
print(a_1d)
# [1 2]

print(pd.Series(a_1d))
# 0    1
# 1    2
# dtype: int64

a_2d = np.array([[1, 2], [3, 4]])
print(a_2d)
# [[1 2]
#  [3 4]]

# print(pd.Series(a_2d))
# ValueError: Data must be 1-dimensional, got ndarray of shape (2, 2) instead

print(pd.Series(a_1d, index=['A', 'B'], name='my_series', dtype=float))
# A    1.0
# B    2.0
# Name: my_series, dtype: float64

a = np.array([1, 2])
print(np.shares_memory(a, pd.Series(a)))
# True

print(np.shares_memory(a, pd.Series(a, copy=True)))
# False

print(np.shares_memory(a, pd.Series(a, dtype=float)))
# False
