import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({'A': range(5),
                   'B': [x**2 for x in range(5)],
                   'C': [x**3 for x in range(5)]})

print(df)
#    A   B   C
# 0  0   0   0
# 1  1   1   1
# 2  2   4   8
# 3  3   9  27
# 4  4  16  64

df_corr = df.corr()
print(df_corr)
print(type(df_corr))
#           A         B         C
# A  1.000000  0.958927  0.905882
# B  0.958927  1.000000  0.987130
# C  0.905882  0.987130  1.000000
# <class 'pandas.core.frame.DataFrame'>

df['D'] = list('abcde')
df['E'] = [True, False, True, True, False]
print(df)
#    A   B   C  D      E
# 0  0   0   0  a   True
# 1  1   1   1  b  False
# 2  2   4   8  c   True
# 3  3   9  27  d   True
# 4  4  16  64  e  False

print(df.dtypes)
# A     int64
# B     int64
# C     int64
# D    object
# E      bool
# dtype: object

df_corr = df.corr()
print(df_corr)
#           A         B         C         E
# A  1.000000  0.958927  0.905882 -0.288675
# B  0.958927  1.000000  0.987130 -0.346023
# C  0.905882  0.987130  1.000000 -0.424522
# E -0.288675 -0.346023 -0.424522  1.000000

df_nan = df.copy()
df_nan.iloc[[2, 3, 4], 1] = np.nan
print(df_nan)
#    A    B   C  D      E
# 0  0  0.0   0  a   True
# 1  1  1.0   1  b  False
# 2  2  NaN   8  c   True
# 3  3  NaN  27  d   True
# 4  4  NaN  64  e  False

df_nan_corr = df_nan.corr()
print(df_nan_corr)
#           A    B         C         E
# A  1.000000  1.0  0.905882 -0.288675
# B  1.000000  1.0  1.000000 -1.000000
# C  0.905882  1.0  1.000000 -0.424522
# E -0.288675 -1.0 -0.424522  1.000000

sns.heatmap(df_corr, vmax=1, vmin=-1, center=0)
plt.savefig('data/dst/seaborn_heatmap_corr_example.png')

df_house = pd.read_csv('data/src/house_prices_train.csv', index_col=0)

print(df_house.shape)
# (1460, 80)

print(df_house.dtypes.value_counts())
# object     43
# int64      34
# float64     3
# dtype: int64

df_house_corr = df_house.corr()

print(df_house_corr.shape)
# (37, 37)

fig, ax = plt.subplots(figsize=(12, 9)) 
sns.heatmap(df_house_corr, square=True, vmax=1, vmin=-1, center=0)
plt.savefig('data/dst/seaborn_heatmap_house_price.png')
