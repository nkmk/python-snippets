import pandas as pd

df = pd.read_csv('data/src/sample_multi.csv')
print(df)
#    level_1 level_2 level_3  val_1  val_2
# 0       A0      B0      C0     98     90
# 1       A0      B0      C1     44      9
# 2       A0      B1      C2     39     17
# 3       A0      B1      C3     75     71
# 4       A1      B2      C0      1     89
# 5       A1      B2      C1     54     60
# 6       A1      B3      C2     47      6
# 7       A1      B3      C3     16      5
# 8       A2      B0      C0     75     22
# 9       A2      B0      C1     19      4
# 10      A2      B1      C2     25     52
# 11      A2      B1      C3     57     40
# 12      A3      B2      C0     64     54
# 13      A3      B2      C1     27     96
# 14      A3      B3      C2    100     77
# 15      A3      B3      C3     22     50

df_m_csv = pd.read_csv('data/src/sample_multi.csv', index_col=['level_1', 'level_2', 'level_3'])
print(df_m_csv)
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

df_m = df.set_index(['level_1', 'level_2', 'level_3'])
print(df_m)
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

df_m_1 = df.set_index('level_1')
print(df_m_1)
#         level_2 level_3  val_1  val_2
# level_1                              
# A0           B0      C0     98     90
# A0           B0      C1     44      9
# A0           B1      C2     39     17
# A0           B1      C3     75     71
# A1           B2      C0      1     89
# A1           B2      C1     54     60
# A1           B3      C2     47      6
# A1           B3      C3     16      5
# A2           B0      C0     75     22
# A2           B0      C1     19      4
# A2           B1      C2     25     52
# A2           B1      C3     57     40
# A3           B2      C0     64     54
# A3           B2      C1     27     96
# A3           B3      C2    100     77
# A3           B3      C3     22     50

df_m_2 = df_m_1.set_index('level_2', append=True)
print(df_m_2)
#                 level_3  val_1  val_2
# level_1 level_2                      
# A0      B0           C0     98     90
#         B0           C1     44      9
#         B1           C2     39     17
#         B1           C3     75     71
# A1      B2           C0      1     89
#         B2           C1     54     60
#         B3           C2     47      6
#         B3           C3     16      5
# A2      B0           C0     75     22
#         B0           C1     19      4
#         B1           C2     25     52
#         B1           C3     57     40
# A3      B2           C0     64     54
#         B2           C1     27     96
#         B3           C2    100     77
#         B3           C3     22     50

df_r_all = df_m.reset_index()
print(df_r_all)
#    level_1 level_2 level_3  val_1  val_2
# 0       A0      B0      C0     98     90
# 1       A0      B0      C1     44      9
# 2       A0      B1      C2     39     17
# 3       A0      B1      C3     75     71
# 4       A1      B2      C0      1     89
# 5       A1      B2      C1     54     60
# 6       A1      B3      C2     47      6
# 7       A1      B3      C3     16      5
# 8       A2      B0      C0     75     22
# 9       A2      B0      C1     19      4
# 10      A2      B1      C2     25     52
# 11      A2      B1      C3     57     40
# 12      A3      B2      C0     64     54
# 13      A3      B2      C1     27     96
# 14      A3      B3      C2    100     77
# 15      A3      B3      C3     22     50

df_r_1 = df_m.reset_index(level='level_1')
print(df_r_1)
#                 level_1  val_1  val_2
# level_2 level_3                      
# B0      C0           A0     98     90
#         C1           A0     44      9
# B1      C2           A0     39     17
#         C3           A0     75     71
# B2      C0           A1      1     89
#         C1           A1     54     60
# B3      C2           A1     47      6
#         C3           A1     16      5
# B0      C0           A2     75     22
#         C1           A2     19      4
# B1      C2           A2     25     52
#         C3           A2     57     40
# B2      C0           A3     64     54
#         C1           A3     27     96
# B3      C2           A3    100     77
#         C3           A3     22     50

df_r_1 = df_m.reset_index(level=0)
print(df_r_1)
#                 level_1  val_1  val_2
# level_2 level_3                      
# B0      C0           A0     98     90
#         C1           A0     44      9
# B1      C2           A0     39     17
#         C3           A0     75     71
# B2      C0           A1      1     89
#         C1           A1     54     60
# B3      C2           A1     47      6
#         C3           A1     16      5
# B0      C0           A2     75     22
#         C1           A2     19      4
# B1      C2           A2     25     52
#         C3           A2     57     40
# B2      C0           A3     64     54
#         C1           A3     27     96
# B3      C2           A3    100     77
#         C3           A3     22     50

df_r_2 = df_m.reset_index(level=['level_1', 'level_2'])
print(df_r_2)
#         level_1 level_2  val_1  val_2
# level_3                              
# C0           A0      B0     98     90
# C1           A0      B0     44      9
# C2           A0      B1     39     17
# C3           A0      B1     75     71
# C0           A1      B2      1     89
# C1           A1      B2     54     60
# C2           A1      B3     47      6
# C3           A1      B3     16      5
# C0           A2      B0     75     22
# C1           A2      B0     19      4
# C2           A2      B1     25     52
# C3           A2      B1     57     40
# C0           A3      B2     64     54
# C1           A3      B2     27     96
# C2           A3      B3    100     77
# C3           A3      B3     22     50

df_r_drop = df_m.reset_index(level='level_1', drop=True)
print(df_r_drop)
#                  val_1  val_2
# level_2 level_3              
# B0      C0          98     90
#         C1          44      9
# B1      C2          39     17
#         C3          75     71
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

df_r_drop_sort = df_r_drop.sort_index()
print(df_r_drop_sort)
#                  val_1  val_2
# level_2 level_3              
# B0      C0          98     90
#         C0          75     22
#         C1          44      9
#         C1          19      4
# B1      C2          39     17
#         C2          25     52
#         C3          75     71
#         C3          57     40
# B2      C0           1     89
#         C0          64     54
#         C1          54     60
#         C1          27     96
# B3      C2          47      6
#         C2         100     77
#         C3          16      5
#         C3          22     50

df_r_drop_sort_2 = df_r_drop.sort_index(level='level_3')
print(df_r_drop_sort_2)
#                  val_1  val_2
# level_2 level_3              
# B0      C0          98     90
#         C0          75     22
# B2      C0           1     89
#         C0          64     54
# B0      C1          44      9
#         C1          19      4
# B2      C1          54     60
#         C1          27     96
# B1      C2          39     17
#         C2          25     52
# B3      C2          47      6
#         C2         100     77
# B1      C3          75     71
#         C3          57     40
# B3      C3          16      5
#         C3          22     50

print(df_m)
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

df_m_swap = df_m.swaplevel('level_1', 'level_3')
print(df_m_swap)
#                          val_1  val_2
# level_3 level_2 level_1              
# C0      B0      A0          98     90
# C1      B0      A0          44      9
# C2      B1      A0          39     17
# C3      B1      A0          75     71
# C0      B2      A1           1     89
# C1      B2      A1          54     60
# C2      B3      A1          47      6
# C3      B3      A1          16      5
# C0      B0      A2          75     22
# C1      B0      A2          19      4
# C2      B1      A2          25     52
# C3      B1      A2          57     40
# C0      B2      A3          64     54
# C1      B2      A3          27     96
# C2      B3      A3         100     77
# C3      B3      A3          22     50

df_m_swap = df_m.swaplevel(0, 2)
print(df_m_swap)
#                          val_1  val_2
# level_3 level_2 level_1              
# C0      B0      A0          98     90
# C1      B0      A0          44      9
# C2      B1      A0          39     17
# C3      B1      A0          75     71
# C0      B2      A1           1     89
# C1      B2      A1          54     60
# C2      B3      A1          47      6
# C3      B3      A1          16      5
# C0      B0      A2          75     22
# C1      B0      A2          19      4
# C2      B1      A2          25     52
# C3      B1      A2          57     40
# C0      B2      A3          64     54
# C1      B2      A3          27     96
# C2      B3      A3         100     77
# C3      B3      A3          22     50

df_m_swap_sort = df_m.swaplevel('level_1', 'level_3').sort_index()
print(df_m_swap_sort)
#                          val_1  val_2
# level_3 level_2 level_1              
# C0      B0      A0          98     90
#                 A2          75     22
#         B2      A1           1     89
#                 A3          64     54
# C1      B0      A0          44      9
#                 A2          19      4
#         B2      A1          54     60
#                 A3          27     96
# C2      B1      A0          39     17
#                 A2          25     52
#         B3      A1          47      6
#                 A3         100     77
# C3      B1      A0          75     71
#                 A2          57     40
#         B3      A1          16      5
#                 A3          22     50

df_m_change = df_m.reset_index().set_index(['level_2', 'level_3', 'level_1']).sort_index()
print(df_m_change)
#                          val_1  val_2
# level_2 level_3 level_1              
# B0      C0      A0          98     90
#                 A2          75     22
#         C1      A0          44      9
#                 A2          19      4
# B1      C2      A0          39     17
#                 A2          25     52
#         C3      A0          75     71
#                 A2          57     40
# B2      C0      A1           1     89
#                 A3          64     54
#         C1      A1          54     60
#                 A3          27     96
# B3      C2      A1          47      6
#                 A3         100     77
#         C3      A1          16      5
#                 A3          22     50
