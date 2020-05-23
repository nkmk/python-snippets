import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mpl_finance

df_org = pd.read_csv('data/src/aapl_2015_2019.csv', index_col=0, parse_dates=True)['2017']
print(df_org)
#               open      high      low   close    volume
# 2017-01-03  115.80  116.3300  114.760  116.15  28781865
# 2017-01-04  115.85  116.5100  115.750  116.02  21118116
# 2017-01-05  115.92  116.8642  115.810  116.61  22193587
# 2017-01-06  116.78  118.1600  116.470  117.91  31751900
# 2017-01-09  117.95  119.4300  117.940  118.99  33561948
# ...            ...       ...      ...     ...       ...
# 2017-12-22  174.68  175.4240  174.500  175.01  16052615
# 2017-12-26  170.80  171.4700  169.679  170.57  32968167
# 2017-12-27  170.10  170.7800  169.710  170.60  21672062
# 2017-12-28  171.00  171.8500  170.480  171.08  15997739
# 2017-12-29  170.52  170.5900  169.220  169.23  25643711
# 
# [251 rows x 5 columns]

df = df_org.copy()

df.index = mdates.date2num(df.index)
data = df.reset_index().values
print(type(data))
# <class 'numpy.ndarray'>

print(data.shape)
# (251, 6)

print(data)
# [[7.3633200e+05 1.1580000e+02 1.1633000e+02 1.1476000e+02 1.1615000e+02
#   2.8781865e+07]
#  [7.3633300e+05 1.1585000e+02 1.1651000e+02 1.1575000e+02 1.1602000e+02
#   2.1118116e+07]
#  [7.3633400e+05 1.1592000e+02 1.1686420e+02 1.1581000e+02 1.1661000e+02
#   2.2193587e+07]
#  ...
#  [7.3669000e+05 1.7010000e+02 1.7078000e+02 1.6971000e+02 1.7060000e+02
#   2.1672062e+07]
#  [7.3669100e+05 1.7100000e+02 1.7185000e+02 1.7048000e+02 1.7108000e+02
#   1.5997739e+07]
#  [7.3669200e+05 1.7052000e+02 1.7059000e+02 1.6922000e+02 1.6923000e+02
#   2.5643711e+07]]

fig = plt.figure(figsize=(12, 4))
ax = fig.add_subplot(1, 1, 1)

mpl_finance.candlestick_ohlc(ax, data, width=2, alpha=0.5, colorup='r', colordown='b')

ax.grid()

locator = mdates.AutoDateLocator()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(mdates.AutoDateFormatter(locator))

plt.savefig('data/dst/candlestick_day.png')

plt.close()

# ![](data/dst/candlestick_day.png)

fig = plt.figure(figsize=(12, 4))
ax = fig.add_subplot(1, 1, 1)

mpl_finance.candlestick_ohlc(ax, data, width=2, alpha=0.5, colorup='r', colordown='b')

ax.grid()

ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m'))

plt.savefig('data/dst/candlestick_day_format.png')

plt.close()

# ![](data/dst/candlestick_day_format.png)

d_ohlcv = {'open': 'first',
           'high': 'max',
           'low': 'min',
           'close': 'last',
           'volume': 'sum'}

df_w = df_org.resample('W-MON', closed='left', label='left').agg(d_ohlcv)

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

# ![](data/dst/candlestick_week.png)

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

# ![](data/dst/candlestick_week_sma.png)

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

# ![](data/dst/candlestick_week_v.png)

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

# ![](data/dst/candlestick_week_sma_v.png)
