import pandas as pd
import datetime

df = pd.read_csv('data/src/sample_datetime_multi.csv')

print(df)
#                   A                   B
# 0  2017-11-01 12:24   2017年11月1日 12時24分
# 1  2017-11-18 23:00  2017年11月18日 23時00分
# 2   2017-12-05 5:05    2017年12月5日 5時05分
# 3   2017-12-22 8:54   2017年12月22日 8時54分
# 4  2018-01-08 14:20    2018年1月8日 14時20分
# 5  2018-01-19 20:01   2018年1月19日 20時01分

print(df.dtypes)
# A    object
# B    object
# dtype: object

print(type(df['A'][0]))
# <class 'str'>

print(pd.to_datetime(df['A']))
# 0   2017-11-01 12:24:00
# 1   2017-11-18 23:00:00
# 2   2017-12-05 05:05:00
# 3   2017-12-22 08:54:00
# 4   2018-01-08 14:20:00
# 5   2018-01-19 20:01:00
# Name: A, dtype: datetime64[ns]

print(pd.to_datetime(df['B'], format='%Y年%m月%d日 %H時%M分'))
# 0   2017-11-01 12:24:00
# 1   2017-11-18 23:00:00
# 2   2017-12-05 05:05:00
# 3   2017-12-22 08:54:00
# 4   2018-01-08 14:20:00
# 5   2018-01-19 20:01:00
# Name: B, dtype: datetime64[ns]

print(pd.to_datetime(df['A']) == pd.to_datetime(df['B'], format='%Y年%m月%d日 %H時%M分'))
# 0    True
# 1    True
# 2    True
# 3    True
# 4    True
# 5    True
# dtype: bool

df['X'] = pd.to_datetime(df['A'])

print(df)
#                   A                   B                   X
# 0  2017-11-01 12:24   2017年11月1日 12時24分 2017-11-01 12:24:00
# 1  2017-11-18 23:00  2017年11月18日 23時00分 2017-11-18 23:00:00
# 2   2017-12-05 5:05    2017年12月5日 5時05分 2017-12-05 05:05:00
# 3   2017-12-22 8:54   2017年12月22日 8時54分 2017-12-22 08:54:00
# 4  2018-01-08 14:20    2018年1月8日 14時20分 2018-01-08 14:20:00
# 5  2018-01-19 20:01   2018年1月19日 20時01分 2018-01-19 20:01:00

print(df.dtypes)
# A            object
# B            object
# X    datetime64[ns]
# dtype: object

print(df['X'][0])
# 2017-11-01 12:24:00

print(type(df['X'][0]))
# <class 'pandas._libs.tslib.Timestamp'>

print(issubclass(pd.Timestamp, datetime.datetime))
# True

print(df['X'][0].year)
# 2017

print(df['X'][0].weekday_name)
# Wednesday

py_dt = df['X'][0].to_pydatetime()
print(type(py_dt))
# <class 'datetime.datetime'>

dt64 = df['X'][0].to_datetime64()
print(type(dt64))
# <class 'numpy.datetime64'>

print(df['X'][0].timestamp())
# 1509539040.0

print(pd.to_datetime('1970-01-01 00:00:00').timestamp())
# 0.0

print(int(df['X'][0].timestamp()))
# 1509539040

print(df['X'][0].strftime('%Y/%m/%d'))
# 2017/11/01

print(df['X'].dt.year)
# 0    2017
# 1    2017
# 2    2017
# 3    2017
# 4    2018
# 5    2018
# Name: X, dtype: int64

print(df['X'].dt.hour)
# 0    12
# 1    23
# 2     5
# 3     8
# 4    14
# 5    20
# Name: X, dtype: int64

print(df['X'].dt.dayofweek)
# 0    2
# 1    5
# 2    1
# 3    4
# 4    0
# 5    4
# Name: X, dtype: int64

print(df[df['X'].dt.dayofweek == 4])
#                   A                  B                   X
# 3   2017-12-22 8:54  2017年12月22日 8時54分 2017-12-22 08:54:00
# 5  2018-01-19 20:01  2018年1月19日 20時01分 2018-01-19 20:01:00

print(df['X'].astype(str))
# 0    2017-11-01 12:24:00
# 1    2017-11-18 23:00:00
# 2    2017-12-05 05:05:00
# 3    2017-12-22 08:54:00
# 4    2018-01-08 14:20:00
# 5    2018-01-19 20:01:00
# Name: X, dtype: object

print(df['X'].dt.strftime('%A, %B %d, %Y'))
# 0    Wednesday, November 01, 2017
# 1     Saturday, November 18, 2017
# 2      Tuesday, December 05, 2017
# 3       Friday, December 22, 2017
# 4        Monday, January 08, 2018
# 5        Friday, January 19, 2018
# Name: X, dtype: object

print(df['X'].dt.strftime('%Y年%m月%d日'))
# 0    2017年11月01日
# 1    2017年11月18日
# 2    2017年12月05日
# 3    2017年12月22日
# 4    2018年01月08日
# 5    2018年01月19日
# Name: X, dtype: object

df['en'] = df['X'].dt.strftime('%A, %B %d, %Y')
df['jp'] = df['X'].dt.strftime('%Y年%m月%d日')

print(df)
#                   A                   B                   X  \
# 0  2017-11-01 12:24   2017年11月1日 12時24分 2017-11-01 12:24:00   
# 1  2017-11-18 23:00  2017年11月18日 23時00分 2017-11-18 23:00:00   
# 2   2017-12-05 5:05    2017年12月5日 5時05分 2017-12-05 05:05:00   
# 3   2017-12-22 8:54   2017年12月22日 8時54分 2017-12-22 08:54:00   
# 4  2018-01-08 14:20    2018年1月8日 14時20分 2018-01-08 14:20:00   
# 5  2018-01-19 20:01   2018年1月19日 20時01分 2018-01-19 20:01:00   
#                              en           jp  
# 0  Wednesday, November 01, 2017  2017年11月01日  
# 1   Saturday, November 18, 2017  2017年11月18日  
# 2    Tuesday, December 05, 2017  2017年12月05日  
# 3     Friday, December 22, 2017  2017年12月22日  
# 4      Monday, January 08, 2018  2018年01月08日  
# 5      Friday, January 19, 2018  2018年01月19日  

print(df['X'].dt.to_pydatetime())
# [datetime.datetime(2017, 11, 1, 12, 24)
#  datetime.datetime(2017, 11, 18, 23, 0)
#  datetime.datetime(2017, 12, 5, 5, 5)
#  datetime.datetime(2017, 12, 22, 8, 54)
#  datetime.datetime(2018, 1, 8, 14, 20)
#  datetime.datetime(2018, 1, 19, 20, 1)]

print(type(df['X'].dt.to_pydatetime()))
print(type(df['X'].dt.to_pydatetime()[0]))
# <class 'numpy.ndarray'>
# <class 'datetime.datetime'>

print(df['X'].values)
# ['2017-11-01T12:24:00.000000000' '2017-11-18T23:00:00.000000000'
#  '2017-12-05T05:05:00.000000000' '2017-12-22T08:54:00.000000000'
#  '2018-01-08T14:20:00.000000000' '2018-01-19T20:01:00.000000000']

print(type(df['X'].values))
print(type(df['X'].values[0]))
# <class 'numpy.ndarray'>
# <class 'numpy.datetime64'>

print(df['X'].map(pd.Timestamp.timestamp))
# 0    1.509539e+09
# 1    1.511046e+09
# 2    1.512450e+09
# 3    1.513933e+09
# 4    1.515421e+09
# 5    1.516392e+09
# Name: X, dtype: float64

print(df['X'].map(pd.Timestamp.timestamp).astype(int))
# 0    1509539040
# 1    1511046000
# 2    1512450300
# 3    1513932840
# 4    1515421200
# 5    1516392060
# Name: X, dtype: int64

df_i = df.set_index('X').drop(['en', 'jp'], axis=1)

print(df_i)
#                                     A                   B
# X                                                        
# 2017-11-01 12:24:00  2017-11-01 12:24   2017年11月1日 12時24分
# 2017-11-18 23:00:00  2017-11-18 23:00  2017年11月18日 23時00分
# 2017-12-05 05:05:00   2017-12-05 5:05    2017年12月5日 5時05分
# 2017-12-22 08:54:00   2017-12-22 8:54   2017年12月22日 8時54分
# 2018-01-08 14:20:00  2018-01-08 14:20    2018年1月8日 14時20分
# 2018-01-19 20:01:00  2018-01-19 20:01   2018年1月19日 20時01分

print(df_i.index)
# DatetimeIndex(['2017-11-01 12:24:00', '2017-11-18 23:00:00',
#                '2017-12-05 05:05:00', '2017-12-22 08:54:00',
#                '2018-01-08 14:20:00', '2018-01-19 20:01:00'],
#               dtype='datetime64[ns]', name='X', freq=None)

print(df_i.index.minute)
# Int64Index([24, 0, 5, 54, 20, 1], dtype='int64', name='X')

print(df_i.index.strftime('%y/%m/%d'))
# ['17/11/01' '17/11/18' '17/12/05' '17/12/22' '18/01/08' '18/01/19']

df_i['min'] = df_i.index.minute
df_i['str'] = df_i.index.strftime('%y/%m/%d')

print(df_i)
#                                     A                   B  min       str
# X                                                                       
# 2017-11-01 12:24:00  2017-11-01 12:24   2017年11月1日 12時24分   24  17/11/01
# 2017-11-18 23:00:00  2017-11-18 23:00  2017年11月18日 23時00分    0  17/11/18
# 2017-12-05 05:05:00   2017-12-05 5:05    2017年12月5日 5時05分    5  17/12/05
# 2017-12-22 08:54:00   2017-12-22 8:54   2017年12月22日 8時54分   54  17/12/22
# 2018-01-08 14:20:00  2018-01-08 14:20    2018年1月8日 14時20分   20  18/01/08
# 2018-01-19 20:01:00  2018-01-19 20:01   2018年1月19日 20時01分    1  18/01/19

df_csv = pd.read_csv('data/src/sample_datetime_multi.csv', parse_dates=[0])

print(df_csv)
#                     A                   B
# 0 2017-11-01 12:24:00   2017年11月1日 12時24分
# 1 2017-11-18 23:00:00  2017年11月18日 23時00分
# 2 2017-12-05 05:05:00    2017年12月5日 5時05分
# 3 2017-12-22 08:54:00   2017年12月22日 8時54分
# 4 2018-01-08 14:20:00    2018年1月8日 14時20分
# 5 2018-01-19 20:01:00   2018年1月19日 20時01分

print(df_csv.dtypes)
# A    datetime64[ns]
# B            object
# dtype: object

df_csv_jp = pd.read_csv('data/src/sample_datetime_multi.csv',
                        parse_dates=[1],
                        date_parser=lambda date: pd.to_datetime(date, format='%Y年%m月%d日 %H時%M分'))

print(df_csv_jp)
#                   A                   B
# 0  2017-11-01 12:24 2017-11-01 12:24:00
# 1  2017-11-18 23:00 2017-11-18 23:00:00
# 2   2017-12-05 5:05 2017-12-05 05:05:00
# 3   2017-12-22 8:54 2017-12-22 08:54:00
# 4  2018-01-08 14:20 2018-01-08 14:20:00
# 5  2018-01-19 20:01 2018-01-19 20:01:00

print(df_csv_jp.dtypes)
# A            object
# B    datetime64[ns]
# dtype: object

df_csv_jp_i = pd.read_csv('data/src/sample_datetime_multi.csv',
                          index_col=1,
                          parse_dates=True,
                          date_parser=lambda date: pd.to_datetime(date, format='%Y年%m月%d日 %H時%M分'))

print(df_csv_jp_i)
#                                     A
# B                                    
# 2017-11-01 12:24:00  2017-11-01 12:24
# 2017-11-18 23:00:00  2017-11-18 23:00
# 2017-12-05 05:05:00   2017-12-05 5:05
# 2017-12-22 08:54:00   2017-12-22 8:54
# 2018-01-08 14:20:00  2018-01-08 14:20
# 2018-01-19 20:01:00  2018-01-19 20:01

print(df_csv_jp_i.index)
# DatetimeIndex(['2017-11-01 12:24:00', '2017-11-18 23:00:00',
#                '2017-12-05 05:05:00', '2017-12-22 08:54:00',
#                '2018-01-08 14:20:00', '2018-01-19 20:01:00'],
#               dtype='datetime64[ns]', name='B', freq=None)
