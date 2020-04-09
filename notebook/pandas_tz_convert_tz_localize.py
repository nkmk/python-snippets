import pandas as pd

s = '2018-01-01T12:00+09:00'
print(s)
# 2018-01-01T12:00+09:00

print(type(s))
# <class 'str'>

ts = pd.to_datetime(s)
print(ts)
# 2018-01-01 12:00:00+09:00

print(type(ts))
# <class 'pandas._libs.tslibs.timestamps.Timestamp'>

print(ts.tz)
# pytz.FixedOffset(540)

ts_utc = pd.to_datetime(s, utc=True)
print(ts_utc)
# 2018-01-01 03:00:00+00:00

print(ts_utc.tz)
# UTC

s_without_tz = '2018-01-01T12:00'

ts_naive = pd.to_datetime(s_without_tz)
print(ts_naive)
# 2018-01-01 12:00:00

print(ts_naive.tz)
# None

ts_set_utc = pd.to_datetime(s_without_tz, utc=True)
print(ts_set_utc)
# 2018-01-01 12:00:00+00:00

print(ts_set_utc.tz)
# UTC

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

print(ts_utc.tz_convert('America/Vancouver'))
# 2017-12-31 19:00:00-08:00

print(ts_naive)
# 2018-01-01 12:00:00

print(ts_naive.tz)
# None

# print(ts_naive.tz_convert('Asia/Tokyo'))
# TypeError: Cannot convert tz-naive Timestamp, use tz_localize to localize

ts_jst_localize = ts_naive.tz_localize('Asia/Tokyo')
print(ts_jst_localize)
# 2018-01-01 12:00:00+09:00

print(ts_jst_localize.tz)
# Asia/Tokyo

print(ts_naive.tz_localize('US/Pacific'))
# 2018-01-01 12:00:00-08:00

print(ts_naive.tz_localize('Asia/Tokyo') == ts_naive.tz_localize('US/Pacific'))
# False

print(ts_jst)
# 2018-01-01 12:00:00+09:00

print(ts_jst.tz)
# Asia/Tokyo

# print(ts_jst.tz_localize('US/Pacific'))
# TypeError: Cannot localize tz-aware Timestamp, use tz_convert for conversions

print(ts_jst)
# 2018-01-01 12:00:00+09:00

print(ts_jst.tz)
# Asia/Tokyo

print(ts_jst.tz_convert(None))
# 2018-01-01 03:00:00

print(ts_jst.tz_localize(None))
# 2018-01-01 12:00:00

df = pd.DataFrame({'date': ['2018-01-01T12:00',
                            '2018-01-02T00:00',
                            '2018-01-03T10:00',
                            '2018-01-03T19:00'],
                   'value': ['A', 'B', 'C', 'D']})

print(df)
#                date value
# 0  2018-01-01T12:00     A
# 1  2018-01-02T00:00     B
# 2  2018-01-03T10:00     C
# 3  2018-01-03T19:00     D

s_naive = pd.to_datetime(df['date'])
print(s_naive)
# 0   2018-01-01 12:00:00
# 1   2018-01-02 00:00:00
# 2   2018-01-03 10:00:00
# 3   2018-01-03 19:00:00
# Name: date, dtype: datetime64[ns]

print(s_naive[0])
# 2018-01-01 12:00:00

print(type(s_naive[0]))
# <class 'pandas._libs.tslibs.timestamps.Timestamp'>

print(s_naive[0].tz)
# None

s_utc = pd.to_datetime(df['date'], utc=True)
print(s_utc)
# 0   2018-01-01 12:00:00+00:00
# 1   2018-01-02 00:00:00+00:00
# 2   2018-01-03 10:00:00+00:00
# 3   2018-01-03 19:00:00+00:00
# Name: date, dtype: datetime64[ns, UTC]

print(s_utc[0].tz)
# UTC

# print(s_naive.tz_localize('Asia/Tokyo'))
# TypeError: index is not a valid DatetimeIndex or PeriodIndex

# print(s_utc.tz_convert('Asia/Tokyo'))
# TypeError: index is not a valid DatetimeIndex or PeriodIndex

print(s_naive.dt.tz_localize('Asia/Tokyo'))
# 0   2018-01-01 12:00:00+09:00
# 1   2018-01-02 00:00:00+09:00
# 2   2018-01-03 10:00:00+09:00
# 3   2018-01-03 19:00:00+09:00
# Name: date, dtype: datetime64[ns, Asia/Tokyo]

print(s_utc.dt.tz_convert('Asia/Tokyo'))
# 0   2018-01-01 21:00:00+09:00
# 1   2018-01-02 09:00:00+09:00
# 2   2018-01-03 19:00:00+09:00
# 3   2018-01-04 04:00:00+09:00
# Name: date, dtype: datetime64[ns, Asia/Tokyo]

# print(s_naive.dt.tz_convert('Asia/Tokyo'))
# TypeError: Cannot convert tz-naive timestamps, use tz_localize to localize

# print(s_utc.dt.tz_localize('Asia/Tokyo'))
# TypeError: Already tz-aware, use tz_convert to convert.

# print(df['date'].dt.tz_localize('Asia/Tokyo'))
# AttributeError: Can only use .dt accessor with datetimelike values

df['date'] = pd.to_datetime(df['date'])
df_ts = df.set_index('date')
print(df_ts)
#                     value
# date                     
# 2018-01-01 12:00:00     A
# 2018-01-02 00:00:00     B
# 2018-01-03 10:00:00     C
# 2018-01-03 19:00:00     D

print(df_ts.index)
# DatetimeIndex(['2018-01-01 12:00:00', '2018-01-02 00:00:00',
#                '2018-01-03 10:00:00', '2018-01-03 19:00:00'],
#               dtype='datetime64[ns]', name='date', freq=None)

print(type(df_ts.index))
# <class 'pandas.core.indexes.datetimes.DatetimeIndex'>

print(df_ts['2018-01-03'])
#                     value
# date                     
# 2018-01-03 10:00:00     C
# 2018-01-03 19:00:00     D

print(df_ts.index.tz_localize('Asia/Tokyo'))
# DatetimeIndex(['2018-01-01 12:00:00+09:00', '2018-01-02 00:00:00+09:00',
#                '2018-01-03 10:00:00+09:00', '2018-01-03 19:00:00+09:00'],
#               dtype='datetime64[ns, Asia/Tokyo]', name='date', freq=None)

print(df_ts.tz_localize('Asia/Tokyo'))
#                           value
# date                           
# 2018-01-01 12:00:00+09:00     A
# 2018-01-02 00:00:00+09:00     B
# 2018-01-03 10:00:00+09:00     C
# 2018-01-03 19:00:00+09:00     D

s_ts = df_ts['value']
print(s_ts)
# date
# 2018-01-01 12:00:00    A
# 2018-01-02 00:00:00    B
# 2018-01-03 10:00:00    C
# 2018-01-03 19:00:00    D
# Name: value, dtype: object

print(s_ts.tz_localize('Asia/Tokyo'))
# date
# 2018-01-01 12:00:00+09:00    A
# 2018-01-02 00:00:00+09:00    B
# 2018-01-03 10:00:00+09:00    C
# 2018-01-03 19:00:00+09:00    D
# Name: value, dtype: object

df = pd.DataFrame({'date': ['2018-01-01T12:00+09:00',
                            '2018-01-02T00:00+09:00',
                            '2018-01-03T10:00+09:00',
                            '2018-01-03T19:00+09:00'],
                   'value': ['A', 'B', 'C', 'D']})

print(df)
#                      date value
# 0  2018-01-01T12:00+09:00     A
# 1  2018-01-02T00:00+09:00     B
# 2  2018-01-03T10:00+09:00     C
# 3  2018-01-03T19:00+09:00     D

print(pd.to_datetime(df['date']))
# 0   2018-01-01 12:00:00+09:00
# 1   2018-01-02 00:00:00+09:00
# 2   2018-01-03 10:00:00+09:00
# 3   2018-01-03 19:00:00+09:00
# Name: date, dtype: datetime64[ns, pytz.FixedOffset(540)]

print(pd.to_datetime(df['date'], utc=True))
# 0   2018-01-01 03:00:00+00:00
# 1   2018-01-01 15:00:00+00:00
# 2   2018-01-03 01:00:00+00:00
# 3   2018-01-03 10:00:00+00:00
# Name: date, dtype: datetime64[ns, UTC]

print(pd.to_datetime(df['date']).dt.tz_convert('US/Pacific'))
# 0   2017-12-31 19:00:00-08:00
# 1   2018-01-01 07:00:00-08:00
# 2   2018-01-02 17:00:00-08:00
# 3   2018-01-03 02:00:00-08:00
# Name: date, dtype: datetime64[ns, US/Pacific]

df['date'] = pd.to_datetime(df['date'])
df_ts = df.set_index('date')
print(df_ts)
#                           value
# date                           
# 2018-01-01 12:00:00+09:00     A
# 2018-01-02 00:00:00+09:00     B
# 2018-01-03 10:00:00+09:00     C
# 2018-01-03 19:00:00+09:00     D

print(df_ts.index)
# DatetimeIndex(['2018-01-01 12:00:00+09:00', '2018-01-02 00:00:00+09:00',
#                '2018-01-03 10:00:00+09:00', '2018-01-03 19:00:00+09:00'],
#               dtype='datetime64[ns, pytz.FixedOffset(540)]', name='date', freq=None)

print(df_ts.tz_convert('US/Pacific'))
#                           value
# date                           
# 2017-12-31 19:00:00-08:00     A
# 2018-01-01 07:00:00-08:00     B
# 2018-01-02 17:00:00-08:00     C
# 2018-01-03 02:00:00-08:00     D

df = pd.DataFrame({'date': ['2018-01-01T12:00+09:00',
                            '2018-01-02T00:00+09:00',
                            '2018-01-03T10:00-05:00',
                            '2018-01-03T19:00-08:00'],
                   'value': ['A', 'B', 'C', 'D']})

print(df)
#                      date value
# 0  2018-01-01T12:00+09:00     A
# 1  2018-01-02T00:00+09:00     B
# 2  2018-01-03T10:00-05:00     C
# 3  2018-01-03T19:00-08:00     D

print(pd.to_datetime(df['date']))
# 0    2018-01-01 12:00:00+09:00
# 1    2018-01-02 00:00:00+09:00
# 2    2018-01-03 10:00:00-05:00
# 3    2018-01-03 19:00:00-08:00
# Name: date, dtype: object

print(type(pd.to_datetime(df['date'])[0]))
# <class 'datetime.datetime'>

print(pd.to_datetime(df['date'])[0].tzinfo)
# tzoffset(None, 32400)

print(pd.to_datetime(df['date'])[2].tzinfo)
# tzoffset(None, -18000)

print(pd.to_datetime(df['date'], utc=True))
# 0   2018-01-01 03:00:00+00:00
# 1   2018-01-01 15:00:00+00:00
# 2   2018-01-03 15:00:00+00:00
# 3   2018-01-04 03:00:00+00:00
# Name: date, dtype: datetime64[ns, UTC]

print(type(pd.to_datetime(df['date'], utc=True)[0]))
# <class 'pandas._libs.tslibs.timestamps.Timestamp'>

# print(pd.to_datetime(df['date']).dt.tz_convert('Asia/Tokyo'))
# ValueError: Tz-aware datetime.datetime cannot be converted to datetime64 unless utc=True

df['date'] = pd.to_datetime(df['date'])
df_dt = df.set_index('date')
print(df_dt)
#                           value
# date                           
# 2018-01-01 12:00:00+09:00     A
# 2018-01-02 00:00:00+09:00     B
# 2018-01-03 10:00:00-05:00     C
# 2018-01-03 19:00:00-08:00     D

print(df_dt.index)
# Index([2018-01-01 12:00:00+09:00, 2018-01-02 00:00:00+09:00,
#        2018-01-03 10:00:00-05:00, 2018-01-03 19:00:00-08:00],
#       dtype='object', name='date')

# print(df_dt.tz_convert('Asia/Tokyo'))
# TypeError: index is not a valid DatetimeIndex or PeriodIndex

# print(df_dt.tz_localize('Asia/Tokyo'))
# TypeError: index is not a valid DatetimeIndex or PeriodIndex
