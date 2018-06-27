import pandas as pd
import seaborn as sns
import numpy as np

df = sns.load_dataset("iris")
print(df.shape)
# (150, 5)

print(df.head(5))
#    sepal_length  sepal_width  petal_length  petal_width species
# 0           5.1          3.5           1.4          0.2  setosa
# 1           4.9          3.0           1.4          0.2  setosa
# 2           4.7          3.2           1.3          0.2  setosa
# 3           4.6          3.1           1.5          0.2  setosa
# 4           5.0          3.6           1.4          0.2  setosa

df.columns = ['sl', 'sw', 'pl', 'pw', 'species']
print(df.head(5))
#     sl   sw   pl   pw species
# 0  5.1  3.5  1.4  0.2  setosa
# 1  4.9  3.0  1.4  0.2  setosa
# 2  4.7  3.2  1.3  0.2  setosa
# 3  4.6  3.1  1.5  0.2  setosa
# 4  5.0  3.6  1.4  0.2  setosa

grouped = df.groupby('species')
print(grouped)
# <pandas.core.groupby.groupby.DataFrameGroupBy object at 0x10c69f6a0>

print(type(grouped))
# <class 'pandas.core.groupby.groupby.DataFrameGroupBy'>

print(grouped.size())
# species
# setosa        50
# versicolor    50
# virginica     50
# dtype: int64

print(grouped.mean())
#                sl     sw     pl     pw
# species                               
# setosa      5.006  3.428  1.462  0.246
# versicolor  5.936  2.770  4.260  1.326
# virginica   6.588  2.974  5.552  2.026

print(grouped.min())
#              sl   sw   pl   pw
# species                       
# setosa      4.3  2.3  1.0  0.1
# versicolor  4.9  2.0  3.0  1.0
# virginica   4.9  2.2  4.5  1.4

print(grouped.max())
#              sl   sw   pl   pw
# species                       
# setosa      5.8  4.4  1.9  0.6
# versicolor  7.0  3.4  5.1  1.8
# virginica   7.9  3.8  6.9  2.5

print(grouped.sum())
#                sl     sw     pl     pw
# species                               
# setosa      250.3  171.4   73.1   12.3
# versicolor  296.8  138.5  213.0   66.3
# virginica   329.4  148.7  277.6  101.3

print(type(grouped.mean()))
# <class 'pandas.core.frame.DataFrame'>

print(grouped.agg(min))
#              sl   sw   pl   pw
# species                       
# setosa      4.3  2.3  1.0  0.1
# versicolor  4.9  2.0  3.0  1.0
# virginica   4.9  2.2  4.5  1.4

print(grouped.agg('max'))
#              sl   sw   pl   pw
# species                       
# setosa      5.8  4.4  1.9  0.6
# versicolor  7.0  3.4  5.1  1.8
# virginica   7.9  3.8  6.9  2.5

# print(grouped.agg(mean))
# NameError: name 'mean' is not defined

print(grouped.agg(np.mean))
#                sl     sw     pl     pw
# species                               
# setosa      5.006  3.428  1.462  0.246
# versicolor  5.936  2.770  4.260  1.326
# virginica   6.588  2.974  5.552  2.026

print(grouped.agg('mean'))
#                sl     sw     pl     pw
# species                               
# setosa      5.006  3.428  1.462  0.246
# versicolor  5.936  2.770  4.260  1.326
# virginica   6.588  2.974  5.552  2.026

print(grouped.agg([min, 'max']))
#              sl        sw        pl        pw     
#             min  max  min  max  min  max  min  max
# species                                           
# setosa      4.3  5.8  2.3  4.4  1.0  1.9  0.1  0.6
# versicolor  4.9  7.0  2.0  3.4  3.0  5.1  1.0  1.8
# virginica   4.9  7.9  2.2  3.8  4.5  6.9  1.4  2.5

print(grouped.agg({'sl': min, 'sw': max, 'pl': np.mean, 'pw': 'mean'}))
#              sl   sw     pl     pw
# species                           
# setosa      4.3  4.4  1.462  0.246
# versicolor  4.9  3.4  4.260  1.326
# virginica   4.9  3.8  5.552  2.026

print(grouped.agg(lambda x: max(x) - min(x)))
#              sl   sw   pl   pw
# species                       
# setosa      1.5  2.1  0.9  0.5
# versicolor  2.1  1.4  2.1  0.8
# virginica   3.0  1.6  2.4  1.1

print(grouped.agg(lambda x: type(x))['sl'])
# species
# setosa        <class 'pandas.core.series.Series'>
# versicolor    <class 'pandas.core.series.Series'>
# virginica     <class 'pandas.core.series.Series'>
# Name: sl, dtype: object

# print(grouped.agg(lambda x: x + 1))
# Exception: Must produce aggregated value

print(grouped.describe()['sl']) 
#             count   mean       std  min    25%  50%  75%  max
# species                                                      
# setosa       50.0  5.006  0.352490  4.3  4.800  5.0  5.2  5.8
# versicolor   50.0  5.936  0.516171  4.9  5.600  5.9  6.3  7.0
# virginica    50.0  6.588  0.635880  4.9  6.225  6.5  6.9  7.9

print(type(grouped.max()))
# <class 'pandas.core.frame.DataFrame'>

ax = grouped.max().plot.bar(rot=0)
fig = ax.get_figure()
fig.savefig('data/dst/iris_pandas_groupby_max.jpg')
