import pandas as pd

df = pd.read_csv('data/src/sample_date.csv', index_col=0, parse_dates=True)
print(df)
#             val_1  val_2
# date                    
# 2017-11-01     65     76
# 2017-11-07     26     66
# 2017-11-18     47     47
# 2017-11-27     20     38
# 2017-12-05     65     85
# 2017-12-12      4     29
# 2017-12-22     31     54
# 2017-12-29     21      8
# 2018-01-03     98     76
# 2018-01-08     48     64
# 2018-01-19     18     48
# 2018-01-23     86     70

print(type(df.index))
# <class 'pandas.core.indexes.datetimes.DatetimeIndex'>

print(df.index.weekday)
# Int64Index([2, 1, 5, 0, 1, 1, 4, 4, 2, 0, 4, 1], dtype='int64', name='date')

print(df.index.dayofweek)
# Int64Index([2, 1, 5, 0, 1, 1, 4, 4, 2, 0, 4, 1], dtype='int64', name='date')

print(df.index.weekday_name)
# Index(['Wednesday', 'Tuesday', 'Saturday', 'Monday', 'Tuesday', 'Tuesday',
#        'Friday', 'Friday', 'Wednesday', 'Monday', 'Friday', 'Tuesday'],
#       dtype='object', name='date')

print(df[df.index.weekday == 0])
#             val_1  val_2
# date                    
# 2017-11-27     20     38
# 2018-01-08     48     64

print(df[df.index.weekday == 0].sum())
# val_1     68
# val_2    102
# dtype: int64

print(df[df.index.weekday == 0].mean())
# val_1    34.0
# val_2    51.0
# dtype: float64

df_w = df.set_index([df.index.weekday, df.index])
print(df_w)
#                  val_1  val_2
# date date                    
# 2    2017-11-01     65     76
# 1    2017-11-07     26     66
# 5    2017-11-18     47     47
# 0    2017-11-27     20     38
# 1    2017-12-05     65     85
#      2017-12-12      4     29
# 4    2017-12-22     31     54
#      2017-12-29     21      8
# 2    2018-01-03     98     76
# 0    2018-01-08     48     64
# 4    2018-01-19     18     48
# 1    2018-01-23     86     70

df_w.index.names = ['weekday', 'date']
print(df_w)
#                     val_1  val_2
# weekday date                    
# 2       2017-11-01     65     76
# 1       2017-11-07     26     66
# 5       2017-11-18     47     47
# 0       2017-11-27     20     38
# 1       2017-12-05     65     85
#         2017-12-12      4     29
# 4       2017-12-22     31     54
#         2017-12-29     21      8
# 2       2018-01-03     98     76
# 0       2018-01-08     48     64
# 4       2018-01-19     18     48
# 1       2018-01-23     86     70

df_w.sort_index(inplace=True)
print(df_w)
#                     val_1  val_2
# weekday date                    
# 0       2017-11-27     20     38
#         2018-01-08     48     64
# 1       2017-11-07     26     66
#         2017-12-05     65     85
#         2017-12-12      4     29
#         2018-01-23     86     70
# 2       2017-11-01     65     76
#         2018-01-03     98     76
# 4       2017-12-22     31     54
#         2017-12-29     21      8
#         2018-01-19     18     48
# 5       2017-11-18     47     47

print(df_w.sum())
# val_1    529
# val_2    661
# dtype: int64

print(df_w.sum(level='weekday'))
#          val_1  val_2
# weekday              
# 0           68    102
# 1          181    250
# 2          163    152
# 4           70    110
# 5           47     47

print(df_w.mean(level='weekday'))
#              val_1      val_2
# weekday                      
# 0        34.000000  51.000000
# 1        45.250000  62.500000
# 2        81.500000  76.000000
# 4        23.333333  36.666667
# 5        47.000000  47.000000

print(df.index.year)
# Int64Index([2017, 2017, 2017, 2017, 2017, 2017, 2017, 2017, 2018, 2018, 2018,
#             2018],
#            dtype='int64', name='date')

df_y = df.set_index([df.index.year, df.index])
df_y.index.names = ['year', 'date']
print(df_y)
#                  val_1  val_2
# year date                    
# 2017 2017-11-01     65     76
#      2017-11-07     26     66
#      2017-11-18     47     47
#      2017-11-27     20     38
#      2017-12-05     65     85
#      2017-12-12      4     29
#      2017-12-22     31     54
#      2017-12-29     21      8
# 2018 2018-01-03     98     76
#      2018-01-08     48     64
#      2018-01-19     18     48
#      2018-01-23     86     70

print(df_y.sum(level='year'))
#       val_1  val_2
# year              
# 2017    279    403
# 2018    250    258

df_m = df.set_index([df.index.month, df.index])
df_m.index.names = ['month', 'date']
print(df_m)
#                   val_1  val_2
# month date                    
# 11    2017-11-01     65     76
#       2017-11-07     26     66
#       2017-11-18     47     47
#       2017-11-27     20     38
# 12    2017-12-05     65     85
#       2017-12-12      4     29
#       2017-12-22     31     54
#       2017-12-29     21      8
# 1     2018-01-03     98     76
#       2018-01-08     48     64
#       2018-01-19     18     48
#       2018-01-23     86     70

print(df_m.sum(level='month'))
#        val_1  val_2
# month              
# 11       158    227
# 12       121    176
# 1        250    258

df_q = df.set_index([df.index.quarter, df.index])
df_q.index.names = ['quarter', 'date']
print(df_q)
#                     val_1  val_2
# quarter date                    
# 4       2017-11-01     65     76
#         2017-11-07     26     66
#         2017-11-18     47     47
#         2017-11-27     20     38
#         2017-12-05     65     85
#         2017-12-12      4     29
#         2017-12-22     31     54
#         2017-12-29     21      8
# 1       2018-01-03     98     76
#         2018-01-08     48     64
#         2018-01-19     18     48
#         2018-01-23     86     70

print(df_q.sum(level='quarter'))
#          val_1  val_2
# quarter              
# 4          279    403
# 1          250    258

df_yw = df.set_index([df.index.year, df.index.weekday, df.index])
df_yw.index.names = ['year', 'weekday', 'date']
df_yw.sort_index(inplace=True)
print(df_yw)
#                          val_1  val_2
# year weekday date                    
# 2017 0       2017-11-27     20     38
#      1       2017-11-07     26     66
#              2017-12-05     65     85
#              2017-12-12      4     29
#      2       2017-11-01     65     76
#      4       2017-12-22     31     54
#              2017-12-29     21      8
#      5       2017-11-18     47     47
# 2018 0       2018-01-08     48     64
#      1       2018-01-23     86     70
#      2       2018-01-03     98     76
#      4       2018-01-19     18     48

print(df_yw.sum(level='weekday'))
#          val_1  val_2
# weekday              
# 0           68    102
# 1          181    250
# 2          163    152
# 4           70    110
# 5           47     47

print(df_yw.sum(level=['year', 'weekday']))
#               val_1  val_2
# year weekday              
# 2017 0           20     38
#      1           95    180
#      2           65     76
#      4           52     62
#      5           47     47
# 2018 0           48     64
#      1           86     70
#      2           98     76
#      4           18     48

print(df_yw.loc[(2017, 1), :])
#             val_1  val_2
# date                    
# 2017-11-07     26     66
# 2017-12-05     65     85
# 2017-12-12      4     29

print(df_yw.xs(1, level='weekday'))
#                  val_1  val_2
# year date                    
# 2017 2017-11-07     26     66
#      2017-12-05     65     85
#      2017-12-12      4     29
# 2018 2018-01-23     86     70

print(df_yw.loc[(2017, [0, 4]), :])
#                          val_1  val_2
# year weekday date                    
# 2017 0       2017-11-27     20     38
#      4       2017-12-22     31     54
#              2017-12-29     21      8

print(df_yw.loc[pd.IndexSlice[:, [0, 4]], :])
#                          val_1  val_2
# year weekday date                    
# 2017 0       2017-11-27     20     38
#      4       2017-12-22     31     54
#              2017-12-29     21      8
# 2018 0       2018-01-08     48     64
#      4       2018-01-19     18     48

df_yqmw = df.set_index([df.index.year, df.index.quarter, df.index.month, df.index.weekday, df.index])
df_yqmw.index.names = ['year', 'quarter', 'month', 'weekday', 'date']
df_yqmw.sort_index(inplace=True)
print(df_yqmw)
#                                        val_1  val_2
# year quarter month weekday date                    
# 2017 4       11    0       2017-11-27     20     38
#                    1       2017-11-07     26     66
#                    2       2017-11-01     65     76
#                    5       2017-11-18     47     47
#              12    1       2017-12-05     65     85
#                            2017-12-12      4     29
#                    4       2017-12-22     31     54
#                            2017-12-29     21      8
# 2018 1       1     0       2018-01-08     48     64
#                    1       2018-01-23     86     70
#                    2       2018-01-03     98     76
#                    4       2018-01-19     18     48

print(df_yqmw.sum(level='month'))
#        val_1  val_2
# month              
# 11       158    227
# 12       121    176
# 1        250    258

print(df_yqmw.sum(level='weekday'))
#          val_1  val_2
# weekday              
# 0           68    102
# 1          181    250
# 2          163    152
# 5           47     47
# 4           70    110

print(df_yqmw.sum(level=['quarter', 'weekday']))
#                  val_1  val_2
# quarter weekday              
# 4       0           20     38
#         1           95    180
#         2           65     76
#         5           47     47
#         4           52     62
# 1       0           48     64
#         1           86     70
#         2           98     76
#         4           18     48

print(df_yqmw.xs(1, level='weekday'))
#                                val_1  val_2
# year quarter month date                    
# 2017 4       11    2017-11-07     26     66
#              12    2017-12-05     65     85
#                    2017-12-12      4     29
# 2018 1       1     2018-01-23     86     70

print(df_yqmw.xs((1, 2017), level=('weekday', 'year')))
#                           val_1  val_2
# quarter month date                    
# 4       11    2017-11-07     26     66
#         12    2017-12-05     65     85
#               2017-12-12      4     29

print(df_yqmw.loc[pd.IndexSlice[2017, :, :, [0, 4]], :])
#                                        val_1  val_2
# year quarter month weekday date                    
# 2017 4       11    0       2017-11-27     20     38
#              12    4       2017-12-22     31     54
#                            2017-12-29     21      8
