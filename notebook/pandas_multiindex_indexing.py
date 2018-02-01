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

print(df.sum(level='level_2'))
#          val_1  val_2
# level_2              
# B0         236    125
# B1         196    180
# B2         146    299
# B3         185    138

print(df.sum(level=['level_2', 'level_3']))
#                  val_1  val_2
# level_2 level_3              
# B0      C0         173    112
#         C1          63     13
# B1      C2          64     69
#         C3         132    111
# B2      C0          65    143
#         C1          81    156
# B3      C2         147     83
#         C3          38     55

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

# print(df.loc[(:, 'B1'), :]) => SyntaxError
print(df.loc[(slice(None), 'B1'), :])
#                          val_1  val_2
# level_1 level_2 level_3              
# A0      B1      C2          39     17
#                 C3          75     71
# A2      B1      C2          25     52
#                 C3          57     40

print(df.loc[pd.IndexSlice[:, 'B1'], :])
#                          val_1  val_2
# level_1 level_2 level_3              
# A0      B1      C2          39     17
#                 C3          75     71
# A2      B1      C2          25     52
#                 C3          57     40

print(df.xs('B1', level='level_2'))
#                  val_1  val_2
# level_1 level_3              
# A0      C2          39     17
#         C3          75     71
# A2      C2          25     52
#         C3          57     40

print(df.xs(['B1', 'C2'], level=['level_2', 'level_3']))
#          val_1  val_2
# level_1              
# A0          39     17
# A2          25     52

# print(df.xs(['B1', 'B2'], level='level_2')) => KeyError
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
