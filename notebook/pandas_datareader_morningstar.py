import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

start = datetime.datetime(2012, 1, 1)
end = datetime.datetime(2017, 12, 31)

f = web.DataReader('SNE', 'morningstar', start, end)

print(f.head())
#                    Close   High    Low   Open   Volume
# Symbol Date                                           
# SNE    2012-01-02  18.04  18.04  18.04  18.04        0
#        2012-01-03  18.38  18.50  18.28  18.28  1414748
#        2012-01-04  18.22  18.27  18.14  18.24  1146367
#        2012-01-05  17.70  17.85  17.60  17.83  1464843
#        2012-01-06  17.44  17.57  17.37  17.57   594057

f2 = web.DataReader(['SNE', 'AAPL'], 'morningstar', start, end)

print(type(f2.index))
print(f2.head())
print(f2.tail())
# <class 'pandas.core.indexes.multi.MultiIndex'>
#                    Close   High    Low   Open   Volume
# Symbol Date                                           
# SNE    2012-01-02  18.04  18.04  18.04  18.04        0
#        2012-01-03  18.38  18.50  18.28  18.28  1414748
#        2012-01-04  18.22  18.27  18.14  18.24  1146367
#        2012-01-05  17.70  17.85  17.60  17.83  1464843
#        2012-01-06  17.44  17.57  17.37  17.57   594057
#                     Close    High      Low    Open    Volume
# Symbol Date                                                 
# AAPL   2017-12-25  175.01  175.01  175.010  175.01         0
#        2017-12-26  170.57  171.47  169.679  170.80  33185536
#        2017-12-27  170.60  170.78  169.710  170.10  21498213
#        2017-12-28  171.08  171.85  170.480  171.00  16480187
#        2017-12-29  169.23  170.59  169.220  170.52  25999922

f2_u = f2.unstack(0)
print(f2_u.head())
#               Close            High             Low            Open         \
# Symbol         AAPL    SNE     AAPL    SNE     AAPL    SNE     AAPL    SNE   
# Date                                                                         
# 2012-01-02  57.8571  18.04  57.8571  18.04  57.8571  18.04  57.8571  18.04   
# 2012-01-03  58.7471  18.38  58.9286  18.50  58.4286  18.28  58.5000  18.28   
# 2012-01-04  59.0629  18.22  59.2400  18.27  58.4686  18.14  58.6000  18.24   
# 2012-01-05  59.7186  17.70  59.7929  17.85  58.9529  17.60  59.2786  17.83   
# 2012-01-06  60.3429  17.44  60.3929  17.57  59.8886  17.37  59.9671  17.57   
#               Volume           
# Symbol          AAPL      SNE  
# Date                           
# 2012-01-02         0        0  
# 2012-01-03  75564699  1414748  
# 2012-01-04  65061108  1146367  
# 2012-01-05  67816805  1464843  
# 2012-01-06  79596412   594057  

print(f2_u['Close'].head())
# Symbol         AAPL    SNE
# Date                      
# 2012-01-02  57.8571  18.04
# 2012-01-03  58.7471  18.38
# 2012-01-04  59.0629  18.22
# 2012-01-05  59.7186  17.70
# 2012-01-06  60.3429  17.44

f2_u['Close'].plot(title='SNE vs AAPL', grid=True)
# plt.show()
plt.savefig('data/dst/pandas_datareader_morningstar.png')

f2_u['Close', 'AAPL'] /= f2_u['Close'].loc[f2_u.index[0], 'AAPL']
f2_u['Close', 'SNE'] /= f2_u['Close'].loc[f2_u.index[0], 'SNE']

f2_u['Close'].plot(title='SNE vs AAPL', grid=True)
# plt.show()
plt.savefig('data/dst/pandas_datareader_morningstar_normalize.png')
