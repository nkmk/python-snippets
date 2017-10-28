import pandas_datareader.data as web
import datetime

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 12, 31)
f = web.DataReader('SNE', 'yahoo', start, end)
print(f)
#                  Open       High        Low      Close  Adj Close   Volume
# Date                                                                      
# 2010-01-04  29.520000  30.180000  29.500000  30.020000  30.020000   988800
# 2010-01-05  29.719999  29.930000  29.500000  29.879999  29.879999   567800
# 2010-01-06  29.879999  29.950001  29.660000  29.850000  29.850000   468200
# 2010-01-07  29.740000  29.870001  29.590000  29.799999  29.799999   645300
# 2010-01-08  30.040001  30.469999  29.930000  30.410000  30.410000   574100
# ...               ...        ...        ...        ...        ...      ...
# 2015-12-24  24.580000  24.780001  24.570000  24.700001  24.700001   467400
# 2015-12-28  24.709999  24.790001  24.530001  24.670000  24.670000   590100
# 2015-12-29  24.860001  24.900000  24.680000  24.830000  24.830000   657600
# 2015-12-30  24.780001  24.900000  24.700001  24.719999  24.719999   344900
# 2015-12-31  24.670000  24.770000  24.510000  24.610001  24.610001   688900
# [1511 rows x 6 columns]

f = web.DataReader(['SNE', 'AAPL'], 'yahoo', start, end)
print(f['Adj Close'])
#                   AAPL        SNE
# Date                             
# 2015-12-31  101.703697  24.610001
# 2015-12-30  103.694107  24.719999
# 2015-12-29  105.066116  24.830000
# 2015-12-28  103.210999  24.670000
# 2015-12-24  104.380112  24.700001
# ...                ...        ...
# 2010-01-08   27.244156  30.410000
# 2010-01-07   27.064222  29.799999
# 2010-01-06   27.114347  29.850000
# 2010-01-05   27.552608  29.879999
# 2010-01-04   27.505054  30.020000
# [1511 rows x 2 columns]

print(f)
# <class 'pandas.core.panel.Panel'>
# Dimensions: 6 (items) x 1511 (major_axis) x 2 (minor_axis)
# Items axis: Adj Close to Volume
# Major_axis axis: 2015-12-31 00:00:00 to 2009-12-31 00:00:00
# Minor_axis axis: AAPL to SNE

import matplotlib.pyplot as plt

f['Adj Close']['SNE'] /= f['Adj Close']['SNE'][-1]
f['Adj Close']['AAPL'] /= f['Adj Close']['AAPL'][-1]
f['Adj Close'].plot(title='SNE vs AAPL', grid=True)
# plt.show()
plt.savefig('data/dst/pandas-datareader-yahoo.png')

# ![pandas-datareader-yahoo.png](data/dst/pandas-datareader-yahoo.png)

from pandas_datareader import wb

f = wb.download(indicator='SP.POP.TOTL', country=['JP', 'US'],
                start=1960, end=2014)
print(f)
#                     SP.POP.TOTL
# country       year             
# Japan         2014    127276000
#               2013    127445000
#               2012    127629000
#               2011    127833000
#               2010    128070000
# ...                         ...
# United States 1989    246819000
#               1988    244499000
#               1987    242289000
# ...                         ...
#               1962    186538000
#               1961    183691000
#               1960    180671000
# [110 rows x 1 columns]

print(wb.search('gdp.*capita.*const').iloc[:, :2])
#                         id                                               name
# 685     6.0.GDPpc_constant  GDP per capita, PPP (constant 2011 internation...
# 8086        NY.GDP.PCAP.KD                 GDP per capita (constant 2010 US$)
# 8088        NY.GDP.PCAP.KN                      GDP per capita (constant LCU)
# 8090     NY.GDP.PCAP.PP.KD  GDP per capita, PPP (constant 2011 internation...
# 8091  NY.GDP.PCAP.PP.KD.87  GDP per capita, PPP (constant 1987 internation...

f = wb.download(indicator='SP.POP.TOTL', country=['JP', 'US'],
                start=1960, end=2014)
f2 = f.unstack(level=0)
print(f2)
#         SP.POP.TOTL              
# country       Japan United States
# year                             
# 1960       92500572     180671000
# 1961       94943000     183691000
# 1962       95832000     186538000
# 1963       96812000     189242000
# 1964       97826000     191889000
# ...                           ...
# 2010      128070000     309348193
# 2011      127833000     311663358
# 2012      127629000     313998379
# 2013      127445000     316204908
# 2014      127276000     318563456

f2.columns = ['Japan', 'United States']
f2.plot(grid=True)
# plt.show()
plt.savefig('data/dst/pandas-datareader-wb.png')

# ![pandas-datareader-wb.png](data/dst/pandas-datareader-wb.png)
