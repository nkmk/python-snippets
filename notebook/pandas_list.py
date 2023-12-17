import pandas as pd

print(pd.__version__)
# 2.1.4

l_1d = [0, 10, 20]

print(pd.Series(l_1d))
# 0     0
# 1    10
# 2    20
# dtype: int64

l_2d = [[0, 10, 20], [30, 40, 50]]

print(pd.DataFrame(l_2d))
#     0   1   2
# 0   0  10  20
# 1  30  40  50

print(pd.DataFrame(l_1d))
#     0
# 0   0
# 1  10
# 2  20

print(pd.DataFrame([l_1d]))
#    0   1   2
# 0  0  10  20

print(pd.DataFrame(zip(*l_2d)))
#     0   1
# 0   0  30
# 1  10  40
# 2  20  50

print(pd.Series(l_1d, index=['X', 'Y', 'Z']))
# X     0
# Y    10
# Z    20
# dtype: int64

print(pd.DataFrame(l_2d, index=['X', 'Y'], columns=['A', 'B', 'C']))
#     A   B   C
# X   0  10  20
# Y  30  40  50

l_2d_multi = [[0, 0.0, 'abc', 123, 'abc'], [10, 0.1, 'xyz', 1.23, 100]]

print(pd.DataFrame(l_2d_multi))
#     0    1    2       3    4
# 0   0  0.0  abc  123.00  abc
# 1  10  0.1  xyz    1.23  100

print(pd.DataFrame(l_2d_multi).dtypes)
# 0      int64
# 1    float64
# 2     object
# 3    float64
# 4     object
# dtype: object

print(pd.DataFrame(l_2d, dtype=float))
#       0     1     2
# 0   0.0  10.0  20.0
# 1  30.0  40.0  50.0

l_1d_index = [['X', 0], ['Y', 1], ['Z', 2]]

index, values = zip(*l_1d_index)
print(index)
# ('X', 'Y', 'Z')

print(values)
# (0, 1, 2)

print(pd.Series(values, index=index))
# X    0
# Y    1
# Z    2
# dtype: int64

l_2d_index = [['X', 0, 0.0], ['Y', 1, 0.1], ['Z', 2, 0.2]]

df_index = pd.DataFrame(l_2d_index, columns=['idx', 'A', 'B'])
print(df_index)
#   idx  A    B
# 0   X  0  0.0
# 1   Y  1  0.1
# 2   Z  2  0.2

print(df_index.set_index('idx'))
#      A    B
# idx        
# X    0  0.0
# Y    1  0.1
# Z    2  0.2

l_2d_index_columns = [['idx', 'A', 'B'], ['X', 0, 0.0], ['Y', 1, 0.1], ['Z', 2, 0.2]]

df_index_columns = pd.DataFrame(l_2d_index_columns[1:], columns=l_2d_index_columns[0])
print(df_index_columns)
#   idx  A    B
# 0   X  0  0.0
# 1   Y  1  0.1
# 2   Z  2  0.2

print(df_index_columns.set_index('idx'))
#      A    B
# idx        
# X    0  0.0
# Y    1  0.1
# Z    2  0.2

s = pd.Series([0, 10, 20])
print(s)
# 0     0
# 1    10
# 2    20
# dtype: int64

print(s.tolist())
# [0, 10, 20]

print(s.to_list())
# [0, 10, 20]

df = pd.DataFrame([[0, 10, 20], [30, 40, 50]])
print(df)
#     0   1   2
# 0   0  10  20
# 1  30  40  50

print(df.values.tolist())
# [[0, 10, 20], [30, 40, 50]]

s_index = pd.Series([0, 1, 2], index=['X', 'Y', 'Z'])
print(s_index)
# X    0
# Y    1
# Z    2
# dtype: int64

print(s_index.reset_index())
#   index  0
# 0     X  0
# 1     Y  1
# 2     Z  2

print(s_index.reset_index().values.tolist())
# [['X', 0], ['Y', 1], ['Z', 2]]

df_index = pd.DataFrame([[0, 1, 2], [3, 4, 5]], index=['A', 'B'], columns=['X', 'Y', 'Z'])
print(df_index)
#    X  Y  Z
# A  0  1  2
# B  3  4  5

print(df_index.reset_index())
#   index  X  Y  Z
# 0     A  0  1  2
# 1     B  3  4  5

print(df_index.reset_index().values.tolist())
# [['A', 0, 1, 2], ['B', 3, 4, 5]]

print(df_index.reset_index().T.reset_index().T.values.tolist())
# [['index', 'X', 'Y', 'Z'], ['A', 0, 1, 2], ['B', 3, 4, 5]]

s_index = pd.Series([0, 1, 2], index=['X', 'Y', 'Z'])
print(s_index)
# X    0
# Y    1
# Z    2
# dtype: int64

print(s_index.index)
# Index(['X', 'Y', 'Z'], dtype='object')

print(s_index.index.tolist())
# ['X', 'Y', 'Z']

df_index = pd.DataFrame([[0, 1, 2], [3, 4, 5]], index=['A', 'B'], columns=['X', 'Y', 'Z'])
print(df_index)
#    X  Y  Z
# A  0  1  2
# B  3  4  5

print(df_index.index)
# Index(['A', 'B'], dtype='object')

print(df_index.index.tolist())
# ['A', 'B']

print(df_index.columns)
# Index(['X', 'Y', 'Z'], dtype='object')

print(df_index.columns.tolist())
# ['X', 'Y', 'Z']

for i in df_index.columns:
    print(i, type(i))
# X <class 'str'>
# Y <class 'str'>
# Z <class 'str'>

print(df_index.columns[0])
# X

print(df_index.columns[:2])
# Index(['X', 'Y'], dtype='object')

# df_index.columns[0] = 'x'
# TypeError: Index does not support mutable operations
