import pandas as pd

print(pd.__version__)
# 2.1.2

df = pd.DataFrame(
    {'c_0': ['A', 'A', 'B', 'B', 'B', 'B'],
     'c_1': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
     'c_2': [0, 1, 4, 9, 16, 25],
     'c_3': [125, 64, 27, 16, 1, 0]},
    index=['r_0', 'r_1', 'r_2', 'r_3', 'r_4', 'r_5']
)
print(df)
#     c_0 c_1  c_2  c_3
# r_0   A   X    0  125
# r_1   A   Y    1   64
# r_2   B   X    4   27
# r_3   B   Y    9   16
# r_4   B   X   16    1
# r_5   B   Y   25    0

grouped = df.groupby('c_0')
print(grouped)
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x1272139d0>

print(type(grouped))
# <class 'pandas.core.groupby.generic.DataFrameGroupBy'>

df_mean = grouped.mean(numeric_only=True)
print(df_mean)
#       c_2   c_3
# c_0            
# A     0.5  94.5
# B    13.5  11.0

print(type(df_mean))
# <class 'pandas.core.frame.DataFrame'>

print(df.groupby('c_0').mean(numeric_only=True))
#       c_2   c_3
# c_0            
# A     0.5  94.5
# B    13.5  11.0

print(df.groupby('c_1').mean(numeric_only=True))
#            c_2        c_3
# c_1                      
# X     6.666667  51.000000
# Y    11.666667  26.666667

print(df.groupby('c_0')['c_2'].mean())
# c_0
# A     0.5
# B    13.5
# Name: c_2, dtype: float64

print(df.groupby('c_0')[['c_2', 'c_3']].mean())
#       c_2   c_3
# c_0            
# A     0.5  94.5
# B    13.5  11.0

print(df.groupby('c_0').sum(numeric_only=True))
#      c_2  c_3
# c_0          
# A      1  189
# B     54   44

print(df.groupby('c_0').count())
#      c_1  c_2  c_3
# c_0               
# A      2    2    2
# B      4    4    4

print(df.groupby(['c_0', 'c_1']).mean())
#           c_2    c_3
# c_0 c_1             
# A   X     0.0  125.0
#     Y     1.0   64.0
# B   X    10.0   14.0
#     Y    17.0    8.0

print(df.groupby('c_0', as_index=False).mean(numeric_only=True))
#   c_0   c_2   c_3
# 0   A   0.5  94.5
# 1   B  13.5  11.0

print(df.groupby(['c_0', 'c_1'], as_index=False).mean())
#   c_0 c_1   c_2    c_3
# 0   A   X   0.0  125.0
# 1   A   Y   1.0   64.0
# 2   B   X  10.0   14.0
# 3   B   Y  17.0    8.0

df_nan = df.copy()
df_nan.iloc[0, 1] = float('nan')
df_nan.iloc[5, 1] = float('nan')
print(df_nan)
#     c_0  c_1  c_2  c_3
# r_0   A  NaN    0  125
# r_1   A    Y    1   64
# r_2   B    X    4   27
# r_3   B    Y    9   16
# r_4   B    X   16    1
# r_5   B  NaN   25    0

print(df_nan.groupby(['c_0', 'c_1']).mean())
#           c_2   c_3
# c_0 c_1            
# A   Y     1.0  64.0
# B   X    10.0  14.0
#     Y     9.0  16.0

print(df_nan.groupby(['c_0', 'c_1'], dropna=False).mean())
#           c_2    c_3
# c_0 c_1             
# A   Y     1.0   64.0
#     NaN   0.0  125.0
# B   X    10.0   14.0
#     Y     9.0   16.0
#     NaN  25.0    0.0

print(df.groupby('c_0').get_group('B'))
#     c_0 c_1  c_2  c_3
# r_2   B   X    4   27
# r_3   B   Y    9   16
# r_4   B   X   16    1
# r_5   B   Y   25    0

print(df.groupby(['c_0', 'c_1']).get_group(('B', 'X')))
#     c_0 c_1  c_2  c_3
# r_2   B   X    4   27
# r_4   B   X   16    1

print(df.groupby('c_0').size())
# c_0
# A    2
# B    4
# dtype: int64

print(df.groupby(['c_0', 'c_1']).size())
# c_0  c_1
# A    X      1
#      Y      1
# B    X      2
#      Y      2
# dtype: int64

print(df.groupby(['c_0', 'c_1']).agg('mean'))
#           c_2    c_3
# c_0 c_1             
# A   X     0.0  125.0
#     Y     1.0   64.0
# B   X    10.0   14.0
#     Y    17.0    8.0

print(df.groupby(['c_0', 'c_1']).agg(['mean', 'min', 'max']))
#           c_2            c_3          
#          mean min max   mean  min  max
# c_0 c_1                               
# A   X     0.0   0   0  125.0  125  125
#     Y     1.0   1   1   64.0   64   64
# B   X    10.0   4  16   14.0    1   27
#     Y    17.0   9  25    8.0    0   16

print(df.groupby(['c_0', 'c_1']).agg({'c_2': 'sum', 'c_3': ['min', 'max']}))
#         c_2  c_3     
#         sum  min  max
# c_0 c_1              
# A   X     0  125  125
#     Y     1   64   64
# B   X    20    1   27
#     Y    34    0   16

# print(df.groupby(['row_0', 'row_1']).agg('xxx'))
# AttributeError: 'xxx' is not a valid function for 'DataFrameGroupBy' object

# print(df.groupby(['row_0', 'row_1']).agg(['xxx']))
# AttributeError: 'SeriesGroupBy' object has no attribute 'xxx'

def my_func(x):
    return x.max() + x.min()

print(df.groupby(['c_0', 'c_1']).agg([my_func, lambda x: x.sum() - x.mean()]))
#             c_2                c_3           
#         my_func <lambda_0> my_func <lambda_0>
# c_0 c_1                                      
# A   X         0        0.0     250        0.0
#     Y         2        0.0     128        0.0
# B   X        20       10.0      28       14.0
#     Y        34       17.0      16        8.0

print(df.groupby(['c_0', 'c_1']).agg(lambda x: str(type(x))).iloc[0, 0])
# <class 'pandas.core.series.Series'>

print(df.groupby(['c_0', 'c_1']).agg([lambda x: str(type(x))]).iloc[0, 0])
# <class 'pandas.core.series.Series'>

print(df.groupby(['c_0', 'c_1']).agg(lambda x: str(x.values)))
#              c_2      c_3
# c_0 c_1                  
# A   X        [0]    [125]
#     Y        [1]     [64]
# B   X    [ 4 16]  [27  1]
#     Y    [ 9 25]  [16  0]

print(df.groupby(['c_0', 'c_1']).describe()['c_2'])
#          count  mean        std  min   25%   50%   75%   max
# c_0 c_1                                                     
# A   X      1.0   0.0        NaN  0.0   0.0   0.0   0.0   0.0
#     Y      1.0   1.0        NaN  1.0   1.0   1.0   1.0   1.0
# B   X      2.0  10.0   8.485281  4.0   7.0  10.0  13.0  16.0
#     Y      2.0  17.0  11.313708  9.0  13.0  17.0  21.0  25.0

print(df.groupby(['c_0', 'c_1']).apply(lambda x: type(x)))
# c_0  c_1
# A    X      <class 'pandas.core.frame.DataFrame'>
#      Y      <class 'pandas.core.frame.DataFrame'>
# B    X      <class 'pandas.core.frame.DataFrame'>
#      Y      <class 'pandas.core.frame.DataFrame'>
# dtype: object

dfs = []
df.groupby(['c_0', 'c_1']).apply(lambda x: dfs.append(x))
print(dfs[0])
#     c_0 c_1  c_2  c_3
# r_0   A   X    0  125

print(dfs[1])
#     c_0 c_1  c_2  c_3
# r_1   A   Y    1   64

print(dfs[2])
#     c_0 c_1  c_2  c_3
# r_2   B   X    4   27
# r_4   B   X   16    1

print(dfs[3])
#     c_0 c_1  c_2  c_3
# r_3   B   Y    9   16
# r_5   B   Y   25    0

print(df.groupby(['c_0', 'c_1']).apply(lambda x: x['c_2'].max()))
# c_0  c_1
# A    X       0
#      Y       1
# B    X      16
#      Y      25
# dtype: int64

print(df.groupby(['c_0', 'c_1'], as_index=False).apply(lambda x: x['c_2'].max()))
#   c_0 c_1  None
# 0   A   X     0
# 1   A   Y     1
# 2   B   X    16
# 3   B   Y    25

print(dfs[0][['c_2', 'c_3']].max())
# c_2      0
# c_3    125
# dtype: int64

print(dfs[0][['c_2', 'c_3']].max(axis=1))
# r_0    125
# dtype: int64

print(df.groupby(['c_0', 'c_1']).apply(lambda x: x[['c_2', 'c_3']].max()))
#          c_2  c_3
# c_0 c_1          
# A   X      0  125
#     Y      1   64
# B   X     16   27
#     Y     25   16

print(df.groupby(['c_0', 'c_1']).apply(lambda x: x[['c_2', 'c_3']].max(axis=1)))
# c_0  c_1     
# A    X    r_0    125
#      Y    r_1     64
# B    X    r_2     27
#           r_4     16
#      Y    r_3     16
#           r_5     25
# dtype: int64

print(
    df.groupby(['c_0', 'c_1'], as_index=False).apply(
        lambda x: x[['c_2', 'c_3']].max(axis=1)
    )
)
# 0  r_0    125
# 1  r_1     64
# 2  r_2     27
#    r_4     16
# 3  r_3     16
#    r_5     25
# dtype: int64

print(
    df.groupby(['c_0', 'c_1'], group_keys=False).apply(
        lambda x: x[['c_2', 'c_3']].max(axis=1)
    )
)
# r_0    125
# r_1     64
# r_2     27
# r_4     16
# r_3     16
# r_5     25
# dtype: int64

print(df.groupby(['c_0', 'c_1']).apply(lambda x: x[['c_2', 'c_3']] * 10))
#              c_2   c_3
# c_0 c_1               
# A   X   r_0    0  1250
#     Y   r_1   10   640
# B   X   r_2   40   270
#         r_4  160    10
#     Y   r_3   90   160
#         r_5  250     0

print(
    df.groupby(['c_0', 'c_1'], as_index=False).apply(lambda x: x[['c_2', 'c_3']] * 10)
)
#        c_2   c_3
# 0 r_0    0  1250
# 1 r_1   10   640
# 2 r_2   40   270
#   r_4  160    10
# 3 r_3   90   160
#   r_5  250     0

print(
    df.groupby(['c_0', 'c_1'], group_keys=False).apply(lambda x: x[['c_2', 'c_3']] * 10)
)
#      c_2   c_3
# r_0    0  1250
# r_1   10   640
# r_2   40   270
# r_3   90   160
# r_4  160    10
# r_5  250     0
