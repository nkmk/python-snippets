import pandas as pd

df = pd.DataFrame({'A': [1, 3, 5], 'B': [10, 30, 50], 'C': [100, 300, 500]},
                  index=pd.date_range('2020-06-01', '2020-06-05', freq='2D'))
print(df)
#             A   B    C
# 2020-06-01  1  10  100
# 2020-06-03  3  30  300
# 2020-06-05  5  50  500

new_index = pd.date_range('2020-06-01', '2020-06-05', freq='1D')
print(new_index)
# DatetimeIndex(['2020-06-01', '2020-06-02', '2020-06-03', '2020-06-04',
#                '2020-06-05'],
#               dtype='datetime64[ns]', freq='D')

print(df.reindex(index=new_index))
#               A     B      C
# 2020-06-01  1.0  10.0  100.0
# 2020-06-02  NaN   NaN    NaN
# 2020-06-03  3.0  30.0  300.0
# 2020-06-04  NaN   NaN    NaN
# 2020-06-05  5.0  50.0  500.0

print(df.reindex(index=new_index, method='bfill'))
#             A   B    C
# 2020-06-01  1  10  100
# 2020-06-02  3  30  300
# 2020-06-03  3  30  300
# 2020-06-04  5  50  500
# 2020-06-05  5  50  500

print(df.reindex(index=new_index).interpolate(method='time'))
#               A     B      C
# 2020-06-01  1.0  10.0  100.0
# 2020-06-02  2.0  20.0  200.0
# 2020-06-03  3.0  30.0  300.0
# 2020-06-04  4.0  40.0  400.0
# 2020-06-05  5.0  50.0  500.0

print(df.reindex(index=['2020-06-01', '2020-06-02', '2020-06-03']))
#              A   B   C
# 2020-06-01 NaN NaN NaN
# 2020-06-02 NaN NaN NaN
# 2020-06-03 NaN NaN NaN

df2 = pd.DataFrame({'A': [1, 1, 1, 1, 1], 'C': [100, 100, 100, 100, 100]},
                   index=pd.date_range('2020-06-01', '2020-06-05', freq='D'))
print(df2)
#             A    C
# 2020-06-01  1  100
# 2020-06-02  1  100
# 2020-06-03  1  100
# 2020-06-04  1  100
# 2020-06-05  1  100

print(df.reindex_like(df2))
#               A      C
# 2020-06-01  1.0  100.0
# 2020-06-02  NaN    NaN
# 2020-06-03  3.0  300.0
# 2020-06-04  NaN    NaN
# 2020-06-05  5.0  500.0

print(df.reindex_like(df2).interpolate(method='time'))
#               A      C
# 2020-06-01  1.0  100.0
# 2020-06-02  2.0  200.0
# 2020-06-03  3.0  300.0
# 2020-06-04  4.0  400.0
# 2020-06-05  5.0  500.0
