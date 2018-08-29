import pandas as pd

dates = pd.date_range('2018-08-01', '2018-08-31', freq='B')

df = pd.DataFrame({'price': dates.day, 'volume': dates.day * 10}, index=dates)

print(df)
#             price  volume
# 2018-08-01      1      10
# 2018-08-02      2      20
# 2018-08-03      3      30
# 2018-08-06      6      60
# 2018-08-07      7      70
# 2018-08-08      8      80
# 2018-08-09      9      90
# 2018-08-10     10     100
# 2018-08-13     13     130
# 2018-08-14     14     140
# 2018-08-15     15     150
# 2018-08-16     16     160
# 2018-08-17     17     170
# 2018-08-20     20     200
# 2018-08-21     21     210
# 2018-08-22     22     220
# 2018-08-23     23     230
# 2018-08-24     24     240
# 2018-08-27     27     270
# 2018-08-28     28     280
# 2018-08-29     29     290
# 2018-08-30     30     300
# 2018-08-31     31     310

print(df.index)
# DatetimeIndex(['2018-08-01', '2018-08-02', '2018-08-03', '2018-08-06',
#                '2018-08-07', '2018-08-08', '2018-08-09', '2018-08-10',
#                '2018-08-13', '2018-08-14', '2018-08-15', '2018-08-16',
#                '2018-08-17', '2018-08-20', '2018-08-21', '2018-08-22',
#                '2018-08-23', '2018-08-24', '2018-08-27', '2018-08-28',
#                '2018-08-29', '2018-08-30', '2018-08-31'],
#               dtype='datetime64[ns]', freq='B')

print(df['price'].resample('W').ohlc())
#             open  high  low  close
# 2018-08-05     1     3    1      3
# 2018-08-12     6    10    6     10
# 2018-08-19    13    17   13     17
# 2018-08-26    20    24   20     24
# 2018-09-02    27    31   27     31

print(df['price'].resample('W-MON', label='left', closed='left').ohlc())
#             open  high  low  close
# 2018-07-30     1     3    1      3
# 2018-08-06     6    10    6     10
# 2018-08-13    13    17   13     17
# 2018-08-20    20    24   20     24
# 2018-08-27    27    31   27     31

print(df['volume'].resample('W').sum())
# 2018-08-05      60
# 2018-08-12     400
# 2018-08-19     750
# 2018-08-26    1100
# 2018-09-02    1450
# Freq: W-SUN, Name: volume, dtype: int64

print(df['volume'].resample('W-MON', label='left', closed='left').sum())
# 2018-07-30      60
# 2018-08-06     400
# 2018-08-13     750
# 2018-08-20    1100
# 2018-08-27    1450
# Freq: W-MON, Name: volume, dtype: int64

print(pd.concat([df['price'].resample('W-MON', label='left', closed='left').ohlc(),
                 df['volume'].resample('W-MON', label='left', closed='left').sum()], axis=1))
#             open  high  low  close  volume
# 2018-07-30     1     3    1      3      60
# 2018-08-06     6    10    6     10     400
# 2018-08-13    13    17   13     17     750
# 2018-08-20    20    24   20     24    1100
# 2018-08-27    27    31   27     31    1450

print(df['price'].resample('W-MON', label='left', closed='left').ohlc()
      .assign(volume=df['volume'].resample('W-MON', label='left', closed='left').sum()))
#             open  high  low  close  volume
# 2018-07-30     1     3    1      3      60
# 2018-08-06     6    10    6     10     400
# 2018-08-13    13    17   13     17     750
# 2018-08-20    20    24   20     24    1100
# 2018-08-27    27    31   27     31    1450

print(pd.concat([df['price'].resample('W-MON', label='left', closed='left').ohlc(),
                 df['volume'].resample('W').sum()], axis=1))
#             open  high   low  close  volume
# 2018-07-30   1.0   3.0   1.0    3.0     NaN
# 2018-08-05   NaN   NaN   NaN    NaN    60.0
# 2018-08-06   6.0  10.0   6.0   10.0     NaN
# 2018-08-12   NaN   NaN   NaN    NaN   400.0
# 2018-08-13  13.0  17.0  13.0   17.0     NaN
# 2018-08-19   NaN   NaN   NaN    NaN   750.0
# 2018-08-20  20.0  24.0  20.0   24.0     NaN
# 2018-08-26   NaN   NaN   NaN    NaN  1100.0
# 2018-08-27  27.0  31.0  27.0   31.0     NaN
# 2018-09-02   NaN   NaN   NaN    NaN  1450.0

print(df['price'].resample('W-MON', label='left', closed='left').ohlc()
      .assign(volume=df['volume'].resample('W').sum().values))
#             open  high  low  close  volume
# 2018-07-30     1     3    1      3      60
# 2018-08-06     6    10    6     10     400
# 2018-08-13    13    17   13     17     750
# 2018-08-20    20    24   20     24    1100
# 2018-08-27    27    31   27     31    1450
