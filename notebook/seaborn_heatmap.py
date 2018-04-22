# %matplotlib inline

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

list_2d = [[0, 1, 2], [3, 4, 5]]

plt.figure()
sns.heatmap(list_2d)
plt.savefig('data/dst/seaborn_heatmap_list.png')
plt.close('all')

arr_2d = np.arange(-8, 8).reshape((4, 4))
print(arr_2d)
# [[-8 -7 -6 -5]
#  [-4 -3 -2 -1]
#  [ 0  1  2  3]
#  [ 4  5  6  7]]

plt.figure()
sns.heatmap(arr_2d)
plt.savefig('data/dst/seaborn_heatmap_ndarray.png')

df = pd.DataFrame(data=arr_2d, index=['a', 'b', 'c', 'd'], columns=['A', 'B', 'C', 'D'])
print(df)
#    A  B  C  D
# a -8 -7 -6 -5
# b -4 -3 -2 -1
# c  0  1  2  3
# d  4  5  6  7

plt.figure()
sns.heatmap(df)
plt.savefig('data/dst/seaborn_heatmap_dataframe.png')

print(type(sns.heatmap(list_2d)))
# <class 'matplotlib.axes._subplots.AxesSubplot'>

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
sns.heatmap(list_2d, ax=ax)
fig.savefig('data/dst/seaborn_heatmap_list.png')

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(8, 6))
sns.heatmap(list_2d, ax=axes[0, 0])
sns.heatmap(arr_2d, ax=axes[1, 2])
fig.savefig('data/dst/seaborn_heatmap_list_sub.png')

plt.figure()
sns.heatmap(df, annot=True)
plt.savefig('data/dst/seaborn_heatmap_annot.png')

plt.figure()
sns.heatmap(df, cbar=False)
plt.savefig('data/dst/seaborn_heatmap_no_cbar.png')

plt.figure()
sns.heatmap(df, square=True)
plt.savefig('data/dst/seaborn_heatmap_square.png')

plt.figure()
sns.heatmap(df, vmax=10, vmin=-10, center=0)
plt.savefig('data/dst/seaborn_heatmap_vmax_vmin_center.png')

plt.figure()
sns.heatmap(df, cmap='hot')
plt.savefig('data/dst/seaborn_heatmap_hot.png')

plt.figure()
sns.heatmap(df, cmap='Blues')
plt.savefig('data/dst/seaborn_heatmap_blues.png')

plt.figure()
sns.heatmap(df, cmap='Blues_r')
plt.savefig('data/dst/seaborn_heatmap_blues_r.png')

current_figsize = mpl.rcParams['figure.figsize']
print(current_figsize)
# [6.0, 4.0]

plt.figure(figsize=(9, 6)) 
sns.heatmap(df, square=True)
plt.savefig('data/dst/seaborn_heatmap_big.png')

current_dpi = mpl.rcParams['figure.dpi']
print(current_dpi)
# 72.0

plt.figure()
sns.heatmap(df, square=True)
plt.savefig('data/dst/seaborn_heatmap_big_2.png', dpi=current_dpi * 1.5)

df_house = pd.read_csv('data/src/house_prices_train.csv', index_col=0)

df_house_corr = df_house.corr()
print(df_house_corr.shape)
# (37, 37)

print(df_house_corr.head())
#              MSSubClass  LotFrontage   LotArea  OverallQual  OverallCond  \
# MSSubClass     1.000000    -0.386347 -0.139781     0.032628    -0.059316   
# LotFrontage   -0.386347     1.000000  0.426095     0.251646    -0.059213   
# LotArea       -0.139781     0.426095  1.000000     0.105806    -0.005636   
# OverallQual    0.032628     0.251646  0.105806     1.000000    -0.091932   
# OverallCond   -0.059316    -0.059213 -0.005636    -0.091932     1.000000   
#              YearBuilt  YearRemodAdd  MasVnrArea  BsmtFinSF1  BsmtFinSF2  \
# MSSubClass    0.027850      0.040581    0.022936   -0.069836   -0.065649   
# LotFrontage   0.123349      0.088866    0.193458    0.233633    0.049900   
# LotArea       0.014228      0.013788    0.104160    0.214103    0.111170   
# OverallQual   0.572323      0.550684    0.411876    0.239666   -0.059119   
# OverallCond  -0.375983      0.073741   -0.128101   -0.046231    0.040229   
#                ...      WoodDeckSF  OpenPorchSF  EnclosedPorch  3SsnPorch  \
# MSSubClass     ...       -0.012579    -0.006100      -0.012037  -0.043825   
# LotFrontage    ...        0.088521     0.151972       0.010700   0.070029   
# LotArea        ...        0.171698     0.084774      -0.018340   0.020423   
# OverallQual    ...        0.238923     0.308819      -0.113937   0.030371   
# OverallCond    ...       -0.003334    -0.032589       0.070356   0.025504   
#              ScreenPorch  PoolArea   MiscVal    MoSold    YrSold  SalePrice  
# MSSubClass     -0.026030  0.008283 -0.007683 -0.013585 -0.021407  -0.084284  
# LotFrontage     0.041383  0.206167  0.003368  0.011200  0.007450   0.351799  
# LotArea         0.043160  0.077672  0.038068  0.001205 -0.014261   0.263843  
# OverallQual     0.064886  0.065166 -0.031406  0.070815 -0.027347   0.790982  
# OverallCond     0.054811 -0.001985  0.068777 -0.003511  0.043950  -0.077856  
# [5 rows x 37 columns]

plt.figure(figsize=(12, 9)) 
sns.heatmap(df_house_corr, square=True, vmax=1, vmin=-1, center=0)
plt.savefig('data/dst/seaborn_heatmap_house_price.png')
