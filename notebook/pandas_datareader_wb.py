import warnings

warnings.simplefilter('ignore', FutureWarning)

from pandas_datareader import wb
import matplotlib.pyplot as plt

df = wb.download(indicator='SP.POP.TOTL', country=['JP', 'US'],
                 start=1960, end=2014)
print(df)
#                     SP.POP.TOTL
# country       year             
# Japan         2014    127276000
#               2013    127445000
#               2012    127629000
#               2011    127833000
#               2010    128070000
# ...                         ...
# United States 1964    191889000
#               1963    189242000
#               1962    186538000
#               1961    183691000
#               1960    180671000
# 
# [110 rows x 1 columns]

df2 = df.unstack(level=0)
print(df2.head())
#         SP.POP.TOTL              
# country       Japan United States
# year                             
# 1960       92500572     180671000
# 1961       94943000     183691000
# 1962       95832000     186538000
# 1963       96812000     189242000
# 1964       97826000     191889000

print(df2.tail())
#         SP.POP.TOTL              
# country       Japan United States
# year                             
# 2010      128070000     309321666
# 2011      127833000     311556874
# 2012      127629000     313830990
# 2013      127445000     315993715
# 2014      127276000     318301008

print(df2.columns)
# MultiIndex([('SP.POP.TOTL',         'Japan'),
#             ('SP.POP.TOTL', 'United States')],
#            names=[None, 'country'])

df2.columns = ['Japan', 'United States']
print(df2.head())
#          Japan  United States
# year                         
# 1960  92500572      180671000
# 1961  94943000      183691000
# 1962  95832000      186538000
# 1963  96812000      189242000
# 1964  97826000      191889000

df2.plot(grid=True)
plt.savefig('data/dst/pandas_datareader_wb.png')
plt.close()

# ![pandas_datareader_wb.png](data/dst/pandas_datareader_wb.png)
