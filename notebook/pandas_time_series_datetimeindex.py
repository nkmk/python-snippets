import pandas as pd

df = pd.read_csv('data/src/sample_date.csv')
print(df)
#           date  val_1  val_2
# 0   2017-11-01     65     76
# 1   2017-11-07     26     66
# 2   2017-11-18     47     47
# 3   2017-11-27     20     38
# 4   2017-12-05     65     85
# 5   2017-12-12      4     29
# 6   2017-12-22     31     54
# 7   2017-12-29     21      8
# 8   2018-01-03     98     76
# 9   2018-01-08     48     64
# 10  2018-01-19     18     48
# 11  2018-01-23     86     70

print(type(df.index))
# <class 'pandas.core.indexes.range.RangeIndex'>

print(df['date'].dtype)
# object

df['date'] = pd.to_datetime(df['date'])
print(df['date'].dtype)
# datetime64[ns]

df.set_index('date', inplace=True)
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

print(df.index[0])
print(type(df.index[0]))
# 2017-11-01 00:00:00
# <class 'pandas._libs.tslib.Timestamp'>

print(df['2018'])
#             val_1  val_2
# date                    
# 2018-01-03     98     76
# 2018-01-08     48     64
# 2018-01-19     18     48
# 2018-01-23     86     70

print(df['2017-11'])
#             val_1  val_2
# date                    
# 2017-11-01     65     76
# 2017-11-07     26     66
# 2017-11-18     47     47
# 2017-11-27     20     38

print(df['2017-12-15':'2018-01-15'])
#             val_1  val_2
# date                    
# 2017-12-22     31     54
# 2017-12-29     21      8
# 2018-01-03     98     76
# 2018-01-08     48     64

print(df.loc['01/19/2018', 'val_1'])
# 18

print(df.loc['20180103', 'val_2'])
# 76

df_jp = pd.read_csv('data/src/sample_date_jp.csv')
print(df_jp)
#            date  val_1  val_2
# 0    2017年11月1日     65     76
# 1    2017年11月7日     26     66
# 2   2017年11月18日     47     47
# 3   2017年11月27日     20     38
# 4    2017年12月5日     65     85
# 5   2017年12月12日      4     29
# 6   2017年12月22日     31     54
# 7   2017年12月29日     21      8
# 8     2018年1月3日     98     76
# 9     2018年1月8日     48     64
# 10   2018年1月19日     18     48
# 11   2018年1月23日     86     70

df_jp['date'] = pd.to_datetime(df_jp['date'], format='%Y年%m月%d日')
df_jp.set_index('date', inplace=True)
print(df_jp)
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

print(type(df_jp.index))
# <class 'pandas.core.indexes.datetimes.DatetimeIndex'>

df = pd.read_csv('data/src/sample_date.csv', index_col='date', parse_dates=True)
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

parser = lambda date: pd.to_datetime(date, format='%Y年%m月%d日')

df_jp = pd.read_csv('data/src/sample_date_jp.csv', index_col='date', parse_dates=True, date_parser=parser)
print(df_jp)
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

print(type(df_jp.index))
# <class 'pandas.core.indexes.datetimes.DatetimeIndex'>

s = pd.read_csv('data/src/sample_date.csv', index_col=0, usecols=[0, 1], squeeze=True)
print(s)
# date
# 2017-11-01    65
# 2017-11-07    26
# 2017-11-18    47
# 2017-11-27    20
# 2017-12-05    65
# 2017-12-12     4
# 2017-12-22    31
# 2017-12-29    21
# 2018-01-03    98
# 2018-01-08    48
# 2018-01-19    18
# 2018-01-23    86
# Name: val_1, dtype: int64

print(type(s))
print(type(s.index))
# <class 'pandas.core.series.Series'>
# <class 'pandas.core.indexes.base.Index'>

s.index = pd.to_datetime(s.index)
print(s)
# date
# 2017-11-01    65
# 2017-11-07    26
# 2017-11-18    47
# 2017-11-27    20
# 2017-12-05    65
# 2017-12-12     4
# 2017-12-22    31
# 2017-12-29    21
# 2018-01-03    98
# 2018-01-08    48
# 2018-01-19    18
# 2018-01-23    86
# Name: val_1, dtype: int64

print(type(s))
print(type(s.index))
# <class 'pandas.core.series.Series'>
# <class 'pandas.core.indexes.datetimes.DatetimeIndex'>

print(s['2017-12-15':'2018-01-15'])
# date
# 2017-12-22    31
# 2017-12-29    21
# 2018-01-03    98
# 2018-01-08    48
# Name: val_1, dtype: int64
