import pandas as pd

print(pd.__version__)
# 1.2.2

df = pd.read_csv('data/src/sample_date.csv',
                  index_col='date', parse_dates=True).head(3)
print(df)
#             val_1  val_2
# date                    
# 2017-11-01     65     76
# 2017-11-07     26     66
# 2017-11-18     47     47

print(type(df.index))
# <class 'pandas.core.indexes.datetimes.DatetimeIndex'>

print(df.index[0])
# 2017-11-01 00:00:00

print(type(df.index[0]))
# <class 'pandas._libs.tslibs.timestamps.Timestamp'>

df_default = pd.read_csv('data/src/sample_date.csv', index_col='date').head(3)
print(df_default)
#             val_1  val_2
# date                    
# 2017-11-01     65     76
# 2017-11-07     26     66
# 2017-11-18     47     47

print(type(df_default.index))
# <class 'pandas.core.indexes.base.Index'>

print(df_default.index[0])
# 2017-11-01

print(type(df_default.index[0]))
# <class 'str'>

df_jp_ng = pd.read_csv('data/src/sample_date_jp.csv',
                       index_col='date', parse_dates=True).head(3)
print(df_jp_ng)
#              val_1  val_2
# date                     
# 2017年11月1日      65     76
# 2017年11月7日      26     66
# 2017年11月18日     47     47

print(type(df_jp_ng.index))
# <class 'pandas.core.indexes.base.Index'>

df_jp = pd.read_csv('data/src/sample_date_jp.csv',
                    index_col='date', parse_dates=True,
                    date_parser=lambda x: pd.to_datetime(x, format='%Y年%m月%d日')).head(3)
print(df_jp)
#             val_1  val_2
# date                    
# 2017-11-01     65     76
# 2017-11-07     26     66
# 2017-11-18     47     47

print(type(df_jp.index))
# <class 'pandas.core.indexes.datetimes.DatetimeIndex'>

df = pd.read_csv('data/src/sample_date.csv').head(3)
print(df)
#          date  val_1  val_2
# 0  2017-11-01     65     76
# 1  2017-11-07     26     66
# 2  2017-11-18     47     47

print(type(df.index))
# <class 'pandas.core.indexes.range.RangeIndex'>

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

print(type(df.index))
# <class 'pandas.core.indexes.datetimes.DatetimeIndex'>

df = pd.read_csv('data/src/sample_date.csv').head(3)
df.set_axis(pd.to_datetime(df['date']), axis='index', inplace=True)
print(df)
#                   date  val_1  val_2
# date                                
# 2017-11-01  2017-11-01     65     76
# 2017-11-07  2017-11-07     26     66
# 2017-11-18  2017-11-18     47     47

print(type(df.index))
# <class 'pandas.core.indexes.datetimes.DatetimeIndex'>

df.drop(['date'], axis='columns', inplace=True)
print(df)
#             val_1  val_2
# date                    
# 2017-11-01     65     76
# 2017-11-07     26     66
# 2017-11-18     47     47

df = pd.read_csv('data/src/sample_date.csv').head(3)
df.index = pd.to_datetime(df['date'])
df.drop(['date'], axis='columns', inplace=True)
print(df)
#             val_1  val_2
# date                    
# 2017-11-01     65     76
# 2017-11-07     26     66
# 2017-11-18     47     47

print(type(df.index))
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

print(df.loc['2018'])
#             val_1  val_2
# date                    
# 2018-01-03     98     76
# 2018-01-08     48     64
# 2018-01-19     18     48
# 2018-01-23     86     70

print(df.loc['2017-11'])
#             val_1  val_2
# date                    
# 2017-11-01     65     76
# 2017-11-07     26     66
# 2017-11-18     47     47
# 2017-11-27     20     38

print(df.loc['2017-12-15':'2018-01-15'])
#             val_1  val_2
# date                    
# 2017-12-22     31     54
# 2017-12-29     21      8
# 2018-01-03     98     76
# 2018-01-08     48     64

print(df.at['01/19/2018', 'val_1'])
# 18

print(df.at['20180103', 'val_2'])
# 76
