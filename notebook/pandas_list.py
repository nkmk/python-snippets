import pandas as pd

l_1d = [0, 1, 2]

s = pd.Series(l_1d)

print(s)
# 0    0
# 1    1
# 2    2
# dtype: int64

s = pd.Series(l_1d, index=['row1', 'row2', 'row3'])

print(s)
# row1    0
# row2    1
# row3    2
# dtype: int64

l_2d = [[0, 1, 2], [3, 4, 5]]

df = pd.DataFrame(l_2d)

print(df)
#    0  1  2
# 0  0  1  2
# 1  3  4  5

df = pd.DataFrame(l_2d,
                  index=['row1', 'row2'],
                  columns=['col1', 'col2', 'col3'])

print(df)
#       col1  col2  col3
# row1     0     1     2
# row2     3     4     5

l_1d_index = [['Alice', 0], ['Bob', 1], ['Charlie', 2]]

index, value = zip(*l_1d_index)

print(index)
print(value)
# ('Alice', 'Bob', 'Charlie')
# (0, 1, 2)

s_index = pd.Series(value, index=index)

print(s_index)
# Alice      0
# Bob        1
# Charlie    2
# dtype: int64

l_2d_index = [['Alice', 0, 0.0], ['Bob', 1, 0.1], ['Charlie', 2, 0.2]]

df_index = pd.DataFrame(l_2d_index, columns=['name', 'val1', 'val2'])

print(df_index)
#       name  val1  val2
# 0    Alice     0   0.0
# 1      Bob     1   0.1
# 2  Charlie     2   0.2

df_index_set = df_index.set_index('name')

print(df_index_set)
#          val1  val2
# name               
# Alice       0   0.0
# Bob         1   0.1
# Charlie     2   0.2

print(df_index_set.dtypes)
# val1      int64
# val2    float64
# dtype: object

s = pd.Series([0, 1, 2])

print(s)
# 0    0
# 1    1
# 2    2
# dtype: int64

l_1d = s.values.tolist()

print(l_1d)
# [0, 1, 2]

df = pd.DataFrame([[0, 1, 2], [3, 4, 5]])

print(df)
#    0  1  2
# 0  0  1  2
# 1  3  4  5

l_2d = df.values.tolist()

print(l_2d)
# [[0, 1, 2], [3, 4, 5]]

s_index = pd.Series([0, 1, 2], index=['row1', 'row2', 'row3'])

print(s_index)
# row1    0
# row2    1
# row3    2
# dtype: int64

l_1d = s_index.values.tolist()

print(l_1d)
# [0, 1, 2]

df_index = pd.DataFrame([[0, 1, 2], [3, 4, 5]],
                        index=['row1', 'row2'],
                        columns=['col1', 'col2', 'col3'])

print(df_index)
#       col1  col2  col3
# row1     0     1     2
# row2     3     4     5

l_2d = df_index.values.tolist()

print(l_2d)
# [[0, 1, 2], [3, 4, 5]]

l_1d_index = s_index.reset_index().values.tolist()

print(l_1d_index)
# [['row1', 0], ['row2', 1], ['row3', 2]]

l_2d_index = df_index.reset_index().T.reset_index().T.values.tolist()

print(l_2d_index)
# [['index', 'col1', 'col2', 'col3'], ['row1', 0, 1, 2], ['row2', 3, 4, 5]]
