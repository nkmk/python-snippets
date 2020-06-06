import pandas as pd

df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [10, 20, 30], 'C': [100, 200, 300]},
                   index=[10, 20, 30])
print(df1)
#     A   B    C
# 10  1  10  100
# 20  2  20  200
# 30  3  30  300

df2 = pd.DataFrame({'A': [1, 1, 1], 'C': [100, 100, 100]},
                   index=[10, 15, 20])
print(df2)
#     A    C
# 10  1  100
# 15  1  100
# 20  1  100

print(df1.reindex(columns=df2.columns, index=df2.index))
#       A      C
# 10  1.0  100.0
# 15  NaN    NaN
# 20  2.0  200.0

print(df1.reindex_like(df2))
#       A      C
# 10  1.0  100.0
# 15  NaN    NaN
# 20  2.0  200.0

print(df1.reindex_like(df2, method='bfill'))
#     A    C
# 10  1  100
# 15  2  200
# 20  2  200

# print(df1.reindex_like(df2, fill_value=0))
# TypeError: reindex_like() got an unexpected keyword argument 'fill_value'

print(df1.reindex_like(df2).fillna(0))
#       A      C
# 10  1.0  100.0
# 15  0.0    0.0
# 20  2.0  200.0
