import pandas as pd
import seaborn as sns

df = sns.load_dataset("iris")
print(df.shape)
print(df.head(5))
# (150, 5)
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
print(type(grouped))
# <pandas.core.groupby.DataFrameGroupBy object at 0x111b209e8>
# <class 'pandas.core.groupby.DataFrameGroupBy'>

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

print(grouped.agg(['min', 'max'])) 
#              sl        sw        pl        pw     
#             min  max  min  max  min  max  min  max
# species                                           
# setosa      4.3  5.8  2.3  4.4  1.0  1.9  0.1  0.6
# versicolor  4.9  7.0  2.0  3.4  3.0  5.1  1.0  1.8
# virginica   4.9  7.9  2.2  3.8  4.5  6.9  1.4  2.5

print(grouped.describe()) 
#               pl                                                 pw         \
#            count   mean       std  min  25%   50%    75%  max count   mean   
# species                                                                      
# setosa      50.0  1.462  0.173664  1.0  1.4  1.50  1.575  1.9  50.0  0.246   
# versicolor  50.0  4.260  0.469911  3.0  4.0  4.35  4.600  5.1  50.0  1.326   
# virginica   50.0  5.552  0.551895  4.5  5.1  5.55  5.875  6.9  50.0  2.026   
#            ...    sl         sw                                                
#            ...   75%  max count   mean       std  min    25%  50%    75%  max  
# species    ...                                                                 
# setosa     ...   5.2  5.8  50.0  3.428  0.379064  2.3  3.200  3.4  3.675  4.4  
# versicolor ...   6.3  7.0  50.0  2.770  0.313798  2.0  2.525  2.8  3.000  3.4  
# virginica  ...   6.9  7.9  50.0  2.974  0.322497  2.2  2.800  3.0  3.175  3.8  
# [3 rows x 32 columns]

print(type(grouped.max()))
# <class 'pandas.core.frame.DataFrame'>

ax = grouped.max().plot.bar(rot=0)
fig = ax.get_figure()
fig.savefig('data/dst/iris_pandas_groupby_max.jpg')
