import pandas as pd
import mplfinance as mpf

df = pd.read_csv('data/src/aapl_2015_2019.csv', index_col=0, parse_dates=True)['2017']
print(df)
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

df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']

%%capture
mpf.plot(df, savefig='data/dst/candlestick_mpf.png')

# ![](data/dst/candlestick_mpf.png)

%%capture
mpf.plot(df[50:100], figratio=(12,4),
         savefig='data/dst/candlestick_mpf_figratio.png')

# ![](data/dst/candlestick_mpf_figratio.png)

%%capture
mpf.plot(df[50:100], type='candle', figratio=(12,4),
         savefig='data/dst/candlestick_mpf_candle.png')

# ![](data/dst/candlestick_mpf_candle.png)

%%capture
mpf.plot(df[50:100], type='candle', volume=True, figratio=(12,4),
         savefig='data/dst/candlestick_mpf_volume.png')

# ![](data/dst/candlestick_mpf_volume.png)

%%capture
mpf.plot(df[50:100], type='candle', volume=True, mav=(5, 25), figratio=(12,4),
         savefig='data/dst/candlestick_mpf_mav.png')

# ![](data/dst/candlestick_mpf_mav.png)

%%capture
mpf.plot(df[50:100], type='candle', figratio=(12,4),
         volume=True, mav=(5, 25), style='yahoo',
         savefig='data/dst/candlestick_mpf_style_yahoo.png')

# ![](data/dst/candlestick_mpf_style_yahoo.png)

d_ohlcv = {'Open': 'first',
           'High': 'max',
           'Low': 'min',
           'Close': 'last',
           'Volume': 'sum'}

df_w = df.resample('W-MON', closed='left', label='left').agg(d_ohlcv)
print(df_w.head())
#               Open    High     Low   Close     Volume
# 2017-01-02  115.80  118.16  114.76  117.91  103845468
# 2017-01-09  117.95  119.93  117.94  119.04  138810760
# 2017-01-16  118.34  120.50  118.22  120.00  116347987
# 2017-01-23  120.00  122.44  119.50  121.95  124748449
# 2017-01-30  120.93  130.49  120.62  129.08  249781248

%%capture
mpf.plot(df_w, type='candle', figratio=(12,4),
         volume=True, mav=(5, 25),
         savefig='data/dst/candlestick_mpf_week.png')

# ![](data/dst/candlestick_mpf_week.png)
