import pandas as pd
import numpy as np

print(pd.__version__)
# 2.1.2

print(np.__version__)
# 1.26.1

print(pd.DataFrame.agg is pd.DataFrame.aggregate)
# True

print(pd.Series.agg is pd.Series.aggregate)
# True

df = pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5]})
print(df)
#    A  B
# 0  0  3
# 1  1  4
# 2  2  5

print(df.agg(['sum', 'mean', 'min', 'max']))
#         A     B
# sum   3.0  12.0
# mean  1.0   4.0
# min   0.0   3.0
# max   2.0   5.0

print(type(df.agg(['sum', 'mean', 'min', 'max'])))
# <class 'pandas.core.frame.DataFrame'>

print(df.agg(['sum']))
#      A   B
# sum  3  12

print(type(df.agg(['sum'])))
# <class 'pandas.core.frame.DataFrame'>

print(df.agg('sum'))
# A     3
# B    12
# dtype: int64

print(type(df.agg('sum')))
# <class 'pandas.core.series.Series'>

print(df.agg({'A': ['sum', 'min', 'max'], 'B': ['mean', 'min', 'max']}))
#         A    B
# sum   3.0  NaN
# min   0.0  3.0
# max   2.0  5.0
# mean  NaN  4.0

print(df.agg({'A': 'sum', 'B': 'mean'}))
# A    3.0
# B    4.0
# dtype: float64

print(df.agg({'A': ['sum'], 'B': 'mean'}))
#         A    B
# sum   3.0  NaN
# mean  NaN  4.0

print(df.agg({'A': ['min', 'max'], 'B': 'mean'}))
#         A    B
# min   0.0  NaN
# max   2.0  NaN
# mean  NaN  4.0

print(df.agg(['sum', 'mean', 'min', 'max'], axis=1))
#    sum  mean  min  max
# 0  3.0   1.5  0.0  3.0
# 1  5.0   2.5  1.0  4.0
# 2  7.0   3.5  2.0  5.0

s = pd.Series([0, 1, 2])
print(s)
# 0    0
# 1    1
# 2    2
# dtype: int64

print(s.agg(['sum', 'mean', 'min', 'max']))
# sum     3.0
# mean    1.0
# min     0.0
# max     2.0
# dtype: float64

print(type(s.agg(['sum', 'mean', 'min', 'max'])))
# <class 'pandas.core.series.Series'>

print(s.agg(['sum']))
# sum    3
# dtype: int64

print(type(s.agg(['sum'])))
# <class 'pandas.core.series.Series'>

print(s.agg('sum'))
# 3

print(type(s.agg('sum')))
# <class 'numpy.int64'>

print(s.agg({'Total': 'sum', 'Average': 'mean', 'Min': 'min', 'Max': 'max'}))
# Total      3.0
# Average    1.0
# Min        0.0
# Max        2.0
# dtype: float64

# print(s.agg({'NewLabel_1': ['sum', 'max'], 'NewLabel_2': ['mean', 'min']}))
# SpecificationError: nested renamer is not supported

print(df.agg(['count', 'amax']))
#        A  B
# count  3  3
# amax   2  5

print(df['A'].count())
# 3

# print(np.count(df['A']))
# AttributeError: module 'numpy' has no attribute 'count'

print(np.amax(df['A']))
# 2

# print(df['A'].amax())
# AttributeError: 'Series' object has no attribute 'amax'

# print(df.agg(['xxx']))
# AttributeError: 'xxx' is not a valid function for 'Series' object

# print(df.agg('xxx'))
# AttributeError: 'xxx' is not a valid function for 'DataFrame' object

print(hasattr(pd.DataFrame, '__array__'))
# True

print(hasattr(pd.core.groupby.GroupBy, '__array__'))
# False

def my_func(x):
    return x.min() + x.max()

print(df.agg([my_func, lambda x: x.min() - x.max()]))
#           A  B
# my_func   2  8
# <lambda> -2 -2

print(df.agg('std'))
# A    1.0
# B    1.0
# dtype: float64

print(df.agg('std', ddof=0))
# A    0.816497
# B    0.816497
# dtype: float64

print(df.agg(['std'], ddof=0))
#             A         B
# std  0.816497  0.816497

# print(df.agg(['max', 'std'], ddof=0))
# TypeError: max() got an unexpected keyword argument 'ddof'

print(df.agg(['max', lambda x: x.std(ddof=0)]))
#                  A         B
# max       2.000000  5.000000
# <lambda>  0.816497  0.816497

df_str = pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5], 'C': ['X', 'Y', 'Z']})
print(df_str)
#    A  B  C
# 0  0  3  X
# 1  1  4  Y
# 2  2  5  Z

# df_str['C'].mean()
# TypeError: Could not convert XYZ to numeric

# print(df_str.agg(['mean']))
# TypeError: Could not convert string 'XYZ' to numeric

print(df_str.mean(numeric_only=True))
# A    1.0
# B    4.0
# dtype: float64

print(df_str.agg('mean', numeric_only=True))
# A    1.0
# B    4.0
# dtype: float64

# df_str['C'].mean(numeric_only=True)
# TypeError: Series.mean does not allow numeric_only=True with non-numeric dtypes.

# print(df_str.agg(['mean'], numeric_only=True))
# TypeError: Series.mean does not allow numeric_only=True with non-numeric dtypes.

print(df_str.select_dtypes(include='number').agg(['sum', 'mean']))
#         A     B
# sum   3.0  12.0
# mean  1.0   4.0
