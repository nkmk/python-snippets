import pandas as pd
import datetime

print(pd.__version__)
# 1.2.2

df = pd.DataFrame(range(6), columns=['A'],
                  index=pd.date_range('2021-01-01', periods=6, freq='8H'))
print(df)
#                      A
# 2021-01-01 00:00:00  0
# 2021-01-01 08:00:00  1
# 2021-01-01 16:00:00  2
# 2021-01-02 00:00:00  3
# 2021-01-02 08:00:00  4
# 2021-01-02 16:00:00  5

print(type(df.index))
# <class 'pandas.core.indexes.datetimes.DatetimeIndex'>

print(datetime.time(8, 0, 0))
# 08:00:00

print(df.at_time(datetime.time(8, 0, 0)))
#                      A
# 2021-01-01 08:00:00  1
# 2021-01-02 08:00:00  4

print(df.at_time(datetime.time(12, 0, 0)))
# Empty DataFrame
# Columns: [A]
# Index: []

print(df.at_time('16:00'))
#                      A
# 2021-01-01 16:00:00  2
# 2021-01-02 16:00:00  5

print(df.at_time('4PM'))
#                      A
# 2021-01-01 16:00:00  2
# 2021-01-02 16:00:00  5

df_sec = pd.DataFrame(range(6), columns=['A'],
                      index=pd.date_range('2021-01-01', periods=6, freq='8H5s'))
print(df_sec)
#                      A
# 2021-01-01 00:00:00  0
# 2021-01-01 08:00:05  1
# 2021-01-01 16:00:10  2
# 2021-01-02 00:00:15  3
# 2021-01-02 08:00:20  4
# 2021-01-02 16:00:25  5

print(df_sec.at_time('8:00'))
# Empty DataFrame
# Columns: [A]
# Index: []

print(df_sec.at_time('8:00:00'))
# Empty DataFrame
# Columns: [A]
# Index: []

print(df_sec.at_time('8:00:05'))
#                      A
# 2021-01-01 08:00:05  1

print(df_sec.between_time('8:00:00', '8:00:30'))
#                      A
# 2021-01-01 08:00:05  1
# 2021-01-02 08:00:20  4

print(df_sec.between_time(datetime.time(8, 0, 0), datetime.time(8, 0, 30)))
#                      A
# 2021-01-01 08:00:05  1
# 2021-01-02 08:00:20  4

print(df_sec.between_time('8:00:30', '8:00:00'))
#                      A
# 2021-01-01 00:00:00  0
# 2021-01-01 16:00:10  2
# 2021-01-02 00:00:15  3
# 2021-01-02 16:00:25  5

print(df_sec.between_time('8:00:05', '8:00:30'))
#                      A
# 2021-01-01 08:00:05  1
# 2021-01-02 08:00:20  4

print(df_sec.between_time('8:00:05', '8:00:30', include_start=False))
#                      A
# 2021-01-02 08:00:20  4
