import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mpl_finance

df = web.DataReader('AAPL', 'iex', '2017-01-01', '2017-12-31')

df.index = pd.to_datetime(df.index)

print(df.shape)
# (251, 5)

print(df.head())
#                 open      high       low     close    volume
# date                                                        
# 2017-01-03  112.6732  113.1889  111.6613  113.0138  28781865
# 2017-01-04  112.7219  113.3641  112.6246  112.8873  21118116
# 2017-01-05  112.7900  113.7087  112.6830  113.4614  22193587
# 2017-01-06  113.6268  114.9695  113.3251  114.7263  31751900
# 2017-01-09  114.7652  116.2052  114.7554  115.7771  33561948

print(df.tail())
#                 open      high       low     close    volume
# date                                                        
# 2017-12-22  172.6967  173.4323  172.5188  173.0230  16349444
# 2017-12-26  168.8608  169.5232  167.7525  168.6334  33185536
# 2017-12-27  168.1687  168.8410  167.7831  168.6630  21498213
# 2017-12-28  169.0585  169.8988  168.5444  169.1376  16480187
# 2017-12-29  168.5839  168.6531  167.2987  167.3086  25999922

df_ = df.copy()

df_.index = mdates.date2num(df_.index)
data = df_.reset_index().values

print(data)
# [[7.3633200e+05 1.1267320e+02 1.1318890e+02 1.1166130e+02 1.1301380e+02
#   2.8781865e+07]
#  [7.3633300e+05 1.1272190e+02 1.1336410e+02 1.1262460e+02 1.1288730e+02
#   2.1118116e+07]
#  [7.3633400e+05 1.1279000e+02 1.1370870e+02 1.1268300e+02 1.1346140e+02
#   2.2193587e+07]
#  ...
#  [7.3669000e+05 1.6816870e+02 1.6884100e+02 1.6778310e+02 1.6866300e+02
#   2.1498213e+07]
#  [7.3669100e+05 1.6905850e+02 1.6989880e+02 1.6854440e+02 1.6913760e+02
#   1.6480187e+07]
#  [7.3669200e+05 1.6858390e+02 1.6865310e+02 1.6729870e+02 1.6730860e+02
#   2.5999922e+07]]

print(data.shape)
# (251, 6)

fig = plt.figure(figsize=(12, 4))
ax = fig.add_subplot(1, 1, 1)

mpl_finance.candlestick_ohlc(ax, data, width=2, alpha=0.5, colorup='r', colordown='b')

ax.grid()

locator = mdates.AutoDateLocator()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(mdates.AutoDateFormatter(locator))

plt.savefig('data/dst/candlestick_day.png')

plt.close()

fig = plt.figure(figsize=(12, 4))
ax = fig.add_subplot(1, 1, 1)

mpl_finance.candlestick_ohlc(ax, data, width=2, alpha=0.5, colorup='r', colordown='b')

ax.grid()

ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m'))

plt.savefig('data/dst/candlestick_day_format.png')

plt.close()

d_ohlcv = {'open': 'first',
           'high': 'max',
           'low': 'min',
           'close': 'last',
           'volume': 'sum'}

df_w = df.resample('W-MON', closed='left', label='left').agg(d_ohlcv).copy()

df_w.index = mdates.date2num(df_w.index)
data_w = df_w.reset_index().values

fig = plt.figure(figsize=(12, 4))
ax = fig.add_subplot(1, 1, 1)

mpl_finance.candlestick_ohlc(ax, data_w, width=4, alpha=0.75, colorup='r', colordown='b')

ax.grid()

locator = mdates.AutoDateLocator()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(mdates.AutoDateFormatter(locator))

plt.savefig('data/dst/candlestick_week.png')

plt.close()

fig = plt.figure(figsize=(12, 4))
ax = fig.add_subplot(1, 1, 1)

mpl_finance.candlestick_ohlc(ax, data_w, width=4, alpha=0.75, colorup='r', colordown='b')
ax.plot(df_w.index, df_w['close'].rolling(4).mean())
ax.plot(df_w.index, df_w['close'].rolling(13).mean())
ax.plot(df_w.index, df_w['close'].rolling(26).mean())

ax.grid()

locator = mdates.AutoDateLocator()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(mdates.AutoDateFormatter(locator))

plt.savefig('data/dst/candlestick_week_sma.png')

plt.close()

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 4), sharex=True,
                         gridspec_kw={'height_ratios': [3, 1]})

mpl_finance.candlestick_ohlc(axes[0], data_w, width=4, alpha=0.75, colorup='r', colordown='b')

axes[1].bar(df_w.index, df_w['volume'], width=4, color='navy')

axes[0].grid()
axes[1].grid()

locator = mdates.AutoDateLocator()
axes[0].xaxis.set_major_locator(locator)
axes[0].xaxis.set_major_formatter(mdates.AutoDateFormatter(locator))

plt.savefig('data/dst/candlestick_week_v.png')

plt.close()

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 4), sharex=True,
                         gridspec_kw={'height_ratios': [3, 1]})

mpl_finance.candlestick_ohlc(axes[0], data_w, width=4, alpha=0.75, colorup='r', colordown='b')
axes[0].plot(df_w.index, df_w['close'].rolling(4).mean())
axes[0].plot(df_w.index, df_w['close'].rolling(13).mean())
axes[0].plot(df_w.index, df_w['close'].rolling(26).mean())

axes[1].bar(df_w.index, df_w['volume'], width=4, color='navy')

axes[0].grid()
axes[1].grid()

locator = mdates.AutoDateLocator()
axes[0].xaxis.set_major_locator(locator)
axes[0].xaxis.set_major_formatter(mdates.AutoDateFormatter(locator))

plt.savefig('data/dst/candlestick_week_sma_v.png')

plt.close()
