import pandas as pd

s = '2018-01-01T12:00+09:00'

print(s)
# 2018-01-01T12:00+09:00

print(type(s))
# <class 'str'>

ts = pd.to_datetime(s)

print(ts)
# 2018-01-01 03:00:00

print(type(ts))
# <class 'pandas._libs.tslibs.timestamps.Timestamp'>

print(ts.tz)
# None

ts_utc = pd.to_datetime(s, utc=True)

print(ts_utc)
# 2018-01-01 03:00:00+00:00

print(ts_utc.tz)
# UTC

ts_jst = ts_utc.tz_convert('Asia/Tokyo')

print(ts_jst)
# 2018-01-01 12:00:00+09:00

print(ts_jst.tz)
# Asia/Tokyo

print(ts_utc.value)
# 1514775600000000000

print(ts_jst.value)
# 1514775600000000000

print(ts_utc == ts_jst)
# True

ts_pst = ts_utc.tz_convert('US/Pacific')

print(ts_pst)
# 2017-12-31 19:00:00-08:00

print(ts_pst.tz)
# US/Pacific

print(ts_utc.tz_convert('America/Los_Angeles'))
# 2017-12-31 19:00:00-08:00

print(ts)
# 2018-01-01 03:00:00

print(ts.tz)
# None

# print(ts.tz_convert('Asia/Tokyo'))
# TypeError: Cannot convert tz-naive Timestamp, use tz_localize to localize

ts_jst_localize = ts.tz_localize('Asia/Tokyo')

print(ts_jst_localize)
# 2018-01-01 03:00:00+09:00

print(ts_jst_localize.tz)
# Asia/Tokyo

print(ts.tz_localize('US/Pacific'))
# 2018-01-01 03:00:00-08:00

print(ts.tz_localize('Asia/Tokyo').value == ts.tz_localize('US/Pacific').value)
# False

print(ts_jst)
# 2018-01-01 12:00:00+09:00

# ts_jst.tz_localize('US/Pacific')
# TypeError: Cannot localize tz-aware Timestamp, use tz_convert for conversions

print(ts_jst)
# 2018-01-01 12:00:00+09:00

print(ts_jst.tz)
# Asia/Tokyo

print(ts_jst.tz_convert(None))
# 2018-01-01 03:00:00

print(ts_jst.tz_localize(None))
# 2018-01-01 12:00:00

df = pd.DataFrame({'date': ['2018-01-01T12:00+09:00',
                            '2018-01-02T00:00+09:00',
                            '2018-01-03T10:00-05:00',
                            '2018-01-03T19:00-08:00'],
                   'value': [0, 1, 2, 3]})

print(df)
#                      date  value
# 0  2018-01-01T12:00+09:00      0
# 1  2018-01-02T00:00+09:00      1
# 2  2018-01-03T10:00-05:00      2
# 3  2018-01-03T19:00-08:00      3

print(pd.to_datetime(df['date']))
# 0   2018-01-01 03:00:00
# 1   2018-01-01 15:00:00
# 2   2018-01-03 15:00:00
# 3   2018-01-04 03:00:00
# Name: date, dtype: datetime64[ns]

print(pd.to_datetime(df['date'], utc=True))
# 0   2018-01-01 03:00:00+00:00
# 1   2018-01-01 15:00:00+00:00
# 2   2018-01-03 15:00:00+00:00
# 3   2018-01-04 03:00:00+00:00
# Name: date, dtype: datetime64[ns, UTC]

# print(pd.to_datetime(df['date'], utc=True).tz_convert('Asia/Tokyo'))
# TypeError: index is not a valid DatetimeIndex or PeriodIndex

df_ts = df.set_index('date')

print(df_ts)
#                         value
# date                         
# 2018-01-01T12:00+09:00      0
# 2018-01-02T00:00+09:00      1
# 2018-01-03T10:00-05:00      2
# 2018-01-03T19:00-08:00      3

print(df_ts.index)
# Index(['2018-01-01T12:00+09:00', '2018-01-02T00:00+09:00',
#        '2018-01-03T10:00-05:00', '2018-01-03T19:00-08:00'],
#       dtype='object', name='date')

print(pd.to_datetime(df_ts.index, utc=True))
# DatetimeIndex(['2018-01-01 03:00:00+00:00', '2018-01-01 15:00:00+00:00',
#                '2018-01-03 15:00:00+00:00', '2018-01-04 03:00:00+00:00'],
#               dtype='datetime64[ns, UTC]', name='date', freq=None)

print(pd.to_datetime(df_ts.index, utc=True).tz_convert('Asia/Tokyo'))
# DatetimeIndex(['2018-01-01 12:00:00+09:00', '2018-01-02 00:00:00+09:00',
#                '2018-01-04 00:00:00+09:00', '2018-01-04 12:00:00+09:00'],
#               dtype='datetime64[ns, Asia/Tokyo]', name='date', freq=None)

print(pd.to_datetime(df_ts.index, utc=True).tz_convert('Asia/Tokyo').tz_localize(None))
# DatetimeIndex(['2018-01-01 12:00:00', '2018-01-02 00:00:00',
#                '2018-01-04 00:00:00', '2018-01-04 12:00:00'],
#               dtype='datetime64[ns]', name='date', freq=None)

df_ts.index = pd.to_datetime(df_ts.index, utc=True).tz_convert('Asia/Tokyo').tz_localize(None)

print(df_ts)
#                      value
# date                      
# 2018-01-01 12:00:00      0
# 2018-01-02 00:00:00      1
# 2018-01-04 00:00:00      2
# 2018-01-04 12:00:00      3

print(df_ts.index)
# DatetimeIndex(['2018-01-01 12:00:00', '2018-01-02 00:00:00',
#                '2018-01-04 00:00:00', '2018-01-04 12:00:00'],
#               dtype='datetime64[ns]', name='date', freq=None)

print(df_ts['2018-01-04'])
#                      value
# date                      
# 2018-01-04 00:00:00      2
# 2018-01-04 12:00:00      3
