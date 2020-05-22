import warnings

warnings.simplefilter('ignore', FutureWarning)

import datetime

import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

with open('data/temp/alpha_vantage_api_key.txt') as f:
    api_key = f.read()

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime(2019, 12, 31)

df_sne = web.DataReader('SNE', 'av-daily', start, end, api_key=api_key)
print(df_sne)
#              open    high    low  close   volume
# 2015-01-02  20.47  20.685  20.43  20.56  1229939
# 2015-01-05  20.45  20.450  20.21  20.26  1083137
# 2015-01-06  20.46  20.580  20.15  20.25  2209124
# 2015-01-07  21.59  21.700  21.47  21.53  2486293
# 2015-01-08  21.53  21.620  21.47  21.56  1296471
# ...           ...     ...    ...    ...      ...
# 2019-12-24  67.98  68.000  67.76  67.76   264463
# 2019-12-26  68.00  68.030  67.85  68.02   517975
# 2019-12-27  68.03  68.100  67.73  67.78   351118
# 2019-12-30  67.78  67.790  67.25  67.72   993865
# 2019-12-31  67.72  68.025  67.51  68.00   549672
# 
# [1258 rows x 5 columns]

df_aapl = web.DataReader('AAPL', 'av-daily', start, end, api_key=api_key)
print(df_aapl)
#               open    high       low   close    volume
# 2015-01-02  111.39  111.44  107.3500  109.33  53204626
# 2015-01-05  108.29  108.65  105.4100  106.25  64285491
# 2015-01-06  106.54  107.43  104.6300  106.26  65797116
# 2015-01-07  107.20  108.20  106.6950  107.75  40105934
# 2015-01-08  109.23  112.15  108.7000  111.89  59364547
# ...            ...     ...       ...     ...       ...
# 2019-12-24  284.69  284.89  282.9197  284.27  12119714
# 2019-12-26  284.82  289.98  284.7000  289.91  23334004
# 2019-12-27  291.12  293.97  288.1200  289.80  36592936
# 2019-12-30  289.46  292.69  285.2200  291.52  36059614
# 2019-12-31  289.93  293.68  289.5200  293.65  25247625
# 
# [1258 rows x 5 columns]

df_sne_aapl = pd.DataFrame({'SNE': df_sne['close'], 'AAPL': df_aapl['close']})
print(df_sne_aapl)
#               SNE    AAPL
# 2015-01-02  20.56  109.33
# 2015-01-05  20.26  106.25
# 2015-01-06  20.25  106.26
# 2015-01-07  21.53  107.75
# 2015-01-08  21.56  111.89
# ...           ...     ...
# 2019-12-24  67.76  284.27
# 2019-12-26  68.02  289.91
# 2019-12-27  67.78  289.80
# 2019-12-30  67.72  291.52
# 2019-12-31  68.00  293.65
# 
# [1258 rows x 2 columns]

df_sne.to_csv('data/src/sne_2015_2019.csv')
df_aapl.to_csv('data/src/aapl_2015_2019.csv')
df_sne_aapl.to_csv('data/src/sne_aapl_2015_2019.csv')

print(type(df_sne_aapl.index))
# <class 'pandas.core.indexes.base.Index'>

df_sne_aapl.index = pd.to_datetime(df_sne_aapl.index)
print(type(df_sne_aapl.index))
# <class 'pandas.core.indexes.datetimes.DatetimeIndex'>

df_sne_aapl.plot(title='SNE vs. AAPL', grid=True)
# plt.show()
plt.savefig('data/dst/pandas_datareader_stock.png')
plt.close()

# ![SNE vs. AAPL](data/dst/pandas_datareader_stock.png)

df_sne_aapl['SNE'] /= df_sne_aapl['SNE'][0]
df_sne_aapl['AAPL'] /= df_sne_aapl['AAPL'][0]

df_sne_aapl.plot(title='SNE vs. AAPL', grid=True)
plt.savefig('data/dst/pandas_datareader_stock_normalize.png')
plt.close()

# ![SNE vs. AAPL normalize](data/dst/pandas_datareader_stock_normalize.png)
