import pandas as pd

df = pd.read_csv('data/src/sample_multi.csv', index_col=[0, 1, 2])
print(df)
#                          val_1  val_2
# level_1 level_2 level_3              
# A0      B0      C0          98     90
#                 C1          44      9
#         B1      C2          39     17
#                 C3          75     71
# A1      B2      C0           1     89
#                 C1          54     60
#         B3      C2          47      6
#                 C3          16      5
# A2      B0      C0          75     22
#                 C1          19      4
#         B1      C2          25     52
#                 C3          57     40
# A3      B2      C0          64     54
#                 C1          27     96
#         B3      C2         100     77
#                 C3          22     50

print(df.index)
# MultiIndex(levels=[['A0', 'A1', 'A2', 'A3'], ['B0', 'B1', 'B2', 'B3'], ['C0', 'C1', 'C2', 'C3']],
#            labels=[[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3], [0, 0, 1, 1, 2, 2, 3, 3, 0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]],
#            names=['level_1', 'level_2', 'level_3'])

print(df.loc['A0', 'val_1'])
# level_2  level_3
# B0       C0         98
#          C1         44
# B1       C2         39
#          C3         75
# Name: val_1, dtype: int64

print(df.loc['A0', :])
#                  val_1  val_2
# level_2 level_3              
# B0      C0          98     90
#         C1          44      9
# B1      C2          39     17
#         C3          75     71

print(df.loc['A0'])
#                  val_1  val_2
# level_2 level_3              
# B0      C0          98     90
#         C1          44      9
# B1      C2          39     17
#         C3          75     71

print(df.loc['A0':'A2', :])
#                          val_1  val_2
# level_1 level_2 level_3              
# A0      B0      C0          98     90
#                 C1          44      9
#         B1      C2          39     17
#                 C3          75     71
# A1      B2      C0           1     89
#                 C1          54     60
#         B3      C2          47      6
#                 C3          16      5
# A2      B0      C0          75     22
#                 C1          19      4
#         B1      C2          25     52
#                 C3          57     40

print(df.loc[['A0', 'A2'], :])
#                          val_1  val_2
# level_1 level_2 level_3              
# A0      B0      C0          98     90
#                 C1          44      9
#         B1      C2          39     17
#                 C3          75     71
# A2      B0      C0          75     22
#                 C1          19      4
#         B1      C2          25     52
#                 C3          57     40

print(df.loc[('A0', 'B1'), :])
#          val_1  val_2
# level_3              
# C2          39     17
# C3          75     71

print(df.loc[('A0', 'B1', 'C2'), :])
# val_1    39
# val_2    17
# Name: (A0, B1, C2), dtype: int64

print(df.loc[(['A0', 'A1'], ['B0', 'B3']), :])
#                          val_1  val_2
# level_1 level_2 level_3              
# A0      B0      C0          98     90
#                 C1          44      9
# A1      B3      C2          47      6
#                 C3          16      5

# print(df.loc[(:, 'B1'), :])
# SyntaxError: invalid syntax

# print(df.loc[('A1':'A3', 'B2'), :])
# SyntaxError: invalid syntax

print(df.loc[(slice(None), 'B1'), :])
#                          val_1  val_2
# level_1 level_2 level_3              
# A0      B1      C2          39     17
#                 C3          75     71
# A2      B1      C2          25     52
#                 C3          57     40

print(df.loc[(slice('A1', 'A3'), 'B2'), :])
#                          val_1  val_2
# level_1 level_2 level_3              
# A1      B2      C0           1     89
#                 C1          54     60
# A3      B2      C0          64     54
#                 C1          27     96

print(df.loc[(slice('A1', 'A3'), ['B0', 'B2'], 'C1'), :])
#                          val_1  val_2
# level_1 level_2 level_3              
# A1      B2      C1          54     60
# A2      B0      C1          19      4
# A3      B2      C1          27     96

print(df.loc[pd.IndexSlice[:, 'B1'], :])
#                          val_1  val_2
# level_1 level_2 level_3              
# A0      B1      C2          39     17
#                 C3          75     71
# A2      B1      C2          25     52
#                 C3          57     40

print(df.loc[pd.IndexSlice['A1':'A3', 'B2'], :])
#                          val_1  val_2
# level_1 level_2 level_3              
# A1      B2      C0           1     89
#                 C1          54     60
# A3      B2      C0          64     54
#                 C1          27     96

print(df.loc[pd.IndexSlice['A1':'A3', ['B0', 'B2'], 'C1'], :])
#                          val_1  val_2
# level_1 level_2 level_3              
# A1      B2      C1          54     60
# A2      B0      C1          19      4
# A3      B2      C1          27     96

print(df.xs('B1', level='level_2'))
#                  val_1  val_2
# level_1 level_3              
# A0      C2          39     17
#         C3          75     71
# A2      C2          25     52
#         C3          57     40

print(df.xs('C1', level=2))
#                  val_1  val_2
# level_1 level_2              
# A0      B0          44      9
# A1      B2          54     60
# A2      B0          19      4
# A3      B2          27     96

print(df.xs(['B1', 'C2'], level=['level_2', 'level_3']))
#          val_1  val_2
# level_1              
# A0          39     17
# A2          25     52

print(df.xs(pd.IndexSlice['A1':'A3'], level='level_1'))
#                  val_1  val_2
# level_2 level_3              
# B2      C0           1     89
#         C1          54     60
# B3      C2          47      6
#         C3          16      5
# B0      C0          75     22
#         C1          19      4
# B1      C2          25     52
#         C3          57     40
# B2      C0          64     54
#         C1          27     96
# B3      C2         100     77
#         C3          22     50

print(df.xs(slice('A1', 'A3'), level='level_1'))
#                  val_1  val_2
# level_2 level_3              
# B2      C0           1     89
#         C1          54     60
# B3      C2          47      6
#         C3          16      5
# B0      C0          75     22
#         C1          19      4
# B1      C2          25     52
#         C3          57     40
# B2      C0          64     54
#         C1          27     96
# B3      C2         100     77
#         C3          22     50

# print(df.xs(['B1', 'B2'], level='level_2'))
# KeyError: ('B1', 'B2')

print(df.loc[pd.IndexSlice[:, ['B1', 'B2']], :])
#                          val_1  val_2
# level_1 level_2 level_3              
# A0      B1      C2          39     17
#                 C3          75     71
# A1      B2      C0           1     89
#                 C1          54     60
# A2      B1      C2          25     52
#                 C3          57     40
# A3      B2      C0          64     54
#                 C1          27     96

df.loc[(['A0', 'A1'], ['B0', 'B3']), :] = -100

print(df)
#                          val_1  val_2
# level_1 level_2 level_3              
# A0      B0      C0        -100   -100
#                 C1        -100   -100
#         B1      C2          39     17
#                 C3          75     71
# A1      B2      C0           1     89
#                 C1          54     60
#         B3      C2        -100   -100
#                 C3        -100   -100
# A2      B0      C0          75     22
#                 C1          19      4
#         B1      C2          25     52
#                 C3          57     40
# A3      B2      C0          64     54
#                 C1          27     96
#         B3      C2         100     77
#                 C3          22     50

df.loc[(['A0', 'A1'], ['B0', 'B3']), :] = [-200, -300]

print(df)
#                          val_1  val_2
# level_1 level_2 level_3              
# A0      B0      C0        -200   -300
#                 C1        -200   -300
#         B1      C2          39     17
#                 C3          75     71
# A1      B2      C0           1     89
#                 C1          54     60
#         B3      C2        -200   -300
#                 C3        -200   -300
# A2      B0      C0          75     22
#                 C1          19      4
#         B1      C2          25     52
#                 C3          57     40
# A3      B2      C0          64     54
#                 C1          27     96
#         B3      C2         100     77
#                 C3          22     50

df.loc[(['A0', 'A1'], ['B0', 'B3']), :] = [[-1, -2], [-3, -4], [-5, -6], [-7, -8]]

print(df)
#                          val_1  val_2
# level_1 level_2 level_3              
# A0      B0      C0          -1     -2
#                 C1          -3     -4
#         B1      C2          39     17
#                 C3          75     71
# A1      B2      C0           1     89
#                 C1          54     60
#         B3      C2          -5     -6
#                 C3          -7     -8
# A2      B0      C0          75     22
#                 C1          19      4
#         B1      C2          25     52
#                 C3          57     40
# A3      B2      C0          64     54
#                 C1          27     96
#         B3      C2         100     77
#                 C3          22     50

# df.xs(['B1', 'C2'], level=['level_2', 'level_3']) = 0
# SyntaxError: can't assign to function call
